
# PROJETO:Calculadora Multifuncional v7
# AUTOR: victorsdados-maker
# OBJETIVO:Aprendizado e Evolução Técnica.

# Primeira base de estabilidade e funcionalidade,com adição de uma nova função para calcular a hipotenusa ou um cateto usando o Teorema de Pitágoras.
# Melhorias na estrutura do código,como o uso de try-except para tratamento de erros e a organização do menu em ordem alfabética para facilitar a interação com o usuário.
# O programa continua evoluindo para se tornar cada vez mais completo e robusto.

import math


def som(S1):
    soma=0
    for q in range(1,S1+1):
        S2=float(input(f"Digite o número {q}:"))
        soma+=S2
    return soma

def fatorial(F1):
    result=1
    for e in range(1,F1+1):
        result *=e
    return result

def JS(c,i,t):
    J=c*i*t
    M=J+c
    return J,M

def JC(c,i,t):
    MJC=c*(1+i)**t
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

# Uso da biblioteca math para calcular a hipotenusa ou um dos catetos,dependendo da escolha do usuário.
# A função recebe três parâmetros: a escolha do usuário (1 para hipotenusa e 2 para cateto).
# O resultado é calculado usando as fórmulas do Teorema de Pitágoras e retornado para ser impresso na tela.
    

def hip(CC_ou_HC,c1_h,c2):
    if CC_ou_HC == 1:
        return math.hypot(c1_h,c2)
    elif CC_ou_HC == 2:
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
    
    try: # Uso de try para tratar erros que possam ocorrer durante a execução do programa,como o usuário inserir um valor inválido ou tentar dividir por zero. O programa continua rodando mesmo após um erro,permitindo que o usuário corrija a entrada e continue usando a calculadora.
        if opcao =="s":
            print("Saindo..Até mais!")  
            break

        elif opcao == "a":
            a = float(input("Digite o valor de a: "))
            while a == 0:
                print("Erro: 'a' não pode ser zero em uma equação de 2º grau!")
                a = float(input("Digite um valor para 'a' diferente de zero: "))
            b=float(input("Digite o valor de b."))
            c=float(input("Digite o valor de c."))  
            delta=(b**2)-4*a*c        
            if delta < 0:
                print("Delta é menor que zero,essa equação não tem raiz.")
            else:
                X1,X2=bhaskara(a,b,c,delta)
                print(f"x1={X1}.\n"
                           f"x2={X2}")
                
        elif opcao == "b":
            g=9.8
            tempo=0
            h=float(input("Qual a altura em metros do prédio?"))
            V,T=queda_livre(h,g)
            while T>=tempo:
                S=h-(g*tempo**2)/2
                if S < 0: S = 0
                print(f"A altura no segundo {tempo:.2f} é {S:.2f}m")
                tempo+=0.1
            print(f"A velocidade final é {V:.2f}m/s")
            
        elif opcao == "c":
            F1=int(input("Qual o número?"))
            fat=fatorial(F1)
            print(f"O fatorial é {fat}.")
            
        elif opcao == "d":
            c=float(input("Qual a capital?"))
            i=float(input("Qual a taxa ao mês?(Digite em formato decimal)"))
            t=int(input("Qual o tempo em meses?"))
            mjc=JC(c,i,t)
            print(f"Montante final:{mjc:.2f}")
            
        elif opcao == "e":
            c=float(input("Qual a capital?"))
            i=float(input("Qual a taxa ao mês?(Digite em formato decimal)"))
            t=int(input("Qual o tempo em meses?"))
            j,m=JS(c,i,t)
            print(f"Juros:R${j:.2f}")
            print(f"Montante final:{m:.2f}")
            
        elif opcao== "f":
            S1=int(input("Quantos números são?"))
            so=som(S1)
            media=so/S1
            print(f"A média é  {media}.")   
       
        elif opcao == "g":
             S1=int(input("Quantos números deseja somar?"))    
             so=som(S1)
             print(f"A soma é {so}")
             
        elif opcao == "h":
            CC_ou_HC=int(input("Digite 1 caso queira descobrir hipotenusa e 2 para descobrir um cateto.")) # Uso de if para que o usuário escolha entre descobrir a hipotenusa ou um cateto, e depois disso o programa solicita os valores necessários para cada caso e chama a função _hip_ para realizar o cálculo. O resultado é então impresso na tela.
            if CC_ou_HC == 1:
                c1_h=float(input("Qual o valor do cateto 1?"))
                c2=float(input("Qual o valor do cateto 2?"))
                res=hip(CC_ou_HC,c1_h,c2)
                print(f"A hipotenusa é {res}") 
            elif CC_ou_HC == 2:
                 c1_h=float(input("Qual o valor da hipotenusa?"))
                 c2=float(input("Qual o valor do cateto?"))
                 res=hip(CC_ou_HC,c1_h,c2)
                 print(f"O cateto é {res}")

    # Tratamento de erros para garantir que o programa não quebre caso o usuário insira um valor inválido,como uma letra onde se espera um número,ou tente dividir por zero.                  
    except ValueError as erro:
        print(f"\nOps!Tivemos um erro de valor:{erro}\nDica:use apenas números e ponto (.) em decimais.voltando ao menu...)")
    except ZeroDivisionError:
        print(f"\nOps!Você tentou dividir por zero.\n")
         
            
    else:
        if opcao not in "abcdefghs":
            print("Opção inválida.")
        





