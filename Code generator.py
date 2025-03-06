import random

print("Your password: ")

chars = 'qwertyuiopasdfghjklzxcvbn123456789AQWERTYUIOPASDFGHJKLZXCVBNM'

password = ''
for x in range(8):
    password += random.choice(chars)
    print(password)