''' 튜플과 리스트 그리고 딕셔너리 '''

# 069. 다섯 개의 국가 이름을 담고 있는 튜플()을 만들고 튜플 전체를 출력하라. 표시된 국가 이름들 중 하나를 입력하라고 사용자에게 요청하고, 입력된 국가 이름의 인덱스 번호(즉, 목록에서의 위치)를 출력하라
fivecountry = ("KOREA", "DENMARK", "NETHERLANDS", "BELGIUM", "JAPAN")
print(fivecountry)
choose = input("국가 중 하나를 선택하세요: ")
choose = choose.upper() 
print(choose, fivecountry.index(choose))

# 070. 사용자에게 숫자를 입력하라고 요청하고, 입력한 위치의 국가 이름이 출력되는 기능을 069번 프로그램에 추가하라.
fivecountry = ("KOREA", "DENMARK", "NETHERLANDS", "BELGIUM", "JAPAN")
print(fivecountry)
choose = input("국가 중 하나를 선택하세요: ")
choose = choose.upper() 
print(choose, fivecountry.index(choose))
num = int(input("숫자를 입력하세요: "))
print(fivecountry[num])

# 071. 두 개의 스포츠 이름을 담고 있는 리스트를 생성 하라. 사용자에게 좋아하는 스포츠가 무엇인지 물어보고 그것을 리스트 끝에 추가하라. 리스트를 정렬하고 출력하라.
sport_list = ["soccer", "baseball"]
sport_list.append(input("좋아하는 스포츠를 쓰세요: "))
sport_list.sort()
print(sport_list)

# 072. 교과목 여섯 개가 담긴 리스트를 생성하라. 이들 중 사용자가 좋아하지 않는 과목을 묻고 그 과목을 리스트에서 삭제한 후에 리스트를 다시 출력하라.
subject = ["수학", "영어", "체육", "도덕", "미술", "과학"]
print(subject)
hatesubject = input("싫어하는 과목이 뭔가요?: ")
subject.remove(hatesubject)
print(subject)

# *** 073. 사용자에게 좋아하는 음식 네 개를 입력하도록 요청하고 그것들은 인덱스 번호 1부터 시작하는 딕셔너리에 저장한 다. 인덱스 번호와 항목이 모두 표시되도록 딕셔너리를 출력한다. 사용자에게 제거하고 싶은 항목을 묻고 그것을 제거한다. 남아있는 데이터를 정렬하고 딕셔너리를 다시 출력하라.
fourfood = {}
food1 = input("좋아하는 음식1 이름을 입력하세요: ")
fourfood[1] = food1
food2 = input("좋아하는 음식2 이름을 입력하세요: ")
fourfood[2] = food2
food3 = input("좋아하는 음식3 이름을 입력하세요: ")
fourfood[3] = food3
food4 = input("좋아하는 음식4 이름을 입력하세요: ")
fourfood[4] = food4
print(fourfood)
wantdel = int(input("제거하고 싶은 항목은?: "))
del fourfood[wantdel]               #del key값
print(sorted(fourfood.values()))    # ***

# 074. 열 개의 색상이 담긴 리스트를 생성한다. 사용자에게 0에서 4 사이의 시작 번호와 5에서 9 사이의 끝 번호를 입력하라고 요청하고, 입력된 시작 번호부터 끝 번호까지의 색상을 출력하라.
color = ["빨강", "검정", "파랑", "하늘", "노랑", "흰색", "초록", "보라", "연두", "주황"]
choose04 = int(input("0~4사이의 시작 번호를 입력하세요: "))
choose59 = int(input("5~9사이의 시작 번호를 입력하세요: "))
print(color[choose04:choose59])

# 075. 세 자리 숫자 네 개가 담긴 리스트 를 생성한다. 리스트의 각 항목을 한 줄에 하나씩 출력하여 사용자 에게 표시한다. 사용자에게 세 자 리의 숫자를 입력하라고 요청한다. 만약 입력한 숫자가 리스트에 있는 숫자들 중 하나라면 리스트에 그 숫자가 위치한 인덱스를 출력하라. 그렇지 않다면 "that is not in the list" 라는 메세지를 출력하라.
number_list = [333,567,234,979]
for i in number_list :
    print(i)
user = int(input("세 자리 수를 적으세요: "))
if user in number_list :            # if...in 리스트
    print(number_list.index(user))
else :
    print("that is not in the list")
    
# 076. *** 사용자에게 파티에 초대할 사람 3명의 이름을 입력하라고 요청하고 리스트에 저장한다. 모든 이름이 입력되면 추가할 사람이 있는지 묻는다. 만약 그렇다면 "n"이라고 답할 때까지 이름을 추가하게 한다. "n"이라고 입력하면 파티에 초대한 사람이 몇 명인지 표시하라.
name1 = input("초대할 사람 이름 적어: ")
name2 = input("초대할 사람 이름 적어: ")
name3 = input("초대할 사람 이름 적어: ")
inviteparty = [name1, name2, name3]
more = input("더 초대할 사람 있어?(y/n): ")
while more == "y" :         # 왜 "y"인지 기억하기
    name = inviteparty.append(input("초대할 사람 이름 또 적어: "))
    more = input("더 초대할 사람 있어?(y/n): ")
print(len(inviteparty))

# 077. 076번 프로그램을 수정하여 초대할 사람들의 이름이 리스트에 모두 추가되면 전체 명단을 출력하고 리스트에 있는 이름들 중 하나를 입력하라고 요청한다. 입력된 이름의 위치(인덱스)를 출력하고 그 사람을 정말로 파티에 초대할 것인지를 묻는다. 만약 "n"라고 답하면 그 항목을 리스트에서 삭제하고 리스트를 다시 출력한다. 
name1 = input("초대할 사람 이름 적어: ")
name2 = input("초대할 사람 이름 적어: ")
name3 = input("초대할 사람 이름 적어: ")
inviteparty = [name1, name2, name3]
more = input("더 초대할 사람 있어?(y/n): ")
while more == "y" :
    name = inviteparty.append(input("초대할 사람 이름 또 적어: "))
    more = input("더 초대할 사람 있어?(y/n): ")
print(inviteparty)

choose = input("이름 중 하나를 입력하세요: ")
x = inviteparty.index(choose)
print(x)
really = input("이 사람을 정말로 초대할 것인가요?(y/n): ")
if really == "n" :
    del inviteparty[x]
    print(inviteparty)
else : pass

# if really == "n" :
#     inviteparty.remove(choose)
# print(inviteparty)
    
# 078. 네 개의 TV 프로그램 타이틀을 담은 리스트를 생성하고 각 항목을 한 줄씩 출력한다. 사용자 에게 다른 프로그램을 입력하도록 요청하고 리 스트에서의 원하는 위치를 묻는다. 입력한 프로그램 타이틀을 원하는 위치에 삽입하고 다섯 개의 tv 프로그램 모두를 다시 출력한다.
tvprogram = ["모던패밀리", "렛잇고", "굿와이프", "워킹데드"]
for i in tvprogram :
    print(i)
user = input("다른 프로그램을 입력하세요: ")
inputnumber = int(input("몇 번 위치에 넣기를 원하십니까?: "))
tvprogram.insert(inputnumber, user)
print(tvprogram)

# 079.'nums'라는 이름의 빈 리스트를 생성한다. 사 용자에게 숫자를 입력하라고 요청한다. 숫자가 입력되면 그것을 nums 리스트 끝에 추가하고 리스트를 출력한다. 세 개의 숫자를 입력받으면 마지막 숫자를 저장할 것인지 묻는다. 만약 "n"이라고 답하면 리스트의 마지막 항목을 삭제하고 리스트를 출력하라. 
nums = []
count = 1
while count < 4 :
    number = int(input("숫자를 입력하세요: "))
    nums.append(number)
    print(nums)
    count = count + 1    
lastnum = input("마지막 숫자를 저장하시겠습니까?: ")

if lastnum == "n" :
    # del nums[2]
    nums.remove(number)
    print(nums)