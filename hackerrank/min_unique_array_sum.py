# https://www.hackerrank.com/x/tests/all/235591/questions/222912/try

def getMinimumUniqueSum(arr):
    in_order = sorted(arr)
    for i in range(len(in_order)-1):
        while in_order[i] >= in_order[i+1]:
            in_order[i+1] = in_order[i+1] + 1
    return sum(in_order)


print getMinimumUniqueSum([1, 1, 1])
