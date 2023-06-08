def find_two_numbers(A, B):
    return max(A), max(B)

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

a, b = find_two_numbers(A, B)
print(a, b)
