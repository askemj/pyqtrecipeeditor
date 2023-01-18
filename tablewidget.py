from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QComboBox

class comboFunction(QComboBox):
    def __init__(self, parent):
        super().__init__(parent) #parent will be the QTablewidget
        self.addItems(['Hovedingrediens', 'Twist', 'Rest'])

    def getComboValue(self):
        return self.currentText() 

class comboCategory():
    def __init__(self, parent):
        super().__init__(parent) #parent will be the QTablewidget
        self.addItems(['Frugt & Grønt', 'Brød', 'Tørvarer'])

    def getComboValue(self):
        return self.currentText() 

class IngredientsTableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent): #FixMe something wrong with the variable passed to the super here
        super.__init__(parent)
        #self.inpIngredients = QtWidgets.QTableWidget(self.centralwidget)
        #self.inpIngredients.setGeometry(QtCore.QRect(20, 330, 691, 192))
        self.setObjectName("inpIngredients")
        self.inpIngredients.setColumnCount(5)
        self.inpIngredients.setRowCount(8)
        ROW_COUNT = 8
        for row in range(ROW_COUNT):
            item = QtWidgets.QTableWidgetItem()
            self.inpIngredients.setVerticalHeaderItem(row, item)
            comboFunc = comboFunction(self)
            self.setCellWidget(row, 3,comboFunc)
            comboCat = comboCategory(self)
            self.setCellWidget(row, 4, comboCat)

        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(0, item)
        self.horizontalHeaderItem(0).setText("Quantity")
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(1, item)
        self.horizontalHeaderItem(1).setText("Unit")
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(2, item)
        self.horizontalHeaderItem(0).setText("Name")
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(3, item)
        self.horizontalHeaderItem(3).setText("Function")
        item = QtWidgets.QTableWidgetItem()
        self.inpIngredients.setHorizontalHeaderItem(4, item)
        self.horizontalHeaderItem(4).setText("Category")


