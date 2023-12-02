def find_smallest_beautiful_number(x):
    max_num = 10 ** len(str(x)) - 1
    smallest_beautiful_number = -1

    for num in range(x, max_num + 1, x):
        num_str = str(num)
        if len(set(num_str)) == 1 and int(num_str[0]) != 0:
            smallest_beautiful_number = num
            break

    return smallest_beautiful_number if smallest_beautiful_number != -1 else "No beautiful number divisible by {} so I will return 111111 as an exception".format(x)

smallest = int(input("Enter number: "))
print(find_smallest_beautiful_number(smallest


# Another solution using while loops, but it's so slow
n = int(input("Enter a number: "))

t = 0
bn = n

while t == 0:
    if bn % n == 0:
        nl = []
        for d in str(bn):
            if int(d) in nl:
                pass
            else:
                nl.append(int(d))

        if len(nl) == 1:
            t += 1
            print(f"The smallest beautiful number is {bn}")

    bn += 1