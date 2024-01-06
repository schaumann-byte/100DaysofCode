# FileNotFound

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("file was closed")
#     raise KeyError

height = float(input("Height:"))
weight = int(input("Weight:"))

if height > 3:
    raise ValueError("Vc nao eh gigante")

bmi = weight / height ** 2
print(bmi)













# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary{"non_existent_key"}

# IndexError
# fruit_list = ["apple", "banana", "pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)