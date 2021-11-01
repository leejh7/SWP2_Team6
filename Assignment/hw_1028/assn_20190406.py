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
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        Name = QLabel("Name: ")
        Age = QLabel("Age: ")
        Score = QLabel("Score: ")
        Amount = QLabel("Amount: ")
        Key = QLabel("Key: ")
        Result = QLabel("Result: ")

        self.nameEdit = QLineEdit(self)
        self.ageEdit = QLineEdit(self)
        self.scoreEdit = QLineEdit(self)
        self.amountEdit = QLineEdit(self)
        self.keyCombo = QComboBox(self)
        self.resultEdit = QTextEdit(self)
        self.resultEdit.setReadOnly(True)

        self.keyCombo.addItem("Name")
        self.keyCombo.addItem("Age")
        self.keyCombo.addItem("Score")

        Add = QPushButton("Add")
        Del = QPushButton("Del")
        Find = QPushButton("Find")
        Inc = QPushButton("Inc")
        Show = QPushButton("show")

        # hbox
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(Name)
        hbox.addWidget(self.nameEdit)
        hbox.addWidget(Age)
        hbox.addWidget(self.ageEdit)
        hbox.addWidget(Score)
        hbox.addWidget(self.scoreEdit)

        # hbox_1
        hbox_1 = QHBoxLayout()
        hbox_1.addStretch(1)
        hbox_1.addWidget(Amount)
        hbox_1.addWidget(self.amountEdit)
        hbox_1.addWidget(Key)
        hbox_1.addWidget(self.keyCombo)

        # hbox_2
        hbox_2 = QHBoxLayout()
        hbox_2.addStretch(1)
        hbox_2.addWidget(Add)
        hbox_2.addWidget(Del)
        hbox_2.addWidget(Find)
        hbox_2.addWidget(Inc)
        hbox_2.addWidget(Show)

        # hbox_3
        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(Result)

        # hbox_4
        hbox_4 = QHBoxLayout()
        hbox_4.addWidget(self.resultEdit)

        # vbox
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        vbox.addLayout(hbox_3)
        vbox.addLayout(hbox_4)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.show()

        Add.clicked.connect(self.Add_button)
        Del.clicked.connect(self.Del_button)
        Find.clicked.connect(self.Find_button)
        Inc.clicked.connect(self.Inc_button)
        Show.clicked.connect(self.showScoreDB)


    def Add_button(self):
        Name = self.nameEdit.text()
        Age = int(self.ageEdit.text())
        Score = int(self.scoreEdit.text())
        record = {'Name': Name, 'Age':Age, 'Score':Score}
        self.scoredb += record
        self.showScoreDB()

    def Del_button(self):
        Name = self.nameEdit.text()
        for p in reversed(self.scoredb):
            if p['Name'] == Name:
                self.scoredb.remove(p)
                target_exist = True
        self.showScoreDB()

    def Find_button(self):
        Name = self.nameEdit.text()
        self.showScoreDB(Name)

    def Inc_button(self):
        Name = self.NameEdit.text()
        Amount = int(self.AmountEdit.text())
        for p in self.scoredb:
            if p['Name'] == Name:
                p['Score'] += int(Amount)
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
            self.scoredb =  pickle.load(fH)
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

    #####
    def showScoreDB(self, keyname=None):
        keyname = self.keyCombo.currentText()
        texts = ''
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                texts += f'{attr}={p[attr]}\t\t'
            texts += '\n'
        self.resultEdit.setText(texts)


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

