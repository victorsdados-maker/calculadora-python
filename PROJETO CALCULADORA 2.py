
# PROJETO:Calculadora Multifuncional v1
# AUTOR: victorsdados-maker
# OBJETIVO:Aprendizado e Evolução Técnica.


#                 Menu de Escolhas
opcao=input("Digite a letra da opção desejada:\n"
                        "a)Soma.\n"
                        "b)Média.\n"
                        "c)Fatorial.\n"
                        "d)Juros simples.\n"
                        "e)Juros compostos.").lower()

def som(S1):
    """Função SOMA,recebe quantos números seram somados,uso de laço for com range para obter os números que devem ser somados."""
    soma=0
    for q in range(1,S1+1):
        S2=float(input(f"Digite o número {q}:"))
        soma+=S2
    return soma

def fatorial(F1):
    """Função FATORIAL,recebe o número que o usuário deseja o fatorial,uso de laço for com range para descrecer a variável _F1_ resultando nos valores de _e_ que são multiplicados em _result_"""
    result=1
    for e in range(1,F1+1):
        result *=e
    return result

def JS(c,i,t):
    """Função JUROS SIMPLES,recebe as variáveis c,i e t que respectivamente são;capital,txa e tempo,uso da fórmula de juros simples."""
    J=c*i*t
    M=J+c
    return J,M

def JC(c,i,t):
    """Função JUROS COMPOSTOS,recebe as mesmas variáveis que a função JS,uso da fórmula de juros compostos."""
    MJC=c*(1+i)**t
    return MJC


if opcao == "a":
     S1=int(input("Quantos números deseja somar?"))     # Obtém o valor de _S1_.
     so=som(S1)                                                                          # Chama a função som(responsável pela soma) e dá valor do retorno a variável _so_.
     print(f"A soma é {so}")
     
elif opcao== "b":
    S1=int(input("Quantos números são?"))     # Obtém o valor de _S1_.
    so=som(S1)                                                        #Chama a função som(é desnecessário o uso de uma função apenas para média),retorna o valor e o aplica em _so_.
    media=so/S1                                                     #Divide _so_ por _S1_.
    print(f"A média é  {media}.")
    
elif opcao == "c":
    F1=int(input("Qual o número?"))     # Obtém o valor de _F1_.
    fat=fatorial(F1)                                     # Chama a função fatorial,concedi o valor do retorno
    print(f"O fatorial é {fat}.")
    
elif opcao == "d":
    c=float(input("Qual a capital?"))
    i=float(input("Qual a taxa ao mês?(Digite em formato decimal)"))     # Três entradas de dados que dão valor a _c_,_i_ e _t_.
    t=int(input("Qual o tempo em meses?"))                                                 
    j,m=JS(c,i,t)                                                                                                       #Chama a função JS(responsável pelos juros simples),concedi o valor do retorno a _j_ e _m_.
    print(f"Juros:R${j:.2f}")
    print(f"Montante final:{m:.2f}")
    
elif opcao == "e":
    c=float(input("Qual a capital?"))
    i=float(input("Qual a taxa ao mês?(Digite em formato decimal)"))     # Três entradas de dados que dão valor a _c_,_i_ e _t_.                                                                                                                              
    t=int(input("Qual o tempo em meses?"))                                                 
    mjc=JC(c,i,t)                                                                                                     # Chama a função JC(responsável pelos juros compostos),concedi o valor do retorno a _mjc_.
    print(f"Montante final:{mjc:.2f}")
    
else:
    print("Opção inválida.")     # Ativo caso digite uma letra não pertencente ao menu.
    
