import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QFormLayout)
from PyQt5.QtCore import Qt

class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB(self.scoredb, 'Name')

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        name = QLabel("Name:")
        self.nameEdit = QLineEdit(self)
        age = QLabel("Age:")
        self.ageEdit = QLineEdit(self)
        score = QLabel("Score:")
        self.scoreEdit = QLineEdit(self)

        amount = QLabel("Amount:")
        self.amountEdit = QLineEdit(self)
        key = QLabel("Key:")
        self.keyComb = QComboBox(self)
        self.keyComb.addItem('Name')
        self.keyComb.addItem('Age')
        self.keyComb.addItem('Score')

        addBtn = QPushButton('Add')
        addBtn.clicked.connect(self.addFunc)
        delBtn = QPushButton('Del')
        delBtn.clicked.connect(self.delFunc)
        findBtn = QPushButton('Find')
        findBtn.clicked.connect(self.findFunc)
        incBtn = QPushButton('Inc')
        incBtn.clicked.connect(self.incFunc)
        showBtn = QPushButton('Show')
        showBtn.clicked.connect(self.showFunc)

        result = QLabel("Result:")
        self.resultEdit = QTextEdit(self)
        self.resultEdit.setReadOnly(True)

        hBox1 = QHBoxLayout()
        hBox1.addWidget(name)
        hBox1.addWidget(self.nameEdit)
        hBox1.addWidget(age)
        hBox1.addWidget(self.ageEdit)
        hBox1.addWidget(score)
        hBox1.addWidget(self.scoreEdit)

        hBox2 = QHBoxLayout()
        hBox2.addStretch(2)
        hBox2.addWidget(amount)
        hBox2.addWidget(self.amountEdit)
        hBox2.addWidget(key)
        hBox2.addWidget(self.keyComb)

        hBox3 = QHBoxLayout()
        hBox3.addStretch(1)
        hBox3.addWidget(addBtn)
        hBox3.addWidget(delBtn)
        hBox3.addWidget(findBtn)
        hBox3.addWidget(incBtn)
        hBox3.addWidget(showBtn)

        hBox4 = QHBoxLayout()
        hBox4.addWidget(result)

        hBox5 = QHBoxLayout()
        hBox5.addWidget(self.resultEdit)

        vBox = QVBoxLayout()
        vBox.addLayout(hBox1)
        vBox.addLayout(hBox2)
        vBox.addLayout(hBox3)
        vBox.addLayout(hBox4)
        vBox.addLayout(hBox5)

        self.setLayout(vBox)
        self.show()

    def addFunc(self):
        if not (self.ageEdit.text().isdigit() and self.scoreEdit.text().isdigit()):
            print('Age or Score is not integer type')
        record = {'Name': self.nameEdit.text(), 'Age': int(self.ageEdit.text()), 'Score': int(self.scoreEdit.text())}
        self.scoredb += [record]
        self.showScoreDB(self.scoredb, self.keyComb.currentText())

    def delFunc(self):
        target = False
        for p in reversed(self.scoredb):
            if p['Name'] == self.nameEdit.text():
                self.scoredb.remove(p)
                target = True
        if not target:
            print('Name is not exist')
        self.showScoreDB(self.scoredb, self.keyComb.currentText())

    def findFunc(self):
        targetScdb = []
        target = False
        for p in self.scoredb:
            if p['Name'] == self.nameEdit.text():
                targetScdb.append(p)
                target = True
        if not target:
            print('Name is not exist')
        self.showScoreDB(targetScdb, self.keyComb.currentText())

    def incFunc(self):
        target = False
        if not self.amountEdit.text().isdigit():
            print('Score is not integer type')
        for p in self.scoredb:
            if p.get('Name') == self.nameEdit.text():
                p['Score'] += int(self.amountEdit.text())
                target = True
        if not target:
            print('Name is not exist')
        self.showScoreDB(self.scoredb, self.keyComb.currentText())

    def showFunc(self):
        sortKey = self.keyComb.currentText()
        self.showScoreDB(self.scoredb, sortKey)

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

    def showScoreDB(self, scdb, keyname):
        texts = ''
        for p in sorted(scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                texts += f'{attr}={p[attr]}\t\t'
            texts += '\n'
        self.resultEdit.setText(texts)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

