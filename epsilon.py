# Def x in y
def epsilon(x: int, y: int):
    dight = x
    bin_num = format(y, 'b')
    if dight > len(bin_num) - 1:
        return 0
    else:
        return bin_num[::-1][dight]
