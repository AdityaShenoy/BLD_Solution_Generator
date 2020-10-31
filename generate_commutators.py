from cube import Cube
from algorithm import apply, to_human_readable

cube = Cube()


def process(commutators, s, s_slice, s_rot, s_rot_inv,
            a1, a1_slice, a1_rot, a1_rot_inv,
            a2, a2_slice, a2_rot, a2_rot_inv,
            b, b_slice, b_rot, b_rot_inv):

    if (s, s_slice, s_rot) == (a1, a1_slice, 4 - a1_rot):
        return

    moves = [f'{s}{s_slice}{s_rot}'] if s else []
    moves.extend([
        f'{a1}{a1_slice}{a1_rot}',
        f'{a2}{a2_slice}{a2_rot}',
        f'{a1}{a1_slice}{a1_rot_inv}',
        f'{b}{b_slice}{b_rot}',
        f'{a1}{a1_slice}{a1_rot}',
        f'{a2}{a2_slice}{a2_rot_inv}',
        f'{a1}{a1_slice}{a1_rot_inv}',
        f'{b}{b_slice}{b_rot_inv}',
    ])
    moves.extend([f'{s}{s_slice}{s_rot_inv}'] if s else [])

    apply(cube, moves)
    for cycle in cube.detect_cycle():
        commutators.write(f'{cycle.upper()},')
        algo = to_human_readable(moves)
        algo = algo.split(' ')
        algo[7 if s else 6] += ')'
        algo[5 if s else 4] = '(' + algo[5 if s else 4]
        algo[3 if s else 2] += ')'
        algo[1 if s else 0] = '(' + algo[1 if s else 0]
        commutators.write(' '.join(algo))
        commutators.write(',Edge,' if 2 in [a1_slice, a2_slice, b_slice]
                          else ',Corner,')
        commutators.write('Pure\n' if not s
                          else 'A9/B9\n' if (s, s_slice) in [(a1, a1_slice),
                                                             (b, b_slice)]
                          else 'Setup\n')

    cube.solve()

    moves = [f'{s}{s_slice}{s_rot}'] if s else []
    moves.extend([
        f'{b}{b_slice}{b_rot}',
        f'{a1}{a1_slice}{a1_rot}',
        f'{a2}{a2_slice}{a2_rot}',
        f'{a1}{a1_slice}{a1_rot_inv}',
        f'{b}{b_slice}{b_rot_inv}',
        f'{a1}{a1_slice}{a1_rot}',
        f'{a2}{a2_slice}{a2_rot_inv}',
        f'{a1}{a1_slice}{a1_rot_inv}',
    ])
    moves.extend([f'{s}{s_slice}{s_rot_inv}'] if s else [])

    apply(cube, moves)
    for cycle in cube.detect_cycle():
        commutators.write(f'{cycle.upper()},')
        algo = to_human_readable(moves)
        algo = algo.split(' ')
        algo[8 if s else 7] += ')'
        algo[6 if s else 5] = '(' + algo[6 if s else 5]
        algo[4 if s else 3] += ')'
        algo[2 if s else 1] = '(' + algo[2 if s else 1]
        # s b a a a b a a a s
        commutators.write(' '.join(algo))
        commutators.write(',Edge,' if 2 in [a1_slice, a2_slice, b_slice]
                          else ',Corner,')
        commutators.write('Pure\n' if not s
                          else 'A9/B9\n' if (s, s_slice) in [(a1, a1_slice),
                                                             (b, b_slice)]
                          else 'Setup\n')

    cube.solve()


with open('output/commutators.csv', 'w') as commutators:
    commutators.write('Cycle,Algorithm,Type,Moves\n')
    for s in ['', *'RUF']:
        for s_slice in [1, 2, 3]:
            for s_rot in [1, 2, 3]:
                s_rot_inv = 4 - s_rot
                for a1 in 'RUF':
                    for a1_slice in [1, 2, 3]:
                        for a1_rot in [1, 3]:
                            a1_rot_inv = 4 - a1_rot
                            for a2 in 'RUF'.replace(a1, ''):
                                for a2_slice in [1, 2, 3]:
                                    for a2_rot in [1, 2, 3]:
                                        a2_rot_inv = 4 - a2_rot
                                        b = a2
                                        for b_slice in [x for x in (1, 2, 3)
                                                        if x != a2_slice]:
                                            for b_rot in [1, 2, 3]:
                                                b_rot_inv = 4 - b_rot
                                                process(commutators,
                                                        s, s_slice,
                                                        s_rot, s_rot_inv,
                                                        a1, a1_slice,
                                                        a1_rot, a1_rot_inv,
                                                        a2, a2_slice,
                                                        a2_rot, a2_rot_inv,
                                                        b, b_slice,
                                                        b_rot, b_rot_inv)
                if not s:
                    break
            if not s:
                break
