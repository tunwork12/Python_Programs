#Linear Programming Problem with 2 Variables solver 

def intersection(a1,b1,c1,a2,b2,c2):

    det = a1*b2-a2*b1
    if det==0:
        return None  #Parallel lines
    x=(c1*b2-c2*b1)/det
    y=(a1*c2-a2*c1)/det
    return(x,y)

def is_feasible(point, constraints):
    x, y = point
    for a, b, c in constraints:
        if a*x + b*y > c :
            return False
    if x < 0 or y < 0:
        return False
    return True

# ---------INPUT ------------
print("Maximize Z = ax + by")
a_obj = float(input("Enter coefficient of x: "))
b_obj = float(input("Enter coefficient of y: "))

n = int(input("Enter number of constraints (Except x>=0 and y>=0 constraints): "))

constraints = []
print("Enter constraints in form: ax + by <= c")

for _ in range(n):
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    constraints.append((a, b, c))

# Adding x>=0 and y>=0 as constraints
constraints.append((-1, 0, 0))  # -x <= 0
constraints.append((0, -1, 0))  # -y <= 0

# ---------FIND INTERSECTION POINTS---------
points = []

for i in range(len(constraints)):
    for j in range(i+1, len(constraints)):
        p = intersection(*constraints[i], *constraints[j])
        if p is not None:
            points.append(p)

# ----------------FILTER FEASIBLE POINTS--------------------------------
feasible_points = [p for p in points if is_feasible(p, constraints)]

#-----OBJECTIVE FUNCTION-----
def objective(x, y):
    return a_obj*x + b_obj*y

#--------------------------FIND OPTIMUM--------------------------------
if feasible_points:
    best = max(feasible_points, key=lambda p: objective(p[0], p[1]))
    
    print("\nFeasible Points:")
    for p in feasible_points:
        print(p)

    print("\nOptimal Solution:")
    print("x =", best[0], "y =", best[1])
    print("Maximum Z =", objective(best[0], best[1]))
else:
    print("No feasible solution found.")



