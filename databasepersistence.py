import mysql.connector # FixMe generate requirements.txt 
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
        self.test_connection()

    def test_connection(self):
        """ Tests database connection by connecting to database using credentials from config-file. 
        Returns success (bool) True if connection is successfull
        """
        success = False
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
            cnx.close()
            return success

    def select_recipe(self, recipe_id): # FixMe insert actual MySQL
        _ingredient_list = []
        _tags_list = []
        ### get ingredients 
        sql_ingredient_query = f""" ingredient query """    #FixMe insert this string and write it to give ID too!

        try:
            cnx = mysql.connector.connect(**self.config)
            cursor = cnx.cursor()
            cursor.execute(sql_ingredient_query)
            result = cursor.fetchall()
            for item in result: #consider getting ID as well 
                ingredient = Ingredient(item[1], item[2], item[3], item[4], item[5], item[6])
                #ingredient.ID = item[0]
                _ingredient_list.append(ingredient)
        except Exception as e:
            print(e)
        finally:
            cnx.commit()
            cnx.close()

        ### Get tags 
        sql_tag_query = f""" tag query """    #FixMe insert this string and write it to give ID too!

        try:
            cnx = mysql.connector.connect(**self.config)
            cursor = cnx.cursor()
            cursor.execute(sql_tag_query)
            result = cursor.fetchall()
            for item in result: #consider getting ID as well 
                tag = Tag(item[1])
                #tag.ID = item[0]
                _tags_list.append(tag)
        except Exception as e:
            print(e)
        finally:
            cnx.commit()
            cnx.close()

        ### Get recipe info and construct recipe 
        sql_recipe_info_query = f""" recipe info """ #FixMe insert this string and write it to give ID too!

        try:
            cnx = mysql.connector.connect(**self.config)
            cursor = cnx.cursor()
            cursor.execute(sql_recipe_info_query)
            result = cursor.fetchone()
            recipe = Recipe(result[1], result[2], result[3], result[4], result[5], result[6], _tags_list, _ingredient_list)
            recipe.ID = result[0]
        except Exception as e:
            print(e)
        finally:
            cnx.commit()
            cnx.close()

    def update_recipe(self, recipe):
        old_recipe = self.select_recipe(recipe.ID)

        

    def insert_recipe(self, recipe): 
        """ Inserts recipe in database 
        
        args: recipe, custom recipe object
        returns: status (boolean) true if succesfull insert
        """

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

        try:
            cnx = mysql.connector.connect(**self.config)
            cursor = cnx.cursor()
            cursor.execute(sql_recipe_info_str)
            cursor.execute(f"""SELECT Ret.ret_id FROM Ret WHERE Ret.ret_navn = '{recipe.name}'""")  #NB in case of update lastrowid is always 0 
            recipe.ID = int( cursor.fetchone()[0] ) #FixMe NB there may be an error if the cursor 
            print(str(recipe.ID)) 
        except Exception as e:
            print(e)
        finally:
            cnx.commit()
            cnx.close()

        try:
            cnx = mysql.connector.connect(**self.config)
            cursor = cnx.cursor()
            for tag in recipe.tags: #FixMe probably insert or ignore instead of on duplicate key ...
                sql_tag_insert_str = f""" INSERT INTO Tag (Tag.tag_tekst) 
                    VALUES ('{tag.text}')
                    ON DUPLICATE KEY UPDATE
                    Tag.tag_tekst = '{tag.text}';"""
                cursor.execute(sql_tag_insert_str)
                cursor.execute(f"""SELECT Tag.tag_id FROM Tag WHERE Tag.tag_tekst = '{tag.text}'""")  #NB in case of update lastrowid is always 0 
                tag.ID = int( cursor.fetchone()[0] ) #FixMe NB there may be an error if the cursor 
                #tag.ID = cursor.lastrowid
                #print(f'recipe id = {recipe.ID}, tag ID is {tag.ID}')
                sql_tag_link_to_recipe = f""" INSERT INTO RetTag (RetTag.Ret_ret_id, RetTag.Tag_tag_id)
                    VALUES ({recipe.ID}, {tag.ID});""" #FixMe fix for duplicate entries 
                cursor.execute(sql_tag_link_to_recipe)
        except Exception as e:
            print(e)
        finally:
            cnx.commit()
            cnx.close()
        
        try: #FixMe remember cases where not all info is defined, eg no unit 
            cnx = mysql.connector.connect(**self.config)
            cursor = cnx.cursor()
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
                cursor.execute(f"""SELECT Vare.vare_id FROM Vare WHERE Vare.vare_navn = '{ingredient.name}'""")  #NB in case of update lastrowid is always 0 
                ingredient.ID = int( cursor.fetchone()[0] ) #FixMe NB there may be an error if the cursor 
                print(str(ingredient.ID))

                sql_insert_unit = f""" INSERT INTO Enhed (enhed_navn)
                    VALUES ('{ingredient.unit}')
                    ON DUPLICATE KEY UPDATE
	                Enhed.enhed_navn = '{ingredient.unit}';
                """
                print(sql_insert_unit)
                cursor.execute(sql_insert_unit)
                cursor.execute(f"""SELECT Enhed.enhed_id FROM Enhed WHERE Enhed.enhed_navn = '{ingredient.unit}'""")  #NB in case of update lastrowid is always 0 
                _unit_id = int( cursor.fetchone()[0] ) #FixMe NB there may be an error if the cursor 
                print(str(_unit_id))

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
                cursor.execute(sql_link_ingredient_info_to_recipe)
                print(sql_link_ingredient_info_to_recipe)
        except Exception as e:
            print(e)
        finally:
            cnx.commit()
            cnx.close()


        #FixMe implement batch type mysql construction 
    

    #FixMe finish implementing the rest of the methods of this class 

if __name__ == "__main__":
    database = DatabasePersistence()

    new_tag = Tag('Lækkert')
    new_ingredient = Ingredient(2,'dl','chokoladesauce','Tørvarer','hovedingrediens',False)
    new_ingredient2 = Ingredient(3,'kugle(r)','is','Frost','hovedingrediens',False)
    new_recipe = Recipe('is og chokolade', 'Tilberedes lige inden servering', 2, 10, 15, 'Dessert', [new_tag], [new_ingredient, new_ingredient2])
    new_recipe.ID=7
    database.insert_recipe(new_recipe)