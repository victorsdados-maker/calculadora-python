
# PROJETO:Calculadora Multifuncional
# AUTOR: victorsdados-maker
# OBJETIVO:Aprendizado e Evolução Técnica.

# Necessária para uso da calculadora da versão 10 e em diante,pois as funções estão organizadas aqui


import math

def bhaskara(a,b,c,delta):
    deltaR=math.sqrt(delta)
    x1=(-b + deltaR )/(2*a)
    x2=(-b - deltaR )/(2*a)
    return x1,x2  

def queda_livre(i,h):
    t=(2*i)/h
    t_final=math.sqrt(t)
    v=h*t_final
    return v , t_final

class temp:
    def conver_celsius(op_conver):
        if op_conver == "a":
            while True:
                try:
                    k_f=input("Deseja converter de Celsius para Fahrenheit ou de Fahrenheit para Celsius?\n"
                            "a)Celsius para Fahrenheit.\n"
                            "b)Celsius para Kelvin.\n").lower()
                    if k_f == "a":
                        c=float(input("Qual a temperatura em Celsius?").replace("°C",""))
                        f=(c*1.8)+32
                        print(f"A temperatura em Fahrenheit é {f:.2f}°F.")
                        break
                    elif k_f == "b":
                        c=float(input("Qual a temperatura em Celsius?").replace("°C",""))
                        k=c+273.15
                        print(f"A temperatura em Kelvin é {k:.2f}K.")
                        break
                    else:
                        print("Opção inválida.Por favor, escolha 'a' ou 'b'.")
                    return k_f
                except ValueError:
                    print("Valor inválido.Por favor,digite um número.")

    def conver_fahrenheit(op_conver):
        if op_conver == "b":
            while True:
                try:
                    c_k=input("Deseja converter de Fahrenheit para Celsius ou de Fahrenheit para Kelvin?\n"
                            "a)Fahrenheit para Celsius.\n"
                            "b)Fahrenheit para Kelvin.\n").lower()
                    if c_k == "a":
                        f=float(input("Qual a temperatura em Fahrenheit?").replace("°F",""))
                        c=(f-32)/1.8
                        print(f"A temperatura em Celsius é {c:.2f}°C.")
                        break
                    elif c_k == "b":
                        f=float(input("Qual a temperatura em Fahrenheit?").replace("°F",""))
                        k=(f-32)*5/9+273.15
                        print(f"A temperatura em Kelvin é {k:.2f}K.")
                        break
                    else:
                        print("Opção inválida.Por favor, escolha 'a' ou 'b'.")
                    return c_k
                except ValueError:
                    print("Valor inválido.Por favor,digite um número.")

    def conver_kelvin(op_conver):
        if op_conver == "c":
            while True:
                try:
                    c_f=input("Deseja converter de Kelvin para Celsius ou de Kelvin para Fahrenheit?\n"
                            "a)Kelvin para Celsius.\n"
                            "b)Kelvin para Fahrenheit.\n").lower()
                    if c_f == "a":
                        k=float(input("Qual a temperatura em Kelvin?").replace("K",""))
                        c=k-273.15
                        print(f"A temperatura em Celsius é {c:.2f}°C.")
                        break
                    elif c_f == "b":
                        k=float(input("Qual a temperatura em Kelvin?").replace("K",""))
                        f=(k-273.15)*1.8+32
                        print(f"A temperatura em Fahrenheit é {f:.2f}°F.")
                        break
                    else:
                        print("Opção inválida.Por favor, escolha 'a' ou 'b'.")
                    return c_f
                except ValueError:
                    print("Valor inválido.Por favor,digite um número.")

def fatorial(F1):
    if F1 == 0 or F1 == 1:
        return 1
    else:
        return math.factorial(F1)
    

def JC(c,i,t):
    MJC=c*(1+i/100)**t
    return MJC

def JS(c,i,t):
    J=c*(i/100)*t
    M=J+c
    return J,M

def som(S1):
    soma=0
    for q in range(1,S1+1):
        while True:
            try:
                 S2=float(input(f"Digite o número {q}:").strip())
                 soma+=S2
                 break
            except ValueError:
                print("Valor inválido.Por favor,digite um número.")
    return soma

def hip(CC_HC,c1_h,c2):
    if CC_HC  == 1:
        return math.hypot(c1_h,c2)
    elif CC_HC== 2:
        if c1_h > c2:
            return math.sqrt(c1_h**2 - c2**2)
        else:
            return "Erro:Hipotenusa menor ou igual ao cateto."







