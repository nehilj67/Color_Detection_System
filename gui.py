
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QLabel,QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(109, 90, 231, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(109, 130, 301, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 170, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 171, 113, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 220, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName("menubar")
        self.menuColour_Detector = QtWidgets.QMenu(self.menubar)
        self.menuColour_Detector.setObjectName("menuColour_Detector")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuColour_Detector.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.clicker)
        self.pushButton_2.clicked.connect(self.clicker_2)
    def clicker(self):
        global s
        name= QFileDialog.getOpenFileName(self.centralwidget,"Select Image Folder","")
        s=str(name)
        a=str(name)
        b=(a[2:])
        c=b.split(',')
        d=c[0]
        sa=(d[0:len(d)-1])
        if name:
            self.lineEdit.setText(sa)
    def clicker_2(self):
        a=s
        b=(a[2:])
        c=b.split(',')
        d=c[0]
        str=(d[0:len(d)-1])
        print(str)
        cmd="python color_detection.py -i "+str
        print(cmd)
        process = subprocess.Popen(cmd,shell=True)
        out, err = process.communicate()
        print(err)
        print(out)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Color Detector"))
        self.label.setText(_translate("MainWindow", "Welcome to the Color Detector App "))
        self.label_2.setText(_translate("MainWindow", "Please select an image to be checked for colors"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.menuColour_Detector.setTitle(_translate("MainWindow", "Color Detector"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
