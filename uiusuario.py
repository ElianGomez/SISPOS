# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiusuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Usuario(object):
    def setupUi(self, Usuario):
        Usuario.setObjectName("Usuario")
        Usuario.resize(1435, 650)
        Usuario.setStyleSheet("*{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Usuario)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("*{\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignTop)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("*{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel{\n"
"    color: rgb(0, 0, 0);\n"
"    height: 25;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(228, 236, 236);\n"
"    border-radius: 5px;\n"
"    height: 50;    \n"
"}\n"
"\n"
"QPushButton{\n"
"    border: none;\n"
"    border: 15px solid rgb(228, 236, 236);\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(228, 236, 236);\n"
"    text-align: center;\n"
"\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(11)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.busidusu = QtWidgets.QLineEdit(self.frame_4)
        self.busidusu.setObjectName("busidusu")
        self.horizontalLayout_2.addWidget(self.busidusu)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.busnombre = QtWidgets.QLineEdit(self.frame_4)
        self.busnombre.setObjectName("busnombre")
        self.horizontalLayout_2.addWidget(self.busnombre)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.busapellido = QtWidgets.QLineEdit(self.frame_4)
        self.busapellido.setObjectName("busapellido")
        self.horizontalLayout_2.addWidget(self.busapellido)
        self.verticalLayout_2.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("*{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel{\n"
"    color: rgb(0, 0, 0);\n"
"    height: 25;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(228, 236, 236);\n"
"    border-radius: 5px;\n"
"    height: 50;    \n"
"}\n"
"\n"
"QPushButton{\n"
"    border: none;\n"
"    border: 15px solid rgb(228, 236, 236);\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(228, 236, 236);\n"
"    text-align: center;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tablausuario = QtWidgets.QTableWidget(self.frame_2)
        self.tablausuario.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablausuario.setDragDropOverwriteMode(True)
        self.tablausuario.setAlternatingRowColors(True)
        self.tablausuario.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tablausuario.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tablausuario.setGridStyle(QtCore.Qt.SolidLine)
        self.tablausuario.setObjectName("tablausuario")
        self.tablausuario.setColumnCount(7)
        self.tablausuario.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablausuario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablausuario.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablausuario.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablausuario.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablausuario.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablausuario.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablausuario.setHorizontalHeaderItem(6, item)
        self.tablausuario.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_3.addWidget(self.tablausuario)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        Usuario.setCentralWidget(self.centralwidget)

        self.retranslateUi(Usuario)
        QtCore.QMetaObject.connectSlotsByName(Usuario)

    def retranslateUi(self, Usuario):
        _translate = QtCore.QCoreApplication.translate
        Usuario.setWindowTitle(_translate("Usuario", "MainWindow"))
        self.label.setText(_translate("Usuario", "Usuarios"))
        self.label_4.setText(_translate("Usuario", "Buscar Por Id"))
        self.label_3.setText(_translate("Usuario", "Busqueda por nombre"))
        self.label_2.setText(_translate("Usuario", "Busqueda por apellido"))
        item = self.tablausuario.horizontalHeaderItem(0)
        item.setText(_translate("Usuario", "ID del Usuario"))
        item = self.tablausuario.horizontalHeaderItem(1)
        item.setText(_translate("Usuario", "Cedula"))
        item = self.tablausuario.horizontalHeaderItem(2)
        item.setText(_translate("Usuario", "Nombre Sucursal"))
        item = self.tablausuario.horizontalHeaderItem(3)
        item.setText(_translate("Usuario", "Nombre Usuario"))
        item = self.tablausuario.horizontalHeaderItem(4)
        item.setText(_translate("Usuario", "Apellido Usuario"))
        item = self.tablausuario.horizontalHeaderItem(5)
        item.setText(_translate("Usuario", "Correo Usuario"))
        item = self.tablausuario.horizontalHeaderItem(6)
        item.setText(_translate("Usuario", "Telefono Usuario"))