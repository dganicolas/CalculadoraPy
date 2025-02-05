# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calcInter.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(938, 678)
        font = QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: gray;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.btn_borrar_todo = QPushButton(self.centralwidget)
        self.btn_borrar_todo.setObjectName(u"btn_borrar_todo")
        self.btn_borrar_todo.setGeometry(QRect(200, 210, 81, 80))
        self.btn_borrar_todo.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #A5A5A5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BFBFBF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D4D4D2;\n"
"}")
        self.btn_borrar_ultimo_digito = QPushButton(self.centralwidget)
        self.btn_borrar_ultimo_digito.setObjectName(u"btn_borrar_ultimo_digito")
        self.btn_borrar_ultimo_digito.setGeometry(QRect(290, 210, 171, 80))
        self.btn_borrar_ultimo_digito.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #A5A5A5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BFBFBF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D4D4D2;\n"
"}")
        self.btn_n9 = QPushButton(self.centralwidget)
        self.btn_n9.setObjectName(u"btn_n9")
        self.btn_n9.setGeometry(QRect(380, 300, 80, 80))
        self.btn_n9.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}")
        self.btn_n8 = QPushButton(self.centralwidget)
        self.btn_n8.setObjectName(u"btn_n8")
        self.btn_n8.setGeometry(QRect(290, 300, 80, 80))
        self.btn_n8.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}")
        self.btn_n7 = QPushButton(self.centralwidget)
        self.btn_n7.setObjectName(u"btn_n7")
        self.btn_n7.setGeometry(QRect(200, 300, 80, 80))
        self.btn_n7.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}")
        self.btn_dividir = QPushButton(self.centralwidget)
        self.btn_dividir.setObjectName(u"btn_dividir")
        self.btn_dividir.setGeometry(QRect(470, 210, 80, 80))
        self.btn_dividir.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\"; /* Usa una fuente integrada en el sistema */\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.btn_n6 = QPushButton(self.centralwidget)
        self.btn_n6.setObjectName(u"btn_n6")
        self.btn_n6.setGeometry(QRect(380, 390, 80, 80))
        self.btn_n6.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}")
        self.btn_n5 = QPushButton(self.centralwidget)
        self.btn_n5.setObjectName(u"btn_n5")
        self.btn_n5.setGeometry(QRect(290, 390, 80, 80))
        self.btn_n5.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}")
        self.btn_n4 = QPushButton(self.centralwidget)
        self.btn_n4.setObjectName(u"btn_n4")
        self.btn_n4.setGeometry(QRect(200, 390, 80, 80))
        self.btn_n4.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}")
        self.btn_multiplicar = QPushButton(self.centralwidget)
        self.btn_multiplicar.setObjectName(u"btn_multiplicar")
        self.btn_multiplicar.setGeometry(QRect(470, 300, 80, 80))
        self.btn_multiplicar.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\"; /* Usa una fuente integrada en el sistema */\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.btn_n3 = QPushButton(self.centralwidget)
        self.btn_n3.setObjectName(u"btn_n3")
        self.btn_n3.setGeometry(QRect(380, 480, 80, 80))
        self.btn_n3.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}")
        self.btn_n2 = QPushButton(self.centralwidget)
        self.btn_n2.setObjectName(u"btn_n2")
        self.btn_n2.setGeometry(QRect(290, 480, 80, 80))
        self.btn_n2.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}")
        self.btn_n1 = QPushButton(self.centralwidget)
        self.btn_n1.setObjectName(u"btn_n1")
        self.btn_n1.setGeometry(QRect(200, 480, 80, 80))
        self.btn_n1.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}")
        self.btn_restar = QPushButton(self.centralwidget)
        self.btn_restar.setObjectName(u"btn_restar")
        self.btn_restar.setGeometry(QRect(470, 390, 80, 80))
        self.btn_restar.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\"; /* Usa una fuente integrada en el sistema */\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.btn_punto = QPushButton(self.centralwidget)
        self.btn_punto.setObjectName(u"btn_punto")
        self.btn_punto.setGeometry(QRect(200, 570, 80, 80))
        self.btn_punto.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}")
        self.btn_n0 = QPushButton(self.centralwidget)
        self.btn_n0.setObjectName(u"btn_n0")
        self.btn_n0.setGeometry(QRect(290, 570, 80, 80))
        self.btn_n0.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}")
        self.btn_sumar = QPushButton(self.centralwidget)
        self.btn_sumar.setObjectName(u"btn_sumar")
        self.btn_sumar.setGeometry(QRect(470, 480, 80, 80))
        self.btn_sumar.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\"; /* Usa una fuente integrada en el sistema */\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.btn_exponente = QPushButton(self.centralwidget)
        self.btn_exponente.setObjectName(u"btn_exponente")
        self.btn_exponente.setGeometry(QRect(20, 300, 80, 80))
        self.btn_exponente.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.editText_pantalla = QTextEdit(self.centralwidget)
        self.editText_pantalla.setObjectName(u"editText_pantalla")
        self.editText_pantalla.setGeometry(QRect(30, 53, 511, 141))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        self.editText_pantalla.setFont(font1)
        self.editText_pantalla.setAutoFillBackground(False)
        self.editText_pantalla.setStyleSheet(u"QTextEdit {\n"
"    background-color: #2b2b2b;  /* Fondo oscuro */\n"
"    color: white;  /* Texto blanco */\n"
"    font-family: \"Arial\";  \n"
"    font-size: 48px;  \n"
"    font-weight: bold;\n"
"    border: 2px solid #555;  /* Borde similar a la tabla */\n"
"    padding: 10px;\n"
"    selection-background-color: #4CAF50;  /* Resaltar texto seleccionado */\n"
"    selection-color: white;\n"
"}")
        self.editText_pantalla.setUndoRedoEnabled(True)
        self.editText_pantalla.setReadOnly(True)
        self.btn_raiz = QPushButton(self.centralwidget)
        self.btn_raiz.setObjectName(u"btn_raiz")
        self.btn_raiz.setGeometry(QRect(110, 390, 80, 80))
        self.btn_raiz.setStyleSheet(u"QPushButton {\n"
"    font-weight: black;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.btn_seno = QPushButton(self.centralwidget)
        self.btn_seno.setObjectName(u"btn_seno")
        self.btn_seno.setGeometry(QRect(20, 210, 80, 80))
        self.btn_seno.setStyleSheet(u"QPushButton {\n"
"    font-weight: black;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.btn_coseno = QPushButton(self.centralwidget)
        self.btn_coseno.setObjectName(u"btn_coseno")
        self.btn_coseno.setGeometry(QRect(110, 300, 80, 80))
        self.btn_coseno.setStyleSheet(u"QPushButton {\n"
"    font-weight: black;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.btn_factorial = QPushButton(self.centralwidget)
        self.btn_factorial.setObjectName(u"btn_factorial")
        self.btn_factorial.setGeometry(QRect(110, 480, 80, 80))
        self.btn_factorial.setStyleSheet(u"QPushButton {\n"
"    font-weight: black;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.btn_n00 = QPushButton(self.centralwidget)
        self.btn_n00.setObjectName(u"btn_n00")
        self.btn_n00.setGeometry(QRect(380, 570, 80, 80))
        self.btn_n00.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}")
        self.btn_igual = QPushButton(self.centralwidget)
        self.btn_igual.setObjectName(u"btn_igual")
        self.btn_igual.setGeometry(QRect(470, 570, 80, 80))
        self.btn_igual.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.btn_parentesis_cerrar = QPushButton(self.centralwidget)
        self.btn_parentesis_cerrar.setObjectName(u"btn_parentesis_cerrar")
        self.btn_parentesis_cerrar.setGeometry(QRect(110, 570, 80, 80))
        self.btn_parentesis_cerrar.setStyleSheet(u"QPushButton {\n"
"    font-weight: black;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.btn_parentesis_abrir = QPushButton(self.centralwidget)
        self.btn_parentesis_abrir.setObjectName(u"btn_parentesis_abrir")
        self.btn_parentesis_abrir.setGeometry(QRect(20, 570, 80, 80))
        self.btn_parentesis_abrir.setStyleSheet(u"QPushButton {\n"
"    font-weight: black;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.btn_tangente = QPushButton(self.centralwidget)
        self.btn_tangente.setObjectName(u"btn_tangente")
        self.btn_tangente.setGeometry(QRect(20, 390, 80, 80))
        self.btn_tangente.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.btn_numero_pi = QPushButton(self.centralwidget)
        self.btn_numero_pi.setObjectName(u"btn_numero_pi")
        self.btn_numero_pi.setGeometry(QRect(20, 480, 80, 80))
        self.btn_numero_pi.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Arial\";\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.btn_ans = QPushButton(self.centralwidget)
        self.btn_ans.setObjectName(u"btn_ans")
        self.btn_ans.setGeometry(QRect(110, 210, 80, 80))
        self.btn_ans.setStyleSheet(u"QPushButton {\n"
"    font-weight: black;\n"
"    font-size: 28px;\n"
"    border-radius: 40px;\n"
"    min-width: 80px;\n"
"    min-height: 80px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FF9500;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFB04C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC7600;\n"
"}\n"
"")
        self.Cview_registro = QTableWidget(self.centralwidget)
        self.Cview_registro.setObjectName(u"Cview_registro")
        self.Cview_registro.setGeometry(QRect(560, 50, 351, 581))
        self.Cview_registro.setStyleSheet(u"QTableWidget {\n"
"    background-color: #2b2b2b;  /* Fondo oscuro */\n"
"    color: white;  /* Texto blanco */\n"
"    gridline-color: #555;  /* L\u00edneas de la tabla */\n"
"    font-size: 15px;\n"
"    selection-background-color: #4CAF50; /* Fondo de selecci\u00f3n */\n"
"    selection-color: white; /* Color del texto seleccionado */\n"
"    border: 2px solid #555;  /* Borde alrededor de la tabla */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #444;  /* Fondo de los encabezados */\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: 1px solid #666;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #4CAF50; /* Color de selecci\u00f3n */\n"
"    color: white;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #333;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #555;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScro"
                        "llBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"")
        self.Cview_registro.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.Cview_registro.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.Cview_registro.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.Cview_registro.setDragEnabled(False)
        self.Cview_registro.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.Cview_registro.horizontalHeader().setStretchLastSection(False)
        self.Cview_registro.verticalHeader().setCascadingSectionResizes(False)
        self.Cview_registro.verticalHeader().setProperty(u"showSortIndicator", False)
        self.Cview_registro.verticalHeader().setStretchLastSection(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_borrar_todo.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_borrar_ultimo_digito.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.btn_n9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_n8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_n7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_dividir.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_n6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_n5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_n4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_multiplicar.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.btn_n3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_n2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_n1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_restar.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_punto.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_n0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_sumar.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_exponente.setText(QCoreApplication.translate("MainWindow", u"^ ", None))
        self.editText_pantalla.setPlaceholderText("")
        self.btn_raiz.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.btn_seno.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.btn_coseno.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.btn_factorial.setText(QCoreApplication.translate("MainWindow", u"!", None))
        self.btn_n00.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.btn_igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_parentesis_cerrar.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.btn_parentesis_abrir.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.btn_tangente.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.btn_numero_pi.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.btn_ans.setText(QCoreApplication.translate("MainWindow", u"ANS", None))
    # retranslateUi

