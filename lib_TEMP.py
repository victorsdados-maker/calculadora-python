
# PROJETO:Calculadora Multifuncional
# AUTOR: victorsdados-maker
# OBJETIVO:Aprendizado e Evolução Técnica.

# Necessário para funcionamento total da versão 9 da calculadora multifuncional,com funções de conversão de temperatura entre Celsius,Fahrenheit e Kelvin,com tratamento de erro para garantir que o programa continue rodando mesmo se o arquivo lib_TEMP.py não for encontrado.
# Caso este módulo não seja encontrado,as funções de conversão de temperatura não estarão disponíveis,mas as outras funcionalidades da calculadora continuarão funcionando normalmente.

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