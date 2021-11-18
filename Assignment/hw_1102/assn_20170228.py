from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setHeight(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.display = QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 2)


        self.digitButton = [x for x in range(0, 10)]

        numLayout = QGridLayout()

        for d in range(1, 10):
            self.digitButton[d] = Button('%d' % d, self.buttonClicked)
            numLayout.addWidget(self.digitButton[d], 2-int((d-1) / 3), ((d-1) % 3))

        self.digitButton[0] = Button('0', self.buttonClicked)
        numLayout.addWidget(self.digitButton[0], 3, 0)

        self.decButton = Button('.', self.buttonClicked)
        self.eqButton = Button('=', self.buttonClicked)
        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        list_ = ['*', '/', '+', '-', '(', ')', 'C']
        index = 0
        for s in list_:
            btn = Button(s, self.buttonClicked)
            opLayout.addWidget(btn, index / 2, index % 2)
            index += 1

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("My Calculator")


    def buttonClicked(self):

        button = self.sender()
        key = button.text()

        if key == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
