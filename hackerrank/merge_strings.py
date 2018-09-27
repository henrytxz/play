# https://www.hackerrank.com/x/library/hackerrank/all/questions/232646/try


# def mergeStrings(a, b):
#     min_len = min(len(a), len(b))
#     l = []
#     for i in range(min_len):
#         l.append(a[i])
#         l.append(b[i])
#     return ''.join(l) + a[min_len:] + b[min_len:]
#
# if mergeStrings('abc', 'stuvwx') == 'asbtcuvwx':
#     print 'yes'


def mergeStrings(a, b):
    al=list(a)
    bl=list(b)
    diff = abs(len(al) - len(bl))
    extendable = al if len(al) < len(bl) else bl
    extendable.extend(['' for x in xrange(diff)])
    return ''.join(['{0}{1}'.format(al[x], bl[x]) for x in xrange(len(al))])


mergeStrings('abc', 'stuvwx')