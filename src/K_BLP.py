import pulp
import time
import csv

def load_data(filepath):
    with open(filepath, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)

    matrix = [list(map(int, row)) for row in data[:-1]] 
    weights = list(map(float, data[-1])) 

    return matrix, weights

def K_BLP(k, w, adjacency_matrix):
    num_vars = len(w)
    solver = pulp.PULP_CBC_CMD(msg=False)

    prob = pulp.LpProblem("Maximize_Weighted_Sum", pulp.LpMaximize)

    x = [pulp.LpVariable(f'x_{i}', cat=pulp.LpBinary) for i in range(num_vars)]

    
    for i in range(num_vars):
        for j in range(i + 1, num_vars):  
            if adjacency_matrix[i][j] == 0:
                prob += x[i] + x[j] <= 1

    prob += pulp.lpSum([w[i] * x[i] for i in range(num_vars)])

    for iteration in range(k):
        prob.solve(solver)

        if pulp.LpStatus[prob.status] == 'Optimal':
            print("Solution:")
            print("Objective value =", pulp.value(prob.objective))
            solution = [pulp.value(var) for var in x]
            print("x =", solution)

            m = 2 * sum(solution) - 1
            y = [4*xi - 2 for xi in solution]
            prob += pulp.lpSum([y[j] * x[j] for j in range(num_vars)]) <= m

        else:
            print(f'The problem does not have an optimal solution on iteration {iteration}.')
            return None

if __name__ == "__main__":
    t1 = time.time()
    matrix, weights = load_data('input_with_weights.csv')
    K_BLP(5, weights, matrix)
    t2 = time.time()
    print(f"t = {t2-t1}")