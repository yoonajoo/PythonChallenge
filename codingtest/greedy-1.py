# 92: 큰 수의 법칙


n, m, k = map(int, input("n, m, k 값을 공백을 포함하여 입력하세요: ").split())

data = list(map(int, input("K개의 자연수를 공백을 포함하여 입력하세요: ").split()))

data.sort()
print(data)

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        else: 
            result += first
            m -= 1
        
    if m == 0:
        break
    else: 
        result += second
        m -= 1
        
print(result)


