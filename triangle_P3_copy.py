
from rich.console import Console

console = Console()


def solution(triangle):
    len_t = len(triangle)
    ans_list = [[0]*len_t for _ in range(len_t)]
    i = 1
    k = 1
    first = triangle[0][0]
    ans_list[0][0] = first
    while i < len_t:
        while k < len(triangle[i]):
            ans_list[i][k-1] = max(ans_list[i-1][k-1] +
                                   triangle[i][k-1], ans_list[i][k-1])
            ans_list[i][k] = max(ans_list[i-1][k-1] +
                                 triangle[i][k], ans_list[i][k])
            k += 1
        k = 1
        i += 1
    answer = max(ans_list[len_t-1])
    return answer


t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(t)
