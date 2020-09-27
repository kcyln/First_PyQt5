# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-09-25 17:18:30
# @LastEditTime: 2020-09-27 21:16:23
# @LastEditors: kcyln
# @Description: pyqt5第一次使用，基本功能介绍

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        # 设置提示文本
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('main window')
        btn = QPushButton('Button', self)
        btn.setToolTip('button window')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        # 设置关闭按钮
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(130, 50)
        # 设置窗口位置，大小，图标
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('images/yjtp.png'))
        # 窗口显示到屏幕中心
        self.center()
        # 窗口显示到桌面上
        self.show()
    
    def closeEvent(self, event):
        # 重写关闭事件，点击关闭时弹窗选择是否关闭
        reply = QMessageBox.question(self, 'Message', 'Are you sure?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def center(self):
        # 显示在屏幕中心位置
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    
    sys.exit(app.exec_())
