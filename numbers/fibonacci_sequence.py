#coding: utf-8
"""
ref: http://www.mathsisfun.com/numbers/fibonacci-sequence.html
"""
MAX = 50
sequence = [0, 1]

while len(sequence) <= MAX:
    sequence.append(sequence[-1] + sequence[-2])

print sequence
