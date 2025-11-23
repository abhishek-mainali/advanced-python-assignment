import intarray

def demo():
    caps = intarray.init(5)
    for i in range(5):
        intarray.set(caps, i, i * 10)
    print('Values: ', [intarray.get(caps, i) for i in range(5)])
    intarray.free(caps)

if __name__ == '__main__':
    demo()
