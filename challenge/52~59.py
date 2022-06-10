''' 랜덤 '''

import random

# 052. 1부터 100포함 사이의 임의의 정수를 출력하라
num = random.randint(1, 100)
print("1부터 100 포함 사이의 임의의 정수는: ",num)

# 053. 다섯 개의 과일 이름들의 목록에서 임의의 과일을 출력하라.
fruit = random.choice(["사과", "포도", "라임", "바나나", "체리"])
print("다섯 개의 과일 이름들의 목록에서 임의의 과일은: ", fruit)

# 054. 앞면과 뒷면(h 그리고 t) 중 임의로 선택한다. 사용자에게 어떤 것을 고를지를 요청한다. 만약 사용자의 선택과 임의로 선택한 값이 서로 같으면 "you win" 메시지를 출력하고, 그렇지 않다면 "bad luck"메시지를 출력하라. 마지막에 컴퓨터가 선택한 것이 무엇인지를 사용자에게 알려줘라.
frontbehind = random.choice(["h", "t"])
userchoice = input("h와 t중 어떤걸 선택하실래요?: ")
if userchoice == frontbehind :
    print("You win!")
else :
    print("Bad luck!")
print("컴퓨터가 선택한 값은...", frontbehind, "입니다.")    
    
# 055. 1과 5사이의 숫자를 임의로 선택한다. 사용자에게 숫자를 선택하라고 요청한다. 입력한 값이 맞으면 "well done" 메시지를 출력하고, 그렇지 않으면 선택한 숫자가 너무 높은지 아니면 너무 낮은지를 알려주고 다시 숫자를 입력하라고 한다. 다시 입력한 숫자가 맞으면 "correct"라고 출력하고, 그렇지 않다면 "you lose" 라고 출력하라. 
number = random.randint(1, 5)
user = int(input("1~5 사이의 수를 입력하세요: "))
if user == number : 
    print("well done")
elif user < number :
    print("too low")
    user = int(input("1~5 사이의 수를 다시 입력하세요: "))
    if user == number :
        print("correct!")
    else :
        print("you lose")
elif user > number :
    print("too high")
    user = int(input("1~5 사이의 수를 다시 입력하세요: "))
    if user == number :
        print("correct!")
    else :
        print("you lose")

# 056. 1과 10사이의 정수를 임의로 선택한다. 사용자에게 숫자를 입력하라고 요청하고 임의로 선택한 숫자를 입력할 때까지 계속 숫자를 입력하게 하라.
num = random.randint(1, 10)
user = int(input("숫자를 입력하세요: "))
while user != num :
    user = int(input("숫자를 다시 입력하세요: "))
print("정답!")

    
# 057. 056번 프로그램을 업데이트하여 사용자가 입력한 숫자가 큰지 작은지를 알려주고 다시 숫자를 고르게 하라.
num = random.randint(1, 10)
user = int(input("숫자를 입력하세요: "))
while user != num :
    if user < num :
        print("숫자가 작습니다")
    else :
       print("숫자가 큽니다.")
    user = int(input("숫자를 다시 입력하세요: "))
print("정답!")

# 058. 임의로 생성된 두 개의 정수를 더하는 다섯 개의 질문 (즉 숫자1 + 숫자2)이 나오는 수학 퀴즈를 만들자. 사용자에게 답을 입력하라고 요청하고 정답을 맞히면 점수를 증가하라. 퀴즈가 끝나면 다섯 문제 중에 몇 개를 맞혔는지 출력하라.
score = 0
for i in range(1,6) :
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    question = num1 + num2
    print(num1, "+", num2, "= ?")
    answer = int(input("정답은: "))
    
    if answer == question :
        score = score + 1
print("다섯 문제 중에", score, "개 맞았습니다!")

# 059. 다섯 개의 색상을 표시하고 그들 중 하나를 사용자에게 선택하라고 요청 한다. 만약 프로그램이 선택한 것과 동일하면 "Well done"이라고 출력하고, 그렇지 않다면 컴퓨터가 선택한 색상이 포함된 위트 있는문장을 출력하라. 다시 맞혀 보라고 사용자에게 색상을 입력하라고 한다. 사용자가 맞힐 때까지 이 작업을 반복한다. 
color = random.choice(["검정", "노랑", "빨강", "초록", "파랑"])
choice = input("색을 하나 선택하세요: ")
while choice != color :
    print("no way!")
    choice = input("색을 다시 선택하세요: ")
print("well done!")    
