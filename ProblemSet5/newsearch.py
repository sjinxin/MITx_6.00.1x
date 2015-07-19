def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False




l = [1,2,3,4,5,6,7,8,9]
print search(l,5)
print newsearch(l,5)

l = [1,2,3]
print search(l,2)
print newsearch(l,2)

l = [1,2]
print search(l,1)
print newsearch(l,1)

