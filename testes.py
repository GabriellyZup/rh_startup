import pytest
from funcionarios import FuncionarioComum, Gerente
from sistema_rh import SistemaRH

def test_calculo_bonus_funcionario_comum():
    funcionario = FuncionarioComum("João", 1000)
    assert funcionario.calcular_bonus() == 100.0  # 10% de 1000

def test_calculo_bonus_gerente():
    gerente = Gerente("Maria", 2000, 500)
    assert gerente.calcular_bonus() == 900.0  # 20% de 2000 (400) + 500

def test_set_salario_negativo():
    funcionario = FuncionarioComum("Ana", 3000)
    with pytest.raises(ValueError):
        funcionario.set_salario(-100)

def test_mostrar_bonus(capsys):
    sistema = SistemaRH()
    funcionario = FuncionarioComum("Pedro", 1500)
    sistema.mostrar_bonus(funcionario)
    captured = capsys.readouterr()
    assert "Pedro - Bônus: 150.0" in captured.out
    assert "Log: Ação relacionada ao bônus registrada" in captured.out

def test_listar_bonuses(capsys):
    sistema = SistemaRH()
    sistema.adicionar_funcionario(FuncionarioComum("João", 1000))  # Método correto
    sistema.adicionar_funcionario(Gerente("Maria", 2000, 500))
    sistema.listar_bonus()
    captured = capsys.readouterr()
    assert "João - Bônus: 100.0" in captured.out
    assert "Maria - Bônus: 900.0" in captured.out