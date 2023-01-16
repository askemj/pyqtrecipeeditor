import pytest
import copy #ensures copying objects and not references 
from databasepersistence import DatabasePersistence #FixMe add __init__.py to root dir and/or set shellpath variable 
from recipe import Ingredient, Recipe, Tag

# Recipe items 
@pytest.fixture
def test_ingredient_1():
    test_ingr = Ingredient(1, 'stk.', 'banan', 'Frugt & Grønt', 'Hovedingrediens', False)
    return test_ingr

@pytest.fixture
def test_ingredient_2():
    test_ingr = Ingredient(3, 'kugle(r)', 'vaniljeis', 'Frost', 'Hovedingrediens', False)
    return test_ingr

@pytest.fixture
def test_ingredient_3():
    test_ingr = Ingredient(1, 'stænk', 'chokoladesauce', 'Tørvarer', 'Hovedingrediens', False)
    return test_ingr

@pytest.fixture
def test_tag_1():
    test_tag = Tag('Børnevenlig')
    return test_tag

@pytest.fixture
def test_tag_2():
    test_tag = Tag('Hurtig')
    return test_tag

@pytest.fixture
def test_recipe_1():
    ingr = [test_ingredient_1, test_ingredient_2, test_ingredient_3]
    taglist = [test_tag_1, test_tag_2]
    note = 'Klargøres umiddelbart før servering'
    recipe = Recipe('Bananasplit', note, 1, 15, 20, 'Dessert', taglist, ingr)
    return recipe

### Arrange 

test_ingredient_1 = Ingredient(1, 'stk.', 'banan', 'Frugt & Grønt', 'Hovedingrediens', False)
test_ingredient_2 = Ingredient(3, 'kugle(r)', 'vaniljeis', 'Frost', 'Hovedingrediens', False)
test_ingredient_3 = Ingredient(1, 'stænk', 'chokoladesauce', 'Tørvarer', 'Hovedingrediens', False)

test_tag_1 = Tag('Børnevenlig')
test_tag_2 = Tag('Hurtig')

# test_recipe_1
ingr = [test_ingredient_1, test_ingredient_2, test_ingredient_3]
taglist = [test_tag_1, test_tag_2]
note = 'Klargøres umiddelbart før servering'
test_recipe_1 = Recipe('Bananasplit', note, 1, 15, 20, 'Dessert', taglist, ingr)

database = DatabasePersistence()

def test_find_items_for_deletion(test_recipe_1): #test_recipe_1):
    #### Arrange
    # ingr1 = Ingredient(1, 'stk.', 'banan', 'Frugt & Grønt', 'Hovedingrediens', False)
    # ingr2 = Ingredient(3, 'kugle(r)', 'vaniljeis', 'Frost', 'Hovedingrediens', False)
    # ingr3 = Ingredient(1, 'stænk', 'chokoladesauce', 'Tørvarer', 'Hovedingrediens', False)
    # ingrlist1 = [ingr1, ingr2, ingr3]
    # ingrlist2 = [ingr1, ingr2, ingr3]
    # taglist = [Tag('Børnevenlig')]
    # note = 'Klargøres umiddelbart før servering'
    # old_rec = Recipe('Bananasplit', note, 1, 15, 20, 'Dessert', taglist, ingrlist1)
    # new_rec = Recipe('Bananasplit', note, 1, 15, 20, 'Dessert', taglist, ingrlist2)
    # new_rec.ingredients.pop(1)
    old_rec = test_recipe_1
    new_rec = copy.copy(old_rec)
    new_rec.ingredients.pop(1)
    ### Act
    items_for_deletion = database._find_items_for_deletion(new_rec, old_rec)
    #### Assert
    item = items_for_deletion[0][0]
    assert item.name == 'vaniljeis'

#print( database._find_items_for_deletion(new_recipe2, new_recipe)[0][0].name ) 

#find_items_for_deletion()