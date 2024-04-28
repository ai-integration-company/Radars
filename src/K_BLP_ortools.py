import time
import csv
from ortools.linear_solver import pywraplp

def load_data(filepath):
    with open(filepath, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)

    matrix = [list(map(int, row)) for row in data[:-1]]  # Process all but the last row as integers
    weights = list(map(float, data[-1]))  # Process the last row as floats

    return matrix, weights

def K_BLP(k, w, adjacency_matrix):
    num_vars = len(w) 

    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print("The specified solver is not available.")
        return None

    # Приводим к задаче целочисленного линейного программирования

    x = [solver.IntVar(0, 1, f'x_{i}') for i in range(num_vars)]

    for i in range(num_vars):
        for j in range(i+1, num_vars):
            if adjacency_matrix[i][j] == 0:
                solver.Add(x[i] + x[j] <= 1)

    objective = solver.Objective()
    for i in range(num_vars):
        objective.SetCoefficient(x[i], w[i])
    objective.SetMaximization()


    for i in range(k):

        status = solver.Solve()

        if status == pywraplp.Solver.OPTIMAL:
            print("Solution:")
            print("Objective value =", solver.Objective().Value())
            solution = [int(x[i].solution_value()) for i in range(num_vars)]
            print("x =", solution)

            m = 2*sum(solution)-1 # см. доказатество леммы
            y = [4*xi - 2 for xi in solution] # см. доказательство леммы
            solver.Add(sum(y[j] * x[j] for j in range(num_vars)) <= m) # см. теорему
            
        else:
            print(f'The problem does not have an optimal solution on step {i}.')
            return None
        
if __name__=="__main__":
    t1 = time.time()
    adjacency_matrix, weights = load_data('input_with_weights.csv')
    K_BLP(5,weights, adjacency_matrix)
    t2 = time.time()
    print(f"time ={t2-t1}")
