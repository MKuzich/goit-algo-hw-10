from pulp import LpMaximize, LpProblem, LpVariable, lpSum, pulp, LpStatus

model = LpProblem(name="maximize_drinks_production", sense=LpMaximize)

x = LpVariable(name="limonade", lowBound=0, cat='Continuous')
y = LpVariable(name="fruit_juice", lowBound=0, cat='Continuous')

model += (2 * x + 1 * y <= 100, "water_constraint")
model += (1 * x <= 50, "sugar_constraint")
model += (1 * x <= 30, "lemon_juice_constraint")
model += (2 * y <= 40, "fruit_puree_constraint")

model += lpSum([x, y]), "Objective"

model.solve(pulp.PULP_CBC_CMD(msg=False))

print(f"Status: {LpStatus[model.status]}")
print(f"Limonade: {x.value()}")
print(f"Fruit Juice: {y.value()}")