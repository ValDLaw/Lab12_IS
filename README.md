# LAB 12
## Integrantes
- Valeria Nicole Espinoza Tarazona - (202110109)

## Tipos de refactorización

### * Renombrar variables o métodos  
Teníamos el siguiente código previamente:  
```python
def leerdatos(self, archivo):
        data = []
        with open(archivo, 'r') as csvfile:
            next(csvfile)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append(fila)
        return data
```
Lo que hicimos fue renombrar el nombre de la función para que se entienda de que data estamos hablando. El código obtenido fue el siguiente:  
```python
def leervotos(self):
        votos = []
        with open('0204.csv', 'r') as csvfile:
            next(csvfile)
            lectorvotos = csv.reader(csvfile)
            for voto in lectorvotos:
                votos.append( voto)
        return votos
```

### * Extracción de métodos  
Teníamos el siguiente código previamente:  
```python 
def calcularganador(self, data):
        votosxcandidato = {}
        for fila in data:
            if not fila[4] in votosxcandidato:
                votosxcandidato[fila[4]] = 0
            if fila[5] == '1':
                votosxcandidato[fila[4]] = votosxcandidato[fila[4]] + 1
        for candidato in votosxcandidato:
            print('candidato: ' + candidato + ' votos validos: ' + str(votosxcandidato[candidato]))
        for candidato in votosxcandidato:
            return [candidato]
```  
Vemos que se calculaba el ganador en una sola función. Decidimos dividirlo en funciones más pequeñas para ordener el código y hacerlo más claro. El resultado fue el siguiente:  
```python 
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
```  

### * Eliminar código duplicado  