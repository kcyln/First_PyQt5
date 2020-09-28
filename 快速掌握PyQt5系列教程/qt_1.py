# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-09-28 17:10:37
# @LastEditTime: 2020-09-28 17:36:15
# @LastEditors: kcyln
# @Description: 信号与槽

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.btn = QPushButton('123', self)
        self.btn.clicked.connect(self.change_text)

        self.show()

    def change_text(self):
        print('haha')
        self.btn.setText('456')
        self.btn.clicked.disconnect(self.change_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
