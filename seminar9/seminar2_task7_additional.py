num = '54.31'.split('.')
result = 0

for digit in num[0] + num[1]:
    result += int(digit)

print(result)
