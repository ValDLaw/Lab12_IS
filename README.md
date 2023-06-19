# LAB 12
## Integrantes
- Valeria Nicole Espinoza Tarazona - (202110109)
- Hector Valentín Quezada Amour - (202120750)
- Enzo Gabriel Camizan Vidal - (202110047)
- Paolo Vásquez Grahammer - (202110379)
- Sofía Valeria García Quintana - (202110567)

## Detección de errores
Antes que nada, hicimos un análisis de nuestro código para garantizar que se cumple con los requerimientos pedidos. Es así que identificamos lo siguientes errores de lógica al momento de devolver el ganador:  

### Error 1  
No se está realizando la siguiente validación:
> Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador.

Para ello, añadiremos la siguiente función:  
```python
def obtener_ganador(self, votosxcandidato, total_votos):
        for candidato, votos in votosxcandidato.items():
            porcentaje = (votos / total_votos) * 100
            if porcentaje > 50:
                return [candidato]
        return None
```

En el método *obtener_ganador*, se calcula el porcentaje de votos para cada candidato y se verifica si supera el 50%

### Error 2  
No se está realizando la siguiente validación:
> Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta.  Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo.  

Para ello, añadiremos la siguiente función:  
```python
def obtener_ganadores(self, votosxcandidato):
        sorted_candidatos = sorted(votosxcandidato.items(), key=lambda x: x[1], reverse=True)
        candidatos_2vuelta = [sorted_candidatos[0],sorted_candidatos[1]]
        return candidatos_2vuelta
```  

Se agregó el método *obtener_ganadores* para poder extraer aquellos dos candidatos con más votos y devolver el que tiene mayor aceptación o el que aparece primero en el archivo.  
## Tipos de refactorización  

Para mejorar nuestro código sin cambiar su funcionalidad, empleamos los siguientes cambios:  
### Renombrar variables o métodos  
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

### Extracción de métodos  
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
Vemos que se calculaba el ganador en una sola función. Decidimos dividirlo en funciones más pequeñas para ordener el código y hacerlo más claro. Todo ello fue englobado en una función llamada calcular_ganador(). El resultado fue el siguiente:  
```python 
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
```  

### Eliminar código duplicado  
Teníamos la siguiente lógica previamente. Eran dos fors que iteraban al diccionario votosxcandidato:  

```python 
for candidato in votosxcandidato:
    print('candidato: ' + candidato + ' votos validos: ' + str(votosxcandidato[candidato]))
for candidato in votosxcandidato:
    return [candidato]
```

Lo que hicimos para no realizar este for dos veces innecesariamente fue lo siguiente:  
```python
sorted_candidatos = sorted(votosxcandidato.items(), key=lambda x: x[1], reverse=True)
        candidatos_2vuelta = [sorted_candidatos[0],sorted_candidatos[1]]
        return candidatos_2vuelta
```  

Calculamos únicamente lo que nos piden, que es en caso haya segunda vuelta, el que haya aperecido primero en el archivo, y lo almaceno en variables.