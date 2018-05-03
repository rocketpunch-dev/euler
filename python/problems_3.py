PRIME_NUMBER = list()
PRIME_NUMBER_SIMPLE = list()


def prime_check(check_number):
    for x in range(2, check_number // 2 + 1, 1):
        if check_number % x == 0:
            return x, int(check_number / x)

    return check_number, 0


def search_prime(input_number):
    x, y = prime_check(input_number)
    PRIME_NUMBER.append(x)
    if y == 0:
        return
    else:
        search_prime(y)


def simple_search(input_number):
    start_num = 2
    while start_num <= input_number:
        if input_number % start_num == 0:
            PRIME_NUMBER_SIMPLE.append(start_num)
            input_number /= start_num
        else:
            start_num += 1


if __name__ == "__main__":
    # INPUT_NUMBER = 13195
    INPUT_NUMBER = 600851475143
    search_prime(INPUT_NUMBER)
    print(PRIME_NUMBER)

    simple_search(INPUT_NUMBER)
    print(PRIME_NUMBER_SIMPLE)


