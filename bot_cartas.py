import numpy as np
import mss
import time
import sys
from pynput.keyboard import Controller, Listener, Key
import cv2

monitor = {"top": 980, "left": 838, "width": 876-838, "height": 1021-980}
sct = mss.mss()
kb = Controller()

# Variables globales
buscar_amarilla = False
ignore_w_until = 0
activado = False
tiempo_inicio_busqueda = 0
ejecutando = True

def detectar_color(img):
    try:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # Solo detectar amarillo
        amarillo_bajo = np.array([20, 100, 100])
        amarillo_alto = np.array([35, 255, 255])
        
        mascara_amarillo = cv2.inRange(hsv, amarillo_bajo, amarillo_alto)
        amarillo = cv2.countNonZero(mascara_amarillo)
        
        # Umbral aumentado a 500 píxeles para mayor precisión
        if amarillo > 500:
            return "AMARILLO"
        else:
            return "SIN COLOR"
    
    except Exception as e:
        return "SIN COLOR"

def on_press(key):
    global buscar_amarilla, ignore_w_until, activado, tiempo_inicio_busqueda, ejecutando
    
    try:
        if key == Key.f6:
            activado = True
            print("✅ BOT ACTIVADO (F6)")
        
        elif key == Key.f7:
            activado = False
            buscar_amarilla = False
            print("❌ BOT DESACTIVADO (F7)")
        
        elif key == Key.f8:
            ejecutando = False
            print("\n🛑 Cerrando programa... (F8)")
            return False
        
        elif activado:
            if hasattr(key, 'char') and key.char == "e":
                if time.time() < ignore_w_until:
                    return
                
                kb.press("w")
                kb.release("w")
                
                # Aumentamos el delay a 0.2 segundos antes de comenzar a buscar
                time.sleep(0.2)
                
                buscar_amarilla = True
                tiempo_inicio_busqueda = time.time()
                ignore_w_until = time.time() + 0.15
                print("🟡 E → Buscando AMARILLA (delay 0.2s)")
    
    except AttributeError:
        pass

listener = Listener(on_press=on_press)
listener.start()

print("🎮 BOT DE CARTAS - LISTO")
print("✅ F6 - Activar bot")
print("❌ F7 - Desactivar bot")
print("🛑 F8 - Cerrar programa")
print("🎯 E - Buscar carta amarilla (con bot activo)")
print("⏰ Timeout: 1.8 segundos")
print("⏳ Delay inicial: 0.2 segundos")
print("🎯 Precisión: 500+ píxeles amarillos")
print("🎯 TAMAÑO DE LA INTERFAZ DE LOL EN 29")

print("😈 by SrJaniot")


try:
    while ejecutando:
        frame = np.array(sct.grab(monitor))
        color = detectar_color(frame)
        
        timeout = time.time() - tiempo_inicio_busqueda > 1.8
        
        if activado and buscar_amarilla:
            if color == "AMARILLO":
                kb.press("w")
                kb.release("w")
                buscar_amarilla = False
                print("🟡 AMARILLA SELECCIONADA ✔")
            elif timeout:
                buscar_amarilla = False
                print("⏰ Timeout: No se encontró AMARILLA")
        
        time.sleep(0.01)
        
except KeyboardInterrupt:
    print("\n🛑 Programa interrumpido")
except Exception as e:
    pass
finally:
    ejecutando = False
    listener.stop()
    sys.exit()