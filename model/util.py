import random
import string

def randomizer(n, list_to_append, iterable):
    for _ in range(n):
        list_to_append.append(random.choice(iterable))

def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):

    generated_id = []
    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    digits = [str(x) for x in range(10)]
    special_chars = [x for x in allowed_special_chars]

    randomizer(number_of_small_letters, generated_id, small_letters)
    randomizer(number_of_capital_letters, generated_id, capital_letters)
    randomizer(number_of_digits, generated_id, digits)
    randomizer(number_of_special_chars, generated_id, special_chars)

    random.shuffle(generated_id)

    return "".join(generated_id)