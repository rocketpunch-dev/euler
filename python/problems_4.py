def is_palindrome(num):
    str_num = str(num)
    for index in range(0, len(str_num) // 2, 1):
        start_index = index
        end_index = (index * (-1)) - 1
        if str_num[start_index] != str_num[end_index]:
            return False

    return True


max_code = 999
max_num = max_code * max_code
while max_num > 0:
    if is_palindrome(max_num):
        for j in range(max_code, int(max_code / 10), -1):
            if max_num % j == 0 and max_code >= (max_num / j) >= (max_code / 10):
                print(f"{j} X {int(max_num / j)} = {max_num}")
                max_num = 0
                break

    max_num -= 1

if __name__ == "__main__":
    pass
