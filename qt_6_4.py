# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-11-07 17:01:46
# @LastEditTime: 2020-11-07 17:17:42
# @LastEditors: kcyln
# @Description: pyqt5控件--QPixmap和QLineEdit

import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication, QLineEdit
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # QPixmap
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('./images/yjtp.png')
        
        lb1 = QLabel(self)
        lb1.setPixmap(pixmap)
        
        # QLineEdit
        self.lb2 = QLabel(self)
        qle = QLineEdit(self)

        qle.move(300 ,100)
        self.lb2.move(200, 40)
        
        qle.textChanged[str].connect(self.onChanged)

        hbox.addWidget(lb1)
        hbox.addWidget(self.lb2)
        self.setLayout(hbox)
        
        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()

    def onChanged(self, text):
        self.lb2.setText(text)
        self.lb2.adjustSize() # 将控件尺寸调整为文本长度
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())