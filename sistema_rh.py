def logar_acao(func):
    def wrapper(*args, **kwargs):
        print(f"Log: Ação relacionada ao bônus registrada")
        return func(*args, **kwargs)
    return wrapper

class SistemaRH:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    @logar_acao
    def mostrar_bonus(self, funcionario):
        print(f"{funcionario.get_nome()} - Bônus: {funcionario.calcular_bonus()}")

    def listar_bonus(self):
        for funcionario in self.funcionarios:
            self.mostrar_bonus(funcionario)