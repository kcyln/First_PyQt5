# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-11-07 17:39:02
# @LastEditTime: 2020-11-07 17:51:39
# @LastEditors: kcyln
# @Description: pyqt5拖拽--简单拖放

import sys
from PyQt5.QtWidgets import QPushButton, QLineEdit, QApplication, QWidget


class Button(QPushButton):
    """
    重写两个方法使QPushButton接受拖放操作
    """
    def __init__(self, title, parent):
        super().__init__(title, parent)
        # 使该控件接受drop(放下)事件
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, e):
        # 重新实现了dragEnterEvent()方法，并设置可接受的数据类型(在这里是普通文本)
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
    
    def dropEvent(self, e):
        # 事件发生时改变按钮显示的文字
        self.setText(e.mimeData().text())


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        edit = QLineEdit('', self)
        # QLineEdit内置了对drag(拖动)操作的支持。我们只需要调用setDragEnabled()方法就可以了。
        edit.setDragEnabled(True)
        edit.move(30, 65)
        
        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag & drop')
        self.setGeometry(300, 300, 300, 150)
        self.show()

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())