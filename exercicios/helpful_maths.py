def xenia_count(s):
    numbers = s.split('+')
    numbers.sort()
    return '+'.join(numbers)

s = input()
print(xenia_count(s))
