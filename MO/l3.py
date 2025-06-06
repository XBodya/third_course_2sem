import numpy as np
import sympy as sp

def newton_method(start_x, func, deriv, deriv2, eps=0.01, cnt_of_max_iters=10):
    if deriv(deriv(start_x, func), func) < 0:
        return ((None, None), None)
    k = 0
    x = [start_x]
    cur_deriv_value = deriv(start_x, func)
    while abs(deriv(x[-1], func)) > eps and cnt_of_max_iters > k:
        cur_x = x[-1]
        d1 = deriv(cur_x, func)
        d2 = deriv2(cur_x, func)
        # print(k, d1, d2, f"x_new={cur_x - d1 / d2}", d1 / d2)
        x.append(cur_x - (d1 / d2))
        k += 1
        # input()
    return ((x[-1], func(x[-1])), x)

def standart_deriv2(x, func, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)

def standart_deriv(x, func, h=1e-5):
    return (func(x) - func(x - h)) / h

def standart_second_deriv(x, func, h=1e-5):
    return (func(x + h) - 2 * func(x) + func(x - h)) / (h * h)

def compute_derivatives(point, f):
    x = sp.symbols('x')
    f_prime = sp.diff(f) 
    return f_prime_val

def golden_iter(a0, b0, f):
    cur_y = a0 + ((3 - np.sqrt(5)) / 2) * (b0 - a0)
    cur_z = a0 + b0 - cur_y

    f_y, f_z = f(cur_y), f(cur_z)
    if f_y <= f_z:
        return a0, cur_z, a0 + cur_z - cur_y, cur_y # a b y z
    else:
        return cur_y, b0, cur_z, a0 + cur_z - cur_y

def golden_alg(a0, b0, f, eps=0.01, iter_cnt=2):
    k = 0
    ak, bk, yk, zk = a0, b0, 0, 0
    for i in range(iter_cnt):
        ak, bk, yk, zk = golden_iter(ak, bk, f)
        # print(ak, bk, yk, zk)
        if i != 0 and abs(ak - bk) <= eps:
            break
        k += 1
    # print("ITERES", k, abs(ak - bk))
    return (ak + bk) / 2
    
if __name__ == "__main__":
    f = lambda x: x * np.atan(x) - (0.5 * np.log(1 + x * x))
    e = 1e-7
    x0 = 3
    a, b = -5, 5

    # print(0.7828898092311964 - standart_deriv(0.7828898092311964, f) / standart_deriv(standart_deriv(0.7828898092311964, f), f))
    try:
        result = newton_method(x0, f, standart_deriv, standart_second_deriv, e)[0]
        print("Solve without golden fix:", result[1])
        if np.isnan(result[1])  or result[1] is None:
            raise ValueError
    except:
        start_solve = golden_alg(a, b, f, eps=e, iter_cnt=10)
        print("new start point with fix:", start_solve)
        result = newton_method(start_solve, f, standart_deriv, standart_second_deriv, e)[0]
        print(result[1])
    # f = lambda x: 127 * x * x / 4 + 61 * x / 4 + 2
    # print(golden_alg(0, 0.5, f, eps=0.15, iter_cnt=10))