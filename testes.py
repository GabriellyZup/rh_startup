import unittest
from unittest.mock import patch
from funcionarios import FuncionarioComum, Gerente
from sistema_rh import SistemaRH

class TestFuncionarios(unittest.TestCase):
    def test_calcular_bonus_funcionario_comum(self):
        funcionario = FuncionarioComum("João", 1000)
        self.assertEqual(funcionario.calcular_bonus(), 100)

    def test_calcular_bonus_gerente(self):
        gerente = Gerente("Maria", 2000, 500)
        self.assertEqual(gerente.calcular_bonus(), 900)

    def test_set_salario_negativo(self):
        funcionario = FuncionarioComum("João", 1000)
        with self.assertRaises(ValueError):
            funcionario.set_salario(-100)

    @patch('builtins.print')
    def test_mostrar_bonus(self, mock_print):
        funcionario = FuncionarioComum("João", 1000)
        sistema = SistemaRH()
        sistema.mostrar_bonus(funcionario)
        mock_print.assert_called_with("João - Bônus: 100.0")

if __name__ == '__main__':
    unittest.main()

    