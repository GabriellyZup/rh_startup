from funcionarios import FuncionarioComum, Gerente
from sistema_rh import SistemaRH

def main():
    joao = FuncionarioComum("João", 1000)
    maria = Gerente("Maria", 2000, 500)
    sistema = SistemaRH()
    sistema.funcionarios.append(joao)
    sistema.funcionarios.append(maria)
    sistema.listar_bonuses()

if __name__ == "__main__":
    main()
    