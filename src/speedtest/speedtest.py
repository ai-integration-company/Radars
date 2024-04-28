import time
import matplotlib.pyplot as plt

k=[1,5,10,20]

K_BLP_time_k_sp={i:[] for i in k}

mwiss_time_k_sp={i:[] for i in k}

K_BLP_time_k_ds={i:[] for i in k}

mwiss_time_k_ds={i:[] for i in k}

N = range(10,110,10)

for i in N:
    adjacency_matrix_sp, weights_sp = load_data(f'speed_test/inputs/input_with_weights_sparse_{i}.csv')
    adjacency_matrix_ds, weights_ds = load_data(f'speed_test/inputs/input_with_weights_dense_{i}.csv')
    for j in k:
        
        t0 = time.time()
        K_BLP(j,weights_sp, adjacency_matrix_sp)
        t1 = time.time()

        K_BLP_time_k_sp[j].append(t0-t1)

        t0 = time.time()
        K_BLP(j,weights_ds, adjacency_matrix_ds)
        t1 = time.time()

        K_BLP_time_k_ds[j].append(t0-t1)

        t0 = time.time()
        _maximum_weighted_independent_set_scipy(j,weights_sp, adjacency_matrix_sp)
        t1 = time.time()

        K_BLP_time_k_sp[j].append(t0-t1)

        t0 = time.time()
        _maximum_weighted_independent_set_scipy(j,weights_ds, adjacency_matrix_ds)
        t1 = time.time()

        K_BLP_time_k_ds[j].append(t0-t1)