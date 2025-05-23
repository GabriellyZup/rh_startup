﻿# rh_startup

# Sistema de Cálculo de Bônus para Funcionários

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Docker](https://img.shields.io/badge/Docker-✔-informational)
![Podman](https://img.shields.io/badge/Podman-Compatível-success)
![GitHub Actions](https://img.shields.io/badge/CI/CD-Automatizado-green)


> 🏆 **Desafio Extra Implementado!**  
> A lista interna de funcionários e método `listar_bonus()` demonstram polimorfismo e boas práticas de POO.

Sistema para gestão transparente de bônus salariais em startups, com registros auditáveis e cálculos precisos.

---

## 🚀 Como Usar

### 1. Cálculo Individual de Bônus
```python
from funcionarios import FuncionarioComum, Gerente

# Funcionário comum: 10% do salário
joao = FuncionarioComum("João Silva", 5000)
print(f"Bônus do João: R$ {joao.calcular_bonus():.2f}")  # R$ 500.00

# Gerente: 20% do salário + adicional
maria = Gerente("Maria Souza", 10000, 3000)
print(f"Bônus da Maria: R$ {maria.calcular_bonus():.2f}")  # R$ 5000.00
```

### 2. Gerenciamento de Múltiplos Funcionários

```python
        from sistema_rh import SistemaRH

        sistema = SistemaRH()
        sistema.adicionar_funcionario(joao)
        sistema.adicionar_funcionario(maria)

        # Listar todos os bônus
        sistema.listar_bonus()
        Saída:
        Log: Ação relacionada ao bônus registrada
        João Silva - Bônus: 500.0
        Log: Ação relacionada ao bônus registrada
        Maria Souza - Bônus: 5000.0
```

### 3. Verificação de Funcionários Cadastrados

```python
        print("Funcionários no sistema:")
        for func in sistema.funcionarios:
            print(f"- {func.get_nome()}")
        Saída:
        Funcionários no sistema:
        - João Silva
        - Maria Souza
```
## 📋 Pré-requisitos

        - Docker/Podman (opcional, para conteinerização)
        - Python 3.12+ (verifique com `python --version`)


 ## 🛠️ Instalação 

**Opção 1: Docker (Recomendado)**

```bash
        # Baixe e execute em 2 comandos:
        docker build -t bonus-system .
        docker run bonus-system
```

**Opção 2: Podman (Alternativa)**
```bash
        # Funciona igual ao Docker!
        podman build -t bonus-system .
        podman run bonus-system
```

**Opção 3: Localmente com Python**
```bash
        python -m venv .venv
        source .venv/bin/activate  # Linux/macOS
        .\.venv\Scripts\Activate.ps1  # Windows
        pip install -r requirements.txt
        python main.py
```

 ## 📌 Funcionalidades Chave

        
| Funcionalidade               | Como Acessar                                  | Exemplo de Uso                           |
|-------------------------------|-----------------------------------------------|-------------------------------------------|
| Calcular bônus individual     | `funcionario.calcular_bonus()`                | `joao.calcular_bonus()`                   |
| Adicionar funcionário         | `sistema.adicionar_funcionario(funcionario)`  | `sistema.adicionar_funcionario(joao)`     |
| Listar todos os bônus         | `sistema.listar_bonus()`                      | `sistema.listar_bonus()`                  |
| Ver funcionários cadastrados  | `sistema.funcionarios`                        | `for func in sistema.funcionarios: ...`   |     

## 🔍 Validações Automáticas

**Teste 1: Salários Negativos São Bloqueados**

```python
        try:
            joao.set_salario(-1000)
        except ValueError as e:
            print(e)  # "Salário não pode ser negativo"
```

**Teste 2: Logs São Gerados**
        Cada chamada de `listar_bonus()` produz logs verificáveis:
```
        Log: Ação relacionada ao bônus registrada
```

 ## ❓ Perguntas Frequentes

### Problemas Comuns

**Meu bônus está sendo calculado errado!**
- Verifique:
- Tipo de funcionário (comum/gerente)
- Bônus adicional informado para gerentes

**Não vejo os logs no Docker**
- Execute com modo interativo:
```bash
        podman run -it bonus-system
```

**Como atualizar salários?**
- Use:
```python
        funcionario.set_salario(novo_valor)
        sistema.listar_bonus()  # Recalcular
```


## 🔄 CI/CD (GitHub Actions)

        Fluxo automatizado que:
        - Executa testes em Python 3.12
        - Constrói imagem Docker para garantia de compatibilidade
        - Prepara para deploy 
