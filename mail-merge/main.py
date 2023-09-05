
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
         #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open("Input/Names/invited_names.txt") as name_list:
    names_barran = name_list.readlines()
    for item in names_barran:
        names.append(item.strip())

# with open("Input/Names/invited_names.txt") as name_list:
#     names_barran = name_list.readlines()
#     names = [item.strip() for item in names_barran] ----> muito legal

with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
    for name in names:
        stripped_name = name.strip()
        with open(f"Output/ReadyToSend/Teste_{stripped_name}.txt", "w") as final_letter:
            final_letter.write(letter.replace("[name]", stripped_name))

