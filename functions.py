import numpy as np


def DtDRV():
    n = 5
    X_table_head = [-1, 0, 1]
    Y_table_head = [0, 1, 3]

    table = np.array([[0.06, 0.27, 0.11],
                      [0.11, 0.10, 0.08],
                      [0.09, 0.15, 0.03]])

    print(table)

    r1 = []
    for _ in range(n):
        r1.append(np.random.random())

    r1 = np.array(r1)
    print("\nСгенерирована случайная величина для X:", r1)

    sum_Xi = np.sum(table, axis=0)
    print("\nСуммы по столбцам:", sum_Xi)
    sum_Yi = np.sum(table, axis=1)
    print("Суммы по строкам:", sum_Yi)

    for i in range(len(table)):
        if (sum_Xi[i] * sum_Yi[i]) != 0.1:
            print("\nАксиома локальной независимости выполняется!")
            break
        else:
            exit()

    cumulative_sum = np.cumsum(sum_Xi)

    print("\nПолученный интервал: ", f"[0; {cumulative_sum[0]}], ({cumulative_sum[0]}; "
                                     f"{cumulative_sum[1]}], ({cumulative_sum[1]};"
                                     f" {cumulative_sum[2]}]\n")

    distribution_X = []
    for num in r1:
        for i, element in enumerate(cumulative_sum):
            if num <= element:
                distribution_X.append(X_table_head[i])
                break

    print("Полученный закон распределения для X: ", distribution_X, "\n")

    normalized_columns = table / sum_Xi

    P_Y_X1 = []
    for i in range(len(table)):
        P_Y_X1.append(normalized_columns[i][0])
    P_Y_X1 = np.cumsum(P_Y_X1)
    print("Интервал для (Y\\X1)", f"[0; {P_Y_X1[0]:.3f}], ({P_Y_X1[0]:.3f}; "
                                  f"{P_Y_X1[1]}], ({P_Y_X1[1]};"
                                  f" {P_Y_X1[2]:.1f}]")

    P_Y_X2 = []
    for i in range(len(table)):
        P_Y_X2.append(normalized_columns[i][1])
    P_Y_X2 = np.cumsum(P_Y_X2)
    print("Интервал для (Y\\X2)", f"[0; {P_Y_X2[0]:.3f}], ({P_Y_X2[0]:.3f}; "
                                  f"{P_Y_X2[1]:.3f}], ({P_Y_X2[1]:.3f};"
                                  f" {P_Y_X2[2]:.1f}]")

    P_Y_X3 = []
    for i in range(len(table)):
        P_Y_X3.append(normalized_columns[i][2])

    P_Y_X3 = np.cumsum(P_Y_X3)
    print("Интервал для (Y\\X3)", f"[0; {P_Y_X3[0]:.3f}], ({P_Y_X3[0]:.3f}; "
                                  f"{P_Y_X3[1]:.3f}], ({P_Y_X3[1]:.3f};"
                                  f" {P_Y_X3[2]:.1f}]")

    r2 = []
    for _ in range(n):
        r2.append(np.random.random())

    r2 = np.array(r2)
    print("\nСгенерирована случайная величина для Y:", r2)

    distribution_Y = []

    if distribution_X[0] == X_table_head[0]:
        print("Так как первое значение X = -1 используем (Y\\X1)")
        for num in r2:
            for i, element in enumerate(P_Y_X1):
                if num <= element:
                    distribution_Y.append(Y_table_head[i])
                    break

    if distribution_X[0] == X_table_head[1]:
        print("Так как первое значение X = 0 используем (Y\\X2)")
        for num in r2:
            for i, element in enumerate(P_Y_X2):
                if num <= element:
                    distribution_Y.append(Y_table_head[i])
                    break

    if distribution_X[0] == X_table_head[2]:
        print("Так как первое значение X = 1 используем (Y\\X3)")
        for num in r2:
            for i, element in enumerate(P_Y_X3):
                if num <= element:
                    distribution_Y.append(Y_table_head[i])
                    break

    print("Полученный закон распределения для Y: ", distribution_Y)

    result = [(distribution_X[i], distribution_Y[i]) for i in range(n)]

    return result