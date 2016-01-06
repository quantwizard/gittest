import pdb


S = ['EMPTY']

def gen(): #[1]
    for i in ['a', 'b']:
        print i
    for i in range(10):
        S[0] = yield i #[2] [4]
        print str(S[0])

def main():
    g = gen() #[a]
    # pdb.set_trace()
    print g.next() #[b]
    # pdb.set_trace()
    print g.send('ok') #[c]
    # pdb.set_trace()
    print g.next() #[d]

if __name__ == '__main__':
    main()
