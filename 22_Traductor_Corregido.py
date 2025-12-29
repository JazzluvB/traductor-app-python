# Idiomas admitidos: https://cloud.google.com/translate/docs/languages?hl=es-419
# pip install gTTS
# pip install deep-translator
import sys 
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from gtts import gTTS # Google Text to Speech
from deep_translator import GoogleTranslator
import subprocess

# Clase
class Traductor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interfaz()
        self.cbSalida.setCurrentIndex(1)

    def interfaz(self):
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Traductor Python")
        self.setStyleSheet("Background-color:#1C1C1E; color: #776F6F")

        # Titulo
        self.lbtitulo = QLabel(self)
        self.lbtitulo.setText("Traductor Python QT")
        self.lbtitulo.setGeometry(300, 20, 400, 40)
        self.lbtitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitulo.setFont(QFont("San Francisco(SF)", 18))
        self.lbtitulo.setStyleSheet("""
            QLabel{
                background-color:#2C2C2E;
                color:#FFFFFF;
                font-weight:500;
                border:2px solid #AA9E9E;
                border-radius: 6px;                                    
            }
        """)

        # Cajas de texto
        self.txtEntrada = QTextEdit(self)
        self.txtEntrada.setGeometry(10, 100, 400, 250)
        self.txtEntrada.setFont(QFont("San Francisco(SF)", 18))
        self.txtEntrada.setStyleSheet("""
            QTextEdit{
                background-color:#2C2C2E;
                color:#FFFFFF;
                font-weight:250;
                border:2px solid #AA9E9E;
                border-radius: 6px;   
            }
        """)
        
        self.txtSalida = QTextEdit(self)
        self.txtSalida.setGeometry(590, 100, 400, 250)
        self.txtSalida.setFont(QFont("San Francisco(SF)", 18))
        self.txtSalida.setStyleSheet("""
            QTextEdit{
                background-color:#2C2C2E;
                color:#FFFFFF;
                font-weight:250;
                border:2px solid #AA9E9E;
                border-radius: 6px;   
            }                            
        """)

        # Botones
        self.btnTraducir = QPushButton("Traducir", self)
        self.btnTraducir.setGeometry(425, 100, 150, 32)
        self.btnLimpiar = QPushButton("Limpiar", self)
        self.btnLimpiar.setGeometry(425, 170, 150, 32)
        self.btnGuardar = QPushButton("Guardar", self)
        self.btnGuardar.setGeometry(425, 245, 150, 32)
        self.btnEscuchar = QPushButton("Escuchar", self)
        self.btnEscuchar.setGeometry(425, 318, 150, 32)

        for btn in [self.btnTraducir, self.btnLimpiar, self.btnGuardar, self.btnEscuchar]:
            btn.setFont(QFont("San Francisco(SF)", 18))
            btn.setStyleSheet("""
                QPushButton{
                    background-color:#2C2C2E;
                    color:#FFFFFF;
                    font-weight:250;
                    border:2px solid #AA9E9E;
                    border-radius: 6px; 
                }
                QPushButton:hover{
                    background-color:#5A5555;
                    color:#FFFFFF;
                }
                QPushButton:pressed{
                    background-color:#4D4747;
                    color:#FFFFFF;
                }
            """)

        # Listas desplegables
        idiomas = ["es", "en", "fr", "ja", "de"]
        self.cbEntrada = QComboBox(self)
        self.cbEntrada.setGeometry(10, 50, 220, 30)
        self.cbEntrada.addItems(idiomas)
        self.cbEntrada.setFont(QFont("San Francisco(SF)", 16))
        self.cbSalida = QComboBox(self)
        self.cbSalida.setGeometry(770, 50, 220, 30)
        self.cbSalida.addItems(idiomas)
        self.cbSalida.setFont(QFont("San Francisco(SF)", 16))

        # Vincular botones con métodos
        self.btnTraducir.clicked.connect(self.traducir)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnEscuchar.clicked.connect(self.escuchar)
        
    def traducir(self):
        texto = self.txtEntrada.toPlainText()
        if len(texto) == 0:
            QMessageBox.warning(self, "Atencion", "No hay texto por traducir")
            return
        try:
            fuente = self.cbEntrada.currentText()
            objetivo = self.cbSalida.currentText()
            traductor = GoogleTranslator(source=fuente, target=objetivo)
            resultado = traductor.translate(texto)
            self.txtSalida.setText(resultado)
            QMessageBox.information(self, "Traducción", "Traducción Exitosa")
        except Exception as error:
            QMessageBox.warning(self, "Error", f"No fue posible realizar la traducción:\n{error}")

    def limpiar(self):
        self.txtEntrada.setText("")
        self.txtSalida.clear()
        self.cbEntrada.setCurrentIndex(0)
        self.cbSalida.setCurrentIndex(1)
        
    def guardar(self):
        traduccion = self.txtSalida.toPlainText()
        if len(traduccion) == 0:
            QMessageBox.warning(self, "Atencion", "No hay traducción por guardar")
            return
        try:
            with open("traduccion.txt", "w", encoding="utf-8") as f:
                f.write(traduccion)
            QMessageBox.information(self, "Guardar", "Traducción guardada en 'traduccion.txt'")
        except Exception as error:
            QMessageBox.warning(self,"Error", f"No fue posible guardar la traducción:\n{error}")
            
    def escuchar(self):
        traduccion = self.txtSalida.toPlainText()
        if len(traduccion) == 0:
            QMessageBox.warning(self, "Atencion", "No hay traducción para escuchar")
            return
        try:
            tts = gTTS(text=traduccion, lang=self.cbSalida.currentText())
            archivo_audio = "audio.mp3"
            tts.save(archivo_audio)
            # Reproducir con afplay (nativo de macOS)
            subprocess.run(["afplay", archivo_audio])
        except Exception as error:
            QMessageBox.warning(self,"Error", f"No fue posible reproducir el audio:\n{error}")

# Arranque de la aplicación
if __name__== "__main__":
    app = QApplication(sys.argv)
    traductor = Traductor()
    traductor.show()
    app.exec()

