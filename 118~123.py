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
import random

def low_high():
    low = int(input("낮은 숫자를 입력하세요: "))
    high = int(input("높은 숫자를 입력하세요: "))
    comp_num = random.randint(low, high)
    print(comp_num)
    return comp_num

def think_num():
    print("I am thinking of a number...")
    ask_thinking = int(input("사용자가 생각하고 있는 숫자를 입력하세요: "))
    return ask_thinking

def check_same(comp_num, ask_thinking):
    try_again = True
    while try_again == True:
        if comp_num == ask_thinking : 
            print("correct, you win")
            try_again = False
            
        elif comp_num > ask_thinking :
            ask_thinking =  int(input("업!: "))
        
        else :
            ask_thinking = int(input("다운!: "))

def main():
    comp_num = low_high()
    ask_thinking = think_num()
    check_same(comp_num, ask_thinking)
    
main()

''' 120. 사용자에게 다음의 메뉴를 표시한다. 
    1) addition
    2) subtraction
    Enter 1 or 2 :
'''    