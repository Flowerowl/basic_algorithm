#encoding:utf-8
"""
鸡尾酒排序，也就是定向冒泡排序, 鸡尾酒搅拌排序, 搅拌排序 (也可以视作选择排序的一种变形),
    涟漪排序, 来回排序 or 快乐小时排序, 是冒泡排序的一种变形。
    此算法与冒泡排序的不同处在于排序时是以双向在序列中进行排序。
time:
    worst O(n^2)
    best O(n)
    avg O(n^2)
"""
origin_list = [2,6,2,1,5,8,9,5,2,1,8,0,9,7,5,2,1]


def bubble_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        swap = False
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
                swap = True

        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swap=True

        print 'current >>>%s' % lst
        if not swap:
            return lst


if __name__ == '__main__':
    print 'origin >>>%s' % origin_list
    bubble_sort(origin_list)
