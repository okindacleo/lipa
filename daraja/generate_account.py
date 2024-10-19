import random
import string

def generate_random_string():
    # Generate 4 random digits
    random_digits = ''.join(random.choices(string.digits, k=4))
    # Combine 'YM' with the random digits
    return 'YM' + random_digits
