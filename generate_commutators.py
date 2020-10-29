with open('output/commutators.csv', 'w') as commutators:
    for a1 in 'RMLUEDFSB':
        for a1_rot in ['', '\'']:
            for a2 in {
                'R': 'UEDFSB',
                'M': 'UEDFSB',
                'L': 'UEDFSB',
                'U': 'RMLFSB',
                'E': 'RMLFSB',
                'D': 'RMLFSB',
                'F': 'RMLUED',
                'S': 'RMLUED',
                'B': 'RMLUED'
            }[a1]:
                for a2_rot in ['', '2', '\'']:
                    a1_rot_inv = {
                        '': '\'',
                        '2': '2',
                        '\'': ''
                    }[a1_rot]
                    a2_rot_inv = {
                        '': '\'',
                        '2': '2',
                        '\'': ''
                    }[a2_rot]
                    for b in {
                        'R': 'ML',
                        'M': 'RL',
                        'L': 'RM',
                        'U': 'ED',
                        'E': 'UD',
                        'D': 'UE',
                        'F': 'SB',
                        'S': 'FB',
                        'B': 'FS'
                    }[a2]:
                        for b_rot in ['', '2', '\'']:
                            b_rot_inv = {
                                '': '\'',
                                '2': '2',
                                '\'': ''
                            }[b_rot]
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
