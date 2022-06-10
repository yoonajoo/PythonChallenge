# 99. 1이 될 때까지

n, k = map(int, input("n의 값과 k의 값을 입력하시오: ").split())

result = 0 
   

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1

    n = n // k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)