

array = [1, 5, 2, 6, 3, 7, 4]

commands = [
    [2, 5, 3],
    [4, 4, 1],
    [1, 7, 3]
]
before_sort_list = [[0]*1 for _ in range(len(commands))]
print(before_sort_list)
ans_index = []
answer = []
for i in range(len(commands)):
    for j in range(3):
        first = commands[i][0]
        last = commands[i][1]
        ans_num = commands[i][2]
    ans_index.append(ans_num)
    before_sort_list[i] = array[first-1:last]

for i in range(len(before_sort_list)):
    before_sort_list[i].sort()
    answer.append(before_sort_list[i][ans_index[i]-1])
print(answer)


# 모범답안

def solution(array, commands):

    return [sorted(array[a[0]-1:a[1]])[a[2]-1] for a in commands]
