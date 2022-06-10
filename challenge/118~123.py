''' 함수 '''

# 118. 사용자에게 숫자를 입력하라고 요청하고 그 값을 'num'이라는 변수에 저장하는 함수를 정의하라. 그리고 'num'을 사용하여 1부터 num에 저장된 숫자까지 세는 다른 함수를 정의하라.
# def ask_num():
#     num = int(input("숫자를 입력하세요: "))
#     return num

# def count(num):
#     n = 1
#     while n <= num :
#       print(n)
#       n = n + 1 

# def main():
#     num = ask_num()
#     count(num)
    
# main()
    
''' 119. 낮은 숫자와 높은 숫자를 입력하도록 요청하는 함 수를 정의하고, 두 값 사이의 임의의 숫자를 생성 하여 'comp_num'이라는 이름의 변수에 저장한다. 

'I am thinking of a number...'라는 메시지를 출력한 다음, 사용자가 생각하고 있는 숫자를 입 력하라고 요청하는 함수 하나를 더 정의한다.

세 번째 함수는 사용자가 입력한 숫자와 comp_num이 같은지 확인하도록 정의한다. 만약 같다면 'correct, you win'이라는 메시지를 출력하고, 그렇지 않다면 사용자가 입력한 값이 너무 낮은지 아니면 너무 높은지를 알려주고 다시 입력하도록 하며, 숫자를 맞출 때까지 계속 반복되게 한다. '''
# import random

# def low_high():
#     low = int(input("낮은 숫자를 입력하세요: "))
#     high = int(input("높은 숫자를 입력하세요: "))
#     comp_num = random.randint(low, high)
#     print(comp_num)
#     return comp_num

# def think_num():
#     print("I am thinking of a number...")
#     ask_thinking = int(input("사용자가 생각하고 있는 숫자를 입력하세요: "))
#     return ask_thinking

# def check_same(comp_num, ask_thinking):
#     try_again = True
#     while try_again == True:
#         if comp_num == ask_thinking : 
#             print("correct, you win")
#             try_again = False
            
#         elif comp_num > ask_thinking :
#             ask_thinking =  int(input("업!: "))
        
#         else :
#             ask_thinking = int(input("다운!: "))

# def main():
#     comp_num = low_high()
#     ask_thinking = think_num()
#     check_same(comp_num, ask_thinking)
    
# main()

''' 120. 사용자에게 다음의 메뉴를 표시한다. 
    1) addition
    2) subtraction
    Enter 1 or 2 :
    
    사용자가 1을 입력하면 5와 20 사이의 임의의 숫 자 두 개를 생성하고 두 수의 합을 사용자에게 묻는 함수가 실행된다.사용자가 입력한 답과 실 제 정답을 반환한다.
    
    사용자가 메뉴에서 2를 입력하면 25에서 50 사 이의 숫자 하나와 1에서 25 사이의 숫자 하나를 생성하고,첫 번째 숫자에서 두 번째 숫자를 빼면 몇인지를 묻는 함수가 실행된다. 이렇게 하면 음수의 답이 나올 염려는 없어진다. 사용자가 입력한 답과 실 제 정답을 반환한다. 
    
    사용자가 입력한 답과 실제 정답을 확인하는 또 다른 함수를 생성한다. 두 값이 같다면 'Correct' 라고 표시하고, 그렇지 않다면 'Incorrect, the answer is'와 함께 실제 정답을 출력한다.
    
    만일 메뉴에 표시된 번호를 선택하지 않는다면 적절한 메시지를 표시한다.
'''    
# import random

# def one():
#     num1 = random.randint(5,20)
#     num2 = random.randint(5,20)    
#     print(num1, "+", num2, "= " )
#     ask = int(input("your answer is..."))
#     actual_answer = num1 + num2
#     answers = (ask, actual_answer)
#     return answers

# def two():
#     num3 = random.randint(25,50)
#     num4 = random.randint(1,25)
#     print(num3, "-", num4, "= ")
#     ask = int(input("your answer is..."))
#     actual_answer = num3 - num4
#     answers = (ask, actual_answer)
#     return answers
   
# def check_same(ask, actual_answer):
#     if ask == actual_answer :
#         print("correct!")
#     else:
#         print("Incorrect, the answer is...", actual_answer )

# def main():
    
#     menu_enter = int(input("1) addition\n2) subtraction\nEnter 1 or 2 :"))

#     if menu_enter == 1:
#         ask, actual_answer = one()
#         check_same(ask, actual_answer)
#     elif menu_enter == 2:
#         ask, actual_answer = two()
#         check_same(ask, actual_answer)
#     else:
#         print("1과 2중에 선택하세요!")

# main()

''' 121. 사용자가 이름 목록을 쉽게 관리할 수 있는 프로그램을 생성한다. 사용자가 목록에 이름을 추가할 수 있 는 메뉴와 목록의 이름을 수정하는 메뉴, 목록에서 이름을 삭제하는 메뉴 그리고 목록의 모든 이름을 표시하는 메뉴를 화면에 표시한다. 또한, 프로그램을 종료하는 메뉴도 있어야 한다. 사용자가 메뉴 외에 다른 것을 선택하면 적절한 메시지를 표시한다.사용자가 선택한 메뉴의 작업이 끝나면 다시 메뉴가 표 시되도록 한다. 되도록 사용하기 쉽게 프로그램을 만들자.
'''
def one():
    name = input("추가할 이름은 작성하세요: ")
    names.append(name)
    return names

def two():
    num = 0
    for i in names:
        print(num, i)
        num = num + 1
    select_num = int(input("수정하고 싶은 이름의 번호를 쓰세요: "))
    name = input("새로 변경할 이름을 작성하세요: ")
    names[select_num] = name
    return names
    
def three():
    num = 0
    for i in names:
        print(num, i)
        num = num + 1
    select_num = int(input("삭제하고 싶은 이름의 번호를 쓰세요: "))
    del names[select_num]
    return names
    
def four():
    print("모든 이름을 표시합니다!")
    num = 0
    for i in names:
        print(num, i)
        num = num + 1

def main():
    
    try_again = "y"
    while try_again == "y":
        print("1.이름 추가하기")
        print("2.이름 수정하기")
        print("3.이름 삭제하기")
        print("4.모든 이름 표시하기")
        print("5.프로그램 종료하기")
        select = int(input("몇 번을 수행하시겠습니까?: "))
    
        if select == 1:
            names = one()
        elif select == 2:
            names = two()
        elif select == 3:
            names = three()
        elif select == 4:
            names = four()
        elif select == 5:
            print("프로그램을 종료하겠습니다!")
            try_again = "n"
        else:
            print("1~5사이의 숫자를 선택해주세요.")

names = []  # 핵심
main()            
                 
                
                
                
''' 122. 다음의 메뉴를 생성한다. 
1) add to file 
2) view all recods 
3) quit program 
Enter the number of your selection:

사용자가 1을 선택하면 Salaries.csv라는 이름 의 파일에 이름과 급여를 저장한다. 2를 선택하면 Salaries.csv 파일의 모든 레코드를 표시한다. 3을 선택하면 프로그램을 종료한다. 만약 올바르지 않은 번호를 입력하면 에러 메시지를 출력한다. 3번을 선택할 때까지 계속해서 메뉴로 돌아간다.
'''

'''123.파이썬에서 csv 파일의 레코드를 직접 삭제하는 것은 기술 적으로 불가능하다. 대신, 파일을 파이썬의 임시 리스트로 저장하고 리스트를 변경한 다음에 임시 리스트를 원본 파일에 덮어쓰면 된다. 이전 프로그램을 수정하여 이 작업을 할 수 있게 만들자.
메뉴는 다음과 같이 표시된다. 
1) Add to file 
2) View all records 
3) Delete a recod
4) Quit program

Enter the number of your selection:
'''
        