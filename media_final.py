# NOTA FINAL DO ALUNO

print("*¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ¨¨¨¨¨¨¨*")
print("*                     MÉDIA FINAL                     *")
print("*¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨*")
print()

#variáveis

nome_do_aluno = ""
nota_1bimestre = 0.0
nota_2bimestre = 0.0
nota_3bimestre = 0.0
nota_4bimestre = 0.0
nota_final = 0.0

#dados

nome_do_aluno = input("Nome do Aluno: ")
nota_1bimestre = float(input("Nota do 1º bimestre: "))
nota_2bimestre = float(input("Nota do 2º bimestre: "))
nota_3bimestre = float(input("Nota do 3º bimestre: "))
nota_4bimestre = float(input("Nota do 4º bimestre: "))

#CALCULO

nota_final = (nota_1bimestre + nota_2bimestre + nota_3bimestre + nota_4bimestre) / 4

situacao = " "

if nota_final >= 7.0:
    situacao = "Você foi aprovado!"
elif nota_final < 5:
    situacao = "Você foi reprovado!"
else:
    situacao = "Você está de recuperação!"

#resultados


print()
print("*¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨*")
print()
print(f"{nome_do_aluno}, {situacao}, a sua nota final é: {nota_final}.")
print()
print("*¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨*")
