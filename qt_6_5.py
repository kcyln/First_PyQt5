# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-11-07 17:18:00
# @LastEditTime: 2020-11-07 17:31:56
# @LastEditors: kcyln
# @Description: pyqt5控件--QSplitter

import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QSplitter, QStyleFactory, QApplication
from PyQt5.QtCore import Qt


class Example(QWidget):
    """
    通过QSplitter，用户可以拖动子控件边界来调整子控件的尺寸。
    """
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        # 使用一个风格框架为了看到QFrame小部件之间的界限
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())