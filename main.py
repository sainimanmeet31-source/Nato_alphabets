import pandas

data=pandas.read_csv('nato_phonetic_alphabet.csv')

d1={row.letter:row.code for (index,row) in data.iterrows()}

x=input('Enter your name: ')

l3=[d1[n.upper()] for n in x]
print(f'For {x} say: {l3}')

