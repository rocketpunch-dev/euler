"""
not solved
"""

pow_dict = dict()


def solve_119a(n):
    check_num = 10
    index = 0
    while index < n:
        check_num += 1
        sum_number = sum([int(x) for x in str(check_num)])

        if sum_number <= 1:
            continue

        pow_num = 0
        pow_index = 2
        while check_num >= pow_num:
            pow_num = pow(sum_number, pow_index)
            if check_num == pow_num:
                index += 1
                print(f"[{index}] {check_num} => {sum_number}^{pow_index}")
                break

            pow_index += 1


def solve_119b(max_number, max_pow):
    pow_list = list()
    pow_dict = dict()

    for x in range(2, max_number):
        for y in range(2, max_pow + 1):
            pow_data = pow(x, y)
            if pow_data < 11:
                continue
            sum_number = sum([int(x) for x in str(pow_data)])
            if sum_number == x:
                pow_list.append(pow_data)
                pow_dict[pow_data] = f"{pow_data} => {x}^{y}"

    pow_list.sort()
    for i, x in enumerate(pow_list, start=1):
        print(f"[{i}] {pow_dict.get(x)}")


if __name__ == "__main__":
    # solve_119a(10)  # Error
    solve_119b(80, 10)
