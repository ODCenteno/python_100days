import pandas

raw_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
df = pandas.DataFrame(raw_alphabet)
alpha_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generador_nato():

    user_word = input(f'Escribe una palabra: ').upper().strip()
    try:
        order_phonetic = [alpha_dict[letter] for letter in user_word]
    except KeyError as ke:
        print(f'{ke} is not a letter.')
    else:
        print(order_phonetic)

generador_nato()