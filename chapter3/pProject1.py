def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

try:
    inp = int(input("Type an integer: "))

    while True:
        inp = collatz(inp)
        if inp == 1:
            break
        else:
            continue

except ValueError:
    print("You must type an integer.")
