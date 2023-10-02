from django.db import connection

class conexion:

    def ejecutar_sp_y_guardar_resultados(self):
        with connection.cursor() as cursor:
            # Ejecutar el procedimiento almacenado
            cursor.execute("select * from SP_getProducts()")
            # Obtener los resultados del procedimiento almacenado
            resultados = cursor.fetchall()

            # Guardar los resultados en objetos Producto
            for resultado in resultados:
                print(resultado)