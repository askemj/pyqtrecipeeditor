from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QComboBox, QCheckBox
from recipe import Ingredient
from PyQt5.QtWidgets import QCompleter 

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
    database_ingredients = []
    INITIAL_ROW_COUNT = 8

    def __init__(self, parent, database_model): 
        """ Custom Ingredient Table widget 
        
        args 
            parent (QWidget): central widget 
        """
        super().__init__(parent)
        self.setObjectName("inpIngredients")
        self.setColumnCount(6) 
        self._set_column_headers()
        self.setRowCount(self.INITIAL_ROW_COUNT)

    def initiate_rows(self, database_model):
        """ initiate initial rows, for calling once database is ready
        
        args 
            ingredient_functions (list): list of ingredient function options for combobox
            ingredient_categories (list): list of ingredient category options for combobox
        """

        self.ingredient_functions = database_model["ingredient_categories"]
        self.ingredient_categories = database_model["ingredient_functions"]
        self.database_ingredients = database_model["ingredients"]
        
        for row in range(self.INITIAL_ROW_COUNT):
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
        self.horizontalHeaderItem(3).setText("Category")
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(4, item)
        self.horizontalHeaderItem(4).setText("Function")
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
            if (None or "") not in (self.item(row, 0), self.cellWidget(row,1), self.cellWidget(row,2).text()): #Check valid entries 
                quantity = float(self.item(row, 0).text())
                unit = self.item(row, 1).text().strip() #stripped of leading and trailing whitespaces
                name = self.cellWidget(row, 2).text().strip()
                category = self.cellWidget(row, 3).currentText() #NB nested combobox  
                function = self.cellWidget(row, 4).currentText() #NB nested combobox  )
                is_basic = False
                if self.cellWidget(row, 5).isChecked():
                    is_basic = True
                ingredient = Ingredient(quantity, unit, name, category, function, is_basic)
                ingredients_list.append(ingredient)
            else:
                print("Error in row: " + str(row) + ", row skipped")
        return ingredients_list
    
    def autofill_data_on_autocomplete(self):
        row = self.currentRow()

        #find ingredient object matching autocompletion 
        selected_ingredient_name = self.cellWidget(row,2).text()
        find_ingredient_list = [item for item in self.database_ingredients if item['name'] == selected_ingredient_name]
        _ingredient = find_ingredient_list[0]
        _category = _ingredient["category"]

        #set category 
        self.cellWidget(row,3).setCurrentText(_category) 
        
        #set is basic status 
        if _ingredient["isBasic"] == True:
            self.cellWidget(row, 5).setChecked(True)
        
    def _add_row_at_index(self, row):   
        item = QtWidgets.QTableWidgetItem()
        self.setVerticalHeaderItem(row, item)
        comboFunc = comboFunction(self, self.ingredient_functions)
        self.setCellWidget(row, 3,comboFunc)
        comboCat = comboCategory(self, self.ingredient_categories)
        self.setCellWidget(row, 4, comboCat)
        cbox = QCheckBox(self)
        self.setCellWidget(row,5,cbox)

        # completion 
        _completer_lineedit = QtWidgets.QLineEdit()
        ingredient_names = [item["name"] for item in self.database_ingredients]
        ingredient_completer = QCompleter(ingredient_names)
        _completer_lineedit.setCompleter(ingredient_completer)
        self.setCellWidget(row,2,_completer_lineedit)
        
        #auto fill data when completing ingredient name 
        ingredient_completer.activated.connect(self.autofill_data_on_autocomplete)

    def add_row(self):
        """ Adds row at the end of the QTableWidget """

        current_number_of_rows = self.rowCount()
        self.setRowCount(current_number_of_rows + 1)
        self._add_row_at_index(current_number_of_rows) #NB 0-indexed!

    def remove_current_row(self): 
        """ Removes currently selected row if a row is selected 
        
        Returns:
            bool: True for success, False otherwise.
        """

        if self.currentRow() >= 0: #ensure a row is picked 
            self.removeRow(self.currentRow())
            return True
        else: 
            return False


