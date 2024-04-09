
# import the random module to generate random passwords
import random

# Define the characters to be used in the password
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# Combine all the characters
all = lowercase + uppercase + numbers + symbols

# Get length from user
length = int(input('Enter the length of the password: '))

# Get number of passwords to generate
numberOfPasswords = int(input('Enter the number of passwords to generate: '))

# generates a single password based on input length
def generate_password(length):
    password = ''
    if length < 8:
        print('Minimium length of password is 8')
        return ''
    else:
        for i in range(length):
            password += random.choice(all)
        return password
    

# generates multiple passwords based on input length
def generate_passwords(length, numberOfPasswords):
    passwords = []
    for i in range(numberOfPasswords):
        passwords.append(generate_password(length))
        print(passwords[i])

# prints the generated passwords
(generate_passwords(length, numberOfPasswords))
