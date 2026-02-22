
# PROJETO:Calculadora Multifuncional v5
# AUTOR: victorsdados-maker
# OBJETIVO:Aprendizado e Evolução Técnica.


import math # biblioteca no início para para melhor performace.

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
            
while True:                  # Diferente da v3 essa versão possui um laço while True que torna desnecessário executar o código manualmente outro vez caso deseje fazzer outra operação. 
    opcao=input("Digite a letra da opção desejada:\n"
                            "a)Soma.\n"
                            "b)Média.\n"
                            "c)Fatorial.\n"
                            "d)Juros simples.\n"
                            "e)Juros compostos.\n"
                            "f)Bhaskara.\n"
                            "s)Sair do programa.").lower()
    
    if opcao =="s":
        print("Saindo..Até mais!")
        break                  # Finaliza o loop.

    
    if opcao == "a":
         S1=int(input("Quantos números deseja somar?"))    
         so=som(S1)
         print(f"A soma é {so}")
         
    elif opcao== "b":
        S1=int(input("Quantos números são?"))
        so=som(S1)
        media=so/S1
        print(f"A média é  {media}.")
        
    elif opcao == "c":
        F1=int(input("Qual o número?"))
        fat=fatorial(F1)
        print(f"O fatorial é {fat}.")
        
    elif opcao == "d":
        c=float(input("Qual a capital?"))
        i=float(input("Qual a taxa ao mês?(Digite em formato decimal)"))
        t=int(input("Qual o tempo em meses?"))
        j,m=JS(c,i,t)
        print(f"Juros:R${j:.2f}")
        print(f"Montante final:{m:.2f}")           # Uso de formatação :.2f para financeiros.
        
    elif opcao == "e":
        c=float(input("Qual a capital?"))
        i=float(input("Qual a taxa ao mês?(Digite em formato decimal)"))
        t=int(input("Qual o tempo em meses?"))
        mjc=JC(c,i,t)
        print(f"Montante final:{mjc:.2f}")         # Uso de formatação :.2f para financeiros.
        
    elif opcao == "f":
        a = float(input("Digite o valor de a: "))
        while a == 0:										# Para que seja uma equação de 2º grau o a não pode ser 0,esta linha cuida disso.
            print("Erro: 'a' não pode ser zero em uma equação de 2º grau!")
            a = float(input("Digite um valor para 'a' diferente de zero: "))
        b=float(input("Digite o valor de b."))
        c=float(input("Digite o valor de c."))
        
        delta=(b**2)-4*a*c
        if delta < 0:										#Delta é calculado e enviado a função caso seja igual ou maior que 0,caso seja negativo o usuário é avisado que não há raiz para essa equação,feito desta forma dentro do corpo principal a função só recebe dados que resultam em números reais.
            print("Delta é menor que zero,essa equação não tem raiz.")    
        else:
            X1,X2=bhaskara(a,b,c,delta)
            print(f"x1={X1:.2f}.\n"
                       f"x2={X2:.2f}")    #Uso de fromatação :.2f para um resultado mais preciso.
        
    else:
        print("Opção inválida.")
        



