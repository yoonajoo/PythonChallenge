''' while 루프 '''

# 045. total이라는 변수를 0으로 설정한다. total의 값이 50이하이면 사용자에게 숫자를 입력하라고 요청한다. 입력된 숫자를 total에 더하고 "the total is ...[total]"이라는 메세지를 출력한다. total의 값이 50을 넘으면 루프를 멈추는 프로그램을 작성하라.
total = 0
while total <= 50 :
    num = int(input("숫자를 입력하세요: "))
    total = total + num
    print("the total is ...[", total, "]")

# 046. 사용자에게 숫자를 입력하라고 요청한다. 입력한 값이 5를 넘을 때까지 숫자를 입력하라고 요청하며, 5를 넘으면 "the last number you entered was a [숫자]"를 출력하고 프로그램을 종료하라.
num = 0
while num < 5 :
    num = int(input("숫자를 입력하세요: "))
    print("the last number you entered was a [", num, "]")
                 
# 047. 사용자에게 숫자를 입력하라고 요청한 다음에 다른 숫자를 입력하라고 요청. 두 숫자들을 더한 뒤, 또 다른 숫자를 더하고 싶은지 묻고 "y" 라고 입력하면 다른 숫자를 입력받아 더하고 다시 같은 질문을 한다. "y"가 아닌 답을 하면 루프를 종료하고 총합을 출력하라.
num = int(input("숫자를 입력하세요: "))
answer = num
thenum = "y"
while thenum == "y" :
    annum = int(input("다른 숫자를 입력하세요: "))
    answer = answer + annum
    thenum = input("또 다른 숫자를 더하고 싶으세요?: ")
print("총합은: ", answer)    
 
# 048. 사용자가 파티에 초대하고 싶은 사람의 이름을 입력하라고 요청한다. 그 다음에, "[이름] has now been invited"라는 메시지를 출력하고 카운트에 1을 더한다. 다른 사람을 더 초대하고 싶은지를 묻고 더 이상 파티에 초대하고 싶은 사람이 없을 때까지 반복한다. 초대하고 싶은 사람이 없다면 몇 명이 파티에 참석하는지를 표시하라.
count = 0
party = "y"
while party == "y" :
    name = input("파티에 초대할 사람 이름 적으세요: ")
    invite = print(name, "has now been invited")
    count = count + 1  
    party = input("더 초대하고 싶은 사람이 있나요? :")
   
print(count, "명이 초대 되었습니다!")
    
# 049. compnum 이라는 이름의 변수를 생성하고 50을 설정한다. 사용자에게 숫자를 입력하라고 요청하고 입력한 값이 compnum과 동일하지 않다면 입력한 값이 높은지 낮은지를 알려주고 다시 맞춰보라고 묻는다. 만약 값이 일치하면 "well done, you took[카운트] attempts"라는 메시지를 출력하라.
compnum = 50
count = 1
num = int(input("숫자를 입력하세요: "))

while num != compnum :
    if num < compnum :
        print("업!")         
    else :
        print("다운!")
    count = count +1
    num = int(input("숫자를 다시 입력하세요"))
print("well done, you took", count, "attempts")

# 050. 사용자에게 10과 20사이의 숫자를 입력하라고 요청한다. 입력한 숫자가 10이하이면 "too low"라는 메시지를 출력하고 다시 입력하라고 요청한다. 만약 20이상이면 "too high"라는 메시지를 출력하고 다시 입력하라고 요청한다. 사용자가 10과 20사이의 값을 입력할 때까지 이 과정을 반복하고 10과 20사이의 값을 입력하면 "thank you"라는 메세지를 출력하라.
num = int(input("10~20사이 숫자를 입력하세요: "))

while num <= 10 or 20 <= num :
    if num <=10 :
       print("too low")
    else :
        print("too high")
    num = int(input("10~20사이 숫자를 다시 입력하세요: "))
print("thank you")

# 051. x