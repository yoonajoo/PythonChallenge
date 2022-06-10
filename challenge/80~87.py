''' 다양한 문자열 처리 '''

# 080. 사용자에게 이름을 입력하라고 요청하고 입력된 이름의 길이를 출력한다. 그런 다음, 성을 입력 하라고 요청하고 성의 길이를 출 력한다. 성과 이름 사이에 공백 하나를 두어 결합하고 그 결과를 출력한다. 마지막으로 공백을 포함한 전체 이름의 길이를 출력하라.
name = input("이름을 입력하세요: ")
print(len(name))
lastname = input("성은 입력하세요: ")
print(len(lastname))
fullname = name + " " + lastname
print(fullname)
print("공백을 포함한 전체 이름의 길이: ", len(fullname))

# 081. 가장 좋아하는 과목 이름을 입력받고 각 문자 뒤에 '-'를 붙여서 출력하라.
subject = input("가장 좋아하는 과목 이름은?: ")
for i in subject :
    print(i, end = "-")

# 082. 시 한 구절을 사용자에게 표시하고 시작 인덱스와 마지막 인덱스 를 입력하도록 요청한다. 입력한 두 값 사이의 문자를 출력하라.
poetry = "rose is red, violet is blue"
print(poetry)
findex = int(input("시작 인덱스를 입력하세요: "))
lindex = int(input("마지막 인덱스를 입력하세요: "))
print(poetry[findex:lindex])

#  *** 083. 사용자에게 대문자로 메시지를 입력하라고 요청한다. 만약 메시지에 소문자가 있다면 모두 대문자로 입력할 때까지 계속해서 다시 입력하라고 요청한다.
uppermsg = input("대문자로 메세지를 입력하세요: ")
wrong = True
while wrong == True :
    if uppermsg.isupper() :
        print("끝!")
        wrong = False
    else :
        uppermsg = input("대문자로 메세지를 다시 입력하세요: ")

# 084. 사용자에게 영어 단어를 입력하라고 요청한다. 처음 두개의 문자만 대문자로 출력하라.
word = input("영어 단어를 입력하세요: ")
upper = word[0:2]
print(upper.upper())

# 085.사용자의 이름을 입력하라고 요청한 뒤, 그 이름에 모음이 몇 개인지 출력하라.
name = input("사용자의 이름을 입력하세요: ")
count = 0
name = name.lower()
for i in name :
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
        count = count +1
print("name에는 모음이", count, "개 있습니다." )

# ***(elif) 086. 사용자에게 새로운 비밀번호를 입력하라고 요청하고, 한 번 더 입력하라고 요청한다. 입력한 두 개의 비밀번호 가 일치하면 "Thank you"라고 출력한다. 만약 입력한 문자는 서로 일치하는데 대소문자가 틀리다면 "They must be in the same case"라고 출력한다. 문자가 일치하지 않든다면 "incorrect"메시지를 출력하라.
password = input("새로운 비밀번호를 입력하세요 :")
againpassword = input("한 번 더 새로운 비밀번호를 입력하세요 :")
if password == againpassword :
    print("thank you!")
elif password.upper() == againpassword.upper() :
    print("They must be in the same case")
else :
    print("incorrect")        
    
# *** 087. 단어를 입력하라고 요청한 뒤, 그 단어의 문자를 한 줄 에 하나씩 거꾸로 출력하라. 예를 들어서 'hello라고 입력했다면 다음과 같이 출력되어야 한다. Enter a word: hello ---- olleh >>> 
word = input("단어를 입력하세요: ")
wordlen = len(word)
num = 1
for i in word :
    decreaseword = wordlen - num
    print(word[decreaseword])
    num = num + 1