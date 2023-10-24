""" 
Faça uma calculadora que forneça as seguintes opções para o usuário, usando funções sempre que necessário. Cada opção deve usar como operando um número lido do teclado e o valor atual da memória. Por exemplo, se o estado atual da memória é 5, e o usuário escolhe somar, ele deve informar um novo número (por exemplo, 3). Após a conclusão da soma, o novo estado da memória passa a ser 8.

Estado da memória: 0
Opções:
(1) Somar
(2) Subtrair
(3) Multiplicar
(4) Dividir
(5) Limpar memória
(6) Sair do programa
 """

estado_memoria = 0;

op = 0

def calculadora():
    print('='*15)
    print('Calculadora')
    print('='*15)
    print('1- Somar')
    print('2- Subtrair')
    print('3- Multiplicar')
    print('4- Dividir')
    print('5- Limpar memória')
    print('6- Sair do programa')
    return int(input('Digite sua opção: '))

def numero(estado_memoria):
    print(f'Memória: {estado_memoria:.0f}')
    num = float(input('Digite o número desejado: '));
    return num

def somar(num, memoria):
    memoria += num
    return memoria

def subtrair(num, memoria):
    memoria -= num
    return memoria

def multiplicar(num, memoria):
    if (memoria == 0):
        num2 = float(input('Sua memória é igual a zero. Digite um número para multiplicar o número anterior: '))
        
    memoria = num2 * num
    return memoria

def dividir(num, memoria):
    if (memoria == 0):
        num2 = float(input('Sua memória é igual a zero. Digite um número para ser dividido pelo número anterior: '))
    
    memoria = num2 / num
    return memoria

def limparmemoria(memoria):
    memoria = 0
    return memoria


while op != 6:
    op = calculadora()
    if op == 1:
        num = numero(estado_memoria);
        estado_memoria = somar(num, estado_memoria);
        print(f'Memória: {estado_memoria:.2f}');
        
    elif op == 2:
        num = numero(estado_memoria);
        estado_memoria = subtrair(num, estado_memoria);
        print(f'Memória: {estado_memoria:.0f}');
    
    elif op == 3:
        num = numero(estado_memoria);
        estado_memoria = multiplicar(num, estado_memoria);
        print(f'Memória: {estado_memoria:.2f}');
    elif op == 4:
        num = numero(estado_memoria);
        estado_memoria = dividir(num, estado_memoria);
        print(f'Memória: {estado_memoria:.2f}');
    
    elif op == 5:
        estado_memoria = limparmemoria(estado_memoria);
        print(f'Memória: {estado_memoria:.2f}');
else:
    print('Saindo....')