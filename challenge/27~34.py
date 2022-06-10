''' 수학 함수 '''
import math

# 027. 사용자에게 소수점 이하 자릿수가 많은 숫자를 입력하도록 요청. 이 숫자에 2를 곱한 결과 출력
floatnumber = float(input("소수점 이하 자릿수가 많은 숫자를 입력하세요: "))
print(floatnumber * 2)

# 028. 027번 프로그램을 업데이트하여 소수점 둘째 자리까지 출력.
print("27번 수의 소수점 둘 째 자리까지 출력됩니다.: ", round(floatnumber*2 ,2))

# 029. 사용자에게 500 이상의 정수를 입력하라고 요청한다. 입력받은 숫자의 제곱근을 구하고 소수점 둘째 자리까지 출력하라.
fivehundred = int(input("500 이상의 정수를 입력하세요: "))
sqrt = math.sqrt(fivehundred)
print(round(sqrt, 2))

# 030. 파이값을 소수점 다섯째 자리까지 출력하라.
print(round(math.pi, 5))

# 031. 사용자에게 원의 반지름을 입력하도록 요청한다. 원의 넓이(파이*반지름 제곱)를 계산하여 출력하라.
half = float(input("원의 반지름을 입력하세요: "))
size = math.pi * (half **2)
print(size)

# 032. 원기둥의 반지름과 깊이를 입력하도록 요청한다. 원기둥의 부피(원 넓이 * 깊이)를 구하고 결과를 반올림하여 소수점 셋째 자리까지 출력하라. 
halfsize = float(input("원기둥의 반지름을 쓰세요: "))
depth = float(input("원기둥의 깊이를 쓰세요: "))
volume = (math.pi * (halfsize ** 2)) * depth
print(round(volume, 3))

# 033. 사용자로부터 숫자 두 개를 입력받는다. 몫 연산을 사용하여 첫 번째 숫자를 두 번째 숫자로 나누고 나머지도 계산하여 사용자가 읽을 수 있는 문장으로 결과를 출력. 예를 들어 7과2를 입력했다면 7 divided by 2 is 3 with 1 remaining 이라고 출력하자.
number1 = int(input("숫자1을 입력하세요: "))
number2 = int(input("숫자2를 입력하세요: "))
divided = number1 // number2
remaining = number1 % number2
print(number1, "divided by", number2, "is", divided, "with", remaining, "remaining!") 

# 034. 다음과 같은 메세지를 표시한다. (1) squre (2) triangle  --- enter a number :  만약 사용자가 1을 입력하면 한 면의 길이를 요청하여 사각형의 넓이를 구하여 출력. 만약 2를 입력하면 밑변과 높이를 요청하여 삼각형의 넓이를 구하여 출력하라. 다른 것을 입력하면 적절한 오류 메시지가 출력 되도록 한다. 
message = int(input("(1) squre \n(2) triangle \n\n Enter a number : "))
if message == 1 :
    squre = int(input("한 면의 길이를 적어주세요: "))
    squre = squre ** 2
    print(squre)

elif message == 2 :    
    base = int(input("밑변의 길이를 적어주세요: "))
    height = int(input("높이를 적어주세요: "))
    triangle = (base * height) / 2
    print(triangle)
else :
    print("wrong!")    
    