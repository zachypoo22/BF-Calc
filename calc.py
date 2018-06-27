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

        self.neck = 0

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
        self.waistLabel = QLabel()

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

        bottomLayout = QVBoxLayout()

        submitLayout = QHBoxLayout()
        submitLayout.addWidget(self.butt)
        submitLayout.addWidget(self.result)

        bottomLayout.addLayout(submitLayout)
        bottomLayout.addWidget(self.waistLabel)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(inputLayout)
        mainLayout.addLayout(bottomLayout)

        self.setLayout(mainLayout)
        self.show()

    def main(self):
        self.butt.clicked.connect(self.click)
        # print(self.waist_sizes())
        # print(self.waist_sizes().values())

    def click(self):
        try:
            self.neck = float(self.neckInput.text()) * 2.54 # convert to cm
            waist = float(self.waistInput.text()) * 2.54 # convert to cm
            self.height = ( int(self.ftInput.text())*12 + float(self.inInput.text()) ) * 2.54 # conversion to cm

            fat = 495 / (1.0324 - .19077 * math.log10(waist - self.neck) + .15456 * math.log10(self.height)) - 450

            self.result.setText("Body fat %: " + str(round(fat, 5)))

        except Exception as e:
            print(e)

        # print(self.waist_sizes())
        waists = "Essential: {ess} Athletic: {athl} Fit: {fit} Average: {avg}".format(**self.waist_sizes())
        self.waistLabel.setText(waists)

    def waist_sizes(self):
        dic = {'ess':0, 'athl': 0, 'fit' : 0, 'avg' : 0}

        for i in range (25, 50):
            fat = 495 / (1.0324 - .19077 * math.log10(i*2.54 - self.neck) + .15456 * math.log10(self.height)) - 450
            if math.floor(fat) in [1,2,3,4,5]: dic['essential [5%]'] = i;
            if math.floor(fat) in [6,7,8,9,10,11,12,13]: dic['Athletic [13%]'] = i;
            if math.floor(fat) in [14,15,16,17]: dic['fit [17%]'] = i;
            if math.floor(fat) in [18,19,20,21,22,23,24,25]: dic['average [25%]'] = i;

        # waist = math.pow(10, ((-495 / ( fat + 450 - + .15456 * math.log10(height)) ) - 1.0324 ) / .19077 ) + neck
        # waist = math.pow( 10, (((495 / fat) + 450 - .15456 * math.log10(height)) - 1.0324)/ - .19077) + neck
        return (dic)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
