def solution(ordering):

    for order in ordering:
        move(order)
    ans1 = ''

    for i in range(1, 10):
        value = int(cube[i])
        if value < 10:
            ans1 += 'w'
        elif value < 19:
            ans1 += 'o'
        elif value < 28:
            ans1 += 'g'
        elif value < 37:
            ans1 += 'b'
        elif value < 46:
            ans1 += 'r'
        elif value < 55:
            ans1 += 'y'
    print(ans1[0:3])
    print(ans1[3:6])
    print(ans1[6:9])


def move(ordering):
    # U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른면   //  +: 시계, -:반시계
    if ordering == 'U+':

        c1 = cube[1]
        c2 = cube[2]
        c3 = cube[3]
        c4 = cube[4]
        c6 = cube[6]
        c7 = cube[7]
        c8 = cube[8]
        c9 = cube[9]
        c16 = cube[16]
        c17 = cube[17]
        c18 = cube[18]
        c28 = cube[28]
        c31 = cube[31]
        c34 = cube[34]
        c37 = cube[37]
        c38 = cube[38]
        c39 = cube[39]
        c21 = cube[21]
        c24 = cube[24]
        c27 = cube[27]

        cube[1] = c7
        cube[2] = c4
        cube[3] = c1
        cube[4] = c8
        cube[6] = c2
        cube[8] = c6
        cube[7] = c9
        cube[9] = c3
        cube[16] = c27
        cube[17] = c24
        cube[18] = c21
        cube[28] = c16
        cube[31] = c17
        cube[34] = c18
        cube[37] = c34
        cube[38] = c31
        cube[39] = c28
        cube[21] = c37
        cube[24] = c38
        cube[27] = c39
    if ordering == 'U-':

        c1 = cube[1]
        c2 = cube[2]
        c3 = cube[3]
        c4 = cube[4]
        c6 = cube[6]
        c7 = cube[7]
        c8 = cube[8]
        c9 = cube[9]
        c16 = cube[16]
        c17 = cube[17]
        c18 = cube[18]
        c28 = cube[28]
        c31 = cube[31]
        c34 = cube[34]
        c37 = cube[37]
        c38 = cube[38]
        c39 = cube[39]
        c21 = cube[21]
        c24 = cube[24]
        c27 = cube[27]

        cube[1] = c3
        cube[2] = c6
        cube[3] = c9
        cube[4] = c2
        cube[6] = c8
        cube[8] = c4
        cube[7] = c1
        cube[9] = c7
        cube[16] = c28
        cube[17] = c31
        cube[18] = c34
        cube[28] = c39
        cube[31] = c38
        cube[34] = c37
        cube[37] = c21
        cube[38] = c24
        cube[39] = c27
        cube[21] = c18
        cube[24] = c17
        cube[27] = c16

    if ordering == 'D+':

        c46 = cube[46]
        c47 = cube[47]
        c48 = cube[48]
        c49 = cube[49]
        c51 = cube[51]
        c52 = cube[52]
        c53 = cube[53]
        c54 = cube[54]
        c19 = cube[19]
        c22 = cube[22]
        c25 = cube[25]
        c30 = cube[30]
        c33 = cube[33]
        c36 = cube[36]
        c43 = cube[43]
        c44 = cube[44]
        c45 = cube[45]
        c10 = cube[10]
        c11 = cube[11]
        c12 = cube[12]

        cube[46] = c52
        cube[47] = c49
        cube[48] = c46
        cube[49] = c53
        cube[51] = c47
        cube[52] = c54
        cube[53] = c51
        cube[54] = c48
        cube[19] = c12
        cube[22] = c11
        cube[25] = c10
        cube[30] = c45
        cube[33] = c44
        cube[36] = c43
        cube[43] = c19
        cube[44] = c22
        cube[45] = c25
        cube[10] = c30
        cube[11] = c33
        cube[12] = c36
    if ordering == 'D-':

        c46 = cube[46]
        c47 = cube[47]
        c48 = cube[48]
        c49 = cube[49]
        c51 = cube[51]
        c52 = cube[52]
        c53 = cube[53]
        c54 = cube[54]
        c19 = cube[19]
        c22 = cube[22]
        c25 = cube[25]
        c30 = cube[30]
        c33 = cube[33]
        c36 = cube[36]
        c43 = cube[43]
        c44 = cube[44]
        c45 = cube[45]
        c10 = cube[10]
        c11 = cube[11]
        c12 = cube[12]

        cube[46] = c48
        cube[47] = c51
        cube[48] = c54
        cube[49] = c47
        cube[51] = c53
        cube[52] = c46
        cube[53] = c49
        cube[54] = c52
        cube[19] = c43
        cube[22] = c44
        cube[25] = c45
        cube[30] = c10
        cube[33] = c11
        cube[36] = c12
        cube[43] = c36
        cube[44] = c33
        cube[45] = c30
        cube[10] = c25
        cube[11] = c22
        cube[12] = c19

    if ordering == 'F+':
        c37 = cube[37]
        c38 = cube[38]
        c39 = cube[39]
        c40 = cube[40]
        c42 = cube[42]
        c43 = cube[43]
        c44 = cube[44]
        c45 = cube[45]
        c34 = cube[34]
        c35 = cube[35]
        c36 = cube[36]
        c25 = cube[25]
        c26 = cube[26]
        c27 = cube[27]
        c7 = cube[7]
        c8 = cube[8]
        c9 = cube[9]
        c52 = cube[52]
        c53 = cube[54]
        c54 = cube[54]

        cube[37] = c43
        cube[38] = c40
        cube[39] = c37
        cube[40] = c44
        cube[42] = c38
        cube[43] = c45
        cube[44] = c42
        cube[45] = c39
        cube[34] = c7
        cube[35] = c8
        cube[36] = c9
        cube[25] = c54
        cube[26] = c53
        cube[27] = c52
        cube[7] = c25
        cube[8] = c26
        cube[9] = c27
        cube[52] = c36
        cube[53] = c35
        cube[54] = c34
    if ordering == 'F-':

        c37 = cube[37]
        c38 = cube[38]
        c39 = cube[39]
        c40 = cube[40]
        c42 = cube[42]
        c43 = cube[43]
        c44 = cube[44]
        c45 = cube[45]
        c34 = cube[34]
        c35 = cube[35]
        c36 = cube[36]
        c25 = cube[25]
        c26 = cube[26]
        c27 = cube[27]
        c7 = cube[7]
        c8 = cube[8]
        c9 = cube[9]
        c52 = cube[52]
        c53 = cube[54]
        c54 = cube[54]

        cube[37] = c39
        cube[38] = c42
        cube[39] = c45
        cube[40] = c38
        cube[42] = c44
        cube[43] = c37
        cube[44] = c40
        cube[45] = c43
        cube[34] = c54
        cube[35] = c53
        cube[36] = c52
        cube[25] = c7
        cube[26] = c8
        cube[27] = c9
        cube[7] = c34
        cube[8] = c35
        cube[9] = c36
        cube[52] = c27
        cube[53] = c26
        cube[54] = c25

    if ordering == 'B+':
        c10 = cube[10]
        c11 = cube[11]
        c12 = cube[12]
        c13 = cube[13]
        c15 = cube[15]
        c16 = cube[16]
        c17 = cube[17]
        c18 = cube[18]
        c28 = cube[28]
        c29 = cube[29]
        c30 = cube[30]
        c19 = cube[19]
        c20 = cube[20]
        c21 = cube[21]
        c1 = cube[1]
        c2 = cube[2]
        c3 = cube[3]
        c46 = cube[46]
        c47 = cube[47]
        c48 = cube[48]

        cube[10] = c16
        cube[11] = c13
        cube[12] = c10
        cube[13] = c17
        cube[15] = c11
        cube[16] = c18
        cube[17] = c15
        cube[18] = c12
        cube[28] = c48
        cube[29] = c47
        cube[30] = c46
        cube[19] = c1
        cube[20] = c2
        cube[21] = c3
        cube[1] = c28
        cube[2] = c29
        cube[3] = c30
        cube[46] = c21
        cube[47] = c20
        cube[48] = c19
    if ordering == 'B-':

        c10 = cube[10]
        c11 = cube[11]
        c12 = cube[12]
        c13 = cube[13]
        c15 = cube[15]
        c16 = cube[16]
        c17 = cube[17]
        c18 = cube[18]
        c28 = cube[28]
        c29 = cube[29]
        c30 = cube[30]
        c19 = cube[19]
        c20 = cube[20]
        c21 = cube[21]
        c1 = cube[1]
        c2 = cube[2]
        c3 = cube[3]
        c46 = cube[46]
        c47 = cube[47]
        c48 = cube[48]

        cube[10] = c12
        cube[11] = c15
        cube[12] = c18
        cube[13] = c11
        cube[15] = c17
        cube[16] = c10
        cube[17] = c13
        cube[18] = c16
        cube[28] = c1
        cube[29] = c2
        cube[30] = c3
        cube[19] = c48
        cube[20] = c47
        cube[21] = c46
        cube[1] = c19
        cube[2] = c20
        cube[3] = c21
        cube[46] = c30
        cube[47] = c29
        cube[48] = c28
    if ordering == 'L+':

        c19 = cube[19]
        c20 = cube[20]
        c21 = cube[21]
        c22 = cube[22]
        c24 = cube[24]
        c25 = cube[25]
        c26 = cube[26]
        c27 = cube[27]
        c10 = cube[10]
        c13 = cube[13]
        c16 = cube[16]
        c1 = cube[1]
        c4 = cube[4]
        c7 = cube[7]
        c37 = cube[37]
        c40 = cube[40]
        c43 = cube[43]
        c46 = cube[46]
        c49 = cube[49]
        c52 = cube[52]

        cube[19] = c25
        cube[20] = c22
        cube[21] = c19
        cube[22] = c26
        cube[24] = c20
        cube[25] = c27
        cube[26] = c24
        cube[27] = c21
        cube[10] = c52
        cube[13] = c49
        cube[16] = c46
        cube[1] = c10
        cube[4] = c13
        cube[7] = c16
        cube[37] = c1
        cube[40] = c4
        cube[43] = c7
        cube[46] = c43
        cube[49] = c40
        cube[52] = c37
    if ordering == 'L-':
        c19 = cube[19]
        c20 = cube[20]
        c21 = cube[21]
        c22 = cube[22]
        c24 = cube[24]
        c25 = cube[25]
        c26 = cube[26]
        c27 = cube[27]
        c10 = cube[10]
        c13 = cube[13]
        c16 = cube[16]
        c1 = cube[1]
        c4 = cube[4]
        c7 = cube[7]
        c37 = cube[37]
        c40 = cube[40]
        c43 = cube[43]
        c46 = cube[46]
        c49 = cube[49]
        c52 = cube[52]

        cube[19] = c21
        cube[20] = c24
        cube[21] = c27
        cube[22] = c20
        cube[24] = c26
        cube[25] = c19
        cube[26] = c22
        cube[27] = c25
        cube[10] = c1
        cube[13] = c4
        cube[16] = c7
        cube[1] = c37
        cube[4] = c40
        cube[7] = c43
        cube[37] = c52
        cube[40] = c49
        cube[43] = c46
        cube[46] = c16
        cube[49] = c13
        cube[52] = c10

    if ordering == 'R+':

        c28 = cube[28]
        c29 = cube[29]
        c30 = cube[30]
        c31 = cube[31]
        c33 = cube[33]
        c34 = cube[34]
        c35 = cube[35]
        c36 = cube[36]
        c12 = cube[12]
        c15 = cube[15]
        c18 = cube[18]
        c3 = cube[3]
        c6 = cube[6]
        c9 = cube[9]
        c39 = cube[39]
        c42 = cube[42]
        c45 = cube[45]
        c48 = cube[48]
        c51 = cube[51]
        c54 = cube[54]

        cube[28] = c34
        cube[29] = c31
        cube[30] = c28
        cube[31] = c35
        cube[33] = c29
        cube[34] = c36
        cube[35] = c33
        cube[36] = c30
        cube[12] = c3
        cube[15] = c6
        cube[18] = c9
        cube[3] = c39
        cube[6] = c42
        cube[9] = c45
        cube[39] = c54
        cube[42] = c51
        cube[45] = c48
        cube[48] = c18
        cube[51] = c15
        cube[54] = c12
    if ordering == 'R-':

        c28 = cube[28]
        c29 = cube[29]
        c30 = cube[30]
        c31 = cube[31]
        c33 = cube[33]
        c34 = cube[34]
        c35 = cube[35]
        c36 = cube[36]
        c12 = cube[12]
        c15 = cube[15]
        c18 = cube[18]
        c3 = cube[3]
        c6 = cube[6]
        c9 = cube[9]
        c39 = cube[39]
        c42 = cube[42]
        c45 = cube[45]
        c48 = cube[48]
        c51 = cube[51]
        c54 = cube[54]

        cube[28] = c30
        cube[29] = c33
        cube[30] = c36
        cube[31] = c29
        cube[33] = c35
        cube[34] = c28
        cube[35] = c31
        cube[36] = c34
        cube[12] = c54
        cube[15] = c51
        cube[18] = c48
        cube[3] = c12
        cube[6] = c15
        cube[9] = c18
        cube[39] = c3
        cube[42] = c6
        cube[45] = c9
        cube[48] = c45
        cube[51] = c42
        cube[54] = c39


def init_cube():
    _cube = {}
    for i in range(1, 55):
        _cube[i] = i
    return _cube


if __name__ == '__main__':
    cube = init_cube()
    n = int(input())
    for _ in range(n):
        input()
        ordering = input().split(sep=' ')
        solution(ordering)
        cube = init_cube()
