# Programa para calcular IMC
# Desenvolvido por Celso

print("****************************************")
print("*        CALCULADORA DE IMC            *")
print("****************************************")
print()

# CRIAÇÃO DAS VARIÁVEIS
nome = ""
peso = 0
altura = 0.0
imc = 0.0

# ENTRADA DOS DADOS
nome = input("Digite o seu nome: ")
peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

# PROCESSAR OS VALORES PARA OBTER O IMC

imc = peso / altura ** 2

# SAÍDA DO PROCESSAMENTO

if imc < 18.5:
    situacao = "Abaixo do peso."
elif imc >= 18.5 and imc < 25:
    situacao = "Peso Normal"
elif imc >= 25 and imc < 30:
    situacao = "Sobrepeso"
elif imc >= 30 and imc < 35:
    situacao = "Obesidade Grau I"
elif imc >= 35 and imc < 40:
    situacao = "Obesidade Grau II"
else:
    situacao = "Obesidade Grau III ou Mórbida"

print()
print("*******************************")
print("*            RESULTADO                 *")
print()
print("NOME: " + nome)
print("PESO: " + str(peso) + "Kg")
print("ALTURA: " + str(altura) + "m")
print("IMC: " + str(imc))
print(f"SITUAÇÃO: {situacao}")

