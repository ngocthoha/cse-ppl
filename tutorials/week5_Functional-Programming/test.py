def convert(x):
    if '0o' in x or '00' in x:
        return int(x, 8)
    elif ('0x' or '0X') in x == True:
        return int(x, 16)
    else:
        return int(x)

a = "0o1"
b = convert(a)
print(b)