nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculas: {nome.upper()}')
print(f'Seu nome em minúsculas: {nome.lower()}')
print(f'Existem {len(nome) - nome.count(" ")} letras ao todo no seu nome.')
print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras')