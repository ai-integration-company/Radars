import gurobipy as gp
from gurobipy import GRB
import scipy.sparse as sp
import numpy as np

def K_gurobipy(k, weights, adjacency_matrix):
    
    with gp.Env(empty=True) as env:
        env.setParam('OutputFlag', 0)
        env.start()
        with gp.Model("mwis", env=env) as model:
            adjacency_matrix = sp.triu(sp.csr_matrix(np.logical_xor(adjacency_matrix, 1)), k = 1)
            
            rows, cols = adjacency_matrix.tocoo().row, adjacency_matrix.tocoo().col
            num_vertices, num_edges = len(weights), len(rows)
            x = model.addMVar(num_vertices, vtype=GRB.BINARY, name="x")
            model.setObjective(weights @ x, sense=GRB.MAXIMIZE)
            indices = []
            for i, j in zip(rows, cols):
                indices.extend([i, j])
            indptr = range(0, len(indices) + 2, 2)
            data = np.ones(2 * num_edges)
            A = sp.csc_array((data, indices, indptr), shape=(num_vertices, num_edges))
            model.addMConstr(
                A.T,
                x,
                GRB.LESS_EQUAL,
                np.ones(A.shape[1]),
                name="no_adjacent_vertices",
            )
            model.Params.PoolSearchMode = 2
            model.Params.PoolSolutions = k
            model.optimize()
            print("---------------------------------------")
            sol = []
            w = []
            for i in range(model.SolCount):
                model.Params.SolutionNumber = i
                g = [int(var.Xn) for var in model.getVars()]
                print(f"{i+1})" + str(g))
                _w = np.dot(weights,g)
                print(f"w = {_w}")
                sol.append(g)
                w.append(_w)
                print("---------------")
            return np.array(sol), np.array(w)