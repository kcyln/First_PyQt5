# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-11-07 17:51:58
# @LastEditTime: 2020-11-09 20:41:42
# @LastEditors: kcyln
# @Description: pyqt5拖拽--拖放一个按钮

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag


class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)
        
    def mouseMoveEvent(self, event):
        if event.buttons() != Qt.RightButton:
            return
        
        mimeData = QMimeData()
        dragData = QDrag(self)
        dragData.setMimeData(mimeData)
        dragData.setHotSpot(event.pos() - self.rect().topLeft())

        dropAction = dragData.exec_(Qt.MoveAction)
    
    def mousePressEvent(self, event):
        QPushButton.mousePressEvent(self, event)

        if event.buttons() == Qt.LeftButton:
            print('press')


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setAcceptDrops(True)
        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Press')
        self.setGeometry(300, 300, 280, 150)
    
    def dragEnterEvent(self, event):
        event.accept()
    
    def dropEvent(self, event):
        position = event.pos()
        self.button.move(position)

        event.setDropAction(Qt.MoveAction)
        event.accept()
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())