# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-11-09 21:08:01
# @LastEditTime: 2020-11-09 21:30:02
# @LastEditors: kcyln
# @Description: pyqt5绘图--画点、颜色、画笔、笔刷


import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        # self.drawPoints(qp)
        # self.drawRectangles(qp)
        # self.drawLines(qp)
        self.drawBrushes(qp)
        qp.end()
    
    def drawPoints(self, qp):
        # 画点，随机1000个点
        qp.setPen(Qt.red)
        size = self.size()
        
        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)

    def drawRectangles(self, qp):
        # 颜色，三个颜色不同的矩形
        col = QColor(0, 0, 0)
        col.setNamedColor("#d4d4d4")
        qp.setPen(col)

        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)
 
        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 90, 60)
    
    def drawLines(self, qp):
        # QPen(画笔)，此处画了6条线段，其中前5条为预定义样式，最后一条为自定义样式
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)
 
        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)
 
        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)
 
        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)
 
        pen.setStyle(Qt.CustomDashLine)
        # 该方法，它的参数(一个数字列表)定义了一种风格，必须有偶数个数字；
        # 其中奇数表示绘制实线，偶数表示留空。数值越大，直线或空白就越大。
        # 这里我们定义了1像素的实线，4像素的空白，5像素实线，4像素空白
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)
    
    def drawBrushes(self, qp):
        # 笔刷
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

        brush.setStyle(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)
 
        brush.setStyle(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)
 
        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)
 
        brush.setStyle(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)
 
        brush.setStyle(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)
 
        brush.setStyle(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)
 
        brush.setStyle(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)
 
        brush.setStyle(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())