def map_string(s):
    res = list()
    for ss in s:
        res.append(ss)
    return res

def mult_n_pow(x,y):
    pows = map(lambda ch: int(ch)**int(y),map_string(x))
    reduced = reduce(lambda r,s: r+s, pows)

    return str(reduced)

def is_pow(x,y):
    xs = str(x)
    ys = str(y)
    if xs==mult_n_pow(xs,ys) and xs!='1':
        return True
    return False

def range_list(n):
    res = list()
    for i in range(1,n+1):
        res.append(str(i))
    return res

def add_two(x,y):
    return int(x)+int(y)

#evaluation
def evaluate(upper_bound, power_of):
    filtered = filter(lambda x: is_pow(x,power_of),range_list(upper_bound))
    added = reduce(lambda a,b: add_two(a,b),filtered)

    return added

print 'added: {}'.format(evaluate(999999, 5))
