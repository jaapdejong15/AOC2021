def file2data(filename: str, x):
    ret = []
    with open(file=filename) as f:
        for val in f:
            ret.append(x(val))
    return ret
