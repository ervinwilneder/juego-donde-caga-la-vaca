import random

class Vaca:
    def __init__(self):
        self.estado = 'mover'

    def actualizar_estado(self, matriz_transicion):
        estados = ['mover', 'descansar', 'comer', 'popó']
        probabilidad = random.random()
        acumulado = 0
        for i, estado in enumerate(estados):
            acumulado += matriz_transicion[self.estado][estado]
            if probabilidad <= acumulado:
                self.estado = estado
                break

class Grilla:
    def __init__(self, ancho=10, alto=10):
        self.ancho = ancho
        self.alto = alto
        self.parcelas = [[' ' for _ in range(ancho)] for _ in range(alto)]

    def posiciones_externas(self):
        posiciones = []
        for i in range(self.ancho):
            posiciones.append((i, 0))
            posiciones.append((i, self.alto - 1))
        for j in range(1, self.alto - 1):
            posiciones.append((0, j))
            posiciones.append((self.ancho - 1, j))
        return posiciones

    def mover_vaca(self, vaca, pos_vaca):
        if vaca.estado == 'mover':
            posibles_movimientos = [
                (pos_vaca[0] + dx, pos_vaca[1] + dy)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if 0 <= pos_vaca[0] + dx < self.ancho and 0 <= pos_vaca[1] + dy < self.alto
            ]
            return random.choice(posibles_movimientos)
        return pos_vaca

def jugar():
    matriz_transicion = {
        'mover': {'mover': 0.5, 'descansar': 0.2, 'comer': 0.2, 'popó': 0.1},
        'descansar': {'mover': 0.6, 'descansar': 0.2, 'comer': 0.1, 'popó': 0.1},
        'comer': {'mover': 0.1, 'descansar': 0.6, 'comer': 0.2, 'popó': 0.1},
        'popó': {'mover': 0.8, 'descansar': 0.1, 'comer': 0.05, 'popó': 0.05}
    }

    grilla = Grilla()
    vaca = Vaca()
    pos_vaca = random.choice(grilla.posiciones_externas())

    while vaca.estado != 'popó':
        vaca.actualizar_estado(matriz_transicion)
        pos_vaca = grilla.mover_vaca(vaca, pos_vaca)
        print(f'Vaca en posición {pos_vaca}, estado: {vaca.estado}')

if __name__ == '__main__':
    jugar()
