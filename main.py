from read_info import read_all
from pereb_resh import pereb_r
from new_map_r import map_r
from tree_r import tree_r
from data_generation import data_gen
import time

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
while index <= 2**10:
    per_time = 0
    map_time = 0
    tree_time = 0
    squares, points = data_gen(index)
    if index < 64:
        start_time = time.time()
        for i in range(1000):
            p_r = pereb_r(squares, points)
        per_time = (time.time() - start_time) / 1000

        start_time = time.time()
        for i in range(100):
            m_r = map_r(squares, points)
        map_time = (time.time() - start_time) / 100

        start_time = time.time()
        for i in range(100):
            t_r = tree_r(squares, points)
        tree_time = (time.time() - start_time) / 100
    else:
       start_time = time.time()
       p_r = pereb_r(squares, points)
       per_time = time.time() - start_time
       start_time = time.time()
       m_r = map_r(squares, points)
       map_time = (time.time() - start_time)
       start_time = time.time()
       t_r = tree_r(squares, points)
       tree_time = (time.time() - start_time)

    print(index, end=' ')
    # print(f'{per_time} {map_time} {tree_time}'.replace('.', ','))
    # print(f'{p_r[1]} {m_r[1]} {t_r[1]}'.replace('.', ','))
    print(f'{p_r[2]} {m_r[2]} {t_r[2]}'.replace('.', ','))
    # print(f'pr:{p_r[0]}\nmr:{m_r}\ntr:{t_r}')
    assert p_r[0] == m_r[0], f'Решение перебором:\n{p_r[0]}\nРешение картой:\n{m_r[0]}\n'
    assert p_r[0] == t_r[0], f'Решение перебором:\n{p_r[0]}\nРешение деревом:\n{t_r[0]}\n'
    assert m_r[0] == t_r[0], f'Решение картой:\n{m_r[0]}\nРешение деревом:\n{t_r[0]}\n'
    index += 100

    
