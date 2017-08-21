# 选择排序
def chooseSort(a):
    for i, val in enumerate(a):
        min = i
        for j in range(i + 1, len(a)):
            if a[min] > a[j]:  # 找到最小位置的下标
                min = j
        a[i], a[min] = a[min], a[i]  # 交换首位和最小位


# 插入排序
def insertSort(a):
    for i, val in enumerate(a):
        for j in range(i, 0, -1):  # 由于前面已经有序，则只需要冒泡一次
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
            else:
                break


# 希尔排序
def shellSort(a):
    gap = len(a) // 2  # 希尔的分组值
    while gap != 0:
        for i in range(gap, len(a)):
            for k in range(i, gap, -gap):
                if a[k] < a[k - gap]:
                    a[k], a[k - gap] = a[k - gap], a[k]
                else:
                    break
        gap //= 2


# 冒泡排序
def bubbSort(a):
    record = len(a) - 1
    for i in range(len(a)):
        isSort = True
        for j in range(record):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                isSort = False
                record = j  # 记录最后一次交换的位置
        if isSort:
            break


# 归并排序
class MergeSortUtil(object):
    # 第一个数组是first-mid 第二个数组是mid+1-temp
    def mergeSort(self, a, first, mid, last, temp):
        i = first
        j = mid + 1
        k = 0
        while i <= mid and j <= last:
            if a[i] < a[j]:
                temp[k] = a[i]
                i += 1
            else:
                temp[k] = a[j]
                j += 1
            k += 1

        while j <= last:
            temp[k] = a[j]
            j += 1
            k += 1

        while i <= mid:
            temp[k] = a[i]
            i += 1
            k += 1

        for i in range(k):
            a[first + i] = temp[i]

    def marge(self, a, first, last, temp):
        if first < last:
            mid = (first + last) // 2
            self.marge(a, first, mid, temp)  # 左边排序
            self.marge(a, mid + 1, last, temp)  # 右边排序
            self.mergeSort(a, first, mid, last, temp)  # 整体排序

    def sort(self, a):
        temp = [i for i in range(len(a))]
        self.marge(a, 0, len(a) - 1, temp)


# 快速排序
def quickSort(a, left, right):
    if left > right:
        return
    base = left
    pointL = left  # 左游标
    pointR = right  # 右游标
    while pointL < pointR:
        while a[pointR] >= a[base] and pointR > pointL:
            pointR -= 1
        while a[pointL] <= a[base] and pointR > pointL:
            pointL += 1
        a[pointL], a[pointR] = a[pointR], a[pointL]

    a[base], a[pointR] = a[pointR], a[base]
    quickSort(a, left, pointR - 1)  # 左边排序
    quickSort(a, pointR + 1, right)  # 右边排序


# 堆排序
class HeapSortUtil(object):
    def builtHeap(self, a):  # 建立堆
        for i,val in enumerate(a):


num = [1, 5, 3, 6, 5, 4, 7, 8, 9, 2]
num1 = [1, 23, 54, 5, 21, 51, 41, 23, 15, 47]
num2 = [5, 4, 3, 2, 1]
quickSort(num, 0, len(num) - 1)
print(num)
chooseSort(num1)
chooseSort(num2)
# mergeSort(num1,num2)
