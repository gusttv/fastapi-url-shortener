import string
import random

# Utility function to generate short URL
def generate_short_url():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=6))