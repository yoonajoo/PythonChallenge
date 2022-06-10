
#  001. 사용자의 이름을 입력받아서 출력하기 > Hello[이름]
numname = input("please enter your name: ")
print("Hello", numname)

# 002. 사용자의 이름을 입력받은 다음, 사용자의 성을 입력받아서 출력하기 > Hello[이름] [성]
numfname = input("please enter your first name: ")
numlname = input("please enter your last name: ")
print("Hello", numfname, numlname)

# 003. 농담 표시 후, 다음 줄에 답은표시하는 코드를 한 줄로 만들자
print("joke: wdycabwnt? \nanswer: a gummy bear!")

# 004. 사용자로부터 2개의 숫자를 입력 받아서 더한 결과를 다음과 같이 출력하라 > The total is [결과]
numnumber1 = int(input("a: "))
numnumber2 = int(input("b: "))
numresult = numnumber1 + numnumber2
print("The total is: ", numresult)

# 005. 사용자로부터 3개의 숫자를 입력 받는다. 첫 번째 숫자와 두 번째 숫자를 더한 값에 세 번째 숫자를 곱한 결과를 다음과 같이 출력하라. > The answer is [결과]
num1 = int(input("a: "))
num2 = int(input("b: "))
num3 = int(input("c: "))
result = (num1+num2)*num3
print("The answer is : ", result)

# 006. 처음 가지고 있던 피자 조각 입력받고, 몇 조각 먹었는지 입력받아서 남은 조각 수 계산하여 사람에게 익숙한 형식으로 출력
firstPizza = int(input("처음 가지고 있던 피자 조각은 몇 개?: "))
eatPizza = int(input("그 중 몇 조각 드셨나요?: "))
leftPizza = firstPizza - eatPizza
print("남은 피자 조각수는", leftPizza,"조각 입니다.")

# 007. 사용자로부터 이름과 나이를 입력받아서 나이에 1을 더한 후 출력 > [이름] next birthday you will be [새로운 나이]
yourname = input("당신의 이름은?: ")
yourage = int(input("당신의 나이는?: "))
ageplus1 = yourage + 1
print(yourname, "next birthday you will be ", ageplus1)

# 008. 계산서의 총 가격과 몇 명이 같이 식사를 했는지 입력받는다. 총 가격을 인원수로 나누고 각 사람이 얼마씩 내야 하는지 출력 (2분10초)
totalPrice = int(input("총 가격은 얼마입니까?: "))
totalPeople = int(input("총 몇 명이 같이 식사를 했죠?: "))
dutchPay = totalPrice / totalPeople
print("각각 내야할 금액은", dutchPay, "원 입니다.")

# 009. 사용자로부터 일수를 입력받아서 그 일수까지 몇 시간 몇 분 몇 초가 남았는지 출력하라
days = int(input("그 날까지 몇 시간 몇 분 몇 초?: "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(days, "일 까지", hours,"시간", minutes,"분", seconds,"초 남았습니다." )

# 010. 1킬로그램은 2.204 파운드다. 몸무게를 킬로그램 단위로 입력받아서 파운드로 변환하여 출력하라. (1분46초)
peopleKg = int(input("몇 키로세요?: "))
pound = peopleKg * 2.204
print("파운드로 계산하면 당신의 무게는: ", pound) 

# 011. 사용자로부터 100이 넘는 숫자를 입력받고 10미만의 숫자 하나를 입력받은 후 , 작은 숫자가 큰 숫자 안에 몇 번 들어가는지 사용자 친화적인 형식으로 출력하라. (1분 48초) // 사용!!
larger = int(input("100이 넘는 숫자를 입력하세요: "))
smaller = int(input("10미만의 숫자를 입력하세요: "))
answer = larger // smaller
print(smaller, "은", larger, "안에", answer, "번 들어갑니다.")