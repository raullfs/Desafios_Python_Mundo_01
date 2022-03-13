times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
         'Corinthians', 'Red Bull Bragantino', 'Fluminense',
         'América-MG', 'Atlético-GO', 'Santos', 'Ceará',
         'Internacional', 'São Paulo', 'Athletico-PR',
         'Cuiabá', 'Juventude', 'Grêmio', 'Bahia',
         'Sport', 'Chapecoense')
print(f'''Lista de times do Brasileirão: 
{times}
Os 5 primeiros são:
{times[:5]}
Os 4 últimos são:
{times[16:]}
Times em ordem alfabética:
{sorted(times)}
O Chapecoense está na {times.index('Chapecoense')+1}ª posição
''')
