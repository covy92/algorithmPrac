numbers = [2, 20, 34, 5, 9, 345, 344]
max_len = len(str(max(numbers)))+1
multiple_count = []
for_sort_list = []
answer_list = []

for i in range(len(numbers)):
    numbers[i] = str(numbers[i])

for i in range(len(numbers)):
    if len(numbers[i]) < max_len:
        multiple_count.append(max_len-len(numbers[i]))
        numbers[i] = numbers[i] * (max_len-len(numbers[i])+max_len)
        numbers[i] = numbers[i][0:max_len]
    else:
        multiple_count.append(+max_len-len(numbers[i]))


for i in range(len(numbers)):
    for_sort_list.append(f'{numbers[i]}-{multiple_count[i]}')


for_sort_list.sort(reverse=True)
# print(for_sort_list)

for i in range(len(numbers)):
    multiple_count[i] = for_sort_list[i][-1]

# print(multiple_count)

for i in range(len(numbers)):
    count = int(multiple_count[i])+2
    # print(count)
    numbers[i] = for_sort_list[i][0:-count]

answer = ''.join(numbers)
if int(answer) == 0:
    answer = '0'
# print(answer)
