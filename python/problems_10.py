CHECK_COUNT = 2000000
prime_number_list = list()

prime_number_tiles = [True for x in range(CHECK_COUNT + 1)]
prime_number_tiles[0] = False
prime_number_tiles[1] = False

for i in range(CHECK_COUNT + 1):
    if prime_number_tiles[i] is False:
        continue

    prime_number_list.append(i)

    for j in range(i, CHECK_COUNT + 1, i):
        prime_number_tiles[j] = False


print(sum(prime_number_list))


if __name__ == "__main__":
    pass
