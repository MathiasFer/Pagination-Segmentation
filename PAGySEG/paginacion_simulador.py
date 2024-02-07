class PaginacionMemoria:
    def __init__(self, tamano_memoria, tamano_pagina):
        self.tamano_memoria = tamano_memoria
        self.tamano_pagina = tamano_pagina
        self.memoria = [None] * tamano_memoria

    def escribir(self, direccion, dato):
        pagina = direccion // self.tamano_pagina
        offset = direccion % self.tamano_pagina
        if pagina >= len(self.memoria) // self.tamano_pagina:
            print("Error: Dirección fuera de rango.")
            return
        if len(dato) > self.tamano_pagina:
            print("Error: El dato es demasiado grande para caber en una página.")
            return
        self.memoria[pagina * self.tamano_pagina + offset] = dato

    def leer(self, direccion):
        pagina = direccion // self.tamano_pagina
        offset = direccion % self.tamano_pagina
        if pagina >= len(self.memoria) // self.tamano_pagina:
            print("Error: Dirección fuera de rango.")
            return None
        return self.memoria[pagina * self.tamano_pagina + offset]

# Ejemplo de uso
simulador_paginacion = PaginacionMemoria(tamano_memoria=32, tamano_pagina=8)
simulador_paginacion.escribir(6, "Hola")
print(simulador_paginacion.leer(6))
