def fn(x):
    x = x * x
    return x


print(fn(5))

fn2 = lambda y: y * y
print(fn2(4))

fn3 = lambda x, y, z: (x + y + z) / 3
print(fn3(1, 2, 3))
