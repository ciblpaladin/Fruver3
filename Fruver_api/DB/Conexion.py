from django.db import connection

class conexion:

    def __init__(self) -> None:
        self.table = []

    def execute_reader(self, sp_name):
        
        def sp_reader(cursor):
            cursor.execute("select * from "+ sp_name)
            result = cursor.fetchall()

            for resultado in result:
                self.table.append(resultado)


        self.__execute_sp(lambda cursor : sp_reader(cursor))


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
