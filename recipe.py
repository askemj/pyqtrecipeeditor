class Tag():
    def __init__(self, text): #FixMe docstring
        self.ID = None #not available before inserted in database
        self.text = text

class Ingredient(): #FixMe make groceryitem parent class and extend with self.function property; add docstring
    """ Ingredient class """

    def __init__(self, quantity, unit, name, category, function, isBasic):
        self.ID = None #not available before inserted in database
        self.quantity = quantity
        self.unit = unit
        self.name = name
        self.function = function
        self.category = category
        self.isBasic = isBasic #FixMe isBasic-bool is deprecated 

    def __eq__(self, other):
        if isinstance(self.__clas__):
            return self.name == other.name and self.unit == other.quantity
        else:
            return False

    def __str__(self):
        return f'{quantity} {unit} {name}'.format(quantity = str(self.quantity), unit=self.unit, name=self.name)

class Recipe(): #FixMe write tests for this class and consider creating databasepersistenceclass and fix up docstrings 
    """ Recipe class """

    def __init__(self, name, notes, Nservings, preparation_time, total_time, recipe_type, tags, ingredients):
        """ Args: name (str)
        id (bool)
        notes (str)
        NServings (float)
        preparation_time (int)
        total_time (int)
        recipe_type (str)
        tags (list of Tag objects )
        ingredients (list of Ingredient objects) """

        self.name = name
        self.ID = None #not available before inserted in database
        self.notes = notes
        self.N_servings = Nservings
        self.preparation_time = preparation_time 
        self.total_time = total_time
        self.recipe_type = recipe_type
        self.tags = tags
        self.ingredients = ingredients

    def scale(scale): #FixMe implement this method 
        """ Scale recipe 
        Args: 
            scale (float) factor to scale recipe with """
        pass 

    def add_ingredient(self, ingredient):
        """ Add ingredient to recipe
        
        Args: ingredient (custom ingredient class object) """
        self.ingredients.add(ingredient)

    def add_tag(self, tag):
        """ Add tag to recipe
        Args: tag (str)
        """
        self.tags.add(tag)

    def __str__(self): 
        return self.name

if __name__ == "__main__": 
    new_tag = Tag('Lækkert')
    new_ingredient = Ingredient(2,'dl','chokoladesauce','Tørvarer','hovedingrediens',False)
    new_recipe = Recipe('is og chokolade', 'Tilberedes lige inden servering', 2, 10, 15, 'Dessert', [new_tag], [new_ingredient])