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
            else:
                break

#希尔排序
def shellSort(a):
    gap = len(a) // 2 #希尔的分组值
    while gap != 0:
        for i in range(gap,len(a)):
            for k in range(i,gap,-gap):
                if a[k] < a[k - gap]:
                    a[k],a[k-gap] = a[k-gap],a[k]
        gap //= 2

#冒泡排序
def bubbSort(a):
    step = 0
    record = 0
    for i in range(len(a)):
        isSort = True
        for j in range(len(a)-i-1):
            if a[j] < a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                isSort = False
                #record = j #记录最后一次交换的位置
            step += 1
        if isSort:
            break
    print(step)
num1 = [1,5,15,21,23,23,41,47,51,54]
num = [1,5,3,6,5,4,7,8,9,2]
bubbSort(num1)
print(num1)