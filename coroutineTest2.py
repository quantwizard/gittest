def coroutine(f):
    def wrapper(*args, **kw): 
        c = f(*args, **kw)
        c.send(None) # This is the same as calling ``next()``, 
                    # but works in Python 2.x and 3.x 
        return c
    return wrapper


@coroutine
def apply(op, next=None):
    while True:
        i = yield
        i = op(i)
        if next:
            next.send(i)


@coroutine
def filter(cond, next=None):
    while True:
        i = yield
        if cond(i) and next:
            next.send(i)


def main():
    result = [] 
    pipeline = filter(lambda x: not x % 2, \
                apply(lambda x: x * 2, \
                apply(lambda x: x + 1, \
                apply(result.append)))) 
    for i in range(10):
        pipeline.send(i)

    print result

if __name__ == '__main__':
    main()