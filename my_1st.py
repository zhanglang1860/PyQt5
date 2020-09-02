# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_1st.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

import chart_studio
chart_studio.tools.set_credentials_file(
    username='zhanglang86', # 这儿就不放我自己的账号和api了
    api_key='MxJLQuDBGkAVEZI7f2J0'
    )
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(543, 409)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(354, 322, 111, 31))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 140, 111, 51))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.label.update)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "打开风资源Excel"))
        self.label.setText(_translate("Form", "TextLabel"))

    def update(self):
        sender = self.sender()
        self.label.setText(sender.text() + ' was pressed')
        # self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
