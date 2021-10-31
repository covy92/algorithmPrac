def solution(n):

    answer = []
    answer.append(1)
    answer.append(2)
    index = 2
    if n > 2:
        while index != n:
            if index > 1:
                a = answer[index-1]+answer[index-2]
                answer.append(a)
                index += 1

    return answer[n-1]


print(solution())
