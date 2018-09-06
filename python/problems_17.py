try:
    from num2words import num2words
except:
    pass  # pip install num2words

WORDS_INFO = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
}


def number_to_text(number):  # TODO thousand logic
    if number == 1000:
        return WORDS_INFO.get(1) + ' ' + WORDS_INFO.get(1000)

    return_text = ''

    hundred = number // 100
    if hundred:
        return_text += WORDS_INFO.get(hundred) or ''
        return_text += ' '
        return_text += WORDS_INFO.get(100)

    remain_number = number - (hundred * 100)
    text = WORDS_INFO.get(remain_number) or ''
    if hundred and text:
        return_text += ' and '
        return_text += text
        return return_text

    ten_number = (remain_number // 10) * 10
    one_number = remain_number - ten_number

    if hundred and (ten_number or one_number):
        return_text += ' and '

    text = WORDS_INFO.get(remain_number) or ''
    if text:
        return_text += text
        return return_text

    if ten_number:
        return_text += WORDS_INFO.get(ten_number)

    if ten_number and one_number:
        return_text += '-'

    return_text += WORDS_INFO.get(one_number) or ''

    return return_text


def get_number_size(number):  # TODO thousand logic
    if number == 1000:
        return len(WORDS_INFO.get(1)) + len(WORDS_INFO.get(1000))

    return_size = 0

    hundred = number // 100
    if hundred:
        return_size += len(WORDS_INFO.get(hundred) or '')
        # return_size += ' '
        return_size += len(WORDS_INFO.get(100))

    remain_number = number - (hundred * 100)
    size = len(WORDS_INFO.get(remain_number) or '')
    if hundred and size:
        return_size += 3  # and
        return_size += size
        return return_size

    ten_number = (remain_number // 10) * 10
    one_number = remain_number - ten_number

    if hundred and (ten_number or one_number):
        return_size += 3  # and

    size = len(WORDS_INFO.get(remain_number) or '')
    if size:
        return_size += size
        return return_size

    if ten_number:
        return_size += len(WORDS_INFO.get(ten_number))
        # return_size += '-'

    return_size += len(WORDS_INFO.get(one_number) or '')

    return return_size


if __name__ == "__main__":
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0

    for num in range(1, 1001):
        text_1 = number_to_text(num)

        try:
            text_2 = num2words(num)
        except:
            text_2 = ''

        text_1_size = len(number_to_text(num).replace(' ', '').replace('-', ''))

        number_size = get_number_size(num)

        size_1 = len(text_1.replace(' ', '').replace('-', ''))
        size_2 = len(text_2.replace(' ', '').replace('-', ''))
        size_3 = number_size

        sum_1 += size_1
        sum_2 += size_2
        sum_3 += size_3

        print(f"{num} => {text_1} | {text_2} | {size_1}:{size_2}:{size_3}")

    print(f"RESULT: {sum_1} | {sum_2} | {sum_3}")
