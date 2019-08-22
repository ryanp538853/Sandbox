"""Ryan"""
MINIMUM_LENGTH = 6

password = input("Please enter your password that has at least {} character: ".format(MINIMUM_LENGTH))
while len(password) < MINIMUM_LENGTH:
    input("Invalid password!\nPlease enter password that contains at least {} characters: ".format(MINIMUM_LENGTH))

print("*" * len(password))
