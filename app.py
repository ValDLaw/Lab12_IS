import csv
# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
# region,provincia,distrito,dni,candidato,esvalido
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta
# Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
# el DNI debe ser valido (8 digitos)
class CalculaGanador:

    def leer_votos(self):
        votos = []
        with open('0204.csv', 'r') as csvfile:
            next(csvfile)
            lectorvotos = csv.reader(csvfile)
            for voto in lectorvotos:
                votos.append( voto)
        return votos
    
    def calcular_ganador(self, data):
        votosxcandidato, total_votos = self.contar_votos(data)
        ganador = self.obtener_ganador(votosxcandidato, total_votos)
        if ganador:
            print('GANADOR')
            print('Candidato: ' + ganador[0])
        else:
            candidatos_2vuelta = self.obtener_ganadores(votosxcandidato)
            print('Candidato: ' + candidatos_2vuelta[0][0] + ', Votos válidos: ' + str(candidatos_2vuelta[0][1]))
            print('Candidato: ' + candidatos_2vuelta[1][0] + ', Votos válidos: ' + str(candidatos_2vuelta[1][1]))
            print('GANADOR')
            print('Candidato: ' + candidatos_2vuelta[0][0])

    def contar_votos(self, data):
        votosxcandidato = {}
        total_votos = 0
        for fila in data:
            candidato = fila[4]
            if candidato not in votosxcandidato:
                votosxcandidato[candidato] = 0
            if fila[5] == '1':
                votosxcandidato[candidato] += 1
                total_votos += 1
        return votosxcandidato, total_votos

    def obtener_ganador(self, votosxcandidato, total_votos):
        for candidato, votos in votosxcandidato.items():
            porcentaje = (votos / total_votos) * 100
            if porcentaje > 50:
                return [candidato]
        return None

    def obtener_ganadores(self, votosxcandidato):
        sorted_candidatos = sorted(votosxcandidato.items(), key=lambda x: x[1], reverse=True)
        candidatos_2vuelta = [sorted_candidatos[0],sorted_candidatos[1]]
        return candidatos_2vuelta

c = CalculaGanador()
#c.calcularvotos(c.leerdatos())
datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
]
print(c.calcular_ganador(datatest))

'''
class CalculaGanador:

    def leerdatos(self, archivo):
        data = []
        with open(archivo, 'r') as csvfile:
            next(csvfile)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append(fila)
        return data

    def contar_votos(self, data):
        votosxcandidato = {}
        for fila in data:
            candidato = fila[4]
            if candidato not in votosxcandidato:
                votosxcandidato[candidato] = 0
            if fila[5] == '1':
                votosxcandidato[candidato] += 1
        return votosxcandidato

    def mostrar_ganador(self, votosxcandidato):
        for candidato, votos in votosxcandidato.items():
            print('Candidato: ' + candidato + ', Votos válidos: ' + str(votos))

    def obtener_ganador(self, votosxcandidato):
        ganador = max(votosxcandidato, key=votosxcandidato.get)
        return [ganador]

c = CalculaGanador()

# Leer datos de un archivo CSV
data = c.leerdatos('0204.csv')

# Calcular los votos por candidato
votosxcandidato = c.contar_votos(data)

# Mostrar los resultados
c.mostrar_ganador(votosxcandidato)

# Obtener el ganador
ganador = c.obtener_ganador(votosxcandidato)
print(ganador)
'''