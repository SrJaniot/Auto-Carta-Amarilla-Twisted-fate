# 🎮 BOT CARTAS - League of Legends

Bot desarrollado en **Python** para automatizar la selección de la
**Carta Amarilla** de **Twisted Fate** mediante detección de color en
pantalla usando **OpenCV**.

> ⚠️ Proyecto con fines educativos sobre automatización, visión por
> computador y procesamiento de imágenes.

## ✨ Características

-   Activación/desactivación con teclas de acceso rápido.
-   Detección de color en tiempo real.
-   Captura de pantalla rápida con MSS.
-   Simulación de teclado con Pynput.
-   Timeout configurable.
-   Código simple y fácil de modificar.

## 🛠️ Tecnologías

-   Python 3
-   OpenCV
-   NumPy
-   MSS
-   Pynput

## 📦 Instalación

``` bash
git clone https://github.com/TU_USUARIO/bot-cartas-lol.git
cd bot-cartas-lol
pip install -r requirements.txt
```

## ▶️ Uso

``` bash
python bot_cartas.py
```

## ⌨️ Controles

  Tecla   Acción
  ------- ----------------------------------------
  F6      Activar bot
  F7      Desactivar bot
  F8      Cerrar programa
  E       Buscar y seleccionar la Carta Amarilla

## ⚙️ Funcionamiento

1.  Presiona **E**.
2.  El bot pulsa **W**.
3.  Espera 0.2 segundos.
4.  Analiza la región configurada de la pantalla.
5.  Si detecta la Carta Amarilla, vuelve a pulsar **W** para
    seleccionarla.
6.  Si no la encuentra en 1.8 segundos, cancela la búsqueda.

## 📂 Estructura

``` text
bot-cartas-lol/
├── bot_cartas.py
├── requirements.txt
├── README.md
└── LICENSE
```

## ⚠️ Aviso

Este proyecto fue desarrollado únicamente con fines educativos. El uso
de este software es responsabilidad exclusiva del usuario.

## 👨‍💻 Autor

**SrJaniot**

GitHub: https://github.com/SrJaniot
Video: https://youtu.be/0-HE7UXBy34

## 📄 Licencia

Licencia MIT.
