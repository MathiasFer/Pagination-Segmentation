class SegmentacionMemoria:
    def __init__(self, tamano_memoria):
        self.tamano_memoria = tamano_memoria
        self.memoria = [None] * tamano_memoria

    def escribir_segmento(self, direccion_base, segmento, dato):
        if direccion_base + len(dato) > self.tamano_memoria:
            print("Error: El segmento excede el tamaño de la memoria.")
            return
        self.memoria[direccion_base:direccion_base+len(dato)] = dato

    def leer_segmento(self, direccion_base, tamano_segmento):
        if direccion_base + tamano_segmento > self.tamano_memoria:
            print("Error: Dirección fuera de rango.")
            return None
        return self.memoria[direccion_base:direccion_base+tamano_segmento]

# Ejemplo de uso
simulador_segmentacion = SegmentacionMemoria(tamano_memoria=32)
simulador_segmentacion.escribir_segmento(1, [0, 0, 0, 0, 0], [10, 20, 30, 40, 50])
print(simulador_segmentacion.leer_segmento(1, 5))
