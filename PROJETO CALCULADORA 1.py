
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

soma=0  #Definição de valor inicial as variáveis.
result=1


#         Executado ao escolher soma,entrada da quantia de números,laço que faz a repetição de entrada.
if opcao == "a":
    S1=int(input("Quantos números deseja somar?"))
    for q in range(1,S1+1):
        S2=float(input(f"Digite o número {q}:"))
        soma+=S2
    print(f"A soma é {soma}.")
    
#         Exato mesma estrutura de SOMA,apenas ocorre de dividir pela variável M1 executando assim a média.
elif opcao== "b":
    M1=int(input("Quantos números são?"))
    for w in range(1,M1+1):
        M2=float(input(f"Digite o número {w}:"))
        soma+=M2
    media=soma/M1
    print(f"A média é  {media}.")
    
#         O laço decresce o valor da variável F1 e dentro do próprio laço ocorre a multiplicação entre os fatores.
elif opcao == "c":
    F1=int(input("Qual o número?"))
    for e in range(1,F1+1):
        result *=e
    print(f"O fatorial é {result}.")
    
#        Três entradas(duas entradas de dados float e uma entrada de int),nenhum laço,apenas o uso das fórmulas de juros simples e montante.
elif opcao == "d":
    c=float(input("Qual a capital?"))
    i=float(input("Qual a taxa ao mês?(Digite em formato decimal)"))
    t=int(input("Qual o tempo em meses?"))
    J=c*i*t
    M=J+c
    print(f"Juros:R${J:.2f}")
    print(f"Montante final:{M:.2f}")
    
#        Entradas iguais as de jJUROS SIMPLES,nenhum laço apenas o uso da fórmula de juros compostos.
elif opcao == "e":
    c=float(input("Qual a capital?"))
    i=float(input("Qual a taxa ao mês?(Digite em formato decimal)"))
    t=int(input("Qual o tempo em meses?"))
    MJC=c*(1+i)**t
    print(f"Montante final:{MJC:.2f}")

#        Caso a o usuário digite uma letra cuja não haja opção no Menu de Escolhas esse else entra em ação.
else:
    print("Opção inválida.")

    