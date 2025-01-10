def kv(n):
    if n == 1:
        return 1 
    else:
        return n + n + kv (n - 1)

print(kv(3))