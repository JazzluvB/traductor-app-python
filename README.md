# Traductor App en Python 🌐

**Proyecto intermedio ejecutable desde VS Code**  
Traductor desarrollado en Python 3.10.11 con PyQt5, conectando la API de Google Translate. Permite traducir texto entre varios idiomas, escuchar la traducción, guardar resultados y demuestra manejo de interfaces gráficas y eventos en Python.

---

## Características

- Traducción de texto entre múltiples idiomas (`es`, `en`, `fr`, `ja`, `de`).  
- Interfaz con **PyQt5**:
  - Cajas de texto de entrada y salida.  
  - Botones interactivos: Traducir, Limpiar, Guardar, Escuchar.  
  - Estilos personalizados con hover y pressed.  
- Validación de entrada y manejo de errores con mensajes.  
- Conexión con la API de Google Translate mediante `deep-translator`.  
- Proyecto ejecutable desde VS Code; no requiere instalación de aplicación independiente.

---

## Tecnologías y librerías usadas

- **Python 3.10.11** – lenguaje principal.  
- **PyQt5** – desarrollo de interfaz gráfica.  
  - `QMainWindow`, `QPushButton`, `QTextEdit`, `QComboBox`, `QLabel`  
- **gTTS** – convertir texto a voz.  
- **deep-translator** – traducir texto mediante Google Translate.  
- **playsound** – reproducir audio.  
- **Visual Studio Code** – entorno de desarrollo.  

---

## Cómo ejecutar

1. Clona este repositorio:

```bash
git clone https://github.com/tu-usuario/traductor-app-python.git
