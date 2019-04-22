def exp(p1, p2, df=0, *vart, **kw):
    print(f'p1 ={p1},p2={p2},df={df},vart={vart},kw ={kw}')


exp(1, 2)
exp(1, 2, c=3)
exp(1, 2, 3, 'a', 'b')
exp(1, 2, 3, 'abc', x=9)

args = (1, 2, 3, 4)         # args定义为tuple
kw = {'x': 8, 'y': '9'}    # kw定义为dict
exp(*args, **kw)
