import numpy as np

def result_for_method(f, h, yk):
    y = yk + (h / 2.) * f
    return y + (h / 2.) * y


def result_function(a, b, h):
    yp = []
    yk = 0.0
    while a <= b:
        res_derivative = result_derivative(a, yk)
        res = result_for_method(res_derivative, h, yk)
        yp.append(res)
        yk = res
        a += h
    return yp


def exp(a, b, h, y, yk):
    e_arr = []
    print("\tx\t\t\ty\t\t\tyk\t\t\te\t\te*100/yk")
    for x in np.arange(a, b, h):
        index = int((x - a) / h)
        if index < len(y) and index < len(yk):
            e = y[index] - yk[index]
            e_arr.append(e)
            print("#%d | %8.10f | %8.10f | %8.10f | %8.10f | %8.10f |" % (
                index, x, y[index], yk[index], e, (e * 100 / yk[index])))
    return e_arr


def result_derivative(x, y, f):
    return f(x, y)


def result_rynge_kyta(a, b, h, arr_func, first_step):
    yp = []
    yk = []
    yk += first_step
    yp.append(yk)
    count_func = len(arr_func)

    while a <= b:
        k1_arr = []
        k2_arr = []
        k3_arr = []
        k4_arr = []
        for i in range(count_func):
            res = result_derivative(a, yk[i], arr_func[i])
            k1_arr.append(h * res)  # k1

        for i in range(count_func):
            res = result_derivative(a + h / 2., yk[i] + k1_arr[i] / 2., arr_func[i])
            k2_arr.append(h * res)  # k2

        for i in range(count_func):
            res = result_derivative(a + h / 2., yk[i] + k2_arr[i] / 2., arr_func[i])
            k3_arr.append(h * res)  # k3

        for i in range(count_func):
            res = result_derivative(a + h, yk[i] + k3_arr[i], arr_func[i])
            k4_arr.append(h * res)  # k4

        yk = result_with_arr_k(k1_arr, k2_arr, k3_arr, k4_arr, yk)

        a += h
        yp.append(yk)
    return yp  # return list[list[y11...y1n],list[y21....y2n]]


def result_with_arr_k(k1_arr, k2_arr, k3_arr, k4_arr, yk):
    y_finish = []
    count_func = len(yk)
    for i in range(count_func):
        y_finish.append(yk[i] + k1_arr[i] / 6. + k2_arr[i] / 3. + k3_arr[i] / 3. + k4_arr[i] / 6.)
    return y_finish
