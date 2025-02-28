def main():
    print("Hello, World!")

def programa1():
    # Crie um programa que peça o nome do usuário e imprima o número de caracteres.
    print("Seu nome contém " + str(len(input("Digite seu nome: "))) + " caracteres.")

def programa2():
    # Crie um programa que peca o usuario que digite 2 numeros e exiba a soma dos dois (use variaveis).
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    print("A soma dos dois números é: " + str(numero1 + numero2))

def desafio():
    #Instruções:
    #Valor de Bonus (Constante)
    valorBonus = 1000
    #O programa deve começar solicitando ao usuário que insira seu nome.
    nomeUsuario = input("Digite o seu nome: ")
    #Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
    valorSalario = float(input("Digite o valor do seu salário: "))
    #Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
    porcentagemBonus = float(input("Digite a porcentagem do bônus recebido: "))
    #O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
    #O valor do bônus é calculado multiplicando o salário do usuário pela porcentagem do bônus.
    valorBonus = valorBonus + valorSalario * (porcentagemBonus / 100)
    #Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
    print(f"Olá {nomeUsuario}, o seu valor bônus foi de {valorBonus}")

if __name__ == "__main__":
    #Peça ao usuário que escolha uma opção e de acordo com ela execute uma das funções acima.
    print("Escolha uma opção:")
    print("1 - Programa 1")
    print("2 - Programa 2")
    print("3 - Programa 3 (Desafio)")
    opcao = input("Digite o número da opção desejada: ")
    if opcao == "1":
        programa1()
    elif opcao == "2":  
        programa2()
    elif opcao == "3":
        desafio()
    else:
        print("Opção inválida!") 