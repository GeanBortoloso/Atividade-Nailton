from Matematica import soma, subtracao, multiplicacao, divisao
from Matematica.Avancados import quadrado, cubo
import os

def calc():
    print('''
Qual operação você gostaria de tentar?:
+ para Adição
- para Subtração
* para Multiplicação
/ para Divisão
2 para Quadrado
3 para Cubo
''')


def escolha():
    calc()
    op = input("Digite a operação que deseja realizar: ")

    if op in ['+', '-', '*', '/']:
        x = float(input("Primeiro número: "))
        y = float(input("Segundo número: "))
        
        if op == '+':
            print(f"O resultado de {x} + {y} é: {soma.soma(x, y)}")


        elif op == '-':
            print(f"O resultado de {x} - {y} é: {subtracao.subtracao(x, y)}")


        elif op == '*':
            print(f"O resultado de {x} * {y} é: {multiplicacao.multiplicacao(x, y)}")


        elif op == '/':
            print(f"O resultado de {x} / {y} é: {divisao.divisao(x, y)}")
        

    elif op == '2':
        x = int(input("Digite o número: "))
        print(f"O resultado de {x}² é: {quadrado.quadrado(x)}")


    elif op == '3':
        x = int(input("Digite o número: "))
        print(f"O resultado de {x}³ é: {cubo.cubo(x)}")
    
    else:
        limpar()
        print("Operação inválida.")
        escolha()

    again()


def again():
    calc_dnv = input('''
Gostaria de fazer outra operação? [S/N]
''')

    if calc_dnv.upper() == 'S':
        limpar()
        escolha()
        
    elif calc_dnv.upper() == 'N':
        limpar()
        print('Até mais!')
        
    else:
        again()

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



escolha()