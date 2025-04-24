from funcionarios import FuncionarioComum, Gerente
from sistema_rh import SistemaRH

def main():
    # Cria funcionários
    joao = FuncionarioComum("João", 1000)
    maria = Gerente("Maria", 2000, 500)
    
    # Configura o sistema de RH
    sistema = SistemaRH()
    sistema.adicionar_funcionario(joao)  
    sistema.adicionar_funcionario(maria)
    
    # Lista todos os bônus
    sistema.listar_bonus()

if __name__ == "__main__":
    main()