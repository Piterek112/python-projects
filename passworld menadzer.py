import random, string

number_of_passwords = int(input("How many passwords do you want to generate? "))
password_length = int(input("Provide the password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

for password_index in range(number_of_passwords):
    password = ""   

    for index in range(password_length):
        password = password + random.choice(characters)


    print("Password {} generated: {}".format(password_index, password))
