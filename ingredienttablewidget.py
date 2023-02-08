from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QComboBox, QCheckBox
from recipe import Ingredient

class comboFunction(QComboBox): 
    def __init__(self, parent, functions):
        super().__init__(parent) #parent will be the QTablewidget
        self.addItems(functions)

class comboCategory(QComboBox):
    def __init__(self, parent, categories):
        super().__init__(parent) #parent will be the QTablewidget
        self.addItems(categories)

class IngredientsTableWidget(QtWidgets.QTableWidget):
    """ Provides ingredient specific TableWidget functionality """
    ingredient_functions = []
    ingredient_categories = []

    def __init__(self, parent, ingredient_functions, ingredient_categories): 
        """ Custom Ingredient Table widget 
        
        args 
            parent (QWidget): central widget 
            ingredient_functions (list): list of ingredient function options for combobox
            ingredient_categories (list): list of ingredient category options for combobox
        """
        super().__init__(parent)
        self.ingredient_functions = ingredient_functions
        self.ingredient_categories = ingredient_categories
        self.setObjectName("inpIngredients")
        self.setColumnCount(6) 
        self._set_column_headers()

        INITIAL_ROW_COUNT = 8
        for row in range(INITIAL_ROW_COUNT):
            self._add_row_at_index(row)

    def _set_column_headers(self):
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

    def get_ingredients(self):
        """ Gets ingredients from view
        
        Returns
            list: list of ingredients
        """

        n_rows = self.rowCount()
        ingredients_list = []
        for row in range(n_rows-1):
            if None not in (self.item(row, 0), self.item(row,1), self.item(row,2)): #Check valid entries 
                quantity = float(self.item(row, 0).text())
                unit = self.item(row, 1).text()
                name = self.item(row, 2).text()
                function = self.cellWidget(row, 3).currentText() #NB nested combobox  
                category = self.cellWidget(row, 4).currentText() #NB nested combobox  )
                is_basic = False
                if self.cellWidget(row, 5).isChecked():
                    is_basic = True
                ingredient = Ingredient(quantity, unit, name, category, function, is_basic)
                ingredients_list.append(ingredient)
            else:
                print("Error in row: " + str(row) + ", row skipped")
        return ingredients_list

    def _add_row_at_index(self, row):        
        item = QtWidgets.QTableWidgetItem()
        self.setVerticalHeaderItem(row, item)
        comboFunc = comboFunction(self, self.ingredient_functions)
        self.setCellWidget(row, 3,comboFunc)
        comboCat = comboCategory(self, self.ingredient_categories)
        self.setCellWidget(row, 4, comboCat)
        cbox = QCheckBox(self)
        self.setCellWidget(row,5,cbox)

    def add_row(self):
        """ Adds row at the end of the QTableWidget """
        current_number_of_rows = self.rowCount()
        self._add_row_at_index(current_number_of_rows + 1)

    def remove_row(self): 
        """ Removes currently selected row if a row is selected 
        
        Returns:
            bool: True for success, False otherwise.
        """

        if self.currentRow() > 0: 
            self.remove_row(self.currentRow)
            return True
        else: 
            return False

