from recipe import Recipe, Tag
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

        #workflow
        self._view.btnInsertInDB.clicked.connect(self.on_insert_recipe_clicked)

    def read_recipe_from_view(self): #FixMe read full recipe and cast as recipe instance 
        """ reads recipe from gui and returns recipe object 

        Returns 
            recipe (recipe object)  """
        
        name = self._view.inpRecTitle.text()
        n_servs = self._view.inpNServings.text() #FixMe must be cast as float !!!
        prep_time = self._view.inpPrepTime.text()
        tot_time = self._view.inpTotTime.text()
        notes = self._view.inpRecNotes.toPlainText()
        rec_type = self._view.inpRecType.currentText()
        tags = self._read_tags_from_view()
        ingredients = self._read_ingredients_from_view()
        recipe = None
        if "" not in [name, n_servs, prep_time, tot_time]: 
            n_servs = float(n_servs)
            prep_time = float(prep_time)
            tot_time = float(tot_time)
            recipe = Recipe(name, notes,n_servs, prep_time, tot_time, rec_type, tags, ingredients)
        return recipe 

    def _read_tags_from_view(self):
        tags = []
        for n in range(self._view.disTags.count()):
            tags.append(Tag(str(self._view.disTags.item(n).text()))) #NB item is a QListWidgetItem
        return tags 

    def _read_ingredients_from_view(self):
        ingredients = self._view.inpIngredients.get_ingredients()
        return ingredients

    def on_add_tag_clicked(self):
        tag = QListWidgetItem(self._view.inpTag.text())
        self._view.disTags.addItem(tag)
        self._view.inpTag.setText("")

    def on_del_tag_clicked(self):
        row = self._view.disTags.currentRow()
        self._view.disTags.takeItem(row)

    def on_insert_recipe_clicked(self): #connect to databasepersistence class 
        recipe = self.read_recipe_from_view()
        if recipe is not None: 
            success = self._database.insert_recipe(recipe)
            if success:
                print("Recipe successfully inserted!")
            elif not success:
                print("An error occurred, recipe not properly inserted!")
        else:
            print("Recipe was not read correctly, please check your input")
    

