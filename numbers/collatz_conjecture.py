#encoding:utf-8
n = 1111101010


while n > 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = n * 3 + 1
    print 'current >>>>', n
