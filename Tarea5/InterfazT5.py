# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InterfazT5.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Practica(object):
    def setupUi(self, Practica):
        if not Practica.objectName():
            Practica.setObjectName(u"Practica")
        Practica.resize(296, 176)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(175, 181, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(215, 218, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(87, 90, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(117, 121, 170, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        Practica.setPalette(palette)
        self.btnGuardar = QPushButton(Practica)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(20, 130, 75, 23))
        self.lblNombre = QLabel(Practica)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(60, 20, 54, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblCorreo = QLabel(Practica)
        self.lblCorreo.setObjectName(u"lblCorreo")
        self.lblCorreo.setGeometry(QRect(60, 60, 49, 16))
        self.lblCorreo.setFont(font)
        self.lblPass = QLabel(Practica)
        self.lblPass.setObjectName(u"lblPass")
        self.lblPass.setGeometry(QRect(40, 100, 80, 16))
        self.lblPass.setFont(font)
        self.txtNombre = QLineEdit(Practica)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(138, 20, 133, 20))
        self.txtCorreo = QLineEdit(Practica)
        self.txtCorreo.setObjectName(u"txtCorreo")
        self.txtCorreo.setGeometry(QRect(138, 57, 133, 20))
        self.txtPass = QLineEdit(Practica)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setGeometry(QRect(138, 94, 133, 20))
        self.btnMostrar = QPushButton(Practica)
        self.btnMostrar.setObjectName(u"btnMostrar")
        self.btnMostrar.setGeometry(QRect(110, 130, 75, 23))
        self.btnEditar = QPushButton(Practica)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setGeometry(QRect(200, 130, 75, 23))
        self.lblId = QLabel(Practica)
        self.lblId.setObjectName(u"lblId")
        self.lblId.setGeometry(QRect(0, 0, 71, 16))

        self.retranslateUi(Practica)

        QMetaObject.connectSlotsByName(Practica)
    # setupUi

    def retranslateUi(self, Practica):
        Practica.setWindowTitle(QCoreApplication.translate("Practica", u"Datos", None))
        self.btnGuardar.setText(QCoreApplication.translate("Practica", u"Guardar", None))
        self.lblNombre.setText(QCoreApplication.translate("Practica", u"Nombre:", None))
        self.lblCorreo.setText(QCoreApplication.translate("Practica", u"Correo:", None))
        self.lblPass.setText(QCoreApplication.translate("Practica", u"Contrase\u00f1a:", None))
        self.btnMostrar.setText(QCoreApplication.translate("Practica", u"Mostrar", None))
        self.btnEditar.setText(QCoreApplication.translate("Practica", u"Modificar", None))
        self.lblId.setText("")
    # retranslateUi

