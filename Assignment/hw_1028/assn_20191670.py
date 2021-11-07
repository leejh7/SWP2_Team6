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
        self.showScoreDB('Name')

    def initUI(self):
        label_text = ['Name: ', 'Age: ', 'Score: ', 'Amount: ', 'Key: ', 'Result: ']
        labels = []
        for lb in label_text:
            labels.append(QLabel(lb))

        self.line_Name = QLineEdit(self)
        self.line_Age = QLineEdit(self)
        self.line_Score = QLineEdit(self)
        self.line_Amount = QLineEdit(self)
        self.text_Result = QTextEdit(self)
        self.combo_Key = QComboBox(self)
        self.combo_Key.addItems(['Name', 'Age', 'Score'])

        button_text = ['Add', 'Del', 'Find', 'Inc', 'Show']
        buttons = []
        for bt in button_text:
            buttons.append(QPushButton(bt))

        button_func = [self.addButton, self.delButton, self.findButton, self.incButton, self.showButton]
        for i in range(len(buttons)):
            buttons[i].clicked.connect(button_func[i])

        layout1_lines = [self.line_Name, self.line_Age, self.line_Score]
        layout1 = QHBoxLayout()
        for i in range(len(layout1_lines)):
            layout1.addWidget(labels[i])
            layout1.addWidget(layout1_lines[i])

        layout2 = QHBoxLayout()
        layout2.addStretch(1)
        layout2.addWidget(labels[3])
        layout2.addWidget(self.line_Amount)
        layout2.addWidget(labels[4])
        layout2.addWidget(self.combo_Key)

        layout3 = QHBoxLayout()
        layout3.addStretch(1)
        for bt in buttons:
            layout3.addWidget(bt)

        layout4 = QVBoxLayout()
        layout4.addWidget(labels[5])
        layout4.addWidget(self.text_Result)

        layouts = [layout1, layout2, layout3, layout4]
        layout5 = QVBoxLayout()
        for lo in layouts:
            layout5.addLayout(lo)

        self.setLayout(layout5)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

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
            print('Empty DB: ', self.dbfilename)
        else:
            print('Open DB: ', self.dbfilename)

        fH.close()

    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, keyname):
        tmp = ''
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            cnt = 1
            for attr in sorted(p):
                tmp += (attr + '=' + str(p[attr]) + '\t' * cnt)
                cnt += 1
            tmp += '\n'
        self.text_Result.setText(tmp)

    def addButton(self):
        record = {'Name': self.line_Name.text(), 'Age': int(self.line_Age.text()), 'Score': int(self.line_Score.text())}
        self.scoredb += [record]
        self.showScoreDB('Name')

    def delButton(self):
        for p in self.scoredb:
            if p['Name'] == self.line_Name.text():
                self.scoredb.remove(p)
        self.showScoreDB('Name')

    def findButton(self):
        tmp = ''
        for p in self.scoredb:
            if p['Name'] == self.line_Name.text():
                cnt = 1
                for attr in sorted(p):
                    tmp += (attr + '=' + str(p[attr]) + '\t' * cnt)
                    cnt += 1
                tmp += '\n'
        self.text_Result.setText(tmp)

    def incButton(self):
        for p in self.scoredb:
            if p['Name'] == self.line_Name.text():
                p['Score'] += int(self.line_Amount.text())
        self.showScoreDB('Name')

    def showButton(self):
        key = self.combo_Key.currentText()
        self.showScoreDB(self.scoredb, key)

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())