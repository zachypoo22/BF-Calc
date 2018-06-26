import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit,\
    QTextEdit, QPushButton, QLabel, QHBoxLayout, QInputDialog, QGridLayout

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.height = 140
        self.width = 280
        self.top = 500
        self.left = 500

        self.setupUi()
        self.main()

    def setupUi(self):
        self.setWindowTitle("Body Fat Calculator")
        self.setGeometry(self.left, self.top, self.width, self.height)

        neckLabel = QLabel("Neck")
        waistLabel = QLabel("Waist")
        heightLabel = QLabel("Height")
        ftLabel = QLabel(" ft ")
        inLabel = QLabel("in")

        self.neckInput = QLineEdit()
        self.waistInput = QLineEdit()
        self.ftInput = QLineEdit()
        self.inInput = QLineEdit()

        self.butt = QPushButton("Submit")
        self.result = QLabel()

        heightLayout = QHBoxLayout()
        heightLayout.addWidget(self.ftInput)
        heightLayout.addWidget(ftLabel)
        heightLayout.addWidget(self.inInput)
        # heightLayout.addWidget(inLabel)

        inputLayout = QGridLayout()
        inputLayout.addWidget(waistLabel, 1, 0)
        inputLayout.addWidget(self.waistInput, 1, 1)
        inputLayout.addWidget(QLabel('in'), 1, 2)
        inputLayout.addWidget(neckLabel, 2, 0)
        inputLayout.addWidget(self.neckInput, 2, 1)
        inputLayout.addWidget(QLabel('in'), 2, 2)
        inputLayout.addWidget(heightLabel, 3, 0)
        inputLayout.addItem(heightLayout, 3, 1)
        inputLayout.addWidget(inLabel, 3, 2)
        # inputLayout.addWidget(self.ftInput,3, 1)
        # inputLayout.addWidget(ftLabel,3, 2)
        # inputLayout.addWidget(self.inInput, 4, 1)
        # inputLayout.addWidget(inLabel, 4, 2)

        # inputLayout.addWidget(self.butt, 5, 0)
        # inputLayout.addWidget(self.result, 6, 0, 5, 1)

        submitLayout = QHBoxLayout()
        submitLayout.addWidget(self.butt)
        submitLayout.addWidget(self.result)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(inputLayout)
        mainLayout.addLayout(submitLayout)

        self.setLayout(mainLayout)
        self.show()

    def main(self):
        self.butt.clicked.connect(self.click)

    def click(self):
        try:
            neck = float(self.neckInput.text()) * 2.54 # convert to cm
            waist = float(self.waistInput.text()) * 2.54 # convert to cm
            height = ( int(self.ftInput.text())*12 + float(self.inInput.text()) ) * 2.54 # conversion to cm
        except Exception as e:
            print(e)

        fat = 495 / (1.0324 - .19077 * math.log10(waist - neck) + .15456 * math.log10(height)) - 450

        self.result.setText("Body fat %: " + str(round(fat, 5)))


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
