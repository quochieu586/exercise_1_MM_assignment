import pandas as pd

supply_data = [
    ["product_1", "unit_1", 1],
    ["product_1", "unit_2", 1],
    ["product_1", "unit_3", 1],
    ["product_1", "unit_4", 1],
    ["product_1", "unit_5", 1],
    ["product_1", "unit_6", 1],
    ["product_1", "unit_7", 1],
    ["product_1", "unit_8", 1],
    ["product_2", "unit_1", 1],
    ["product_2", "unit_2", 1],
    ["product_2", "unit_3", 1],
    ["product_2", "unit_4", 1],
    ["product_2", "unit_5", 1],
    ["product_2", "unit_6", 1],
    ["product_2", "unit_7", 1],
    ["product_2", "unit_8", 1],
    ["product_3", "unit_1", 1],
    ["product_3", "unit_2", 1],
    ["product_3", "unit_3", 1],
    ["product_3", "unit_4", 1],
    ["product_3", "unit_5", 1],
    ["product_3", "unit_6", 1],
    ["product_3", "unit_7", 1],
    ["product_3", "unit_8", 1],
    ["product_4", "unit_1", 1],
    ["product_4", "unit_2", 1],
    ["product_4", "unit_3", 1],
    ["product_4", "unit_4", 1],
    ["product_4", "unit_5", 1],
    ["product_4", "unit_6", 1],
    ["product_4", "unit_7", 1],
    ["product_4", "unit_8", 1],
    ["product_5", "unit_1", 1],
    ["product_5", "unit_2", 1],
    ["product_5", "unit_3", 1],
    ["product_5", "unit_4", 1],
    ["product_5", "unit_5", 1],
    ["product_5", "unit_6", 1],
    ["product_5", "unit_7", 1],
    ["product_5", "unit_8", 1],
]

supply_matrix = pd.DataFrame(
    supply_data,
    columns=["product", "unit", "supply"]
).set_index(["product", "unit"])

demand_1 = pd.DataFrame(
    [["product_1", 4],
    ["product_2", 4],
    ["product_3", 4],
    ["product_4", 4],
    ["product_5", 4]],
    columns=["product", "demand_1"]
).set_index("product")

demand_2 = pd.DataFrame(
    [["product_1", 6],
    ["product_2", 6],
    ["product_3", 6],
    ["product_4", 6],
    ["product_5", 6]],
    columns=["product", "demand_1"]
).set_index("product")

demand = [demand_1, demand_2]

product_cost = pd.DataFrame(
    [["product_1", 1], ["product_2", 1],["product_3", 1], ["product_4", 1],["product_5", 1]],
    columns=["product", "cost"]
).set_index("product")

unit_cost = pd.DataFrame(
    [["unit_1", 1],
    ["unit_2", 1],
    ["unit_3", 1],
    ["unit_4", 1],
    ["unit_5", 1],
    ["unit_6", 1],
    ["unit_7", 1],
    ["unit_8", 1]],
    columns=["unit", "cost"]
).set_index("unit")

def main():
    frames = [demand_1, demand_2]
    result = pd.concat(frames)
    print(result)

if __name__ == "__main__":
    main()