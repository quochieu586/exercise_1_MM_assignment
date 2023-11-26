import math

from tabulate import tabulate
from model import *

print('Supply matrix (a_ij):')
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
    for row in supply_data_frame]))

product = pd.concat([product_cost, product_selling_price, demand[0], demand[1]], axis='columns')
print(tabulate(product, headers='keys', tablefmt='psql'))

unit = pd.concat([preorder_cost, unit_selling_price], axis='columns')
print(tabulate(unit, headers='keys', tablefmt='psql'))

wait = input("Press Enter to solve the system...")

transport.solve(solver="CPLEX")
if math.isnan(transport.objective_value):
    print("The feasible solution is unbounded")
else:
    print("x:\n", x.records)
    print("+-----------------------------------------------------+")
    print("y in scenerio 1:\n", y[0].records)
    print("+-----------------------------------------------------+")
    print("z in scenerio 1:\n", z[0].records)
    print("+-----------------------------------------------------+")
    print("y in scenerio 2:\n", y[1].records)
    print("+-----------------------------------------------------+")
    print("z in scenerio 2:\n", z[1].records)
    print("+-----------------------------------------------------+")
    print("objective value:", transport.objective_value)
