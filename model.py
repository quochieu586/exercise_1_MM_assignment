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
for count in range(scenerio_num):
    d[count] = Parameter(m, "d_" + str(count), domain=i, description="demand", records=demand[count].reset_index())

l = Parameter(m, "l", domain=i, description="product cost", records=product_cost.reset_index())
q = Parameter(m, "q", domain=i, description="product selling price", records=product_selling_price.reset_index())
s = Parameter(m, "s", domain=j, description="unit selling price", records=unit_selling_price.reset_index())

x = Variable(m, "x", type="Positive", domain=j)
y = [None]*scenerio_num
z = [None]*scenerio_num

supply = [None]*scenerio_num
demand_constraint = [None]*scenerio_num

obj = 0

for count in range(scenerio_num):
    y[count] = Variable(m, "y" + str(count), type="Positive", domain=j)
    z[count] = Variable(m, "z" + str(count), type="Positive", domain=i)
    supply[count] = Equation(
        m, "supply" + str(count),
        domain=j, description="supply of unit j to product i"
    )
    supply[count][j] = y[count][j] == x[j] - Sum(i, a_ij[i,j]*z[count][i])

    demand_constraint[count] = Equation(
        m, "demand" + str(count),
        domain=i, description="Demand for each product"
    )
    demand_constraint[count][i] = z[count][i] <= d[count][i]

    obj += 0.5*Sum(i, (l[i]-q[i])*z[count][i]) - 0.5*Sum(j, s[j]*y[count][j])

transport = Model(
    m, "transport",
    problem="LP", equations=m.getEquations(),
    sense=Sense.MIN, objective=obj
)

if __name__ == "__main__":
    print(y[0].records)
    # print(equationss)
    print(transport.objective_value)
