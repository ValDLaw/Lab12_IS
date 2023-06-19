import unittest
from app import CalculaGanador

class TestCalculaGanador(unittest.TestCase):

    def setUp(self):
        self.calculadora = CalculaGanador()

    def test_contar_votos(self):
        datatest = [
        ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
        ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        votosxcandidato, total_votos = self.calculadora.contar_votos(datatest)

        self.assertEqual(votosxcandidato['Aundrea Grace'], 2)
        self.assertEqual(votosxcandidato['Eddie Hinesley'], 1)
        self.assertEqual(total_votos, 3)

    def test_obtener_ganador(self):
        votosxcandidato = {'Candidato A': 10, 'Candidato B': 5}
        total_votos = 15

        ganador = self.calculadora.obtener_ganador(votosxcandidato, total_votos)
        self.assertEqual(ganador, ['Candidato A'])

    def test_obtener_ganadores(self):
        votosxcandidato = {'Candidato A': 8, 'Candidato B': 8, 'Candidato C': 5}

        ganadores = self.calculadora.obtener_ganadores(votosxcandidato)
        self.assertEqual(ganadores, [('Candidato A', 8), ('Candidato B', 8)])

if __name__ == '__main__':
    unittest.main()
