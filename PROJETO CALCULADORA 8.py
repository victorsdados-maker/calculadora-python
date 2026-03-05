
# PROJETO:Calculadora Multifuncional v8
# AUTOR: victorsdados-maker
# OBJETIVO:Aprendizado e Evolução Técnica.

# Foi feito um tratamento de erros em cada opção para garantir que o programa não quebre caso o usuário insira um valor inválido,como uma letra onde se espera um número,ou tente dividir por zero. O programa continua rodando mesmo após um erro,permitindo que o usuário corrija a entrada e continue usando a calculadora. 
# Melhorias na função de juros simples e juros compostos para calcular corretamente os juros com base na taxa informada pelo usuário.(Aceito o uso de porventagem com o símbolo %)
# Corrigida a função de média aritmética para calcular a média corretamente dividindo a soma pelo número de elementos.
# Melhorias na função de soma para garantir que o usuário insira um número válido de elementos e valores numéricos para somar.
# A última melhoria se trata de um tratamento de erro na função de hipotenusa para garantir que a hipotenusa seja maior que os catetos e que os valores sejam positivos,evitando resultados matematicamente incorretos ou erros de execução.

import math


def som(S1):
    soma=0
    for q in range(1,S1+1):
        while True:
            try:
                 S2=float(input(f"Digite o número {q}:"))
                 soma+=S2
                 break
            except ValueError:
                print("Valor inválido.Por favor,digite um número.")
    return soma

def fatorial(F1):
    result=1
    for e in range(1,F1+1):
        result *=e
    return result

def JS(c,i,t):
    J=c*(i/100)*t
    M=J+c
    return J,M

def JC(c,i,t):
    MJC=c*(1+i/100)**t
    return MJC

def bhaskara(a,b,c,delta):
    deltaR=math.sqrt(delta)
    x1=(-b + deltaR )/(2*a)
    x2=(-b - deltaR )/(2*a)
    return x1,x2  

def queda_livre(h,g):
    t=(2*h)/g
    t_final=math.sqrt(t)
    v=g*t_final
    return v , t_final

def hip(CC_HC,c1_h,c2):
    if CC_HC  == 1:
        return math.hypot(c1_h,c2)
    elif CC_HC== 2:
        if c1_h > c2:
            return math.sqrt(c1_h**2 - c2**2)
        else:
            return "Erro:Hipotenusa menor ou igual ao cateto!"

while True:
    opcao=input("Digite a letra da opção desejada:\n"
                            "a)Bhaskara.\n"
                            "b)Cálculo de queda livre.\n"
                            "c)Fatorial.\n"
                            "d)Juros compostos.\n"
                            "e)Juros simples.\n"
                            "f)Média arimética.\n"
                            "g)Soma.\n"
                            "h)Teorema de Pitágoras\n"
                            "s)Sair do programa.").lower()
    try:
        if opcao =="s":
            print("Saindo..Até mais!")
            break

        elif opcao == "a":
            while True:
                try:
                    a = float(input("Digite o valor de a: "))
                    if a == 0:
                        print("Erro: 'a' não pode ser zero em uma equação de 2º grau!")
                        continue
                    b=float(input("Digite o valor de b."))
                    c=float(input("Digite o valor de c."))  
                    delta=(b**2)-4*a*c        
                    if delta < 0:
                        print("Delta é menor que zero,essa equação não tem raiz.")
                        break
                    else:
                        X1,X2=bhaskara(a,b,c,delta)
                        print(f"x1={X1}.\n"
                                f"x2={X2}")
                        break
                except ValueError:
                    print("Valor inválido.Por favor,digite um número.")
                
        elif opcao == "b":
            while True:
                try:
                    g=9.8
                    tempo=0
                    h=float(input("Qual a altura em metros do prédio?"))
                    if h < 0:
                        print("Erro:A altura não pode ser negativa!")
                        continue
                    V,T=queda_livre(h,g)
                    while T>=tempo:
                        S=h-(g*tempo**2)/2
                        if S < 0: S = 0
                        print(f"A altura no segundo {tempo:.2f} é {S:.2f}m")
                        tempo+=0.1
                    print(f"A velocidade final é {V:.2f}m/s")
                    break
            
                except ValueError:
                    print("Valor inválido.Por favor,digite um número.")
                

        elif opcao == "c":
            while True:
                try:
                    F1=int(input("Qual o número?"))
                    if F1 < 0:
                        print("Erro:Não existe fatorial para números negativos!")
                        continue
                    fat=fatorial(F1)
                    print(f"O fatorial é {fat}.")
                    break
                
                except ValueError:
                    print("Valor inválido.Por favor,digite um número inteiro não negativo.")
            
        elif opcao == "d":
            while True:
                try:
                    c=float(input("Qual a capital?"))
                    i=float(input("Qual a taxa ao mês?(Ex:5%)").replace("%",""))
                    t=int(input("Qual o tempo em meses?"))
                    if c < 0 or i < 0 or t < 0:
                        print("Erro:Capital,taxa e tempo não podem ser negativos!")
                        continue
                    mjc=JC(c,i,t)
                    print(f"Montante final:{mjc:.2f}")
                    break

                except ValueError:
                    print("Valor inválido.Por favor,digite um número.")
            
        elif opcao == "e":
            while True:
                try:
                    c=float(input("Qual a capital?"))
                    i=float(input("Qual a taxa ao mês?(Ex:5%)").replace("%",""))
                    t=int(input("Qual o tempo em meses?"))
                    if c < 0 or i < 0 or t < 0:
                        print("Erro:Capital,taxa e tempo não podem ser negativos!")
                        continue
                    j,m=JS(c,i,t)
                    print(f"Juros:R${j:.2f}")
                    print(f"Montante final:{m:.2f}")
                    break

                except ValueError:
                    print("Valor inválido.Por favor,digite um número.")
            
        elif opcao== "f":
            while True:      
                    try:
                        S1=int(input("Quantos números são?"))
                        if S1 <= 0:
                            print("Erro:O número de elementos deve ser maior que zero!")
                            continue
                        so=som(S1)
                        media=so/S1
                        print(f"A média é  {media}.")   
                        break
                
                    except ValueError:
                        print("Valor inválido.Por favor,digite um número.")
       
        elif opcao == "g":
            while True:
                try:
                    S1=int(input("Quantos números deseja somar?"))
                    if S1 <= 0:
                        print("Erro:O número de elementos deve ser maior que zero!")
                        continue 
                    so=som(S1)
                    print(f"A soma é {so}")
                    break
                    
                except ValueError:
                    print("Valor inválido.Por favor,digite um número.")

        elif opcao == "h":
            while True:
                try:
                    CC_HC=int(input("Digite 1 caso queira descobrir hipotenusa e 2 para descobrir um ccateto."))
                    if CC_HC not in [1,2]:
                        print("Opção inválida.Por favor, digite 1 ou 2.")
                        continue
                    if CC_HC == 1:
                        c1_h=float(input("Qual o valor do cateto 1?"))
                        c2=float(input("Qual o valor do cateto 2?"))
                        if c1_h <= 0 or c2 <= 0:
                            print("Erro:Valores dos catetos devem ser maiores que zero!")
                            continue
                        res=hip(CC_HC,c1_h,c2)
                        print(f"A hipotenusa é {res}")
                    elif CC_HC == 2:
                        c1_h=float(input("Qual o valor da hipotenusa?"))
                        c2=float(input("Qual o valor do cateto?"))
                        if c1_h <= c2 or c1_h < 0 or c2 <= 0:
                            print("Erro:Hipotenusa deve ser maior que o cateto e ambos devem ser maiores que zero!")
                            continue
                        res=hip(CC_HC,c1_h,c2)
                        print(f"O cateto é {res}")
                    break

                except ValueError:
                    print("Valor inválido.Por favor,digite um número.") 
                      
    except ValueError as erro:
        print(f"\nOps!Tivemos um erro de valor:{erro}\nDica:use apenas números e ponto (.) em decimais.voltando ao menu...)")
    except ZeroDivisionError:
        print(f"\nOps!Você tentou dividir por zero.\n")
         
            
    else:
        if opcao not in "abcdefghs":
            print("Opção inválida.")
        
