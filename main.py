def solve():
    steps = int(0)
    num = int(input('Input a Positive Integer: '))
    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
            print(str(num) + " Number is Odd ")
            steps = steps + 1
        else:
            num = int(3 * num + 1)
            print(str(num) + " Number is Even")
            steps = steps + 1
    else:
        print('Finished! Problem Took ' + str(steps) + " Steps")
    solve()

solve()
