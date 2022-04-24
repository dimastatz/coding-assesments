import sys
sys.path.append('../')

import unittest
import src.tetris


def print_state(state: list) -> list:
    print('\nSTATE SNAPSHOT:')
    print('\n'.join(str(''.join('_' if c == 0 else '*' for c in x)) for x in reversed(state)))
    return state


class TestTetris(unittest.TestCase):
    def test_get_height(self):
        state = [[0 for _ in range(10)] for _ in range(10)]
        self.assertEqual(src.tetris.get_height(state), 0)
        state.insert(0, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(src.tetris.get_height(state), 1)
        state.insert(3, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(src.tetris.get_height(state), 4)

    def test_add_q(self):
        letter = src.tetris.init_letters()["Q"]
        state = [[0 for _ in range(10)] for _ in range(10)]

        state = src.tetris.add_shape(state, letter,  0)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 2)
        state = src.tetris.add_shape(state, letter,  0)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 4)
        state = src.tetris.add_shape(state, letter,  2)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 4)
        state = src.tetris.add_shape(state, letter,  3)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 4)
        print_state(state)

    def test_add_z(self):
        letter = src.tetris.init_letters()["Z"]
        state = [[0 for _ in range(10)] for _ in range(10)]
        state = src.tetris.add_shape(state, letter, 0)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 2)
        state = src.tetris.add_shape(state, letter, 1)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 3)
        print_state(state)

    def test_add_s(self):
        letter = src.tetris.init_letters()["S"]
        state = [[0 for _ in range(10)] for _ in range(10)]
        state = src.tetris.add_shape(state, letter, 2)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 2)
        state = src.tetris.add_shape(state, letter, 0)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 2)
        state = src.tetris.add_shape(state, letter, 4)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 4)
        print_state(state)

    def test_add_t(self):
        letter = src.tetris.init_letters()["T"]
        state = [[0 for _ in range(10)] for _ in range(10)]
        state = src.tetris.add_shape(state, letter, 0)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 2)
        state = src.tetris.add_shape(state, letter, 2)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 3)
        state = src.tetris.add_shape(state, letter, 0)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 4)
        print_state(state)

    def test_add_i(self):
        letter = src.tetris.init_letters()["I"]
        state = [[0 for _ in range(10)] for _ in range(10)]
        state = src.tetris.add_shape(state, letter, 0)
        state = src.tetris.add_shape(state, letter, 4)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 1)
        state = src.tetris.add_shape(state, letter, 6)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 2)
        print_state(state)

    def test_add_l(self):
        letter = src.tetris.init_letters()["L"]
        state = [[0 for _ in range(10)] for _ in range(10)]
        state = src.tetris.add_shape(state, letter, 0)
        print_state(state)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 3)
        state = src.tetris.add_shape(state, letter, 1)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 4)
        print_state(state)
        state = src.tetris.add_shape(state, letter, 0)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 7)
        print_state(state)

    def test_add_j(self):
        letter = src.tetris.init_letters()["J"]
        state = [[0 for _ in range(10)] for _ in range(10)]
        state = src.tetris.add_shape(state, letter, 0)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 3)
        print_state(state)
        state = src.tetris.add_shape(state, letter, 0)
        self.assertTrue(next(i for i in range(len(state)) if 1 not in state[i]) == 6)
        print_state(state)

    def test_add_ex1(self):
        state = [[0 for _ in range(10)] for _ in range(10)]
        letters = src.tetris.init_letters()
        state = src.tetris.add_shapes(state, 'I0,I4,Q8', letters)
        self.assertTrue(src.tetris.get_height(state) == 1)
        print_state(state)

    def test_add_ex2(self):
        state = [[0 for _ in range(10)] for _ in range(10)]
        letters = src.tetris.init_letters()
        state = src.tetris.add_shapes(state, 'T1,Z3,I4', letters)
        self.assertTrue(src.tetris.get_height(state) == 4)
        print_state(state)

    def test_add_ex3(self):
        state = [[0 for _ in range(10)] for _ in range(10)]
        letters = src.tetris.init_letters()
        state = src.tetris.add_shapes(state, 'Q0,I2,I6,I0,I6,I6,Q2,Q4', letters)
        self.assertTrue(src.tetris.get_height(state) == 3)
        print_state(state)

    def test_add_my_test_1(self):
        state = [[0 for _ in range(10)] for _ in range(10)]
        letters = src.tetris.init_letters()
        state = src.tetris.add_shapes(state, 'L2,Z3,J0', letters)
        self.assertTrue(src.tetris.get_height(state) == 3)
        print_state(state)

    def test_add_my_test_2(self):
        state = [[0 for _ in range(10)] for _ in range(10)]
        letters = src.tetris.init_letters()
        state = src.tetris.add_shapes(state, 'L2,Z3,J0', letters)
        self.assertTrue(src.tetris.get_height(state) == 3)
        print_state(state)

    def test_add_my_test_3(self):
        state = [[0 for _ in range(10)] for _ in range(10)]
        letters = src.tetris.init_letters()
        state = src.tetris.add_shapes(state, 'L2,Z3,J0', letters)
        self.assertTrue(src.tetris.get_height(state) == 3)
        print_state(state)

    def test_add_all_letters(self):
        state = [[0 for _ in range(10)] for _ in range(10)]
        letters = src.tetris.init_letters()
        state = src.tetris.add_shapes(state, 'Q0,Z3,S7', letters)
        self.assertTrue(src.tetris.get_height(state) == 2)
        print_state(state)
        state = src.tetris.add_shapes(state, 'T0,I4', letters)
        self.assertTrue(src.tetris.get_height(state) == 4)
        print_state(state)
        state = src.tetris.add_shapes(state, 'L0,J8', letters)
        self.assertTrue(src.tetris.get_height(state) == 7)
        print_state(state)
        state = src.tetris.add_shapes(state, 'I3,Q7', letters)
        self.assertTrue(src.tetris.get_height(state) == 6)
        print_state(state)

    def test_case_05(self):
        # 'Q0,Q2,Q4,Q6,Q8,Q1,Q1'
        letters = src.tetris.init_letters()
        state = [[0 for _ in range(10)] for _ in range(10)]
        state = src.tetris.add_shapes(state, 'Q0,Q2,Q4,Q6', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 2)
        state = src.tetris.add_shapes(state, 'Q8,Q1,Q1', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 4)

    def test_case_16(self):
        # 'L0,J3,L5,J8,T1,T6,J2,L6,T0,T7'
        letters = src.tetris.init_letters()
        state = [[0 for _ in range(10)] for _ in range(10)]
        state = src.tetris.add_shapes(state, 'L0,J3', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 3)
        state = src.tetris.add_shapes(state, 'L5,J8', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 3)
        state = src.tetris.add_shapes(state, 'T1,T6', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 1)
        state = src.tetris.add_shapes(state, 'J2,L6', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 3)
        state = src.tetris.add_shapes(state, 'T0,T7', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 2)

    def test_case_17(self):
        # 'L0,J3,L5,J8,T1,T6,J2,L6,T0,T7,Q4'
        letters = src.tetris.init_letters()
        state = [[0 for _ in range(10)] for _ in range(10)]
        state = src.tetris.add_shapes(state, 'L0,J3,L5,J8', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 3)
        state = src.tetris.add_shapes(state, 'T1,T6', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 1)
        state = src.tetris.add_shapes(state, 'J2,L6', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 3)
        state = src.tetris.add_shapes(state, 'T0,T7', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 2)
        state = src.tetris.add_shapes(state, 'Q4', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 1)

    def test_case_19(self):
        # 'S0,S2,S4,S5,Q8,Q8,Q8,Q8,T1,Q1,I0,Q4'
        letters = src.tetris.init_letters()
        state = [[0 for _ in range(10)] for _ in range(10)]
        state = src.tetris.add_shapes(state, 'S0,S2,S4,S5', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 8)

        state = src.tetris.add_shapes(state, 'Q8,Q8,Q8,Q8', letters)
        print_state(state)
        state = src.tetris.add_shapes(state, 'T1,Q1', letters)
        print_state(state)
        state = src.tetris.add_shapes(state, 'I0,Q4', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 8)

    def test_case_20(self):
        # 'L0,J3,L5,J8,T1,T6,S2,Z5,T0,T7'
        letters = src.tetris.init_letters()
        state = [[0 for _ in range(10)] for _ in range(10)]

        state = src.tetris.add_shapes(state, 'L0,J3', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 3)

        state = src.tetris.add_shapes(state, 'L5,J8', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 3)

        state = src.tetris.add_shapes(state, 'T1,T6', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 1)

        state = src.tetris.add_shapes(state, 'S2,Z5', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 2)

        state = src.tetris.add_shapes(state, 'T0,T7', letters)
        print_state(state)
        self.assertTrue(src.tetris.get_height(state) == 0)


if __name__ == '__main__':
    unittest.main()
