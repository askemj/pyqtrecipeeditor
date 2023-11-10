import mysql.connector # FixMe generate requirements.txt 
from mysql.connector import errorcode
import json 
from recipe import Recipe, Tag, Ingredient

class DatabasePersistence:
    """ DatabasePersistence class handles MariaDB CRUD operations 
    
    Attributes
    ----------
    config : dict 
        dictionary of connection credentials 

    Methods 
    -------
    test_connection()
        tests connection 
    select_recipe(recipe_id)
        selects recipe based on recipe id 
    insert_recipe(recipe)
        inserts recipe in database 
    """

    def __init__(self): #FixMe maybe implement databaseconnectionclass
        with open('dbconfig.txt') as f:
            data = f.read()
        self.config = json.loads(data) #NB must be double quotes and bool follow json style so true not True

    def test_connection(self):
        """ Tests database connection by connecting to database using credentials from config-file. 
        Returns success (bool) True if connection is successfull
        """
        success = False
        cnx = None 
        try:
            cnx = mysql.connector.connect(**self.config)
            #cursor = cnx.cursor() #FixMe return some info from DB 
            #cursor.execute("SHOW TABLES;")
            print("Connection established")
            success = True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        finally:
            if cnx is not None:
                    cnx.close()
            return success

    def select_recipe(self, recipe_id):
        """ Selects recipe in database based on passed recipe ID 
        
        args: recipe_id, database id of recipe
        returns: recipe, custom recipe object 
        """
        _ingredient_list = []
        _tags_list = []

        sql_ingredient_query = f""" SELECT RetVare.maengde, Enhed.enhed_navn, Vare.vare_navn, Varekategori.varekategori_tekst,  
                Varefunktion.Varefunktion_tekst, Vare.basisvare FROM RetVare 
            INNER JOIN Enhed ON RetVare.Enhed_enhed_id = Enhed.enhed_id
            INNER JOIN Vare ON RetVare.Vare_vare_id = Vare.vare_id
            INNER JOIN Varekategori ON  RetVare.Vare_vare_id = Vare.vare_id AND Vare.vare_id = Varekategori.varekategori_id
            INNER JOIN Varefunktion ON Varefunktion_Varefunktion_id = Varefunktion_id 
            WHERE RetVare.Ret_ret_id = {str(recipe_id)};  """
        
        sql_tag_query = f""" SELECT Tag.tag_id, Tag.tag_tekst FROM Ret 
            INNER JOIN RetTag ON Ret.ret_id = RetTag.Ret_ret_id
            INNER JOIN Tag ON Tag.tag_id = RetTag.Tag_tag_id WHERE Ret.ret_id = {str(recipe_id)}; """ 
        
        sql_recipe_info_query = f""" SELECT Ret.ret_navn, Ret.noter, Ret.antal_portioner, Ret.forberedelsestid_tid, 
                Ret.totaltid_tid, Opskriftstype.opskriftstype_tekst
            FROM Ret
            INNER JOIN Opskriftstype ON Ret.Opskriftstype_opskriftstype_id = Opskriftstype.opskriftstype_id
            WHERE Ret.ret_id = {str(recipe_id)}; """

        try:
            cnx = mysql.connector.connect(**self.config)
            cursor = cnx.cursor()

            ### get ingredients 
            cursor.execute(sql_ingredient_query)
            result = cursor.fetchall()
            for item in result: 
                #ingredient constructor takes: quantity, unit, name, category, function, isBasic)
                ingredient = Ingredient(item[0], item[1], item[2], item[3], item[4], item[5])
                print(ingredient)
                _ingredient_list.append(ingredient)

            ### Get tags
            cursor.execute(sql_tag_query)
            result = cursor.fetchall()
            for item in result: 
                tag = Tag(item[1])
                tag.ID = item[0]
                print(tag)
                _tags_list.append(tag)

            ### Get recipe info and construct recipe 
            cursor.execute(sql_recipe_info_query)
            result = cursor.fetchone()
            # recipe constructor takes: name, notes, Nservings, preparation_time, total_time, recipe_type, tags, ingredients
            recipe = Recipe(result[0], result[1], result[2], result[3], result[4], result[5], _tags_list, _ingredient_list)
            recipe.ID = recipe_id
            print(recipe)
        except Exception as e:
            recipe = None 
            print("0000ps! \nAn exception occurred:")
            print(e)
        finally:
            cnx.close()
        return recipe

    def update_recipe(self, new_recipe):
        old_recipe = self.select_recipe(new_recipe.ID) # retrieves recipe as is in database
        rem_ingr, rem_tags = self._find_ingredients_for_deletion(new_recipe, old_recipe)
        self._delete_ingredients(rem_ingr, rem_tags)
        self.insert_recipe(new_recipe) #insert recipe also updates existing entries 

    def _find_items_for_deletion(self, new_recipe, old_recipe):
        ingredients_for_removal = []
        for old_item in old_recipe.ingredients: 
            if not any(new_item for new_item in new_recipe.ingredients if new_item.name == old_item.name): #if old item is not in new list, add to removal list 
                ingredients_for_removal.append(old_item)
        
        tags_for_removal = []
        ### #FixMe implement code for tag search 
        return [ingredients_for_removal, tags_for_removal]

    def _delete_items(self, ingredients_for_removal, tags_for_removal):
        sql_delete_ingredients = "FROM .. DELETE item1, item 2" #FixMe Not yet implemented 

        try:
            cnx = mysql.connector.connect(**self.config)
            cursor = cnx.cursor()
            cursor.execute(sql_delete_ingredients)
        except Exception as e:
            print(e)
        finally:
            cnx.commit()
            cnx.close()

    def insert_recipe(self, recipe): 
        """ Inserts recipe in database 
        
        args: recipe, custom recipe object
        returns: status (boolean) true if succesfull insert
        """
        status = False
        ### Recipe info 
        try: #FixMe Refactor Worlds largest try statement 
            cnx = mysql.connector.connect(**self.config) #NB "master" connection object
            sql_recipe_info_str = f"""INSERT INTO Ret (Ret.ret_navn, Ret.noter, Ret.forberedelsestid_tid,
                Ret.totaltid_tid, Ret.antal_portioner, Ret.Opskriftstype_opskriftstype_id )
                VALUES ('{recipe.name}', '{recipe.notes}', {str(recipe.preparation_time)}, {str(recipe.total_time)}, {str(recipe.N_servings)}, 
                    (SELECT opskriftstype_id FROM Opskriftstype WHERE opskriftstype_tekst = '{recipe.recipe_type}'))
                ON DUPLICATE KEY UPDATE
                    Ret.ret_navn = '{recipe.name}',
                    Ret.noter = '{recipe.notes}', 
                    Ret.forberedelsestid_tid = {str(recipe.preparation_time)},
                    Ret.totaltid_tid = {str(recipe.total_time)},
                    Ret.antal_portioner = {str(recipe.N_servings)},
                    Ret.Opskriftstype_opskriftstype_id = (SELECT opskriftstype_id FROM Opskriftstype WHERE opskriftstype_tekst = '{recipe.recipe_type}');"""
            cursor = cnx.cursor()

            #insert general recipe info 
            cursor.execute(sql_recipe_info_str)

            #get recipe ID
            cursor.execute(f"""SELECT Ret.ret_id FROM Ret WHERE Ret.ret_navn = '{recipe.name}'""")  #NB in case of update lastrowid is always 0 
            recipe.ID = int( cursor.fetchone()[0] ) #FixMe NB there may be an error if the cursor 
            print("recipe id is " + str(recipe.ID) + " for recipe: " + recipe.name) 

            ### Tags 
            for tag in recipe.tags: #FixMe probably insert or ignore instead of on duplicate key ...
                sql_tag_insert_str = f""" INSERT INTO Tag (Tag.tag_tekst) 
                    VALUES ('{tag.text}')
                    ON DUPLICATE KEY UPDATE
                    Tag.tag_tekst = '{tag.text}';"""
                print(sql_tag_insert_str)
                cursor.execute(sql_tag_insert_str)

                #Get tag ID
                cursor.execute(f"""SELECT Tag.tag_id FROM Tag WHERE Tag.tag_tekst = '{tag.text}'""")  #NB in case of update lastrowid is always 0 
                tag.ID = int( cursor.fetchone()[0] ) #FixMe NB there may be an error if the cursor 
                print(f'recipe id = {recipe.ID}, tag ID is {tag.ID}')

                #Link tag to recipe
                sql_tag_link_to_recipe = f""" INSERT INTO RetTag (RetTag.Ret_ret_id, RetTag.Tag_tag_id)
                    VALUES ({recipe.ID}, {tag.ID});""" #FixMe fix for duplicate entries 
                cursor.execute(sql_tag_link_to_recipe)
        
            ### Ingredients      #FixMe remember cases where not all info is defined, eg no unit 
            for ingredient in recipe.ingredients: #FixMe probably insert or ignore instead of on duplicate key ...
                sql_ingredient_insert_str = f""" INSERT INTO Vare (vare_navn, basisvare, Varekategori_varekategori_id) 
                    VALUES ('{ingredient.name}', {ingredient.isBasic}, 
                    (SELECT Varekategori.varekategori_id from Varekategori WHERE Varekategori.varekategori_tekst = '{ingredient.category}'))
                    ON DUPLICATE KEY UPDATE
                    Vare.vare_navn = '{ingredient.name}',
                    Vare.basisvare = {ingredient.isBasic},
                    Vare.Varekategori_varekategori_id = (SELECT Varekategori.varekategori_id from Varekategori WHERE Varekategori.varekategori_tekst = '{ingredient.category}');
                """
                print(sql_ingredient_insert_str)

                cursor.execute(sql_ingredient_insert_str)

                #get ID of ingredient
                cursor.execute(f"""SELECT Vare.vare_id FROM Vare WHERE Vare.vare_navn = '{ingredient.name}'""")  #NB in case of update lastrowid is always 0 
                ingredient.ID = int( cursor.fetchone()[0] ) #FixMe NB there may be an error if the cursor 
                print(str(ingredient.ID))

                #insert unit
                sql_insert_unit = f""" INSERT INTO Enhed (enhed_navn)
                    VALUES ('{ingredient.unit}')
                    ON DUPLICATE KEY UPDATE
	                Enhed.enhed_navn = '{ingredient.unit}';
                """
                print(sql_insert_unit)
                cursor.execute(sql_insert_unit)

                #get ID of unit
                cursor.execute(f"""SELECT Enhed.enhed_id FROM Enhed WHERE Enhed.enhed_navn = '{ingredient.unit}'""")  #NB in case of update lastrowid is always 0 
                _unit_id = int( cursor.fetchone()[0] ) #FixMe NB there may be an error if the cursor 
                print(str(_unit_id))

                #link all ingredient info with recipe
                sql_link_ingredient_info_to_recipe = f""" INSERT INTO RetVare (maengde, Enhed_enhed_id, Ret_ret_id, Vare_vare_id, Varefunktion_Varefunktion_id) 
                    VALUES ({ingredient.quantity}, {_unit_id}, {recipe.ID}, {ingredient.ID}, 
                        (SELECT Varefunktion.varefunktion_id FROM Varefunktion WHERE Varefunktion.Varefunktion_tekst = '{ingredient.function}'))
                    ON DUPLICATE KEY UPDATE
                        RetVare.maengde = {ingredient.quantity},
                        RetVare.Enhed_enhed_id = {_unit_id}, 
                        RetVare.Ret_ret_id = {recipe.ID}, 
                        RetVare.Vare_vare_id = {ingredient.ID},
                        RetVare.Varefunktion_Varefunktion_id = 
                            (SELECT Varefunktion.varefunktion_id FROM Varefunktion WHERE Varefunktion.Varefunktion_tekst = '{ingredient.function}');"""
                print(sql_link_ingredient_info_to_recipe)
                cursor.execute(sql_link_ingredient_info_to_recipe)
                print(sql_link_ingredient_info_to_recipe)

                #If no errors so far, set successfull status 
                cnx.commit() #commit new info to database 
                status = True 
        except Exception as e:
            print(e)
            status = False
        finally:
            cnx.close()
        return status
    
    def read_all_secondary_database_data(self):
        """ Reads all supplemental databasedata
        
        Returns 
            secondary_db_data (dict), tags (list), ingredient_functions (list), ingredient_categories (list), ingredients (list(dict)) NB Not ingredient-class instances, recipe_types (list)"""
        
        db_model = {
            'tags': [],
            'ingredient_functions': [],
            'ingredient_categories': [],
            'ingredients': [],
            'recipe_types': []
        }

        sql_tags_query = "SELECT Tag.tag_tekst FROM Tag;"
        sql_ingr_function_query = "SELECT Varefunktion.varefunktion_tekst FROM Varefunktion ORDER BY varefunktion_id;"
        sql_ingr_category_query = "SELECT Varekategori.varekategori_tekst FROM Varekategori ORDER BY varekategori_id;"
        sql_type_query = "SELECT Opskriftstype.opskriftstype_tekst FROM Opskriftstype ORDER BY opskriftstype_id;"
        queries = [[sql_tags_query, 'tags'], [sql_ingr_function_query, 'ingredient_functions'], [sql_ingr_category_query, 'ingredient_categories'], [sql_type_query, 'recipe_types']]

        sql_ingredients_query = """ SELECT Vare.vare_navn, Vare.basisvare, Varekategori.varekategori_tekst FROM Vare
            INNER JOIN Varekategori ON Vare.Varekategori_varekategori_id = Varekategori.varekategori_id;"""
        try:
            # tags, ingr_fcts, ingr_cats and types
            cnx = mysql.connector.connect(**self.config)
            cursor = cnx.cursor()
            for query, field in queries:
                cursor.execute(query)
                response = cursor.fetchall()
                for item in response:
                    result = item[0]
                    db_model[field].append(result)
            
            # ingredients 
            cursor.execute(sql_ingredients_query)
            response = cursor.fetchall()
            for item in response:  
                ingredient = {'name': item[0],
                        'isBasic': item[1],
                        'category': item[2]
                    }
                db_model['ingredients'].append(ingredient)

        except Exception as e:
            print(e)
        finally:
            cnx.close()
        return db_model

    #FixMe finish implementing the rest of the methods of this class 

if __name__ == "__main__":
    database = DatabasePersistence()

    #new_tag = Tag('Lækkert')
    #new_ingredient = Ingredient(2,'dl','chokoladesauce','Tørvarer','hovedingrediens',False)
    #new_ingredient2 = Ingredient(3,'kugle(r)','is','Frost','hovedingrediens',False)
    #new_ingredient3 = Ingredient(2,'spsk','frysetørret hindbær','Tørvarer','hovedingrediens',False)
    #new_recipe = Recipe('is og chokolade', 'Tilberedes lige inden servering', 2, 10, 15, 'Dessert', [new_tag], [new_ingredient, new_ingredient2])
    #new_recipe2 = Recipe('is og chokolade', 'Tilberedes lige inden servering', 2, 10, 15, 'Dessert', [new_tag], [new_ingredient3, new_ingredient2])
    #new_recipe.ID=7
    #database.insert_recipe(new_recipe)
    
    #print( database._find_items_for_deletion(new_recipe2, new_recipe)[0][0].name )
    #db_info = database.read_all_secondary_database_data()
    #print(db_info)
    #print(str(database.test_connection))
    #_recipe = database.select_recipe(7)
    #print(_recipe)