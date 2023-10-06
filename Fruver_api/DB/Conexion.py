from django.db import connection
from ..Response_server.Response import Response

class conexion:

    def __init__(self) -> None:
        self.table = []
        self.rows_affected = 0

    def execute_reader(self, sp_name):
        
        def sp_reader(cursor):

            self.table = []

            cursor.execute("select * from "+ sp_name)

            column_names = [desc[0] for desc in cursor.description]
            self.table = [dict(zip(column_names, row)) for row in cursor.fetchall()]

        try:

            self.__execute_sp(lambda cursor : sp_reader(cursor))

        except Exception as e:

            return Response(
                    Status=False,
                    Messague=f"Error al obtener datos {e}",
                    Data= []
                    
                    )
        
        return Response(

                    Status=True,
                    Messague=f"Datos obtenidos correctamente",
                    Data = self.table

                    )
    
    def execute_cmd(self, sp_cmd_name, arg_list):
        
        def sp_cmd(cursor):
                    
                cursor.callproc(sp_cmd_name, arg_list)
                self.rows_affected = cursor.rowcount

        try:

            self.__execute_sp(lambda cursor : sp_cmd(cursor))
            
        except Exception as e:

            return Response(

                    Status=False,
                    Messague=f"Error al insertar datos {e}",
                    Data = []

                    )

        return Response(

                    Status=True,
                    Messague=f"Ejecucion completada correctamente, filas afectadas: {self.rows_affected}",
                    Data = []

                    )

    def __execute_sp(self, call):

        with connection.cursor() as cursor:
            call(cursor)
