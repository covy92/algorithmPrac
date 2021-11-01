
def solution(triangle):
    len_t = len(triangle)
    ans_list = [[]]
    i = 1
    k = 1
    first = triangle[0][0]
    ans_list[0].append(first)
    print(ans_list)
    while i == len_t:
        while k == len(len_t[i]):
            ans_list[i].append(ans_list[i-1][k-1]+triangle[i][k-1])
            ans_list[i].append(ans_list[i-1][k-1]+triangle[i][k])
            k += 1
        i += 1
    answer = max(ans_list[len_t-1])
    return answer
