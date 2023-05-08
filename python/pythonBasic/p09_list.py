#!/usr/bin/env python

numbers=[0,1,2,3]
names=['kim','lee','park','choi']
print(numbers[0])
print(names[2:])
print(numbers[-1])
print(numbers+names)

names.append('moon')
print((names))


empty=[]

print(empty)

names.insert(1, 'moon')
print((names))

del names[1]
print(names)

names.remove('moon')
print(names)

value=names.pop()
print(value)

value=names.pop(2)
print(value)

numbers.extend([4,5,6,4,4,5,6])
print(numbers)

print(numbers.count(4))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.clear()
print(numbers)





