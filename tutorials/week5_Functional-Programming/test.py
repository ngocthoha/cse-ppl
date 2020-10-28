def convert(x):
    if '0o' in x or '00' in x:
        return int(x, 8)
    elif ('0x' or '0X') in x == True:
        return int(x, 16)
    else:
        return int(x)

a = [1, 2]
b = [3, 4]
c = (a, b)

print(c[0][0])