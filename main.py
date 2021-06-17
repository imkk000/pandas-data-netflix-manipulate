import pandas as pd
from itertools import permutations

# read data
df = pd.read_csv('NetflixOriginals.csv')

# manipulate data
df['Premiere'] = df['Premiere'].str.replace('.', ',', regex=False)
df['Language'] = df['Language'].str.split('/')
df['Genre'] = df['Genre'].str.replace('[-//]', ' ', regex=True)
df['Genre'] = df['Genre'].str.title()
df['Genre'] = df['Genre'].str.split(' ')

data = []
for index, row in df.iterrows():
    list1 = list(filter(None, row['Language']))
    list2 = list(filter(None, row['Genre']))
    for c in [ (l1, l2) for l2 in list2 for l1 in list1 ]:
        data.append([
            row['Title'],
            c[1], # Genre
            row['Premiere'],
            row['Runtime'],
            row['IMDB Score'],
            c[0], # Language
        ])

df = pd.DataFrame(data, columns=['Title', 'Genre', 'Premiere', 'Runtime', 'IMDB Score', 'Language'])
df.to_csv('NetflixOriginalsNew.csv')
