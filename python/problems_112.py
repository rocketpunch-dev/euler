def is_bouncy(number):
    is_increasing = False
    is_decreasing = False

    str_number = str(number)
    check_num = str_number[0]

    for s in str_number[1:]:
        if int(check_num) < int(s):
            is_increasing = True
        elif int(check_num) > int(s):
            is_decreasing = True

        check_num = s

    if is_increasing and is_decreasing:
        return True

    return False


def bouncy_rate(rate):
    bouncy_count = 0
    total_count = 1

    number = 1
    while rate > (bouncy_count / total_count) * 100:
        number += 1

        # print(bouncy_count / total_count)

        if is_bouncy(number):
            bouncy_count += 1

        total_count += 1

    print(number)


if __name__ == "__main__":
    bouncy_rate(99)
