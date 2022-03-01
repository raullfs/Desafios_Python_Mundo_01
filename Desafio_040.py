nota1 = float(input('Informe a 1° nota: '))
nota2 = float(input('Informe a 2° nota: '))
media = (nota1 + nota2) / 2
print(f'Sua media foi de {media:.1f}')
if media < 5.0:
    print('Aluno REPROVADO.')
elif media >= 5.0 and media <= 6.9:
    print(('Aluno de RECUPERAÇÃO.'))
else:
    print('Aluno APROVADO.')