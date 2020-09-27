# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-09-27 14:51:37
# @LastEditTime: 2020-09-27 21:18:30
# @LastEditors: kcyln
# @Description: pyqt5菜单和工具栏


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 菜单栏
        exitAction = QAction(QIcon('images/yjtp.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit app')
        exitAction.triggered.connect(qApp.quit)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        # 工具栏
        exit_action = QAction(QIcon('images/yjtp.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+W')
        exit_action.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exit_action)
        
        # 状态栏
        self.statusBar().showMessage("Ready")
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('StatusBar')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())