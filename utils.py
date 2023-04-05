import string
import json
import random


def count_punkt(text: str) -> str:
    cnt = 0
    for i in text:
        if i in string.punctuation:
            cnt += 1
    return str(cnt)


def data_get_json() -> str:
    num = random.randint(0, 100)
    data_dict = {'0d num': num,
                 '0x num': hex(num),
                 '0b num': bin(num)}
    return json.dumps(data_dict)


def num_verify(text: str):
    if len(text) != 6:
        return f'шестизначным числом'
    else:
        i = 0
        j = 3
        part1 = 0
        part2 = 0
        while i <= 2:
            part1 = part1 + int(text[i])
            i += 1
        while j <= len(text) - 1:
            part2 = part2 + int(text[j])
            j += 1
        if part1 == part2:
            return True
        else:
            return False