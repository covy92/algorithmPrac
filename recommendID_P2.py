import re


def solution(new_id):
    new_id = new_id.lower()

    def find_x(a):
        a = list(a)
        banlist = list('~!@#$%^&*()=+[{]}:?,<>/')
        for i in a:
            if i in banlist:
                a.remove(i)
        return a

    nid = list(filter(find_x, new_id))
    new_id = "".join(nid)

    new_id = re.sub('\.+', '.', new_id)
    new_id = list(new_id)

    if len(new_id) != 0:
        if new_id[0] == '.':
            new_id.remove('.')

    if len(new_id) != 0:
        if new_id[-1] == '.':
            del new_id[-1]

    if len(new_id) == 0:
        new_id = ['a']

    if len(new_id) >= 16:
        new_id = new_id[0:15]

    if len(new_id) != 0:
        if new_id[0] == '.':
            new_id.remove('.')

    if len(new_id) != 0:
        if new_id[-1] == '.':
            del new_id[-1]

    if len(new_id) == 1:
        new_id = [new_id[0], new_id[0], new_id[0]]

    if len(new_id) == 2:
        new_id = [new_id[0], new_id[1], new_id[1]]

    new_id = "".join(new_id)

    new_id = "".join(new_id)

    answer = new_id

    return answer
