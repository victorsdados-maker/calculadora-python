
# PROJETO:Calculadora Multifuncional v10
# AUTOR: victorsdados-maker
# OBJETIVO:Aprendizado e Evolução Técnica.

# Limpeza e organização devido a criação de uma biblioteca geral.
#A falta da biblioteca geral não causa quebra e fechamento do programa,porém o inutiliza.
import math

biblioteca_disponivel = True
try:
    import lib_geral as geral
except ModuleNotFoundError:
    print("Erro: O arquivo 'lib_calculadora_geral.py' não foi encontrado na mesma pasta!Funções de conversão de temperatura não estarão disponíveis.")
    biblioteca_disponivel= False


while True:
    opcao=input("Digite a letra da opção desejada:\n"
                            "a)Bhaskara.\n"
                            "b)Cálculo de queda livre.\n"
                            "c)Conversor de temperatura.\n"
                            "d)Fatorial.\n"
                            "e)Juros compostos.\n"
                            "f)Juros simples.\n"
                            "g)Média arimética.\n"
                            "h)Soma.\n"
                            "i)Teorema de Pitágoras\n"
                            "s)Sair do programa.").lower().strip()
    try:
        if opcao =="s":
            print("Saindo..Até mais!")
            break

        elif opcao == "a":
            while True:
                try:
                    a = float(input("Digite o valor de a: ").strip())
                    if a == 0:
                        print("Erro: 'a' não pode ser zero em uma equação de 2º grau!")
                        continue
                    b=float(input("Digite o valor de b.").strip())
                    c=float(input("Digite o valor de c.").strip())
                    delta=(b**2)-4*a*c        
                    if delta < 0:
                        print("Delta é menor que zero,essa equação não tem raiz.")
                        break
                    else:
                        X1,X2=geral.bhaskara(a,b,c,delta)
                        print(f"x1={X1}.\n"
                                f"x2={X2}")
                        break
                except ValueError:
                    print("Valor inválido.Por favor,digite um número.")
                
        elif opcao == "b":
            while True:
                try:
                    h=9.8
                    tempo=0
                    i=float(input("Qual a altura em metros do prédio?").strip())
                    if i < 0:
                        print("Erro:A altura não pode ser negativa!")
                        continue
                    V,T=geral.queda_livre(i,h)
                    while T>=tempo:
                        S=i-(h*tempo**2)/2
                        if S < 0: S = 0
                        print(f"A altura no segundo {tempo:.2f} é {S:.2f}m")
                        tempo+=0.1
                    print(f"A velocidade final é {V:.2f}m/s")
                    break
            
                except ValueError:
                    print("Valor inválido.Por favor,digite um número.")
                
        elif opcao == "c":
            if not biblioteca_disponivel:
                print("Funções de conversão de temperatura não estão disponíveis devido à ausência do arquivo 'biblioteca_mat_TEMP.py'.")
                continue
            while True:
                try:
                    op_conver=input("Digite a letra equivalente a medida que deseja converter:\n"
                                    "a)Celsius.\n"
                                    "b)Fahrenheit.\n"
                                    "c)Kelvin.").lower().strip()
                    
                    if op_conver == "a":
                        res=geral.temp.conver_celsius(op_conver)
                        print(res)
                    elif op_conver == "b":
                        res=geral.temp.conver_fahrenheit(op_conver)
                        print(res)
                    elif op_conver == "c":
                        res=geral.temp.conver_kelvin(op_conver)
                        print(res)
                    else:
                        print("Opção inválida.Por favor, escolha 'a', 'b' ou 'c'.")
                    break
                except ValueError:
                    print("Valor inválido.Por favor,digite um número.")
                    

        elif opcao == "d":
            while True:
                try:
                    F1=int(input("Qual o número?"))
                    if F1 < 0:
                        print("Erro:Não existe fatorial para números negativos!")
                        continue
                    fat=geral.fatorial(F1)
                    print(f"O fatorial é {fat}.")
                    break
                
                except ValueError:
                    print("Valor inválido.Por favor,digite um número inteiro não negativo.")
            
        elif opcao == "e":
            while True:
                try:
                    c=float(input("Qual a capital?").strip())
                    i=float(input("Qual a taxa ao mês?(Ex:5%)").replace("%","").strip())
                    t=int(input("Qual o tempo em meses?").strip())
                    if c < 0 or i < 0 or t < 0:
                        print("Erro:Capital,taxa e tempo não podem ser negativos!")
                        continue
                    mjc=geral.JC(c,i,t)
                    print(f"Montante final:{mjc:.2f}")
                    break

                except ValueError:
                    print("Valor inválido.Por favor,digite um número.")
            
        elif opcao == "f":
            while True:
                try:
                    c=float(input("Qual a capital?").strip())
                    i=float(input("Qual a taxa ao mês?(Ex:5%)").replace("%","").strip())
                    t=int(input("Qual o tempo em meses?").strip())
                    if c < 0 or i < 0 or t < 0:
                        print("Erro:Capital,taxa e tempo não podem ser negativos!")
                        continue
                    j,m=geral.JS(c,i,t)
                    print(f"Juros:R${j:.2f}")
                    print(f"Montante final:{m:.2f}")
                    break

                except ValueError:
                    print("Valor inválido.Por favor,digite um número.")
            
        elif opcao== "g":
            while True:      
                    try:
                        S1=int(input("Quantos números são?").strip())
                        if S1 <= 0:
                            print("Erro:O número de elementos deve ser maior que zero!")
                            continue
                        so=geral.som(S1)/S1
                        print(f"A média é  {so}.")   
                        break
                
                    except ValueError:
                        print("Valor inválido.Por favor,digite um número.")
       
        elif opcao == "h":
            while True:
                try:
                    S1=int(input("Quantos números deseja somar?").strip())
                    if S1 <= 0:
                        print("Erro:O número de elementos deve ser maior que zero!")
                        continue 
                    so=geral.som(S1)
                    print(f"A soma é {so}")
                    break
                    
                except ValueError:
                    print("Valor inválido.Por favor,digite um número.")

        elif opcao == "i":
            while True:
                try:
                    CC_HC=int(input("Digite 1 caso queira descobrir hipotenusa e 2 para descobrir um ccateto.").strip())
                    if CC_HC not in [1,2]:
                        print("Opção inválida.Por favor, digite 1 ou 2.")
                        continue
                    if CC_HC == 1:
                        c1_h=float(input("Qual o valor do cateto 1?").strip())
                        c2=float(input("Qual o valor do cateto 2?").strip())
                        if c1_h <= 0 or c2 <= 0:
                            print("Erro:Valores dos catetos devem ser maiores que zero!")
                            continue
                        res=geral.hip(CC_HC,c1_h,c2)
                        print(f"A hipotenusa é {res}")
                    elif CC_HC == 2:
                        c1_h=float(input("Qual o valor da hipotenusa?").strip())
                        c2=float(input("Qual o valor do cateto?").strip())
                        if c1_h <= c2 or c1_h < 0 or c2 <= 0:
                            print("Erro:Hipotenusa deve ser maior que o cateto e ambos devem ser maiores que zero!")
                            continue
                        res=geral.hip(CC_HC,c1_h,c2)
                        print(f"O cateto é {res}")
                    break

                except ValueError:
                    print("Valor inválido.Por favor,digite um número.") 
                      
    except ZeroDivisionError:
        print(f"\nOps!Você tentou dividir por zero.\n")
                
    else:
        if opcao not in "abcdefghis":
            print("Opção inválida.")
        
