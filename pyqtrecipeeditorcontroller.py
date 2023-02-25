from recipe import Recipe, Ingredient

class PyQtRecipeEditorController():
    """ PyQt Recipe Editor Controller Class """ 

    def __init__(self, database, view):
        self._database = database 
        self._view = view 
        self._connectSignalsAndSlots()

    def _connectSignalsAndSlots(self):
        self._view.btnValidate.clicked.connect(self.on_validate_clicked)

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
        for n in range(self._view.inpTags.count()-1):
            tags.append(self._view.inpTags.item(n))
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


    def on_insert_recipe_clicked(self): #connect to databasepersistence class 
        return

    def on_validate_clicked(self):
        print(self.read_recipe_from_view())
        pass
