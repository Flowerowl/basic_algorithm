#encoding:utf-8
"""
1.通过比较数组中相邻的（奇-偶）位置数字对，如果该奇偶对是错误的顺序（第一个大于第二个），则交换。
2.重复1，但针对所有的（偶-奇）位置数字对。
3.重复1，2。
time:
    O(n^2)
"""
origin_list = [1,3,5,2,1,4,6,7,5,4,2,12,4,6,1,5]


def odd_even_sort(lst):
    while True:
        sorted = True
        for i in range(1, len(lst)-1, 2):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                sorted = False
        print 'current >>> %s' % lst
        for i in range(0, len(lst)-1, 2):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                sorted = False
        print 'current >>> %s' % lst
        if sorted:
            break


if __name__ == '__main__':

    print 'origin >>>%s' % origin_list
    odd_even_sort(origin_list)

