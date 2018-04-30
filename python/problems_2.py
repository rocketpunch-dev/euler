list_data = [1, 2]
list_sum = 2


def _p(list_data):
    list_data.append(list_data[-1] + list_data[-2])


while True:
    _p(list_data)

    if list_data[-1] >= 4000000:
        break

    if list_data[-1] % 2 == 0:
        list_sum += list_data[-1]


print(list_sum)


if __name__ == "__main__":
    pass
