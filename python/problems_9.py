MAX_NUM = 1000


def get_pythagorean(num):
    for i in range(1, num):
        for j in range(1, num):
            for k in range(1, num):
                if (i + j + k) == num and i != j != k and i*i + j*j == k*k:
                    print(f"{i} * {j} * {k} = {i * j * k} ")
                    return


get_pythagorean(MAX_NUM)

if __name__ == "__main__":
    pass
