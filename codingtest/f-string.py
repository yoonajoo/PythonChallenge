# f-string 문법

'''문자열에 'f'를 붙임으로써
    단순히 중괄호{} 안에 변수를 넣어
    자료형의 변환 없이도 문자열과 정수를 함께 넣을 수 있다.'''


answer = 8

# 기본 방식
print("정답은", answer, "입니다.")
print("정답은 " + str(answer) + " 입니다.")

# f-string 문법 방식
print(f"정답은 {answer} 입니다.")