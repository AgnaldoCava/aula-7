def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    print(f"El factorial de {num} es {factorial(num)}")
