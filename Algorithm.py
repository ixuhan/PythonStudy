#二分查找
def binSearch(n,a):
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

#选择排序，缺点：如果已经有序，仍然要做N^2/2次比较
def chooseSort(a):
    for i,val in enumerate(a):
        min = i
        for j in range(i+1,len(a)):
            if a[min] > a[j]: #找到最小位置的下标
                min = j
        a[i],a[min] = a[min],a[i] #交换首位和最小位

#插入排序
def insertSort(a):
    for i,val in enumerate(a):
        for j in range(i,0,-1): #由于前面已经有序，则只需要冒泡一次
            if a[j] < a[j - 1]:
                a[j],a[j-1] = a[j-1],a[j]

#希尔排序
def shellSort(a):
    gap = len(a) // 2 #希尔的分组值
    while gap != 0:
        for i in range(gap):
            for j in range(i + gap,len(a) - gap,gap):
                if a[j] < a[j + gap]:
                    a[j],a[j+gap] = a[j+gap],a[j]
        gap //= 2

num = [1,5,3,6,5,4,7,8,9,2]
shellSort(num)
print(num)