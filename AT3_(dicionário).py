# criando o dicionário

alunos = {'Ana': 8.5, 'Pedro': 7.0, 'Maria': 9.2}

# Adicionando o aluno Carlos

alunos['Carlos'] = 6.5

# Atualizando a nota de Ana

alunos['Ana'] = 9.0

# Removendo o aluno Pedro

del alunos['Pedro']

# Fazendo a média das notas dos alunos

notas = alunos.values()
soma = sum(notas)
N_de_alunos = len(alunos)
media = soma / N_de_alunos

print(f'A média geral dos alunos é: {media:.2f}')

# Verificanddo se Maria está no dicionário

'Maria' in alunos
if 'Maria' in alunos:
    print('Maria é aluna dessa turma')
else:
    print('Consulte um aluno da turma')
