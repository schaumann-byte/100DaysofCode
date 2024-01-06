# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato_dataframe.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# MINHA SOLUÇAO:
# continuar = True
# while continuar:
#     try:
#         user_input = input("Escreva uma palavra: ")
#         phonetic_list = [nato_dict[letter.upper()] for letter in user_input]
#     except KeyError:
#         print("Apenas letras desse alfabeto")
#     else:
#         continuar = False

# SOLUÇAO DA ANGELA
def generate_phonetic():
    user_input = input("Escreva uma palavra: ")
    try:
        phonetic_list = [nato_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Apenas letras desse alfabeto")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()