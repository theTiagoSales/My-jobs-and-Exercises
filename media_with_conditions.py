n1 = float(input('insira sua primeira nota de 0 a 10: '))
while n1 < 0 or n1 > 10:
    print('insira uma nota válida')
    n1 = float(input('insira sua primeira nota de 0 a 10: '))
n2 = float(input('insira sua segunda nota de 0 a 10: '))
while n2 < 0 or n2 > 10:
    print('insira uma nota válida')
    n2 = float(input('insira sua segunda nota de 0 a 10: '))
média = (n1 + n2) / 2
print('sua média é', média)
if média >= 6:
   print('você foi aprovado!')
else:
   print('aluno reprovado.')
