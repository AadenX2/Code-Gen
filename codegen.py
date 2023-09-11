import random
import string

def generate_random_code(length):
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return code
        # Change the 5 in the parenthesis to any higher/lower number if needed
random_code = generate_random_code(5)
print ("Your code is:", random_code)
