import mysql.connector
import json 
from recipe import recipe, Tag, Ingredient

class DatabasePersistence:
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
        

        #FixMe implement batch type mysql construction 

        # self.name = name
        # self.ID = ID
        # self.notes = notes
        # self.NServings = Nservings
        # self.preparation_time = preparation_time 
        # self.total_time = total_time
        # self.recipe_type = recipe_type
        # self.tags = tags
        # self.ingredients = ingredients

        # self.quantity = quantity
        # self.unit = unit
        # self.name = name
        # self.function = function
        # self.category = category
    

    #FixMe finish implementing the rest of the methods of this class 

# class DatabaseConnection:
#     def __init__(self): #FixMe maybe implement databaseconnectionclass
#         with open('dbconfig.txt') as f:
#             data = f.read()
#             print(type(data))
#         self.config = json.loads(data) #NB must be double quotes and bool follow json style so true not True
#         self.test_connection()

#     def test_connection(self):
#         try:
#             cnx = mysql.connector.connect(**self.config)
#             cursor = cnx.cursor()

#             query = ("SHOW TABLES;")
#             cursor.execute(query)
#             #tables= [tables + next_table for next_table in cursor]
#             #print("Connection is open with the following tables available: " + tables)
#             for line in cursor:
#                 print(line)
#             print("Connection established")

#         except mysql.connector.Error as err:
#             if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#                 print("Something is wrong with your user name or password")
#             elif err.errno == errorcode.ER_BAD_DB_ERROR:
#                 print("Database does not exist")
#             else:
#                 print(err)
#         finally:
#             cnx.close()

if __name__ == "__main__":
    database = DatabasePersistence()

    new_tag = Tag('Lækkert')
    new_ingredient = Ingredient(2,'dl','chokoladesauce','Tørvarer','hovedingrediens',False)
    new_recipe = recipe('is og chokolade', 'Tilberedes lige inden servering', 2, 10, 15, 'Dessert', [new_tag], [new_ingredient])
    new_recipe.ID=7
    #recipe = recipe('Sovs og kartofler', 'Tilberedes i god tid før servering', 4, 45, 90, 'Hovedret, taglist, ingreds') #name, notes, Nservings, preparation_time, total_time, recipe_type, tags, ingredients):
    database.insert_recipe(new_recipe)