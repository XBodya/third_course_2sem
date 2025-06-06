import numpy as np
import l3
from scipy.optimize import minimize
from typing import Tuple

import matplotlib.pyplot as plt

log_str = ""

e1 = np.array([0, 1], dtype=np.float64)
e2 = np.array([1, 0], dtype=np.float64)

alphas = []

def is_equal_float(a: float, b:float, eps=1e-6):
    return abs(a - b) < eps

def is_equal_points(a: Tuple[float, float], b: Tuple[float, float], eps=1e-6):
    return is_equal_float(a[0], b[0], eps=eps) and is_equal_float(a[1], b[1], eps=eps)

def euclid_norm(x1n, x2n):
    res = 0
    for i in range(min(len(x1n), len(x2n))):
        res += (x1n[i] - x2n[i]) * (x1n[i] - x2n[i])
    return np.sqrt(res)

norm_stop_cond = lambda x1, x2, f, eps: euclid_norm(x1, x2) < eps

f = lambda x1, x2: 2 * x1 * x1 + x2 * x2 + x1 * x2
eps = 0.01
default_stop_cond = lambda x1, x2, f, eps: abs(f(*x1) - f(*x2)) < eps
start = [0.5, 1]
all_y = [start]
def pauell_method(start_point, f, eps=0.01, cnt_iter=100, stop_condition=default_stop_cond):
    x = [start_point]
    q = [e1, e2, e1]
    for i in range(cnt_iter):
        print("ITER NO.", i)
        y = [x[-1]]
        fnc_point_y_cur = []
        for j in range(3):
            print(f"{y[-1][0]} + alpha * {q[j][0]}, {y[-1][1]} + alpha * {q[j][1]})")
            fnc_point_y_cur = lambda alpha: (y[-1][0] + alpha * q[j][0], y[-1][1] + alpha * q[j][1])
            func_for_minimize = lambda alpha: f(*fnc_point_y_cur(alpha))
            cur_alpha_start_point =  l3.golden_alg(-1, 1, func_for_minimize, eps=eps)
            # print(func_for_minimize(1))
            # alpha_value = l3.newton_method(cur_alpha_start_point, func_for_minimize, l3.standart_deriv, l3.standart_second_deriv, eps=eps)[0][0]
            alpha_value = minimize(func_for_minimize, cur_alpha_start_point).x[0]
            print(f'cur alpha value={alpha_value}')
            print(f"{fnc_point_y_cur(alpha_value)[0]}, {fnc_point_y_cur(alpha_value)[1]}")
            y.append(fnc_point_y_cur(alpha_value))
            all_y.append(fnc_point_y_cur(alpha_value))
            print('new y: {}'.format(y[-1]))
            print()
            alphas.append(alpha_value)
        if is_equal_points(y[1], y[3], 1e-10):
            print("FAST FIND DOWN", i)
            return y[3], x
        x.append(y[3])
        print(f"x_last={x[-1]}")
        if stop_condition(x[-2], x[-1], f, eps=1e-10):
            print("STOP COND", i)
            return x[-2], x
        q[1] = q[2].copy()
        print(f"q[1] = q[2] = {q[2]}")
        q[0] = [y[3][0] - y[1][0], y[3][1] - y[1][0]]
        q[2] = [y[3][0] - y[1][0], y[3][1] - y[1][0]]
        print(f"q[0] = q[2] = [{y[3][0] - y[1][0]}, {y[3][1] - y[1][0]}]")
    print("ITER DOWN")
    return x[-1], x
        
if '__main__' == __name__:
    res = pauell_method(start, f, stop_condition=norm_stop_cond)
    vals = res[1]
    for i in range(0, len(alphas), 3):
        print(alphas[i], alphas[i + 1], alphas[i + 2])
    # print(alphas)
    # vals = all_y
    print('result is ', res[0])
    for i in range(0, len(vals) - 1):
        cur_x = [vals[i][0], vals[i + 1][0]]
        cur_y = [vals[i][1], vals[i + 1][1]]
        plt.plot(cur_x, cur_y, 'ro-')
    plt.grid()
    plt.show()

    # print(*vals, sep='\n')
    