import mysql.connector
from mysql.connector import Error
import time

#############################################s#######

#######>       à faire ensemble  

####################################################

def read_text_file(txt_file, name_folder):
    """
    Inserts serveral all the content of a .txt file into the database
    """
    txt_file_content = open(f"../{name_folder}/{txt_file}", "r")

    # print(f.read()) 
    # print(type(f)) 

    # print(txt_file_content)
    file_list = []
    for row in txt_file_content:
        # Create a list of dictionnary
        if ("country_code capital" not in row):
            # Create a dictionnary of key/value
            row_dict = {}
            # Remove \n, split line into values, get first value
            row_dict['country_code'] = row.strip('\n').split()[0]
            row_dict['country_capital'] = row.split()[1]
            # Add dictionnary to list
            file_list.append(row_dict)

    return file_list

    # print(file_list[2]['country_code'])


def insert_one_row(connection_config, table, colonne_1_name, colonne_2_name,
    colonne_1_value, colonne_2_value):
    """
    Inserts data into database
    """

    # table, country_code, capital
    try :
        mydb = mysql.connector.connect(**connection_config)

        mycursor = mydb.cursor()
        sql = f"""INSERT INTO {table} ({colonne_1_name}, {colonne_2_name})
        VALUES ("{colonne_1_value}", "{colonne_2_value}")

        ON DUPLICATE KEY 
        UPDATE {colonne_2_name} = "{colonne_2_value}";"""

        mycursor.execute(sql)

        mydb.commit()

        print(mycursor.rowcount, f"record inserted.")

        return True

    except Error as e:
        print(f"ça marche pas, parce que : {e}")

        return False

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            # print("MySQL connection is closed")



def insert_from_text_file(connection_config, text_file):

    for i, row in enumerate(text_file):

        country_code = text_file[i]['country_code']
        country_capital = text_file[i]['country_capital']

        insert_one_row(connection_config, "countries", "country_code", "capital",
        country_code, country_capital)
        print(i, type(i))


####################################################

#######>        à faire tout.e seul.e  

####################################################
def delete_one_row(connection_config, table, colonne_1_name,
    colonne_1_value):
    """
    Deletes a row of a given table
    """

    # table, country_code, capital
    try :
        mydb = mysql.connector.connect(**connection_config)

        mycursor  =mydb.cursor()
        sql = f"""DELETE FROM {table} WHERE {colonne_1_name}="{colonne_1_value}";"""

        mycursor.execute(sql)

        mydb.commit()

        print(mycursor.rowcount, f"row of {table} content is deleted")

        return True

    except Error as e:
        print(f"ça marche pas, parce que : {e}")

        return False

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()


def delete_all_table_content(connection_config, table):
    """
    Inserts data into database
    """

    # table, country_code, capital
    try :
        mydb = mysql.connector.connect(**connection_config)

        mycursor = mydb.cursor()
        sql = f"""DELETE FROM {table} ;"""
        
        mycursor.execute(sql)

        mydb.commit()

        print(mycursor.rowcount, f"{table} content is deleted.")

        return True

    except Error as e:
        print(f"ça marche pas, parce que : {e}")

        return False

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            # print("MySQL connection is closed")



if __name__ == "__main__":

    connection_config = {
        "host" : "localhost",
        "user" :"antan",
        "password":"example",
        "auth_plugin" : "mysql_native_password",
        "database" : "BDD_Countries",
        "port" : "3307"        
    }

    text_file = read_text_file("country.txt", "documents")
    delete_one_row(connection_config, "countries", "country_code", "BE")


    # INSERT_ONE_ROW = False
    # INSERT_TXT_FILE = False
    # DELETE_ONE_ROW = False
    # DELETE_ALL_TABLE_CONTENT = False

    # if INSERT_ONE_ROW:
    #     #db_is_OK Variable qui stocke le status bdd
    #     db_is_OK = insert_one_row(connection_config, "countries",
    #     "country_code", "capital", "JP", "Tokyo") 

    #     # print(help(insert_data))
    #     print(db_is_OK)

    # if INSERT_TXT_FILE:
    #     pass

    # if DELETE_ONE_ROW:
    #     pass

    # if DELETE_ALL_TABLE_CONTENT:
    #     delete_all_table_content(connection_config, "countries")
    




  

    
    # """UPDATE countries SET capital = "Caen" WHERE id = 1; """