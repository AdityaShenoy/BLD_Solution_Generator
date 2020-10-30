import clipboard

adjacents = {
    'R': 'UEDFSB',
    'M': 'UEDFSB',
    'L': 'UEDFSB',
    'U': 'RMLFSB',
    'E': 'RMLFSB',
    'D': 'RMLFSB',
    'F': 'RMLUED',
    'S': 'RMLUED',
    'B': 'RMLUED'
}

all_slices = 'RMLUEDFSB'

quarter_turns = ['', '\'']

quarter_half_turns = ['', '2', '\'']

inverse = {
    '': '\'',
    '2': '2',
    '\'': ''
}

parallels = {
    'R': 'ML',
    'M': 'RL',
    'L': 'RM',
    'U': 'ED',
    'E': 'UD',
    'D': 'UE',
    'F': 'SB',
    'S': 'FB',
    'B': 'FS'
}

turn_count = {
    '': 1,
    '2': 2,
    '\'': 3
}

edge_interchanges = {
    'R': ['MNOP', 'BTVJ'],
    'M': ['AIUS', 'QCKW'],
    'L': ['EFGH', 'DLXR'],
    'U': ['ABCD', 'QMIE'],
    'E': ['FJNR', 'LPTH'],
    'D': ['UVWX', 'KOSG'],
    'F': ['IJKL', 'CPUF'],
    'S': ['BOXE', 'MVGD'],
    'B': ['QRST', 'AHWN'],
}

corner_interchanges = {
    'R': ['MNOP', 'BTVJ', 'CQWK'],
    'L': ['EFGH', 'DLXR', 'AIUS'],
    'U': ['ABCD', 'EQMI', 'FRNJ'],
    'D': ['UVWX', 'GKOS', 'HLPT'],
    'F': ['IJKL', 'CPUF', 'DMVG'],
    'B': ['QRST', 'AHWN', 'BEXO'],
}


def process_commutators(commutators, commutator_type, interchanges,
                        a1, a1_rot, a1_rot_inv,
                        a2, a2_rot, a2_rot_inv,
                        b, b_rot, b_rot_inv):
    pass


with open('output/commutators.csv', 'w') as commutators:
    for a1 in all_slices:
        for a1_rot in quarter_turns:
            a1_rot_inv = inverse[a1_rot]
            for a2 in adjacents[a1]:
                for a2_rot in quarter_half_turns:
                    a2_rot_inv = inverse[a2_rot]
                    for b in parallels[a2]:
                        for b_rot in quarter_half_turns:
                            b_rot_inv = inverse[b_rot]
                            if set('MES') & set(a1 + a2 + b):
                                process_commutators(commutators, 'Edge',
                                                    edge_interchanges,
                                                    a1, a1_rot, a1_rot_inv,
                                                    a2, a2_rot, a2_rot_inv,
                                                    b, b_rot, b_rot_inv)
                            else:
                                process_commutators(commutators, 'Corner',
                                                    corner_interchanges,
                                                    a1, a1_rot, a1_rot_inv,
                                                    a2, a2_rot, a2_rot_inv,
                                                    b, b_rot, b_rot_inv)
