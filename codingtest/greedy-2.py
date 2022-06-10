# 96. 숫자 카드 게임

n,m = map(int, input("n은 행, m은 열: ").split())

result = 0

for i in range(n):
    data = list(map(int, input("값을 적어주세요: ").split()))
    min_value = min(data)
    
    result = max(result, min_value)

print(result)

 