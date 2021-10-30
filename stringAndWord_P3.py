import re


def solution(s):

    ans_dic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
               'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    for k, v in ans_dic.items():

        s = re.sub(f'({k})', str(v), s)

    answer = int(s)

    return answer
