# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-11-09 15:10:09
# @LastEditTime: 2020-11-09 15:33:21
# @LastEditors: kcyln
# @Description: 

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\123\locoyposter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(382, 426)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QLabel(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(20, 10, 54, 20))
        self.table.setObjectName("table")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 54, 12))
        self.label_5.setObjectName("label_5")
        self.table_name = QtWidgets.QLineEdit(self.centralwidget)
        self.table_name.setGeometry(QtCore.QRect(90, 10, 181, 20))
        self.table_name.setObjectName("table_name")
        self.mul_line = QtWidgets.QTextEdit(self.centralwidget)
        self.mul_line.setGeometry(QtCore.QRect(90, 40, 181, 61))
        self.mul_line.setObjectName("mul_line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 360, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 51, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 320, 54, 12))
        self.label_7.setObjectName("label_7")
        self.one_line = QtWidgets.QTextEdit(self.centralwidget)
        self.one_line.setGeometry(QtCore.QRect(90, 110, 271, 40))
        self.one_line.setObjectName("one_line")
        self.sql_line = QtWidgets.QTextEdit(self.centralwidget)
        self.sql_line.setGeometry(QtCore.QRect(90, 160, 271, 40))
        self.sql_line.setObjectName("sql_line")
        self.var_line = QtWidgets.QTextEdit(self.centralwidget)
        self.var_line.setGeometry(QtCore.QRect(90, 210, 271, 40))
        self.var_line.setObjectName("var_line")
        self.create_line = QtWidgets.QTextEdit(self.centralwidget)
        self.create_line.setGeometry(QtCore.QRect(90, 260, 271, 40))
        self.create_line.setObjectName("create_line")
        self.insert_line = QtWidgets.QTextEdit(self.centralwidget)
        self.insert_line.setGeometry(QtCore.QRect(90, 310, 271, 40))
        self.insert_line.setObjectName("insert_line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "浏览器SQL工具"))
        self.table.setText(_translate("MainWindow", "输入表名："))
        self.label_2.setText(_translate("MainWindow", "输入字段："))
        self.label_3.setText(_translate("MainWindow", "字段整理："))
        self.label_4.setText(_translate("MainWindow", "变量形式："))
        self.label_5.setText(_translate("MainWindow", "SQL 字段："))
        self.pushButton.setText(_translate("MainWindow", "执行"))
        self.label_6.setText(_translate("MainWindow", "建表语句："))
        self.label_7.setText(_translate("MainWindow", "插入语句："))

