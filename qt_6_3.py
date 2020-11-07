# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-11-07 16:51:37
# @LastEditTime: 2020-11-07 17:30:37
# @LastEditors: kcyln
# @Description: pyqt5控件--日历控件

import sys
from PyQt5.QtWidgets import QWidget, QCalendarWidget, QLabel, QApplication
from PyQt5.QtCore import QDate


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 日历控件
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)
        
        self.lb1 = QLabel(self)
        date = cal.selectedDate()
        self.lb1.setText(date.toString())
        self.lb1.move(130, 260)
        
        self.setGeometry(300, 300, 550, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        # 显示选择的日期
        self.lb1.setText(date.toString())
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())