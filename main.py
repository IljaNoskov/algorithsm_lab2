from read_info import read_all
from pereb_resh import pereb_r
from new_map_r import map_r
from tree_r import tree_r

parms, points = read_all()
pereb_r(parms, points)
print()
map_r(parms, points)
print()
tree_r(parms, points)
