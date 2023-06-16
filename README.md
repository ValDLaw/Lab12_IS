# LAB 12
## Integrantes
- Valeria Nicole Espinoza Tarazona - (202110109)

## Tipo de refactorización

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