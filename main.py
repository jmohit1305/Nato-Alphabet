import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
user_input = input("Enter a word: ").upper()
nato_list = [nato_dict[user_input[i]] for i in range(len(user_input)) if user_input[i] in nato_dict]
print(nato_list)
