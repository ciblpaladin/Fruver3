from django.db import connection

class conexion:

    def __init__(self) -> None:
        self.table = []


    def execute_reader(self, sp_name):
        
        def sp_reader(cursor):

            self.table = []

            cursor.execute("select * from "+ sp_name)

            column_names = [desc[0] for desc in cursor.description]
            self.table = [dict(zip(column_names, row)) for row in cursor.fetchall()]


        self.__execute_sp(lambda cursor : sp_reader(cursor))
        print(self.table)
        return self.table
    
    def execute_cmd(self, sp_cmd_name):
        
        def sp_cmd(cursor):
            try:          
                cursor.execute("call "+ sp_cmd_name)

            except Exception as e:

                print(f"error al ejecutar procedimiento {e}")


    def __execute_sp(self, call):

        with connection.cursor() as cursor:
            call(cursor)
