"""
 * @Author: kcyln
 * @Date: 2020-09-27 11:50:37
 * @LastEditTime: 2020-09-27 14:51:02
 * @LastEditors: kcyln
 * @Description: pyqt5布局管理
"""

import sys

from PyQt5.QtWidgets import QGridLayout, QWidget, QLabel, QApplication

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication

from PyQt5.QtWidgets import QLineEdit, QTextEdit

class Example(QWidget):
    """
    绝对定位：使用move()来控制控件的位置
    """

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        lbl1 = QLabel('zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('绝对定位')
        self.show()


class Boxlayout(QWidget):
    """
    框布局：使用QHBoxLayout和QVBoxLayout，来分别创建横向布局和纵向布局。
    """
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout() # 水平布局
        # 伸展因子，使按钮靠左或靠右显示，此处位于按钮前面，所以按钮会靠右显示
        hbox.addStretch(1) 
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout() # 垂直布局
        # 伸展因子，使按钮靠上或靠下显示，此处位于按钮前面，所以按钮会靠下显示
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Buttons')
        self.show()


class GridLayout(QWidget):
    """
    表格布局: 将空间划分为行和列。我们使用QGridLayout类创建一个网格布局。
    """
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == "":
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()
        

class Comment(QWidget):
    """
    控件可以在网格中跨越多个行或列。在这个示例中,我们说明了这一点。
    """
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        title = QLabel('title')
        author = QLabel('author')
        review = QLabel('review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
 
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
 
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')    
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # ex = Example()
    # box = Boxlayout()
    # grid = GridLayout()
    comment = Comment()
    sys.exit(app.exec_())
