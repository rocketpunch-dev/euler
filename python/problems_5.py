LOOP_NUM = 20


def main():
    for last_num in range(3, LOOP_NUM + 1, 1):
        num_list = list(range(2, last_num + 1, 1))
        print(f"start[{num_list[0]}] ~ end[{num_list[-1]}]  ==> 나누어 떨어지는 가장 작은 수: {int(get_list_lcm(num_list))}")


def greatest_common_divisor(n, m):
    if n < m:
        (n, m) = (m, n)

    while m != 0:
        (n, m) = (m, n % m)

    return n


def least_common_multiple(n, m):
    gcd = greatest_common_divisor(n, m)

    if gcd == 0:
        return 0

    return abs((n * m) / gcd)


def get_list_lcm(list_num, lcm=None):
    if len(list_num) == 0:
        return lcm or 0

    if lcm is None:
        if len(list_num) == 1:
            return list_num[0]

        return get_list_lcm(list_num[2:], least_common_multiple(list_num[0], list_num[1]))

    return get_list_lcm(list_num[1:], least_common_multiple(list_num[0], lcm))


if __name__ == "__main__":
    main()
