LOOP_NUM = 100

i = 0
j = 0

for num in range(1, LOOP_NUM + 1, 1):
    i += num * num
    j += num

j = j * j
k = abs(i - j)
print(f"1 ~ {LOOP_NUM}: {i} - {j} = {k}")

if __name__ == "__main__":
    pass
