
citations = [0, 1, 1]

citations.sort()
print(citations)
count = 0
over_num = 0
answer_list = [0]
while count < len(citations)+1:
    for i in range((len(citations))):
        if citations[i] >= count:
            over_num += 1
    print(count, over_num)
    if count <= over_num:
        answer_list.append(count)
    over_num = 0
    count += 1
answer = max(answer_list)
print(answer)


# 모법답안

def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


print(solution(citations))
