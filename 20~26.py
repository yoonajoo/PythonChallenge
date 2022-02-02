''' 문자열 '''
# 020. 사용자에게 이름을 요청하고 그 이름의 길이 출력
# yourname = input("what is your name?: ")
# // length = len(yourname)
# // print(length)
# print(len(yourname))

# 021. 이름을 묻고 그 다음으로 성을 묻는다. 이름과 성 사이에 공백 하나를 두어 출력하고 공백을 포함한 전체 이름의 길이를 출력하라.
# fname = input("what is your first name?: ")
# lname = input("what is your last name?: ")
# flname = (fname + " " + lname)
# print(flname)
# print(len(flname))

# 022. 사용자에게 이름과 성을 소문자로 입력하라고 요청한다. 각 첫 문자만 대문자로 변경하고 이름과 성 사이에 공백을 하나 두어 결합한 후에 그 결과를 출력하라.
# firstname = input("what is your first name?: ")
# lastname = input("what is your last name?: ")
# firstname = firstname.title()
# lastname = lastname.title()
# entirename = firstname + " " + lastname
# print(entirename)

# 023. 사용자에게 자장가의 첫 줄을 입력하라고 요청. 그 문자열의 길이를 출력. 사용자에게 범위를 시작할 인덱스 번호를 묻고 범위의 끝 인덱스 번호를 묻는다. 그런 후 그 범위의 텍스트를 출력하라. (파이썬에서 인덱스는 1이 아닌 0부터 시작)
# sleepsong = input("자장가의 첫 줄을 입력하세요: ")
# print(len(sleepsong))
# indexfnumber = int(input("범위의 시작 인덱스 번호는?: "))
# indexlnumber = int(input("범위의 끝 인덱스 번호는?: "))
# song = (sleepsong[indexfnumber:indexlnumber])
# print(song)

# 024. 사용자에게 아무 단어나 입력하라고 하고 그것을 대문자로 출력하라
# word = input("아무 영어 단어나 쓰세요: ")
# word = word.upper()
# print(word)

# 025. 사용자에게 이름을 입력하라고 요청. 만약 이름의 길이가 5자 미만이면 성을 입력하라고 요청하고 중간 공백 없이 이름과 성을 결합하고 대문자로 출력. 만약 이름의 길이가 5자 이상이면 이름을 소문자로 출력.
# name = input("what is your name?: ")
# if len(name) < 5 :
#     lstname = input("what is your last name?: ")
#     name = name + lstname
#     print(name.upper())
# else :
#     print(name.lower())    

# 026. 단어의 첫 자음을 가져와서 단어 끝으로 이동하고 마지막에 ay를 추가. 만약 단어가 모음으로 시작한다면 단어의 끝에 그냥 way를 붙인다. 예를 들어 pig 라는 단어는 igpay, banana는 ananabay 그리고 aadvark 는 aadvarkway가 된다. 사용자에게 단어를 입력받아서 변환하고 소문자로 출력하는 프로그램을 만들어봐라.
 