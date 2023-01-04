countries = ['india', 'china', 'japan', 'croatia', 'crance', 'portugal', 'spain',
             'pakistan', 'england', 'germany', 'cafrica', 'moracco', 'argentina', 'sweden', 'crazil']

i = 0
count = 0
while i <= len(countries):

    if countries[i].startswith('c'):
        count = count + 1
        print(countries[i])

    if count == 5:
        break

    i = i + 1