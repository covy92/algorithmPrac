def solution(lottos, win_nums):
    zero = lottos.count(0)                  # 주어진 리스트의 0의 갯수
    while lottos.count(0) != 0:            # 주어진 리스트에서 0을 제거
        lottos.remove(0)  # (set을 했을때 0이 남아있으면 있는 케이스 없는케이스로 나눠지면서 복잡해짐 )
    lottoslen = len(lottos)                  # 0을 제거한 주어진 리스트의 길이
    winlen = len(win_nums)               # 당첨번호 리스트의 길이
    total = lottos+win_nums               # 두 리스트를 합하여 중첩 번호를 얻어내기위함
    totallen = len(total)

    totalset = set(total)                         # set으로 중복을 없앰
    winniglen = totallen - len(totalset)    # 두 리스트 합 길이- set 리스트 길이 = 중첩된 번호 수

    answer1 = 7-winniglen-zero            # 중첩된 번호 수 + 0의 수 = 최고 순위일 때 당첨 번호 수
    answer2 = 7-winniglen                   # 중첩된 번호 수 = 최저 순위일 때 당첨 번호 수
    # 7에서 위의 숫자들을 빼주면 = 순위
    if answer1 > 6:                             # 7등은 없기에 7등 이상은 6으로 만들어줌
        answer1 = 6
    if answer2 > 6:
        answer2 = 6
    answer = [answer1, answer2]
    return answer
