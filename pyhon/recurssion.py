def show(n):
    if n == 0:
        return 0
    else:
        return n + show(n - 1)

print(show(3))  # 6
print(show(4))  # 10
print(show(5))  # 15
print(show(6))  # 21
