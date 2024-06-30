def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Penggunaan fungsi
jumlah = 10
print(f"Deret Fibonacci hingga {jumlah} bilangan pertama:")
fibonacci(jumlah)
