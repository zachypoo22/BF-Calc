import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit,\
    QTextEdit, QPushButton, QLabel, QHBoxLayout, QInputDialog, QMessageBox

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.main()

    def setupUi(self):
        self.setWindowTitle("Body Fat Calculator")

        neckLabel = QLabel("Neck")
        waistLabel = QLabel("Waist")
        heightLabel = QLabel("Height")
        ftLabel = QLabel("ft")
        inLabel = QLabel("in")

        self.neckInput = QLineEdit()
        self.waistInput = QLineEdit()
        self.ftInput = QLineEdit()
        self.inInput = QLineEdit()

        self.butt = QPushButton("Submit")
        self.result = QLabel('body fat %: ')

        mainLayout = QVBoxLayout()
        neckLayout = QHBoxLayout()
        waistLayout = QHBoxLayout()
        heightLayout = QVBoxLayout()
        ftinLayout = QVBoxLayout()
        fLayout = QHBoxLayout()
        iLayout = QHBoxLayout()

        fLayout.addWidget(heightLabel)
        fLayout.addWidget(self.ftInput)
        fLayout.addWidget(ftLabel)

        iLayout.addWidget(QLabel('          '))
        iLayout.addWidget(self.inInput)
        iLayout.addWidget(inLabel)

        ftinLayout.addLayout(fLayout)
        ftinLayout.addLayout(iLayout)

        # heightLayout.addWidget(heightLabel)
        heightLayout.addLayout(ftinLayout)

        neckLayout.addWidget(neckLabel)
        neckLayout.addWidget(self.neckInput)
        neckLayout.addWidget(QLabel("in"))

        waistLayout.addWidget(waistLabel)
        waistLayout.addWidget(self.waistInput)
        waistLayout.addWidget(QLabel("in"))

        mainLayout.addLayout(neckLayout)
        mainLayout.addLayout(waistLayout)
        mainLayout.addLayout(heightLayout)
        mainLayout.addWidget(self.butt)
        mainLayout.addWidget(self.result)

        self.setLayout(mainLayout)
        self.show()

    def main(self):
        self.butt.clicked.connect(self.click)

    def click(self):
        try:
            neck = int(self.neckInput.text()) * 2.54 # convert to cm
            waist = int(self.waistInput.text()) * 2.54 # convert to cm
            height = ( int(self.ftInput.text())*12 + int(self.inInput.text()) ) * 2.54 # conversion to cm
        except Exception as e:
            print(e)

        fat = 495 / (1.0324 - .19077 * math.log10(waist - neck) + .15456 * math.log10(height)) - 450

        self.result.setText("Body fat %: " + str(fat))

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
