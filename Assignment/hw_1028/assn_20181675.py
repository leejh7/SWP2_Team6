import pickle
import sys
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (QMessageBox, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import QCoreApplication


class Button(QPushButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setText(text)
        self.clicked.connect(callback)


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB(self.scoredb, 'Name')

    def initUI(self):
        self.display = QTextEdit()
        self.display.setReadOnly(True)

        firstLayout = QHBoxLayout()
        secondLayout = QHBoxLayout()
        secondLayout.addStretch(2)
        thirdLayout = QHBoxLayout()
        thirdLayout.addStretch(1)
        lastLayout = QHBoxLayout()

        self.nameEdit = QLineEdit(self)
        self.ageEdit = QLineEdit(self)
        self.scoreEdit = QLineEdit(self)
        self.amountEdit = QLineEdit(self)
        self.keyComb = QComboBox(self)
        self.keyComb.addItems(['Name', 'Age', 'Score'])

        labelGroups = [
            {'text': 'Name:', 'layout': firstLayout},
            {'text': 'Age:', 'layout': firstLayout},
            {'text': 'Score:', 'layout': firstLayout},
            {'text': 'Amount:', 'layout': secondLayout},
            {'text': 'Key:', 'layout': secondLayout},
            {'text': 'Result:', 'layout': lastLayout}
        ]

        editGroups = [
            self.nameEdit,
            self.ageEdit,
            self.scoreEdit,
            self.amountEdit,
            self.keyComb,
            None
        ]

        buttonGroups = [
            {'text': 'Add', 'layout': thirdLayout},
            {'text': 'Del', 'layout': thirdLayout},
            {'text': 'Find', 'layout': thirdLayout},
            {'text': 'Inc', 'layout': thirdLayout},
            {'text': 'Show', 'layout': thirdLayout}
        ]

        for label, edit in zip(labelGroups, editGroups):
            label['layout'].addWidget(QLabel(label['text']))
            if label['layout'] == lastLayout:
                break
            label['layout'].addWidget(edit)

        for btn in buttonGroups:
            button = Button(btn['text'], self.doScoreDB)
            btn['layout'].addWidget(button)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(firstLayout)
        mainLayout.addLayout(secondLayout)
        mainLayout.addLayout(thirdLayout)
        mainLayout.addLayout(lastLayout)
        mainLayout.addWidget(self.display)

        self.setLayout(mainLayout)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def clearEdit(self):
        editGroups = [
            self.nameEdit,
            self.ageEdit,
            self.scoreEdit,
            self.amountEdit
        ]
        for edit in editGroups:
            edit.clear()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            QMessageBox.warning(
                self, 'Empty DB', f'Empty DB: {self.dbfilename}')
        else:
            reply = QMessageBox.information(
                self, 'Open DB', f'Are you sure to Open DB: {self.dbfilename}',
                QMessageBox.Yes | QMessageBox.No
            )

        fH.close()

        if reply == QMessageBox.Yes:
            return
        else:
            self.closeEvent(QCloseEvent())
            sys.exit()

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
        self.display.setText(texts)

    def doScoreDB(self):
        button = self.sender()
        command = button.text()
        try:
            target_exist = False
            if command == 'Add':
                if not(self.ageEdit.text().isdigit() and self.scoreEdit.text().isdigit()):
                    raise Exception('Enter the age and score in integer form')
                record = {'Name': self.nameEdit.text(), 'Age': int(self.ageEdit.text()),
                          'Score': int(self.scoreEdit.text())}
                self.scoredb += [record]
                self.clearEdit()
                self.showScoreDB(self.scoredb, self.keyComb.currentText())
            elif command == 'Del':
                for p in reversed(self.scoredb):
                    if p['Name'] == self.nameEdit.text():
                        self.scoredb.remove(p)
                        target_exist = True
                if not target_exist:
                    raise Exception('There\'s no target to Delete')
                self.clearEdit()
                self.showScoreDB(self.scoredb, self.keyComb.currentText())
            elif command == 'Find':
                target_scdb = []
                for p in self.scoredb:
                    if p['Name'] == self.nameEdit.text():
                        target_scdb.append(p)
                        target_exist = True
                if not target_exist:
                    raise Exception('There\'s no target to Find')
                self.clearEdit()
                self.showScoreDB(target_scdb, self.keyComb.currentText())
            elif command == 'Inc':
                if not self.amountEdit.text().isdigit():
                    raise Exception('Enter score in integer form')
                for p in self.scoredb:
                    if p.get('Name') == self.nameEdit.text():
                        p['Score'] += int(self.amountEdit.text())
                        target_exist = True
                if not target_exist:
                    raise Exception('There\'s no target to Increase')
                self.clearEdit()
                self.showScoreDB(self.scoredb, self.keyComb.currentText())
            else:
                sortKey = self.keyComb.currentText()
                self.showScoreDB(self.scoredb, sortKey)
        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
