## modelling vs solving
## don't solve. translate -> call solver -> query results
## human friendly syntax, call solver
## eg pyomo(python based)  http://www.pyomo.org/ 

##solver implements algos, actual solves
##input to solver not human friendly 

#pyomo
## linear and non linear both caan be modelled
from pyomo.environ import *

##concrete model needs data, creates concrete instance corresponding to data
##abstract don't need data
model = ConcreteModel()
##linear program  linear obj and constraints  solved using enumeration of corner points
## horrible but fast

##decesion variables (model var not python variables model.x = 5 blunder)
model.x = Var(domain= NonNegativeReals)
model.y = Var(domain= NonNegativeReals)
## domain = binary, int, conti, semi cont

##declare objective (default sense = min)
model.obj =-  Objective(expr= 40*model.x + 30*model.y, sense= maximize)

##declare constraints (strict inequalities not allowed,  strict equality allowed)
model.const1 = Constraint(expr= model.x <= 40)
model.const2 = Constraint(expr= model.x + model.y <= 80)
model.const3 = Constraint(expr= 2*model.x + model.y <= 100)

##problem defined print model
model.pprint()

## using solver coinor-cbc
solver = SolverFactory('cbc', executable = '/usr/bin/cbc')
solver.solve(model)

##display
print("x = ", model.x )
print("y = ", model.y )

print("nconstraints " )
print("Constraint1 = ", model.const1 )
print("Constraint2 = ", model.const2 )
print("Constraint3 = ", model.const3)

##min vortex read from .ipynb
#simple syntax
