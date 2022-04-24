import sys
from functools import reduce


def init_letters() -> dict:
    return {
        'I': lambda r, c: [(r, c), (r, c + 1), (r, c + 2), (r, c + 3)],
        'L': lambda r, c: [(r, c), (r, c + 1), (r + 1, c), (r + 2, c)],
        'Q': lambda r, c: [(r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1)],
        'J': lambda r, c: [(r, c), (r, c + 1), (r + 1, c + 1), (r + 2, c + 1)],
        'Z': lambda r, c: [(r, c + 1), (r, c + 2), (r + 1, c), (r + 1, c + 1)],
        'S': lambda r, c: [(r, c), (r, c + 1), (r + 1, c + 1), (r + 1, c + 2)],
        'T': lambda r, c: [(r, c + 1), (r + 1, c), (r + 1, c + 1), (r + 1, c + 2)]
    }


def get_letter_height(get_letter) -> int:
    return max(x[0] for x in get_letter(0, 0)) + 1


def disappear(state: list, cols=10) -> list:
    lst = [[x for x in row] for row in state if 0 in row]
    return lst + [[0 for _ in range(cols)] for _ in range(len(state) - len(lst))]


def recreate_state(s: list, get_letter, c: int, r: int) -> list:
    return [[1 if (i, j) in get_letter(r, c) else s[i][j] for j in range(len(s[i]))] for i in range(len(s))]


def add_shape(s: list, get_letter, c: int, r=None) -> list:
    r = len(s) - get_letter_height(get_letter) if r is None else r
    if r < 0 or sum(s[i][j] for i, j in get_letter(r, c)) != 0:
        return []
    else:
        res = add_shape(s, get_letter, c, r - 1)
        return res if res else recreate_state(s, get_letter, c, r)


def get_height(state: list) -> int:
    return max([i for i in range(len(state)) if 1 in state[i]], default=-1) + 1


def add_shapes(state: list, shapes: str, letters: dict) -> (list, list):
    items = [(letters[x[0]], int(x[1])) for x in shapes.split(',')]
    return reduce(lambda s, i: disappear(add_shape(s, i[0], i[1])), items, state)


def play_game(shapes: list, cols=10, rows=100) -> (list, list):
    empty_state = [[0 for _ in range(cols)] for _ in range(rows)]
    return [get_height(add_shapes(empty_state, x, init_letters())) for x in shapes]


if __name__ == '__main__':
    shapes_lst = [x[:-1].strip() for x in sys.stdin]
    sys.stdout.write('\n'.join(str(i) for i in play_game(shapes_lst)))
