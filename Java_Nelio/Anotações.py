# Solicita ao usuário que insira o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o segundo número
num2 = float(input("Digite o segundo número: "))

# Calcula a soma dos dois números
soma = num1 + num2

# Imprime o resultado
print("A soma dos números é: ", soma)

class Banco:
    def __init__(self):
        # Inicializa a tabela de agências e contas
        self.tabela = [
            {"agencia": "001", "conta": "123456"},
            {"agencia": "002", "conta": "789012"},
            # Adicione mais contas conforme necessário
        ]

    def buscar_cliente(self, agencia, conta):
        # Procura o cliente na tabela
        for linha in self.tabela:
            if linha["agencia"] == agencia and linha["conta"] == conta:
                return True
        return False

# Uso da classe
banco = Banco()
existe = banco.buscar_cliente("001", "123456")
print("Cliente existe na lista: ", existe)