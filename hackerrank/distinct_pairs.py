from collections import Counter

def numberOfPairs(a, k):
    # a is the array of ints and k is the target that we want a pair of ints to add up to
    s = set(a)
    distinct_pairs = set()
    counter = Counter(a)
    for x in a:
        if k-x in s:
            if x == k-x and counter[x] == 1:
                # exclude the case a = [1, ] and k = 2 because in this case there is not a pair
                continue
            else:
                distinct_pairs.add((min(x, k-x), max(x, k-x)))
    return len(distinct_pairs)


assert numberOfPairs([6, 12, 3, 9, 3, 5, 1], 12) == 1
