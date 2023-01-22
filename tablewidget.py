from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QComboBox, QCheckBox
from recipe import Ingredient

class comboFunction(QComboBox): 
    def __init__(self, parent):
        super().__init__(parent) #parent will be the QTablewidget
        self.addItems(['Hovedingrediens', 'Twist', 'Rest'])

class comboCategory(QComboBox):
    def __init__(self, parent):
        super().__init__(parent) #parent will be the QTablewidget
        self.addItems(['Frugt & Grønt', 'Brød', 'Tørvarer'])

class IngredientsTableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent): #FixMe something wrong with the variable passed to the super here
        super().__init__(parent)
        #self.inpIngredients = QtWidgets.QTableWidget(self.centralwidget)
        #self.inpIngredients.setGeometry(QtCore.QRect(20, 330, 691, 192))
        self.setObjectName("inpIngredients")
        self.setColumnCount(6) 
        self.setRowCount(8)

        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(0, item)
        self.horizontalHeaderItem(0).setText("Quantity")
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(1, item)
        self.horizontalHeaderItem(1).setText("Unit")
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(2, item)
        self.horizontalHeaderItem(2).setText("Name")
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(3, item)
        self.horizontalHeaderItem(3).setText("Function")
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(4, item)
        self.horizontalHeaderItem(4).setText("Category")
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(5, item)
        self.horizontalHeaderItem(5).setText("Basic Item?")

        ROW_COUNT = 8
        for row in range(ROW_COUNT):
            item = QtWidgets.QTableWidgetItem()
            self.setVerticalHeaderItem(row, item)
            comboFunc = comboFunction(self)
            self.setCellWidget(row, 3,comboFunc)
            comboCat = comboCategory(self)
            self.setCellWidget(row, 4, comboCat)
            cbox = QCheckBox(self)
            self.setCellWidget(row,5,cbox)

    def get_ingredients(self):
        """ Returns ingredients list (list) """
        n_rows = self.rowCount()
        ingredients_list = []
        for row in range(n_rows-1):
            quantity = float(self.item(row, 0).text())
            unit = self.item(row, 1).text()
            name = self.item(row, 2).text()
            function = self.cellWidget(row, 3).currentText() #NB nested combobox  
            category = self.cellWidget(row, 4).currentText() #NB nested combobox  )
            is_basic = False
            if self.cellWidget(row, 5).isChecked():
                is_basic = True
            if name is not None and function is not None and category is not None:
                ingredient = Ingredient(quantity, unit, name, category, function, is_basic)
                print(ingredient) ########## FixMe Delete me in production edition 
                ingredients_list.append(ingredient)
        return ingredients_list


