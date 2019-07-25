def inv(move):
    """Returns the inverse of the move"""

    # 180 deg move is same as its inverse
    if move[-1] == "2":
        return move
    # Anticlockwise move
    if len(move) == 2:
        return move[0]
    # Clockwise move
    return move + "'"


def pure_commutator(a, i1, i2, i3):
    """Moves the cube positions in [i1 i2 i1', i3]"""

    global moves
    algo = [i1, i2, inv(i1), i3, i1, inv(i2), inv(i1), inv(i3)]
    for i in algo:
        a = [a[moves[moves_ind[i] + x * 18]] for x in range(24)]
    return a


def a9_and_setup(a, i1, i2, i3, i4):
    """Moves the cube positions in [i4: [i1 i2 i1', i3]]"""

    global moves
    algo = [i4, i1, i2, inv(i1), i3, i1, inv(i2), inv(i1), inv(i3), inv(i4)]
    for i in algo:
        a = [a[moves[moves_ind[i] + x * 18]] for x in range(24)]
    return a


def find_cycles(a1):
    """Returns all the cycles from current and initial state of the cube"""

    s = ''
    s_rev = ''
    for i in range(24):
        if chr(97 + i) != a1[i]:
            s1 = a1[i]
            s1 += a1[ord(s1[-1]) - 97]
            s1 += a1[ord(s1[-1]) - 97]
            s += s1[::-1] + ';'
            s_rev += s1 + ';'
    return s, s_rev


def find_reduced_move(i1, i4):
    """Returns the combined single move of i1 and i4"""

    # R R or R' R'
    if i1 == i4:
        return i1[0] + "2"
    # R R2 or R' R2
    if len(i1) == 2 and i1[1] == "2":
        return inv(i4)
    # R2 R or R2 R'
    return inv(i1)


def write_output(f, s, s_rev, i1, i2, i3, i4=None):
    """Writes cycle and algorithm to the output file"""

    A = ' '.join([i1, i2, inv(i1)])
    B = i3
    A1 = ' '.join([i1, inv(i2), inv(i1)])
    B1 = inv(i3)

    algo = "({}) {} ({}) {}".format(A, B, A1, B1)
    algo_short = "[({} {} {}), {}]".format(i1, i2, inv(i1), i3)
    algo_inv = "{} ({}) {} ({})".format(B, A, B1, A1)
    algo_inv_short = "[{}, ({} {} {})]".format(i3, i1, i2, inv(i1))

    if i4 != None:
        # If first 2 moves can get reduced to one
        if i1[0] == i4[0]:
            red = find_reduced_move(i1, i4)
            algo = "({} {} {}) {} ({}) {} {}".format(
                red, i2, inv(i1), B, A1, B1, inv(i4))
            algo_inv = "{} {} ({}) {} ({} {} {})".format(
                i4, B, A, B1, i1, inv(i2), inv(red))
        else:
            algo = "{} {} {}".format(i4, algo, inv(i4))
            algo_inv = "{} {} {}".format(i4, algo_inv, inv(i4))
        algo_short = "[{}: {}]".format(i4, algo_short)
        algo_inv_short = "[{}: {}]".format(i4, algo_inv_short)

    f.write(s.upper())
    f.write(algo_short + ';')
    f.write(algo + '\n')
    f.write(s_rev.upper())
    f.write(algo_inv_short + ';')
    f.write(algo_inv + '\n')


# Face moves
u = ["U", "U'", "U2"]
l = ["L", "L'", "L2"]
f = ["F", "F'", "F2"]
r = ["R", "R'", "R2"]
b = ["B", "B'", "B2"]
d = ["D", "D'", "D2"]

all_moves = u + l + f + r + b + d
opp = {"u": d, "l": r, "f": b, "r": l, "b": f, "d": u}
adj = {"u": l + f + r + b, "l": u + f + b + d,
       "f": u + l + r + d, "r": u + f + b + d,
       "b": u + l + r + d, "d": l + f + r + b}

# All valid transitions are stored in this txt file
moves = eval(open('moves_location.txt').readline())
# This indices helps to get the correct column out of the whole transition matrix
moves_ind = {
    "U": 1, "U'": 0, "U2": 2,
    "L": 4, "L'": 3, "L2": 5,
    "F": 7, "F'": 6, "F2": 8,
    "R": 10, "R'": 9, "R2": 11,
    "B": 13, "B'": 12, "B2": 14,
    "D": 16, "D'": 15, "D2": 17
}

# This is the output file where all the algorithms will be written
f = open('output.txt', 'w')

for i1 in all_moves:
    for i2 in adj[i1[0].lower()]:
        for i3 in opp[i2[0].lower()]:
            # Initial state of the cube
            a = [chr(97 + x) for x in range(24)]
            # State of cube after applying algorithm
            a1 = pure_commutator(a, i1, i2, i3)
            # This will find the cycle and reverse cycles done by the algorithm
            s, s_rev = find_cycles(a1)

            # Invalid commutator
            if len(s) != 36:
                continue

            # Write the output and cycle to output file
            write_output(f, s, s_rev, i1, i2, i3)

            for i4 in all_moves:
                # This would cancel 2 moves and give a pure commutator again
                # which we covered already
                if i4 == inv(i1):
                    continue
                a = [chr(97 + x) for x in range(24)]
                a1 = a9_and_setup(a, i1, i2, i3, i4)
                # This will find the cycle and reverse cycles done by the algorithm
                s, s_rev = find_cycles(a1)
                # Invalid commutator
                if len(s) != 36:
                    continue

                # Write the output and cycle to output file
                write_output(f, s, s_rev, i1, i2, i3, i4)

f.close()
