# 二分查找
def binSearch(n, a):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if n < a[mid]:
            hi = mid - 1
        elif n > a[mid]:
            lo = mid + 1
        else:
            return mid
    return -1


