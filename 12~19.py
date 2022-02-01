''' if문 '''

# 012. 두 개의 숫자를 입력받는다. 만약 첫 번째 숫자가 두 번째 숫자보다 크면, 두 번째 숫자를 먼저 출력한 다음에 첫 번째 숫자를 출력하라. 그렇지 않다면 첫 번째 숫자를 출력한 다음에 두 번째 숫자를 출력하라.
number1 = int(input("첫번째 숫자를 입력하세요: "))
number2 = int(input("두번째 숫자를 입력하세요: "))
if number1 > number2 :
    print(number2, number1)
else : print(number1, number2)

# 013. 사용자에게 20보다 작은 숫자를 입력하라고 요청한다. 만약 입력된 값이 20과 같거나 크면 "Too high"라는 메세지를 출력하라. 그렇지 않다면 "Thank you"를 출력하라.
lessTwenty = int(input("20보다 작은 숫자를 입력하세요: "))
if lessTwenty >= 20 :
    print("Too high")
else : print("Thank you")    

# 014. 사용자에게 10과 20(포함) 사이의 숫자를 입력하라고 요청한다. 만약 입력한 값이 이 범위 안의 숫자이면 "Thank you"라는 메시지를 출력하라. 그렇지 않다면 "Incorrect answer"라는 메시지를 출력하라. 
number = int(input("10과 20포함 사이의 숫자를 입력하세요: "))
if 20 >= number > 9 : 
    print("Thank you")
else : print("Incorrect answer")

# 015. 사용자에게 좋아하는 색을 입력하라고 요청한다. 만약 "red" 나 "RED" 또는 "Red"를 입력하면 "I like red too" 라는 메시지를 출력하라. 그렇지 않다면 "I don't like that color, I prefer red" 라는 메시지를 출력하라.
color = input("what is your favorite color?: ")
if color == "red" or color == "RED" or color == "Red" : 
    print("I like red too")
else : 
    print("I don't like that color, I prefer red")    

# 016. 비가 오는지 묻고, 그 대답을 소문자로 변환하여 대소문자에 상관없도록 한다. 만약 "yes"라고 입력한다면 바람이 부는지 묻는다. 두번째 질문에 대해 "yes"라고 입력하면 "It is too windy for an umbrella"라는 메시지를 표시하라. 그렇지 않다면 "Take an umbrella" 라는 메시지를 표시하라. 만약 첫 번째 질문에 대해 "yes" 라고 입력하지 않는다면 "Enjoy your day"라는 메시지를 표시하라.
raining = input("오늘 비 와?: ")
raining = str.lower(raining)
if raining == "yes" :
    windy = input("바람 불어?: ")
    windy = str.lower(windy)
    if windy == "yes" :
        print("It is too windy for an umbrella")
    else : print("Take an umbrella")    
else : print("Enjoy your day")       

# 017. 사용자의 나이를 묻자. 만약 18세 이상이면 "you can vote"라는 메시지를 표시하라. 만약 17세라면 "you can learn to drive"라는 메시지를 표시하라. 만약 16세라면 "ycbalt" 라는 메시지를 표시하라. 만약 16세 미만이라면 "ycgtot"이라는 메시지를 표시하라.
age = int(input("나이가 어떻게 되세요?: "))
if age >= 18 :
    print("유 캔 보트")
elif age == 17 :
    print("you can learn to drive")
elif age == 16 :
    print("ycbalt")
else :
    print("ycgtot")
    

# 018. 사용자에게 숫자를 입력하라고 요청. 만약 10미만이면 "too low"라는 메시지 표기. 만약 입력한 숫자가 10에서 20 사이라면 "correct" 라고 표시. 그렇지 않다면 "too high"라고 표시.
num = int(input("숫자 입력: "))
if num < 10 : 
    print("too low")
elif 10 <= num < 20 :
    print("correct") 
else : print("too high")

# 019. 사용자에게 1이나 2 또는 3을 입력하라고 하자. 만약 1을 이력하면 "ty" 라는 메시지를 표시. 만약 2를 입력하면 "well done" 표시. 만약 3을 입력하면 "correct " 표시. 만약 사용자가 다른 것을 입력하면 "Eorror message" 표시. 
ott = int(input("1,2,3 중 입력: "))
if ott == "1" :
    print("ty")
elif ott == "2" :
    print("well done")
elif ott == "3" :
    print("correct")
else :
    print("Eorror message")