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
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]

        for i in range(0, 10):
            self.digitButton[i] = Button(str(i), self.buttonClicked)

        # Function Buttons & Symbols
        functionSymbol = ['.', '=', '*', '/', '+', '-', '(', ')', 'C']

        self.functionButton = [x for x in functionSymbol]

        for i, symbol in enumerate(functionSymbol):
            self.functionButton[i] = Button(symbol, self.buttonClicked)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        numLayout.addWidget(self.digitButton[0], 3, 0)
        idx = 1
        for row in reversed(range(3)):
            for col in range(3):
                numLayout.addWidget(self.digitButton[idx], row, col)
                idx += 1

        numLayout.addWidget(self.functionButton[0], 3, 1)
        numLayout.addWidget(self.functionButton[1], 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        idx = 2
        for row in range(0, 3):
            for col in range(0, 2):
                opLayout.addWidget(self.functionButton[idx], row, col)
                idx += 1
        opLayout.addWidget(self.functionButton[idx], 3, 0)

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
