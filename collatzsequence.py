print("name:Yashaswini R \N USN:1AY24AI116\n sec:O")
def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

if _name_ == "_main_":
    try:
        num = int(input("Enter a positive integer: "))
        if num < 1:
            raise ValueError("Number must be positive.")
        print("Collatz sequence:", collatz(num))
    except ValueError as e:
        print("Error:", e)
