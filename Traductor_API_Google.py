# Idiomas admitidos: https://cloud.google.com/translate/docs/languages?hl=es-419
# pip install gTTS
# pip install deep-translator
# pip install playsound
import sys 
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from gtts import gTTS # Google Text to Speech
from deep_translator import GoogleTranslator
from playsound import playsound

# Clase
class Traductor(QMainWindow):
    # Constructor (Es el primer metodo en ejecutarse)
    def __init__(self):
        # Constructor de la clase heredada
        super().__init__()
        # Mandar llamar el FrontEnd
        self.interfaz()
        # Seleccionar el 2do elemento de la cbSalida
        self.cbSalida.setCurrentIndex(1)


    def interfaz(self):
        # Ventana
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Traductor Python")
        self.setWindowIcon(QIcon("C:/Users/soporte/Desktop/Python769/logotraductor1.png"))
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

        # Caja izquierda de texto
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
        
         # Caja Derecha de texto
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
        #Traducir
        self.btnTraducir = QPushButton(self)
        self.btnTraducir.setText("Traducir")
        self.btnTraducir.setGeometry(425, 100, 150, 32)
        self.btnTraducir.setFont(QFont("San Francisco(SF)", 18))
        self.btnTraducir.setStyleSheet("""
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
        # Limpiar
        self.btnLimpiar = QPushButton(self)
        self.btnLimpiar.setText("Limpiar")
        self.btnLimpiar.setGeometry(425, 170, 150, 32)
        self.btnLimpiar.setFont(QFont("San Francisco(SF)", 18))
        self.btnLimpiar.setStyleSheet("""
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
        # Guardar
        self.btnGuardar = QPushButton(self)
        self.btnGuardar.setText("Guardar")
        self.btnGuardar.setGeometry(425, 245, 150, 32)
        self.btnGuardar.setFont(QFont("San Francisco(SF)", 18))
        self.btnGuardar.setStyleSheet("""
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
        # Escuchar
        self.btnEscuchar = QPushButton(self)
        self.btnEscuchar.setText("Escuchar")
        self.btnEscuchar.setGeometry(425, 318, 150, 32)
        self.btnEscuchar.setFont(QFont("San Francisco(SF)", 18))
        self.btnEscuchar.setStyleSheet("""
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

        # Listas Desplegables
        idiomas = ["es", "en", "fr", "ja", "de"]
        self.cbEntrada = QComboBox(self)
        self.cbEntrada.setGeometry(10, 50, 220, 30)
        self.cbEntrada.addItems(idiomas)
        self.cbEntrada.setFont(QFont("San Francisco(SF)", 16))
        self.cbEntrada.setStyleSheet("""
                                    QComboBox{
                                        background-color:#2C2C2E;
                                        color:#FFFFFF;
                                        font-weight:500;
                                        border:2px solid #AA9E9E;
                                        border-radius: 6px;                                    
                                    }
                                    """)
        
        self.cbSalida = QComboBox(self)
        self.cbSalida.setGeometry(770, 50, 220, 30)
        self.cbSalida.addItems(idiomas)
        self.cbSalida.setFont(QFont("San Francisco(SF)", 16))
        self.cbSalida.setStyleSheet("""
                                    QComboBox{
                                        background-color:#2C2C2E;
                                        color:#FFFFFF;
                                        font-weight:500;
                                        border:2px solid #AA9E9E;
                                        border-radius: 6px;                                    
                                    }
                                    """)


        # Vincular los botones con los metodos
        self.btnTraducir.clicked.connect(self.traducir)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnEscuchar.clicked.connect(self.escuchar)
        

    def traducir(self):
        # Guardar la informacion de la caja de entrada
        texto = self.txtEntrada.toPlainText()
        # Validar que la variable tenga datos
        if len(texto) == 0:
            QMessageBox.warning(self, "Atencion", "No hay texto por traducir")
            return # Salir del metodo
        # intentar realizar la traducción
        try:
            # Mandar llamar la API
            fuente = self.cbEntrada.currentText()
            objetivo = self.cbSalida.currentText()
            traductor = GoogleTranslator(source=fuente, target=objetivo)
            # Guardar la traducción
            resultado = traductor.translate(texto)
            # Avisar sobre la traducción
            QMessageBox.information(self, "Traducción", "Traducción Exitosa")
            # Mostrar la traducción en la caja de salida
            self.txtSalida.setText(resultado)                               
        except Exception as error:
            QMessageBox.warning(self,"Error", f"{error}")
            QMessageBox.warning(self,"Error", "No fue posible realizar la traducción")
    
    def limpiar(self):
        # Limpiar el contenido de ambas cajas
        self.txtEntrada.setText("")
        self.txtSalida.clear()
        # Establecer los indices de las listas despleadas
        self.cbEntrada.setCurrentIndex(0)
        self.cbSalida.setCurrentIndex(1)
        
    
    def guardar(self):
        # Almacenar la traducción en una variable
        traducción = self.txtSalida.toPlainText()
        # Validar que haya una traducción
        if len(traducción) == 0:
            QMessageBox.warning(self, "Atencion", "No hay traducción por guardar")
            return # Salir del metodo
        # Intentar guardar la traducción
        try:
            pass
        except Exception as error:
            QMessageBox.warning(self,"Error", f"{error}")
            QMessageBox.warning(self,"Error", "No fue posible guardar la traducción")
            
    
    def escuchar(self):
         # Almacenar la traducción en una variable
        traducción = self.txtSalida.toPlainText()
        # Validar que haya una traducción
        if len(traducción) == 0:
            QMessageBox.warning(self, "Atencion", "No hay traducción por guardar")
            return # Salir del metodo
        # Intentar guardar el audio
        try:
            pass
        except Exception as error:
            QMessageBox.warning(self,"Error", f"{error}")
            QMessageBox.warning(self,"Error", "No fue posible guardar el audio")

# Estructura de arranque
if __name__== "__main__":
    # Instancia para iniciar la app
    app = QApplication(sys.argv)
    # Instancia de la clase principal
    traductor = Traductor()
    # Mostrar el FrontEnd
    traductor.show()
    # Ejecutar el BackEnd
    app.exec()
    