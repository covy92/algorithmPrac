
import copy
import re
# from typing import Match


def check(two_array):
    print(two_array)
    for i in range(len(two_array)):
        j = len(two_array[i])
        s = j+1
        for s in range(j):
            delete_ans = two_array[i][s]
            if two_array[i][j] == delete_ans:
                two_array[i][j] = ''
    return (two_array)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]

match_list = []
check_list = []
answer_list = []
answer_table = [['']*len(user_id)for _ in range(len(banned_id))]
answer_match_table = []

for i in range(len(banned_id)):
    check_list.append((banned_id[i].split("*")))
    check_list[i] = '.'.join(check_list[i])

for i in range(len(check_list)):
    for j in range(len(user_id)):
        match_word = check_list[i]
        compiled_match_word = re.compile(match_word)
        answer_word = compiled_match_word.match(user_id[j])
        if answer_word != None:
            if answer_word[0] == user_id[j]:
                match_list.append(answer_word[0])
                if answer_word[0] not in answer_list:
                    answer_list.append(answer_word[0])
    answer_table[i] = copy.deepcopy(match_list)
    match_list = []


for i in range(len(answer_table)):
    check(answer_table)
