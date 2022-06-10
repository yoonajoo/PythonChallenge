# 92. 큰 수의 법칙

n, m, k = map(int, input("n, m, k를 공백 있게 입력하시오: ").split())
data = list(map(int, input("리스트를 작성하시오: ").split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        else: 
            result = result + first
            m = m - 1
    
    if m == 0:
        break
    else:
        result = result + second
        m = m - 1
        
print(result)