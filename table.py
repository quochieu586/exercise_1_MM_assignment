import pandas as pd
import numpy as np
from scipy.stats import binom

r_values = list(range(11))
dist = [binom.pmf(r, 10, 0.5) for r in r_values]

default_unit_data = [
        ["unit_1", 2],
        ["unit_2", 2],
        ["unit_3", 2],
        ["unit_4", 2],
        ["unit_5", 2],
        ["unit_6", 2],
        ["unit_7", 2],
        ["unit_8", 2]
    ]

default_product_data = [["product_1", 2], ["product_2", 2],["product_3", 2], ["product_4", 2],["product_5", 2]]

supply_data_frame = []

try:
    lines = open("supply_matrix.txt").readlines()
    for line in lines:
        num = line.split()
        arr = []
        for s in num:
            arr.append(int(s))
        supply_data_frame.append(arr)
except OSError:
    print("Can not read supply_matrix.txt file")
    supply_data_frame = [   # default value
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ]


supply_data = []
for i in range(5):
    for j in range(8):
        prod_str = "product_" + str(i+1)
        unit_str = "unit_" + str(j+1)
        supply_data.append([prod_str, unit_str, supply_data_frame[i][j]])

supply_matrix = pd.DataFrame(
    supply_data,
    columns=["product", "unit", "supply"]
).set_index(["product", "unit"])

demand = []

demand.append(
    pd.DataFrame(
        [["product_1", np.random.choice(np.arange(0,11), p=dist)],
        ["product_2", np.random.choice(np.arange(0,11), p=dist)],
        ["product_3", np.random.choice(np.arange(0,11), p=dist)],
        ["product_4", np.random.choice(np.arange(0,11), p=dist)],
        ["product_5", np.random.choice(np.arange(0,11), p=dist)]],
        columns=["product", "demand_0"]
    ).set_index("product")
)

demand.append(
    pd.DataFrame(
        [["product_1", np.random.choice(np.arange(0,11), p=dist)],
        ["product_2", np.random.choice(np.arange(0,11), p=dist)],
        ["product_3", np.random.choice(np.arange(0,11), p=dist)],
        ["product_4", np.random.choice(np.arange(0,11), p=dist)],
        ["product_5", np.random.choice(np.arange(0,11), p=dist)]],
        columns=["product", "demand_1"]
    ).set_index("product")
)

product_cost_data = []
product_price_data = []

try:
    lines = open("product.txt").readlines()
    for i in range (1, 6):
        line = lines[i].split()
        product_cost_data.append(["product_" + str(i), int(line[0])])
        product_price_data.append(["product_" + str(i), int(line[1])])
except OSError: # default value
    print("Can not read product.txt file")
    product_cost_data = default_product_data
    product_price_data = default_product_data

product_cost = pd.DataFrame(
    product_cost_data,
    columns=["product", "cost\n(l_i)"]
).set_index("product")

product_selling_price = pd.DataFrame(
    product_price_data,
    columns=["product", "selling price\n(q_i)"]
).set_index("product")

unit_price_data = []
preorder_cost_unit_data = []

try:
    lines = open("unit.txt").readlines()
    for j in range (1,9):
        unit_price_data.append(["unit_"+str(j), int(lines[j].split()[0])])
        preorder_cost_unit_data.append(["unit_"+str(j), int(lines[j].split()[1])])
except OSError: # default value
    print("Can not read unit.txt file")
    unit_price_data = default_unit_data
    preorder_cost_unit_data = default_unit_data

unit_selling_price = pd.DataFrame(
    unit_price_data,
    columns=["unit", "selling price\n(s_j)"]
).set_index("unit")

preorder_cost = pd.DataFrame(
    preorder_cost_unit_data,
    columns=["unit", "preorder cost\n(b_j)"]
).set_index("unit")

scenerio_num = len(demand)

if __name__ == "__main__":
    print(preorder_cost)
    pass