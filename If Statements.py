x = input("First number: ")
y = input("Second number: ")

x = int(x)
y = int(y)

if x <y:
    print("x is less than y!")
elif x>y:
    print("x is greater than y!")
    if x > 100:
        print("x is greater than 100")
else:
    print("x is equal to y!")

