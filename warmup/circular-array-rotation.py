mygenerator=(x*x for x in range(3))

def printing(x):
    for i in x:
        yield i

printing(mygenerator)
