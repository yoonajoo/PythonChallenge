''' for 루프 '''

# 035. 사용자의 이름을 입력하라고 요청한 뒤, 그 이름을 세 번 출력하라.
name = input("what is your name?: ")
for i in range(0,3) :
    print(name)

# 036. 035번 프로그램을 수정하여 사용자가 이름과 숫자를 입력하게 하여 이름을 입력한 숫자만큼 출력하라
name = input("what is your name?: ")
number = int(input("what is number?: "))
for i in range(0, number) :
    print(name)

# 037. 사용자의 이름을 입력하라고 요청하고, 그 이름의 각 문자를 한 줄에 하나씩 출력하라.
yourname = input("what is your name?: ")
for i in yourname :
    print(i)

# 038. 037번 프로그램을 수정하여 숫자도 입력하도록 요청하자. 이름의 각 문자를 한 줄에 하나씩 출력하는 작업을 입력한 숫자만큼 반복하라
yourname = input("what is your name?: ")
yournumber = int(input("what is number?: "))        
for p in range(0, yournumber) :
    for i in yourname :
        print(i)
 
# 039. 1부터 12사이의 값을 입력하도록 요청한 뒤, 그 숫자에 대해 12까지의 곱셈표를 출력하라.
number = int(input("what is number?: "))
for i in range(1,13) :
    answer = number * i
    print(answer)
 

# 040. 50 미만의 숫자를 입력하도록 요청한다. 50부터 입력한 숫자까지 카운트 다운하면서 숫자를 출력하되, 입력한 숫자까지 출력되로록 하라.
fifnum = int(input("50 미만 숫자 입력: "))
for i in range(50, fifnum -1, -1) :
    print(i)
    
# 041. 이름과 숫자를 입력하도록 요청한다. 입력한 숫자가 10미만이면 입력한 숫자만큼 이름을 출력하고, 10이상이면 "too high"를 세번 출력하라.
username = input("what is your name?: ")
usernumber = int(input("what is number?: "))
if usernumber < 10 :
    for i in range(0, usernumber) :
        print(username)
else :
    for i in range(0,3) :
        print("too high")

# 042. total이라는 이름의 변수에 0을 설정하고 숫자를 입력하라는 요청을 다섯 번 반복한다. 숫자를 입력할 때마다 입력한 값을 total에 더할 것인지를 묻는다. 더하길 원한다는 답을 하면 total에 그 값을 더하고, 그렇지 않다면 더하지 않는다. 다섯개의 숫자가 모두 입력되면 total을 출력하라
total = 0
for i in range(0,5) :
    num = int(input("숫자를 입력해주세요: "))
    toq = input("입력한 값을 total에 더할까요?: ")
    if toq == "y" :
        total = total + num
    else : 
        pass
print(total)
        
# 043. 사용자에게 원하는 카운트 방향(카운트 다운 또는 카운트 업)을 묻는다. 만약 업을 선택하면 가장 큰 숫자를 묻고, 1부터 그 숫자까지 출력하라. 다운을 선택하면 20미만의 숫자를 요청하고 20부터 그 숫자까지 출력하라. 업 또는 다운이 아닌 다른 것을 선택하면 "아이 돈 언더스탠드"를 출력하라.
count = input("카운트 업? 다운?: ")
if count == "업" :
    upnum = int(input("업하고 싶은 수 쓰세요: "))
    for i in range(1, upnum + 1) :
        print(i)
elif count == "다운" :
    downnum = int(input("20미만의 수 쓰세요: "))
    for i in range(20, downnum-1, -1) :
        print(i)
else : print("아이 돈 언더스탠드")

# 044. 파티에 몇 명을 초대하고 싶은지 묻는다. 만약 10미만을 입력하면 이름을 묻고 "[이름] has been invited"라고 출력하는 것을 입력한 숫자만큼 반복하라. 10이상을 입력하면 "too many people" 이라는 메시지를 출력하라.
party = int(input("몇 명 초대하고싶어?: "))
if party < 10 :
    for i in range(0, party) :
        name = input("이름이 뭐야?: ")
        print(name, "has been invited")
else :
    print("too many people")
    