from PyQt_recipe_editor_mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ingredienttablewidget import IngredientsTableWidget

class RecipeEditorView(Ui_MainWindow):
    """ Recipe editor view 
    inherits from Ui_MainWindow generated by Qt Designer and implements custom Ingredient QTablewidget """

    database_model = {
        'tags': [],
        'ingredient_functions': [],
        'ingredient_categories': [],
        'ingredients': [],
        'recipe_types': []
    }

    def __init__(self, main_window):
        super().__init__()
        super().setupUi(main_window)

        #set dictionary for static offline database data

        self.inpIngredients = IngredientsTableWidget(self.centralwidget)
        self.inpIngredients.setGeometry(QtCore.QRect(20, 330, 691, 192)) 


    def load_static_database_data(self):
        """ loads database data into view, for calling when database is ready 
        """
        db = self.database_model 
        self.inpRecType.addItems(db["recipe_types"])
        self.inpIngredients.initiate_rows(db['ingredient_categories'], db["ingredient_functions"])
    
    def read_ingredients(self):
        """ returns ingredients (list): list of ingredients added in the view """
        ingredients = self.inpIngredients.get_ingredients()
        return ingredients
        
    # og saa videre.... her skal vaere kode til at samle QTableWidget og definere metoder som controlleren skal kunne kalde 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RecipeEditorView(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())