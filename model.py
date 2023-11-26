from gamspy import *
from table import *

m = Container()

i = Set(m, "i", description="product", records=product_selling_price.index)
j = Set(m, "j", description="unit", records=unit_selling_price.index)

a_ij = Parameter(
    container=m,
    name="a_ij",
    description="supply matrix",
    domain=[i, j],
    records=supply_matrix.reset_index(),
)
d = [None]*scenerio_num
for scenerio in range(scenerio_num):
    d[scenerio] = Parameter(m, "d_" + str(scenerio), domain=i, description="demand", records=demand[scenerio].reset_index())

l = Parameter(m, "l", domain=i, description="product cost", records=product_cost.reset_index())
q = Parameter(m, "q", domain=i, description="product selling price", records=product_selling_price.reset_index())
s = Parameter(m, "s", domain=j, description="unit selling price", records=unit_selling_price.reset_index())
b = Parameter(m, "b", domain=j, description="preorder cost per unit", records=preorder_cost.reset_index())

x = Variable(m, "x", type="Positive", domain=j)
y = [None]*scenerio_num
z = [None]*scenerio_num

supply = [None]*scenerio_num
demand_constraint = [None]*scenerio_num

obj = Sum(j, x[j]*b[j])

for scenerio in range(scenerio_num):
    y[scenerio] = Variable(m, "y" + str(scenerio), type="Positive", domain=j)
    z[scenerio] = Variable(m, "z" + str(scenerio), type="Positive", domain=i)
    supply[scenerio] = Equation(
        m, "supply" + str(scenerio),
        domain=j, description="supply of unit j to product i"
    )
    supply[scenerio][j] = y[scenerio][j] == x[j] - Sum(i, a_ij[i,j]*z[scenerio][i])

    demand_constraint[scenerio] = Equation(
        m, "demand" + str(scenerio),
        domain=i, description="Demand for each product"
    )
    demand_constraint[scenerio][i] = z[scenerio][i] <= d[scenerio][i]

    obj += 0.5*Sum(i, (l[i]-q[i])*z[scenerio][i]) - 0.5*Sum(j, s[j]*y[scenerio][j])

transport = Model(
    m, "transport",
    problem="LP", equations=m.getEquations(),
    sense=Sense.MIN, objective=obj
)

if __name__ == "__main__":
    print(y[0].records)
    # print(equationss)
    print(transport.objective_value)
