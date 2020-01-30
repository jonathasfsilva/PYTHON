n = input()
while n:
    if 0 <= int(n) <= 100:
        if int(n) >= 1:
            print("vai ter duas!")
        if int(n) == 0:
            print("vai ter copa!")
    n = input()