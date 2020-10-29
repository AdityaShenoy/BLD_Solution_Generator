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

edge_interchanges = {
    'R': ['MNOP', 'BTVJ'],
    'M': ['AIUS', 'CKWQ'],
    'L': ['EFGH', 'DLXR'],
    'U': ['ABCD', 'EQMI'],
    'E': ['FJNR', 'HLPT'],
    'D': ['UVWX', 'GKOS'],
    'F': ['IJKL', 'CPUF'],
    'S': ['BOXE', 'DMVG'],
    'B': ['QRST', 'AHWN'],
}

with open('output/commutators.csv', 'w') as commutators:
    for a1 in all_slices:
        for a1_rot in quarter_turns:
            for a2 in adjacents[a1]:
                for a2_rot in quarter_half_turns:
                    a1_rot_inv = inverse[a1_rot]
                    a2_rot_inv = inverse[a2_rot]
                    for b in parallels[a2]:
                        for b_rot in quarter_half_turns:
                            b_rot_inv = inverse[b_rot]
                            commutators.write(f'({a1}{a1_rot} '
                                              f'{a2}{a2_rot} '
                                              f'{a1}{a1_rot_inv}) ')
                            commutators.write(f'{b}{b_rot} ')
                            commutators.write(f'({a1}{a1_rot} '
                                              f'{a2}{a2_rot_inv} '
                                              f'{a1}{a1_rot_inv}) ')
                            commutators.write(f'{b}{b_rot_inv},')

                            if ('M' in a1 + a2 + b) or \
                                    ('E' in a1 + a2 + b) or \
                                    ('S' in a1 + a2 + b):
                                commutators.write('Edge\n')
                            else:
                                commutators.write('Corner\n')

                            commutators.write(f'{b}{b_rot} ')
                            commutators.write(f'({a1}{a1_rot} '
                                              f'{a2}{a2_rot} '
                                              f'{a1}{a1_rot_inv}) ')
                            commutators.write(f'{b}{b_rot_inv} ')
                            commutators.write(f'({a1}{a1_rot} '
                                              f'{a2}{a2_rot_inv} '
                                              f'{a1}{a1_rot_inv}),')

                            if ('M' in a1 + a2 + b) or \
                                    ('E' in a1 + a2 + b) or \
                                    ('S' in a1 + a2 + b):
                                commutators.write('Edge\n')
                            else:
                                commutators.write('Corner\n')