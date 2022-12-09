import pytest
from . import DatabasePersistence #FixMe add __init__.py to root dir and/or set shellpath variable 


database = DatabasePersistence()

new_tag = Tag('Lækkert')
new_ingredient = Ingredient(2,'dl','chokoladesauce','Tørvarer','hovedingrediens',False)
new_ingredient2 = Ingredient(3,'kugle(r)','is','Frost','hovedingrediens',False)
new_ingredient3 = Ingredient(2,'spsk','frysetørret hindbær','Tørvarer','hovedingrediens',False)
new_recipe = Recipe('is og chokolade', 'Tilberedes lige inden servering', 2, 10, 15, 'Dessert', [new_tag], [new_ingredient, new_ingredient2])
new_recipe2 = Recipe('is og chokolade', 'Tilberedes lige inden servering', 2, 10, 15, 'Dessert', [new_tag], [new_ingredient3, new_ingredient2])
new_recipe.ID=7
#database.insert_recipe(new_recipe)

print( database._find_items_for_deletion(new_recipe2, new_recipe)[0][0].name ) 