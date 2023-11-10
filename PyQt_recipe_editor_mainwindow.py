# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt-recipe-editor-ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1244, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 210, 81, 17))
        self.label_6.setObjectName("label_6")
        self.inpRecNotes = QtWidgets.QTextEdit(self.centralwidget)
        self.inpRecNotes.setGeometry(QtCore.QRect(20, 230, 421, 91))
        self.inpRecNotes.setObjectName("inpRecNotes")
        self.disTags = QtWidgets.QListWidget(self.centralwidget)
        self.disTags.setGeometry(QtCore.QRect(460, 90, 291, 191))
        self.disTags.setObjectName("disTags")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(460, 70, 81, 17))
        self.label_8.setObjectName("label_8")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 70, 421, 89))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.inpRecTitle = QtWidgets.QLineEdit(self.layoutWidget)
        self.inpRecTitle.setObjectName("inpRecTitle")
        self.gridLayout.addWidget(self.inpRecTitle, 0, 1, 1, 5)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.inpNServings = QtWidgets.QLineEdit(self.layoutWidget)
        self.inpNServings.setObjectName("inpNServings")
        self.gridLayout.addWidget(self.inpNServings, 1, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 3)
        self.inpPrepTime = QtWidgets.QLineEdit(self.layoutWidget)
        self.inpPrepTime.setObjectName("inpPrepTime")
        self.gridLayout.addWidget(self.inpPrepTime, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 4, 1, 1)
        self.inpTotTime = QtWidgets.QLineEdit(self.layoutWidget)
        self.inpTotTime.setObjectName("inpTotTime")
        self.gridLayout.addWidget(self.inpTotTime, 2, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 4, 1, 1)
        self.btnLoadFromDB = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadFromDB.setGeometry(QtCore.QRect(270, 530, 131, 25))
        self.btnLoadFromDB.setObjectName("btnLoadFromDB")
        self.btnInsertInDB = QtWidgets.QPushButton(self.centralwidget)
        self.btnInsertInDB.setGeometry(QtCore.QRect(410, 530, 161, 25))
        self.btnInsertInDB.setObjectName("btnInsertInDB")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(670, 530, 80, 25))
        self.btnExit.setObjectName("btnExit")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(580, 530, 80, 25))
        self.btnClear.setObjectName("btnClear")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 170, 81, 17))
        self.label_9.setObjectName("label_9")
        self.inpRecType = QtWidgets.QComboBox(self.centralwidget)
        self.inpRecType.setGeometry(QtCore.QRect(110, 170, 331, 25))
        self.inpRecType.setObjectName("inpRecType")
        self.ingredientWidget = QtWidgets.QWidget(self.centralwidget)
        self.ingredientWidget.setGeometry(QtCore.QRect(20, 340, 691, 171))
        self.ingredientWidget.setObjectName("ingredientWidget")
        self.btnAddIngrRow = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddIngrRow.setGeometry(QtCore.QRect(720, 440, 30, 25))
        self.btnAddIngrRow.setObjectName("btnAddIngrRow")
        self.btnDelIngrRow = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelIngrRow.setGeometry(QtCore.QRect(720, 470, 30, 25))
        self.btnDelIngrRow.setObjectName("btnDelIngrRow")
        self.inpTag = QtWidgets.QLineEdit(self.centralwidget)
        self.inpTag.setGeometry(QtCore.QRect(460, 290, 211, 25))
        self.inpTag.setObjectName("inpTag")
        self.btnAddTag = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddTag.setGeometry(QtCore.QRect(680, 290, 30, 25))
        self.btnAddTag.setObjectName("btnAddTag")
        self.btnDelTag = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelTag.setGeometry(QtCore.QRect(720, 290, 30, 25))
        self.btnDelTag.setObjectName("btnDelTag")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(780, 80, 21, 451))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(810, 70, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.disAssistantHUD = QtWidgets.QTextBrowser(self.centralwidget)
        self.disAssistantHUD.setGeometry(QtCore.QRect(810, 280, 411, 241))
        self.disAssistantHUD.setAutoFillBackground(False)
        self.disAssistantHUD.setObjectName("disAssistantHUD")
        self.disAssistantList = QtWidgets.QListView(self.centralwidget)
        self.disAssistantList.setGeometry(QtCore.QRect(810, 100, 411, 161))
        self.disAssistantList.setObjectName("disAssistantList")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1244, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Recipe editor"))
        self.label_6.setText(_translate("MainWindow", "Recipe notes:"))
        self.label_8.setText(_translate("MainWindow", "Tags"))
        self.label_2.setText(_translate("MainWindow", "Recipe title:"))
        self.label_3.setText(_translate("MainWindow", "Number of Servings:"))
        self.label_4.setText(_translate("MainWindow", "Preparation/total  time:"))
        self.label_5.setText(_translate("MainWindow", "/"))
        self.label_7.setText(_translate("MainWindow", "Recipe ID"))
        self.btnLoadFromDB.setText(_translate("MainWindow", "Load from Database"))
        self.btnInsertInDB.setText(_translate("MainWindow", "Insert in Database"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))
        self.btnClear.setText(_translate("MainWindow", "Clear editor"))
        self.label_9.setText(_translate("MainWindow", "Recipe Type"))
        self.btnAddIngrRow.setText(_translate("MainWindow", "+"))
        self.btnDelIngrRow.setText(_translate("MainWindow", "-"))
        self.btnAddTag.setText(_translate("MainWindow", "+"))
        self.btnDelTag.setText(_translate("MainWindow", "-"))
        self.label_10.setText(_translate("MainWindow", "Recipe assistant"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
