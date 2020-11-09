# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-11-09 11:04:52
# @LastEditTime: 2020-11-09 15:11:17
# @LastEditors: kcyln
# @Description: 浏览器SQL工具

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from Ui_locoyposter import Ui_MainWindow


class QLocoyposterWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.__ui.pushButton.clicked.connect(self.changeValue)

    def changeValue(self):
        base_text = self.__ui.mul_line.toPlainText()
        if base_text:
            one_line = ",".join([i for i in base_text.split()])
            sql_line = ",".join([i + " varchar(250)" for i in base_text.split()])
            var_line = ",".join(["'{-var." + i + "-}'" for i in base_text.split()])

            create_sql = f"create table {self.__ui.table_name.text()} (id integer primary key autoincrement,{sql_line});"
            insert_sql = f"insert into {self.__ui.table_name.text()} ({one_line}) values ({var_line})"

            self.__ui.one_line.setText(one_line)
            self.__ui.sql_line.setText(sql_line)
            self.__ui.var_line.setText(var_line)
            self.__ui.create_line.setText(create_sql)
            self.__ui.insert_line.setText(insert_sql)
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    LocoyposterWindow = QLocoyposterWindow()
    LocoyposterWindow.show()
    sys.exit(app.exec_())
