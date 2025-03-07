# Prog08: Print count of odd numbers
odds = 0
for _ in range(10):
    if int(float(input("Enter a number: "))) % 2 != 0:
        odds += 1
print(odds)