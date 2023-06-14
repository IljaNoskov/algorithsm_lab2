from read_info import read_all
from pereb_resh import pereb_r
from new_map_r import map_r
from tree_r import tree_r
from data_generation import data_gen

#parms, points = read_all()

index = 1
while index < 2**10:
    squares, points = data_gen(index)
    p_r = pereb_r(squares, points)
    m_r = map_r(squares, points)
    t_r = tree_r(squares, points)
    print(index)
    assert p_r == m_r, f'pr:\n{p_r}\n mr:\n{m_r}\n'
    assert p_r == t_r, f'pr:\n{p_r}\n tr:\n{t_r}\n'
    assert m_r == t_r, f'mr:\n{m_r}\n tr:\n{t_r}\n'
    print(f'')
    index = index * 2

    
