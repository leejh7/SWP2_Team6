import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()



    def initUI(self):

        name = QLabel("Name:")
        age = QLabel("Age:")
        score = QLabel("Score:")

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(name)
        hbox1.addWidget(self.nameEdit)
        hbox1.addWidget(age)
        hbox1.addWidget(self.ageEdit)
        hbox1.addWidget(score)
        hbox1.addWidget(self.scoreEdit)

        amount = QLabel("Amount:")
        key = QLabel("Key:")

        self.amountEdit = QLineEdit()
        self.keycombobox = QComboBox()

        self.keycombobox.addItem("Name")
        self.keycombobox.addItem("Age")
        self.keycombobox.addItem("Score")

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amountEdit)
        hbox2.addWidget(key)
        hbox2.addWidget(self.keycombobox)

        self.AddButton = QPushButton("Add")
        self.DelButton = QPushButton("Del")
        self.FindButton = QPushButton("Find")
        self.IncButton = QPushButton("Inc")
        self.ShowButton = QPushButton("Show")

        self.ShowButton.clicked.connect(self.showScoreDB)
        self.AddButton.clicked.connect(self.add)
        self.FindButton.clicked.connect(self.find)
        self.DelButton.clicked.connect(self.delete)
        self.IncButton.clicked.connect(self.inc)


        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.AddButton)
        hbox3.addWidget(self.DelButton)
        hbox3.addWidget(self.FindButton)
        hbox3.addWidget(self.IncButton)
        hbox3.addWidget(self.ShowButton)

        result = QLabel("Result:")
        self.resultEdit = QTextEdit()
        hbox4 = QHBoxLayout()
        hbox4.addWidget(result)
        hbox4.addWidget(self.resultEdit)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def showScoreDB(self):
        keyname = self.keycombobox.currentText()
        msg = ""
        for p in sorted(self.scoredb, key = lambda person : person[keyname]):
            for attr in sorted(p):
                msg += str(attr) + "=" + str(p[attr]) + " "
            msg += '\n'
        self.resultEdit.setPlainText(msg)

    def add(self):
        name = str(self.nameEdit.text())
        age = int(self.ageEdit.text())
        score = int(self.scoreEdit.text())
        record = {'Name':name,'Age':age,'Score':score}
        self.scoredb += [record]
        self.showScoreDB()

    def find(self):
        msg = ""
        for p in self.scoredb:
            if p['Name'] == self.nameEdit.text():
                msg += "Name:" + str(p['Name']) + " " + "Age:" + str(p['Age']) + " " + "Score:" + str(p['Score'])
                msg += '\n'
        self.resultEdit.setPlainText(msg)

        
    def delete(self):
        for p in reversed(self.scoredb):
            if p['Name'] == self.nameEdit.text():
                self.scoredb.remove(p)
        self.showScoreDB()

    def inc(self):
        add = int(self.amountEdit.text())
        for p in self.scoredb:
            if p['Name'] == self.nameEdit.text():
               p['Score'] = int(p['Score']) + add
        self.showScoreDB()


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
            for record in self.scoredb:
                record["Score"] = int(record["Score"])
                record["Age"] = int(record["Age"])

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
