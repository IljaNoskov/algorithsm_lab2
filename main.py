from read_info import read_all
from pereb_resh import pereb_r
from new_map_r import map_r
from tree_r import tree_r
from data_generation import data_gen


'''
squares, points = read_all()
p_r = pereb_r(squares, points)
m_r = map_r(squares, points)
t_r = tree_r(squares, points)
assert p_r == m_r, f'Решение перебором:\n{p_r}\nРешение картой:\n{m_r}\n'
assert p_r == t_r, f'Решение перебором:\n{p_r}\nРешение деревом:\n{t_r}\n'
assert m_r == t_r, f'Решение картой:\n{m_r}\nРешение деревом:\n{t_r}\n'
print(f'pr:{p_r}\nmr:{m_r}\ntr:{t_r}')
'''


index = 1
while index < 2**10:
    squares, points = data_gen(index)
    p_r = pereb_r(squares, points)
    m_r = map_r(squares, points)
    t_r = tree_r(squares, points)
    print(index)
    print(f'pr:{p_r}\nmr:{m_r}\ntr:{t_r}')
    assert p_r == m_r, f'Решение перебором:\n{p_r}\nРешение картой:\n{m_r}\n'
    assert p_r == t_r, f'Решение перебором:\n{p_r}\nРешение деревом:\n{t_r}\n'
    assert m_r == t_r, f'Решение картой:\n{m_r}\nРешение деревом:\n{t_r}\n'
    index = index * 2

    
