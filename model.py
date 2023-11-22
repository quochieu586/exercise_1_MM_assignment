from gamspy import *
from table import *

m = Container()

i = Set(m, "i", description="product", records=demand[0].index)
j = Set(m, "j", description="unit", records=unit_cost.index)

a_ij = Parameter(
    container=m,
    name="a_ij",
    description="supply matrix",
    domain=[i, j],
    records=supply_matrix.reset_index(),
)
d_1 = Parameter(m, "d_1", domain=i, description="demand", records=demand[0].reset_index())
d_2 = Parameter(m, "d_2", domain=i, description="demand", records=demand[1].reset_index())
d = [d_1, d_2]
l = Parameter(m, "l", domain=i, description="product cost", records=product_cost.reset_index())
s = Parameter(m, "s", domain=j, description="unit cost", records=unit_cost.reset_index())

x = Variable(m, "x", type="Positive", domain=j)
y = Variable(m, "y", type="Positive", domain=j)
z = Variable(m, "z", type="Positive", domain=i)
y_2 = Variable(m, "y_1", type="Positive", domain=j)
z_2 = Variable(m, "z_1", type="Positive", domain=i)

supply = Equation(m, "supply", domain=j, description="supply of unit j to product i")
supply[j] = y[j] == -x[j] + Sum(i, a_ij[i,j]*z[i])

supply_2 = Equation(m, "supply_2", domain=j, description="supply of unit j to product i")
supply_2[j] = y_2[j] == -x[j] + Sum(i, a_ij[i,j]*z_2[i])

demand_constraint = Equation(m, "demand", domain=i, description="Demand for each product")
demand_constraint[i] = z[i] <= d[0][i]

demand_constraint_2 = Equation(m, "demand_2", domain=i, description="Demand for each product")
demand_constraint_2[i] = z_2[i] <= d[1][i]

obj = 1/2*(Sum(i, l[i]*z[i]) - Sum(j, s[j]*y[j]) + Sum(i, l[i]*z_2[i]) - Sum(j, s[j]*y_2[j]))

transport = Model(
    m, "transport",
    problem="LP", equations=[supply, supply_2, demand_constraint, demand_constraint_2],
    sense=Sense.MIN, objective=obj
)

transport.solve(solver="CPLEX")

if __name__ == "__main__":
    print(y.records)
    print(z.records)
    print(transport.objective_value)
