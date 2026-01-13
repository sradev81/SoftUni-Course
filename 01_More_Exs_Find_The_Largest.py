

number = int(input())
stored_digit = []

if number == 0:
    print(0)
    exit()

while number > 0:
    digit = number % 10
    stored_digit.append(digit)
    number = number // 10

stored_digit.sort(reverse=True)

max_number = 0
for digit in stored_digit:
    max_number = max_number * 10 + digit

print(max_number)