import sqlite3 as sq
import os 
import json

class DB_ORM:
    def __init__(self):
        self.__connect()
    
    def __connect(self):
        os.mkdir('DBs') if not os.path.exists('DBs') else ...

        self.connection = sq.connect("DBs/TESTS.db")
        self.cursor = self.connection.cursor()


    def execute(self, query : str, is_change : bool, **values) -> list:
        if self.connection_check():

            if values:
                if list(values.keys())[0] == 'values':
                    self.cursor.execute(query, values['values'])
            else:
                self.cursor.execute(query)
            
            if is_change:
                self.connection.commit()
                return True
            
            else:
                return self.cursor.fetchall()
            
        else:
            print('Have no connection to database')

    
    def get_route(self, route_num : int, route_type_ : str) -> tuple:
        if self.connection_check():
            self.__response = self.execute(is_change = False, query = f"SELECT * FROM test_table where Route = ? and Type = ?;", values = [route_num, route_type_])
            return(json.loads(self.__response[0][2]) if self.__response else False)
            

    def connection_check(self):
        try:
            self.cursor.execute('SELECT 1;')
            return True

        except Exception:
            return False


    def connection_close(self):
        self.connection.close()