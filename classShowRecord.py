class ShowRecord:
    __textoRegistro = None

    def mostrar_datos(self, registro, label):
        # Procesa el registro para mostrarlo como texto
        self.__textoRegistro = (
            f"ID: {registro['id']}\n"
            f"Nombre: {registro['nombre']}\n"
            f"Apellido: {registro['apellido']}\n"
            f"Ciudad: {registro['ciudad']}\n"
            f"Calle: {registro['calle']}"
        )

        # Actualiza el texto del label en la interfaz gráfica
        label.config(text=self.__textoRegistro)
