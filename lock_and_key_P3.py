from copy import deepcopy


def key_right(arr):
    len_arr = len(arr)
    new_key = [[0]*len_arr for _ in range(len_arr)]
    for i in range(len_arr):
        for j in range(len_arr-1):
            new_key[i][j+1] = arr[i][j]
    for i in range(len_arr):
        for j in range(len_arr):
            arr[i][j] = new_key[i][j]
    return arr


def key_down(arr):
    len_arr = len(arr)
    new_key = [[0]*len_arr for _ in range(len_arr)]
    for i in range(len_arr-1):
        for j in range(len_arr):
            new_key[i+1][j] = arr[i][j]
    for i in range(len_arr):
        for j in range(len_arr):
            arr[i][j] = new_key[i][j]
    return arr


def key_turn(arr):
    len_arr = len(arr)
    new_key = [[0]*len_arr for _ in range(len_arr)]
    for i in range(len_arr):
        for j in range(len_arr):
            new_key[i][j] = arr[j][len_arr-1-i]
    for i in range(len_arr):
        for j in range(len_arr):
            arr[i][j] = new_key[i][j]
    return arr


def original_key(arr, origin):
    len_arr = len(arr)
    for i in range(len_arr):
        for j in range(len_arr):
            arr[i][j] = origin[i][j]
    return arr


def check(k, l, answer_count):
    len_l = int((len(l)+2)/3)
    ans_list = [[0]*len_l for _ in range(len_l)]
    match_list = [[0]*len_l for _ in range(len_l)]
    for i in range(len_l):
        for j in range(len_l):
            ans_list[i][j] = l[len_l+i-1][len_l+j-1]
            match_list[i][j] = k[len_l+i-1][len_l-1+j]

    ans_box = sum(ans_list, [])

    count = [x+y for x, y in zip(ans_box, sum(match_list, []))].count(1)

    if count == len_l*len_l:
        answer_count = 1
    else:
        answer_count = 0
    return answer_count


key_len = len(key)
match_len = (len(lock)-1)*2+len(lock)


# key 배열을 계속 움직여서 비교할 것이기에 제한사항에 맞는 최대범위로 큰 배열 생성
key_list = [[0]*match_len for _ in range(match_len)]
ans_list = [[0]*match_len for _ in range(match_len)]  # 답인지 비교할 리스트
ans_list1 = []
ans_list2 = []
ans_list3 = []
for i in range(len(lock)):
    for j in range(len(lock[i])):
        ans_list[len(lock)-1+i][len(lock)-1+j] = lock[i][j]


ans_list1 = deepcopy(key_turn(ans_list))
ans_list2 = deepcopy(key_turn(ans_list))
ans_list3 = deepcopy(key_turn(ans_list))
key_turn(ans_list)


key_original = [[0]*len(key) for _ in range(len(key))]

for i in range(len(key)):
    for j in range(len(key)):
        key_original[i][j] = key[i][j]

key_originmatch = [[0]*len(ans_list) for _ in range(len(ans_list))]
key_copy = []
key_copydown = []

for i in range(len(key)):
    for j in range(len(key)):
        key_originmatch[i][j] = key_original[i][j]
key_copy = deepcopy(key_originmatch)
key_copydown = deepcopy(key_originmatch)

count = 0
# 체크시작
for _ in range(match_len-len(key)+1):
    for j in range(match_len-len(key)+1):
        if check(key_copy, ans_list, count) > 0:
            count += 1
        key_right(key_copy)
        if check(key_copy, ans_list, count) > 0:
            count += 1
    original_key(key_copy, key_down(key_copydown))
    if check(key_copy, ans_list, count) > 0:
        count += 1

key_copy = deepcopy(key_originmatch)
key_copydown = deepcopy(key_originmatch)

for _ in range(match_len-len(key)+1):
    for j in range(match_len-len(key)+1):
        if check(key_copy, ans_list1, count) > 0:
            count += 1
        key_right(key_copy)
        if check(key_copy, ans_list1, count) > 0:
            count += 1
    original_key(key_copy, key_down(key_copydown))
    if check(key_copy, ans_list1, count) > 0:
        count += 1

key_copy = deepcopy(key_originmatch)
key_copydown = deepcopy(key_originmatch)

for _ in range(match_len-len(key)+1):
    for j in range(match_len-len(key)+1):
        if check(key_copy, ans_list2, count) > 0:
            count += 1
        key_right(key_copy)
        if check(key_copy, ans_list2, count) > 0:
            count += 1
    original_key(key_copy, key_down(key_copydown))
    if check(key_copy, ans_list2, count) > 0:
        count += 1

key_copy = deepcopy(key_originmatch)
key_copydown = deepcopy(key_originmatch)

for _ in range(match_len-len(key)+1):
    for j in range(match_len-len(key)+1):

        if check(key_copy, ans_list3, count) > 0:
            count += 1
        key_right(key_copy)
        if check(key_copy, ans_list3, count) > 0:
            count += 1
    original_key(key_copy, key_down(key_copydown))
    if check(key_copy, ans_list3, count) > 0:
        count += 1
if count > 0:
    answer = True
else:
    answer = False

if sum(lock, []) == len(lock)*len(lock):
    answer = True
print(answer)
