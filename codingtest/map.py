# 일반 데이터의 개수 입력
n = int(input("값을 입력하세요: "))
print(n)

# 공백으로 구분된 데이터 받기
m, k, b = map(int, input("값 세개를 입력하세요: ").split())
print(m,k,b)


# 여러개의 데이터 공백으로 구분하여 받아 리스트 만들기
data = list(map(int, input("여러개의 데이터를 입력하세요: ").split()))
        
# 데이터 정렬하여 출력하기
data.sort()
print(data)
# 역배열
data.sort(reverse = True)
print(data)

