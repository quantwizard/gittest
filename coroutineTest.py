def coroutine(f):
    def wrapper(*args, **kwargs):
        c = f(*args, **kwargs)
        c.send(None)
        return c
    return wrapper


@coroutine
def apply(f, next=None):
    while True:
        i = yield
        i = f(i)
        if next:
            next.send(i)

@coroutine
def filter(con, next=None):
    while True:
        i = yield
        if con(i) and next:
            next.send(i)

# 无论是filter还是apply, 其参数都是function，所以我们可以实现任何想要实现的功能
# 而filter和apply就是起到一个pipeline的作用，由于其内部使用无限循环while True
# 所以这个管道可以无限长

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