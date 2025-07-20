import random
import string

print("Welcome to Password generator")

def password_generator(length):
    # number of random characters (in ratio of 50%:25%:25%)
    num_letters = round(length * 0.5)
    num_digits = round(length * 0.25)
    num_symbols = length - num_letters - num_digits  # ensures total = length

    # Generate characters
    letters = random.choices(string.ascii_letters, k=num_letters)
    digits = random.choices(string.digits, k=num_digits)
    symbols = random.choices(string.punctuation, k=num_symbols)

    # Combine all
    password_list = letters + digits + symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    return password

password_len = int(input("Enter the length of password: "))
random_password = password_generator(password_len)
print(f'Generated Password: {random_password}')
