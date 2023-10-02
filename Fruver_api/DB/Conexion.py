from django.db import connection

class conexion:

    def __init__(self) -> None:
        self.products = []

    def ejecutar_sp_y_guardar_resultados(self):
        with connection.cursor() as cursor:
            # Ejecutar el procedimiento almacenado
            cursor.execute("select * from SP_getProducts()")
            # Obtener los resultados del procedimiento almacenado
            resultados = cursor.fetchall()

            # Guardar los resultados en objetos Producto
            for resultado in resultados:
                self.products.append(resultado)

        return self.products