import cmath
import numpy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton, QMessageBox

class Ui_MainWindow(object):

    # setting up widgets
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 600)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # calculate widget
        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate.setGeometry(QtCore.QRect(180, 440, 75, 25))
        self.Calculate.clicked.connect(self.compute)
        self.Calculate.setAutoDefault(True)

        # clear widget
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(280, 440, 75, 25))
        self.Clear.clicked.connect(self.clear_inputs)

        # input widgets
        self.V1_arg = QtWidgets.QLineEdit(self.centralwidget)
        self.V1_arg.setGeometry(QtCore.QRect(70, 310, 113, 20))
        self.V1_arg.setText("75")
        self.V1_arg.returnPressed.connect(self.Calculate.click)

        self.V1_phase = QtWidgets.QLineEdit(self.centralwidget)
        self.V1_phase.setGeometry(QtCore.QRect(70, 340, 113, 20))
        self.V1_phase.setText("0")
        self.V1_phase.returnPressed.connect(self.Calculate.click)

        self.V2_arg = QtWidgets.QLineEdit(self.centralwidget)
        self.V2_arg.setGeometry(QtCore.QRect(70, 370, 113, 20))
        self.V2_arg.setText("100")
        self.V2_arg.returnPressed.connect(self.Calculate.click)

        self.V2_phase = QtWidgets.QLineEdit(self.centralwidget)
        self.V2_phase.setGeometry(QtCore.QRect(70, 400, 113, 20))
        self.V2_phase.setText("60")
        self.V2_phase.returnPressed.connect(self.Calculate.click)

        self.R1 = QtWidgets.QLineEdit(self.centralwidget)
        self.R1.setGeometry(QtCore.QRect(330, 310, 113, 20))
        self.R1.setText("4")
        self.R1.returnPressed.connect(self.Calculate.click)

        self.R2 = QtWidgets.QLineEdit(self.centralwidget)
        self.R2.setGeometry(QtCore.QRect(330, 340, 113, 20))
        self.R2.setText("2")
        self.R2.returnPressed.connect(self.Calculate.click)

        self.XL1 = QtWidgets.QLineEdit(self.centralwidget)
        self.XL1.setGeometry(QtCore.QRect(330, 370, 113, 20))
        self.XL1.setText("4j")
        self.XL1.returnPressed.connect(self.Calculate.click)

        self.XC1 = QtWidgets.QLineEdit(self.centralwidget)
        self.XC1.setGeometry(QtCore.QRect(330, 400, 113, 20))
        self.XC1.setText("-j")
        self.XC1.returnPressed.connect(self.Calculate.click)


        # LCD Widgets
        self.Va_arg = QtWidgets.QLCDNumber(self.centralwidget)
        self.Va_arg.setGeometry(QtCore.QRect(73, 480, 101, 30))
        self.Va_arg.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Va_arg.display(96.8)

        self.Vb_arg = QtWidgets.QLCDNumber(self.centralwidget)
        self.Vb_arg.setGeometry(QtCore.QRect(310, 480, 101, 30))
        self.Vb_arg.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Vb_arg.display(16.89)

        self.Va_phase = QtWidgets.QLCDNumber(self.centralwidget)
        self.Va_phase.setGeometry(QtCore.QRect(73, 510, 101, 30))
        self.Va_phase.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Va_phase.display(69.67)

        self.Vb_phase = QtWidgets.QLCDNumber(self.centralwidget)
        self.Vb_phase.setGeometry(QtCore.QRect(310, 510, 101, 30))
        self.Vb_phase.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Vb_phase.display(165.7)

        # labels
        self.Supernode = QtWidgets.QLabel(self.centralwidget)
        self.Supernode.setEnabled(True)
        self.Supernode.setGeometry(QtCore.QRect(150, 9, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Supernode.setFont(font)
        self.Supernode.setTextFormat(QtCore.Qt.RichText)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 310, 100, 13))

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 340, 100, 16))

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 370, 100, 13))

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 400, 100, 16))

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 400, 91, 16))

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 370, 47, 13))

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 340, 91, 16))

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 310, 47, 13))

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(45, 490, 47, 13))

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(280, 490, 47, 13))

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(180, 490, 50, 13))

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(180, 520, 100, 13))

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(420, 490, 50, 13))

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(420, 520, 100, 13))

        # import image
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(70, 70, 391, 201))
        self.label_11.setPixmap(QtGui.QPixmap("Sample Circuit.PNG"))
        self.label_11.setScaledContents(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # Widgets Renaming
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Supernode Calculator"))
        self.Calculate.setText(_translate("MainWindow", "Calculate"))
        self.Clear.setText(_translate("MainWindow", "Clear"))
        self.Supernode.setText(_translate("MainWindow", "Sample Circuit"))
        self.label.setText(_translate("MainWindow", "V1 Magnitude"))
        self.label_2.setText(_translate("MainWindow", "V1 Phase (degrees)"))
        self.label_3.setText(_translate("MainWindow", "V2 Magnitude"))
        self.label_5.setText(_translate("MainWindow", "V2 Phase (degrees)"))
        self.label_6.setText(_translate("MainWindow", "XC (ohm)"))
        self.label_4.setText(_translate("MainWindow", "XL (ohm)"))
        self.label_7.setText(_translate("MainWindow", "R2 (ohm)"))
        self.label_8.setText(_translate("MainWindow", "R1 (ohm)"))
        self.label_9.setText(_translate("MainWindow", "Va = "))
        self.label_10.setText(_translate("MainWindow", "Vb = "))
        self.label_12.setText(_translate("MainWindow", "Magnitude"))
        self.label_13.setText(_translate("MainWindow", "Phase (degrees)"))
        self.label_14.setText(_translate("MainWindow", "Magnitude"))
        self.label_15.setText(_translate("MainWindow", "Phase (degrees)"))


    # Modified Nodal Analysis Algorithm
    def compute(self):
        try:
            # putting inputs into variables
            v1arg = float(self.V1_arg.text())
            v1phase = float(self.V1_phase.text())
            v2arg = float(self.V2_arg.text())
            v2phase = float(self.V2_phase.text())
            r1 = float(self.R1.text())
            r2 = float(self.R2.text())
            xL = complex(self.XL1.text())
            xC = complex(self.XC1.text())


            # getting the rect form of V1 and V2
            v1 = cmath.rect(v1arg, v1phase * (cmath.pi / 180))
            v2 = cmath.rect(v2arg, v2phase * (cmath.pi / 180))

            # making the matrix equation Ax=B to get the unknown values in matrix x
            A = numpy.array([
                [1 / r1 + 1 / xL, 1 / r2 + 1 / xC],
                [1, -1]
                ])
            B = numpy.array([v1/r1, v2])

            # solve system
            x = numpy.linalg.solve(A, B)
            Va = cmath.polar(x[0])
            Vb = cmath.polar(x[1])

            # display answer
            self.Va_arg.display(Va[0])
            self.Va_phase.display(Va[1]*(180/cmath.pi))
            self.Vb_arg.display(Vb[0])
            self.Vb_phase.display(Vb[1]*(180/cmath.pi))

        # show error pop-up
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText('Invalid Input')

            msg.exec_()

    # clear inputs
    def clear_inputs(self):
        self.V1_arg.setText("")
        self.V1_phase.setText("")
        self.V2_arg.setText("")
        self.V2_phase.setText("")
        self.R1.setText("")
        self.R2.setText("")
        self.XC1.setText("")
        self.XL1.setText("")
        self.Va_arg.display(0)
        self.Va_phase.display(0)
        self.Vb_arg.display(0)
        self.Vb_phase.display(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
