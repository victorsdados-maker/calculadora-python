
# PROJETO:Calculadora Multifuncional v6
# AUTOR: victorsdados-maker
# OBJETIVO:Aprendizado e Evolução Técnica.


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

def queda_livre(h,g): #Função de queda livre,recebe _h_ e _g_,faz uso dá Função Horária do Tempo de Queda,Equação da Velocidade no MUV e fora do def,mas especificamente dentro do elif equivalente o uso da Função Horária da Posição (ou Altura) na linha 80.
    t=(2*h)/g
    t_final=math.sqrt(t)
    v=g*t_final
    return v , t_final

while True:
    opcao=input("Digite a letra da opção desejada:\n"
                            "a)  Bhaskara.\n"
                            "b)  Cálculo de queda livre.\n"
                            "c)  Fatorial.\n"                                   # Menu agora em ordem alfabética para facilitar a interação com o usuário.
                            "d)  Juros compostos.\n"
                            "e)  Juros simples.\n"
                            "f)  Média Aritmética.\n"
                            "g)  Soma.\n"
                            "s)  Sair do programa.").lower()
    
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
        g=9.8 #Valor fixo da gravidade.
        tempo=0  #Valor primário de tempo
        h=float(input("Qual a altura em metros do prédio?"))
        V,T=queda_livre(h,g)                                                             # Chama a função e concedi o valor de retorno as variáveis _V_ e _T_.
        while T>=tempo:                                                                   #Laço é executado enquanto _tempo_ é menor que _T_ que representa o tempo final.
            S=h-(g*tempo**2)/2
            if S < 0: S = 0                                                                       # Nesta linha o if define que caso _S_ venha a se tornar negativo seu valor será forçado a ser zero.
            print(f"A altura no segundo {tempo:.2f} é {S:.2f}m")
            tempo+=0.1                                                                        # Decorrer do tempo no cronõmetro,cada atualização é usada usada no ínicio do loop novamente até que ele venha a parar.
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
         
    

    
    else:
        print("Opção inválida.")
        




