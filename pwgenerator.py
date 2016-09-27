#Password generator
import random
import string

#set the characters to choose from for Password
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@&*()"
print "Hello and welcome to Menad's random password generator\n\n"

length = int(raw_input("How many characters in length would you like the password:  "))

quantity = int(raw_input("How many passwords do you need generated? :   "))

file = open("passwords.txt", "a")

final_output = ""


def Pwgenerate(numchar):
    lenchar = 0

    password = random.sample(characters, numchar)
    output = ''.join(password)
    file.write(output + "\n")
    print output


print "\nHere are your generated passwords. Thank you for using this app: \n\n"

def Number(quantity, length):
    count = 0
    while count != quantity:
        Pwgenerate(length)
        count += 1

    file.close()


Number(quantity, length)
file.close()
