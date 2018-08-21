"""
not solved
"""


def get_prime(max_number):
    number_tiles = set(range(2, max_number))
    prime_list = list()

    while len(number_tiles) > 0:
        min_number = min(number_tiles)
        prime_list.append(min_number)

        delete_tiles = set(range(min_number, max_number, min_number))
        number_tiles = number_tiles - delete_tiles

        print(len(number_tiles))

    return prime_list


if __name__ == "__main__":
    # print(get_prime(987654321))
    pass
