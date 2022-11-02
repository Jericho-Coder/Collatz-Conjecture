from rich import *

global raw
global numbers
numbers = []

raw = open("raw.txt", "a")

def solve():
    steps = int(0)
    num = int(input('Input a Positive Integer: '))
    while num != 1:
        numbers.append(num)
        if num % 2 == 0:
            num = int(num / 2)
            print("[red]" + str(num) + " Number is Odd ")
            steps = steps + 1
        else:
            num = int(3 * num + 1)
            print("[green]" + str(num) + " Number is Even")
            steps = steps + 1
    else:
        numbers.append(num)
        print('Finished! Problem Took ' + str(steps) + " Steps.")

solve()

numbers.reverse()
print(numbers)

def plot():
    steps = 0
    for value in numbers:
        raw.write("(" + str(value) + "," + str(steps) + "),")
        steps = steps + 1

plot()
raw.write("\n")
raw.close() 