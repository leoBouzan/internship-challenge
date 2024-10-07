def is_fibonacci(n):
    sequence = [0, 1]
    if n in sequence: 
        return f"{n} é um número de Fibonacci \nSequência de Fibonacci: {sequence}"
    value = 0

    while value <= n:
        value = sequence[-1] + sequence[-2]
        sequence.append(value)
        if n in sequence: return f"{n} é um número de Fibonacci \nSequência de Fibonacci: {sequence}"

    return f"{n} não é um número de Fibonacci \nSequência de Fibonacci: {sequence}"

while True:
    try:
        n = int(input("Insira um número: "))
        print(is_fibonacci(n))
        break

    except ValueError:
        print("Insira apenas números inteiros")

