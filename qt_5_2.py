# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-09-28 20:40:12
# @LastEditTime: 2020-09-28 20:52:11
# @LastEditors: kcyln
# @Description: pyqt5对话框--文件对话框

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('images/yjtp.png'), "Open", self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        meunbar = self.menuBar()
        fileMenu = meunbar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()       
    
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '/home')
        print(fname)  # fname = ('/home/kcyln/nohup.out', 'All Files (*)')
        if fname[0]:
            with open(fname[0], 'r') as f:
                data = f.read()
                self.textEdit.setText(data)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())