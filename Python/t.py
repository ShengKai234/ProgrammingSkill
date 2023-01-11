x = -123
res = 0
isNegaticve = false
if x < 0:
    x = -123 * -1
print('test')
while x > 0:
    tmp = x % 10
    x = x // 10
    res = res * 10 + tmp


print(res)