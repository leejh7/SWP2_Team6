import pickle
import sys
import os

from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout)
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets



class Button(QPushButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setText(text)
        self.clicked.connect(callback)


class ass6(object):

    def __init__(self):
        super().__init__()
        self.initUI(Form)
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB(self.scoredb, 'Name')

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, scdb, keyname):
        s = ''
        for p in sorted(scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                s += f'{attr}={p[attr]}\t\t'
            s += '\n'
        self.textEdit.setText(s)

    def doScoreDB(self):
        button = self.sender()
        key = button.text()

        if key == 'Add':
            if not (self.ageEdit.text().isdigit() and self.scoreEdit.text().isdigit()):
                raise Exception('Enter the age and score in integer form')
            else:
                record = {'Name': self.lineEdit.text(), 'Age': self.lineEdit_2.text(), 'Score': self.lineEdit_3.text()}
                self.scoredb += [record]

                self.showScoreDB(self.scoredb, self.comboBox.currentText())
        elif key == 'Del':
            for p in reversed(self.scoredb):
                if p['Name'] == self.nameEdit.text():
                    self.scoredb.remove(p)
                    target_exist = True
            if not target_exist:
                raise Exception('There\'s no target to Delete')
            self.showScoreDB(self.scoredb, self.keyComb.currentText())
        elif key == 'Find':
            target_scdb = []
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    target_scdb.append(p)
                    target_exist = True
            if not target_exist:
                raise Exception('There\'s no target to Find')
            self.showScoreDB(target_scdb, self.keyComb.currentText())
        elif key == 'Inc':
            if not self.amountEdit.text().isdigit():
                raise Exception('Enter score in integer form')
            for p in self.scoredb:
                if p.get('Name') == self.nameEdit.text():
                    p['Score'] += int(self.amountEdit.text())
                    target_exist = True
            if not target_exist:
                raise Exception('There\'s no target to Increase')
            self.showScoreDB(self.scoredb, self.keyComb.currentText())
        else:
            sortKey = self.keyComb.currentText()
            self.showScoreDB(self.scoredb, sortKey)

    def initUI(self, Form):

        Form.setObjectName("Assignment6")
        Form.resize(834, 574)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 70, 701, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        # self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.label.setText("Name:")
        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Age:")
        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Score:")
        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(440, 110, 331, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setText("Amount:")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)

        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("Key:")
        self.horizontalLayout_2.addWidget(self.label_5)

        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Name")
        self.comboBox.addItem("Age")
        self.comboBox.addItem("Score")
        self.horizontalLayout_2.addWidget(self.comboBox)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(150, 140, 621, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)

        self.pushButton = Button('Add', self.doScoreDB)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Del")
        self.pushButton_2.clicked.connect(self.doScoreDB)
        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Find")
        self.pushButton_3.clicked.connect(self.doScoreDB)
        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setText("Inc")
        self.pushButton_4.clicked.connect(self.doScoreDB)
        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setText("Show")
        self.pushButton_5.clicked.connect(self.doScoreDB)
        self.horizontalLayout_3.addWidget(self.pushButton_5)

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 210, 701, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.label_6.setText("Result:")
        self.verticalLayout.addWidget(self.label_6)

        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        # self.textEdit.setText(self.readScoreDB)
        self.verticalLayout.addWidget(self.textEdit)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ass6()
    Form.show()
    ui.initUI(Form)

    sys.exit(app.exec_())
