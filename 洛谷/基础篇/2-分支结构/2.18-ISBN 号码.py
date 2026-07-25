isbn = input()

total = (
    int(isbn[0]) * 1
    + int(isbn[2]) * 2
    + int(isbn[3]) * 3
    + int(isbn[4]) * 4
    + int(isbn[6]) * 5
    + int(isbn[7]) * 6
    + int(isbn[8]) * 7
    + int(isbn[9]) * 8
    + int(isbn[10]) * 9
)

code = total % 11

if code == 10:
    correct_code = "X"
else:
    correct_code = str(code)

if isbn[12] == correct_code:
    print("Right")
else:
    print(isbn[:12] + correct_code)