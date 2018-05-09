CHECK_COUNT = 10001
prime_number_list = list()

CHECK_NUM = 1

while len(prime_number_list) < CHECK_COUNT:
    CHECK_NUM += 1
    is_prime_number = True

    for i in prime_number_list:
        if CHECK_NUM % i == 0:
            is_prime_number = False
            break

    if is_prime_number:
        print(CHECK_NUM)
        prime_number_list.append(CHECK_NUM)

print(prime_number_list[-1])

if __name__ == "__main__":
    pass
