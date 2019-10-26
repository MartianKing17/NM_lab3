import method as m


def main():
    a = m.init_matrix()
    x0 = m.init_vector()
    ell = float(input("Enter ellipses: "))
    lambda_num = m.find_max_lambda(a, x0, ell)
    print("Maximum lambda: " + str(lambda_num))
    lambda_num = m.find_min_lambda(a, x0, ell)
    print("Minimum lambda: " + str(lambda_num))


main()
