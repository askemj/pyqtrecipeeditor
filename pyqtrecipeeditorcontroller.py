from recipe import Recipe
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem

class PyQtRecipeEditorController():
    """ PyQt Recipe Editor Controller Class """ 

    def __init__(self, database, view):
        self._database = database 
        self._view = view 
        self._connectSignalsAndSlots()
        if self._database.test_connection():
            self._view.database_model = self._database.read_all_secondary_database_data()
            self._view.load_static_database_data() 
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical )
            msg_box.setText("Database connection error!")
            msg_box.setInformativeText("The database connection could not be established")
            msg_box.setWindowTitle("Critical error")
            msg_box.exec()
            #msg_box.setDetailedText("...insert actual error message")

    def _connectSignalsAndSlots(self):     
        #Ingredients 
        self._view.btnAddIngrRow.clicked.connect(self._view.inpIngredients.add_row)
        self._view.btnDelIngrRow.clicked.connect(self._view.inpIngredients.remove_current_row)

        #Tags 
        self._view.btnAddTag.clicked.connect(self.on_add_tag_clicked)
        self._view.btnDelTag.clicked.connect(self.on_del_tag_clicked)

        #Recipe Assistant 
        self._view.inpIngredients.cellActivated.connect(self.on_inpIngredients_cell_activated)
        self._view.inpTag.textChanged.connect(self.on_tag_editing)

    def read_recipe_from_view(self): #FixMe read full recipe and cast as recipe instance 
        """ reads recipe from gui and returns recipe object 
        Returns recipe (recipe object)  """
        name = self._view.inpRecTitle.text()
        n_servs = self._view.inpNServings.text()
        prep_time = self._view.inpPrepTime.text()
        tot_time = self._view.inpTotTime.text()
        notes = self._view.inpRecNotes.toPlainText()
        rec_type = self._view.inpRecType.currentText()
        tags = self.read_tags_from_view()
        ingredients = self.read_ingredients_from_view()
        recipe = Recipe(name, notes,n_servs, prep_time, tot_time, rec_type, tags, ingredients)
        return recipe 

    def read_tags_from_view(self):
        tags = []
        for n in range(self._view.disTags.count()-1):
            tags.append( str(self._view.inpTags.item(n))) #NB item is a QListWidgetItem
        return tags 

    def read_ingredients_from_view(self):
        # ingredients = []
        # for row in range(self._view.inpIngredients.rowCount()):
        #     quantity = self._view.inpIngredients.item(row, 0).text()
        #     unit = self._view.inpIngredients.item(row, 1).text()
        #     name = self._view.inpIngredients.item(row, 2).text()
        #     function = self._view.inpIngredients.item(row, 3).text()
        #     category = self._view.inpIngredients.item(row, 4).text()
        #     ingredient = Ingredient(quantity=quantity, unit=unit, name=name, function=function, category=category, isBasic=False) #FixMe hardcoded to not render basic items
        #     ingredients.append(ingredient)
        ingredients = self._view.inpIngredients.get_ingredients()
        return ingredients

    def on_tag_editing(self):
        self._view.disAssistantHUD.setPlainText('Tag help text ...')
        tag_draft = self._view.inpTag.text()
        if len(tag_draft) > 0:
            suggestions = [match for match in self._view.database_model['tags'] if tag_draft in match]
            self._view.disAssistantSuggestions.clear()
            self._view.disAssistantSuggestions.addItems(suggestions)

    def on_add_tag_clicked(self):
        tag = QListWidgetItem(self._view.inpTag.text())
        self._view.disTags.addItem(tag)
        self._view.inpTag.setText("")

    def on_del_tag_clicked(self):
        row = self._view.disTags.currentRow()
        self._view.disTags.takeItem(row)

    def on_insert_recipe_clicked(self): #connect to databasepersistence class 
        return

    def on_inpIngredients_cell_activated(self, row, column):
        print("controller-oninpingr_cell_activated: cell activated event fired ...")
        self._view.disAssistantHUD.setPlainText('Ingredients help text ...')

    def on_validate_clicked(self):
        print(self.read_recipe_from_view())
        pass
