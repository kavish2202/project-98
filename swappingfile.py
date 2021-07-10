def swapData(path1, path2):
    with open(path1, 'r') as a:
        data_a = a.read()

    with open(path2) as b:
        data_b = b.read()

    with open(path1, "w") as c:
        c.write(data_b)

    with open(path2, "w") as d:
        d.write(data_a)


swapData("sample1.txt", "sample2.txt")