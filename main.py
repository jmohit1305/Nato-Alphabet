import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

re_ask = True


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        nato_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_list)


generate_phonetic()
