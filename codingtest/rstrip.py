''' input()함수보다 '빠른' sys.stdin.readline() 함수. 
    input()함수처럼 한 줄씩 '입력받기 위해' 사용 된다. '''
    
import sys

data = sys.stdin.readline().rstrip()
print(data)

''' readline()입력하면 엔터가 줄 바꿈 기호로 입력된다.
    이 공백 문자를 제거하려면 rstrip()함수를 사용해야 한다.'''



