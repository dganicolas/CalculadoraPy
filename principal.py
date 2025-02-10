from decimal import Decimal
import os
import sys
from PyQt6 import uic  # Librería para trabajar con el archivo de la interfaz
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6.QtGui import QIcon
import math

"""
Comando utilizado para empaquetar
pyinstaller ---> el instalador encargado a empaquetar el proyecto
--windowed ---> comando para que no se abra la consola cuando se ejecute el programa
--name "Calculadora_windowed_icon" ---> comando para cambiar el nombre del ejecutable
--icon=Calculator_30001.ico --->  comando para cambiar el icono del ejecutable
--add-data="calculator_30001.ico;." --->  principal.py comando para anadir el icono al ejecutable
principal.py ---> nombre del archivo principal

EN CASO DE ERROR IR A ESTA DIRECCION: 
https://github.com/dganicolas/CalculadoraPy
"""


class pantalla(QMainWindow):   # Se crea una clase por ventana
    def __init__(self): 
        super(pantalla, self).__init__() # Reservamos un espacio en memoria para la clase
        self.setWindowIcon(QIcon('_internal\Calculator_30001.ico'))
        self.setWindowTitle("Calculadora") # Nombre de la Ventana al abrir la aplicación
        uic.loadUi(os.path.abspath('_internal\calcInter.ui'), self)  # Cargamos la interfaz de Designe
        self.pantalla_texto = ""
        self.ans = "0"
        self.refrescar_pantalla()
        # conectamos los eventos de los botones con las funciones a desarrollar
        self.btn_borrar_todo.clicked.connect(lambda: self.borrar_todo()) # nombre del componente.evento(clicked).connect(self.<funcion>)
        self.btn_borrar_ultimo_digito.clicked.connect(lambda: self.borrar_ultimo_digito())
        self.btn_dividir.clicked.connect(lambda: self.anadir_digito("/"))
        self.btn_raiz.clicked.connect(lambda: self.anadir_digito("√"))
        self.btn_multiplicar.clicked.connect(lambda: self.anadir_digito("*"))
        self.btn_seno.clicked.connect(lambda: self.anadir_digito("sen("))
        self.btn_coseno.clicked.connect(lambda: self.anadir_digito("cos("))
        self.btn_tangente.clicked.connect(lambda: self.anadir_digito("tan("))
        self.btn_numero_pi.clicked.connect(lambda: self.anadir_digito("π"))
        self.btn_restar.clicked.connect(lambda: self.anadir_digito("-"))
        self.btn_sumar.clicked.connect(lambda: self.anadir_digito("+"))
        self.btn_igual.clicked.connect(lambda: self.calcular())
        self.btn_ans.clicked.connect(lambda: self.anadir_digito("ans"))
        self.btn_factorial.clicked.connect(lambda: self.anadir_digito("!"))
        self.btn_punto.clicked.connect(lambda: self.anadir_digito("."))
        self.btn_exponente.clicked.connect(lambda: self.anadir_digito("^"))
        self.btn_n00.clicked.connect(lambda: self.anadir_digito("00"))
        self.btn_parentesis_cerrar.clicked.connect(lambda: self.anadir_digito(")"))
        self.btn_parentesis_abrir.clicked.connect(lambda: self.anadir_digito("("))

        #bucle para conectar los botones de los números
        for i in range(10):
            getattr(self, f"btn_n{i}").clicked.connect(lambda _, i=i: self.anadir_digito(str(i)))
# A partir de aquí se escribe la lógica los componentes de la interfaz

    # Función para guardar el historial de operaciones
    def guardar_historial(self):
        self.Cview_registro.setColumnCount(2)
        row_count = self.Cview_registro.rowCount()
        self.Cview_registro.insertRow(row_count)
        if len(self.ans) > 25:
            self.ans = "{:.2E}".format(Decimal(self.ans))
        # Crear el ítem con el texto formateado
        item = QTableWidgetItem(self.copia_pantalla_texto)

        # Anadir el ítem a la tabla
        self.Cview_registro.setItem(row_count, 0, item)
        self.Cview_registro.setItem(row_count, 1, QTableWidgetItem(self.ans))
        self.Cview_registro.resizeColumnsToContents()  # Ajustar ancho de columna
        self.Cview_registro.resizeRowToContents(row_count)  # Ajustar altura de la fila

    # Función para calcular la operación
    def calcular(self):
        self.copia_pantalla_texto = self.pantalla_texto
        try:
            # Reemplazar los caracteres de la operación
            if "sen" in self.pantalla_texto:
                self.pantalla_texto = self.pantalla_texto.replace("sen", "math.sin")
            if "cos" in self.pantalla_texto:
                self.pantalla_texto = self.pantalla_texto.replace("cos", "math.cos")
            if "tan" in self.pantalla_texto:
                self.pantalla_texto = self.pantalla_texto.replace("tan", "math.tan")
            if "π" in self.pantalla_texto:
                self.pantalla_texto = self.pantalla_texto.replace("π", "3.14159265359")
            if "√" in self.pantalla_texto:
                self.pantalla_texto = "math.sqrt(" +self.pantalla_texto.replace("√", "") + ")"
            if "!" in self.pantalla_texto:
                self.pantalla_texto = "math.factorial(" + self.pantalla_texto.replace("!", ")")
            if "^" in self.pantalla_texto:
                self.pantalla_texto = self.pantalla_texto.replace("^", "**")
            
            # Calcular la operación
            self.ans = str(eval(self.pantalla_texto))
            self.pantalla_texto = self.ans
            self.guardar_historial()
        except Exception as e:
            self.pantalla_texto = "Systanx Error"
            self.refrescar_pantalla()
            self.ensenar_error()
        self.pantalla_texto = ""  
        self.refrescar_pantalla()

    # Función para mostrar un mensaje de error
    def ensenar_error(self):
        ventana= QMessageBox()
        ventana.setIcon(QMessageBox.Icon.Critical)
        ventana.setWindowTitle("Error")
        ventana.setText("operacion invalida")
        ventana.exec()

    # Función para anadir un dígito a la pantalla
    def anadir_digito(self, digito):
        if len(self.pantalla_texto) < 34:
            if digito == "ans":
                self.pantalla_texto += self.ans
            else:
                self.pantalla_texto += digito
        self.refrescar_pantalla()

    # Función para borrar todo el contenido de la pantalla
    def borrar_todo(self):
        self.pantalla_texto = ""
        self.refrescar_pantalla()

    # Función para borrar el último dígito de la pantalla
    def borrar_ultimo_digito(self):
        self.pantalla_texto = self.pantalla_texto[:-1]
        self.refrescar_pantalla()

    # Función para refrescar la pantalla
    def refrescar_pantalla(self):   
        self.editText_pantalla.setText(self.pantalla_texto if self.pantalla_texto else "0") # Asignamos el valor de la variable pantalla al componente editText_pantalla

# Función principal para ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = pantalla()
    window.show()
    app.exec() 