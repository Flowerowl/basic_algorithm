# encoding: utf-8
"""
time:
    build_heap O(n)
    heapify(lgn)
    avg O(nlgn)
"""
import random

def heapify(heap, size, root):
    left = 2 * root + 1
    right = left + 1
    tmp = root

    if left < size and heap[tmp] < heap[left]:
        tmp = left
    if right < size and heap[tmp] < heap[right]:
        tmp = right
    if tmp != root:
        heap[tmp], heap[root] = heap[root], heap[tmp]
        heapify(heap, size, tmp)


def heap_sort(heap):
    size = len(heap)
    for i in xrange((size-2)//2, -1, -1):
        heapify(heap, size, i)

    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapify(heap, i, 0)
    return heap

if __name__ == '__main__':
    lst = [random.randint(1, 100) for i in range(20)]
    print lst
    heap_sort(lst)
    print lst
