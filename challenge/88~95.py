''' 숫자 배열 '''

# 088. 다섯 개의 정수를 입력받아 배열에 저장한다. 정렬을 한 후 역순으로 표시하라.
from array import*

nums = array('i', [])  #기본
count = 0
while count < 5:
    fiveValue = int(input("다섯 개의 정수를 입력하세요: "))
    nums.append(fiveValue)
    print(nums)
    count = count + 1
nums = sorted(nums)
nums.reverse()
print(nums)

# 089. 정수들을 저장할 배열을 생성한다. 임의의 수 다섯 개를 생성하고 배열에 저장한다. 배열의 항목을 한 줄에 하나씩 출력하라.
from array import*
import random

nums = array('i', [])

count = 0
while count < 5:
    randomnums = random.randint(1,100)
    nums.append(randomnums)
    count = count + 1
print(nums)

for x in nums:
    print(x)
    
# 090. 사용자에게 숫자를 입력하라고 요청한다. 10에서 20 사 이의 숫자를 입력한다면 배열에 저장한다. 다른 값이라면 "Outside the range"라는 메시지를 출력한다.다섯 개의 숫자가 입력되었다면 "Thank you" 메시지를 출력하고 배열의 항목을 한 줄에 하나씩 출력하라. 
from array import* 

savenums = array('i', [])
count = 0
while count < 5: 
    nums = int(input("10에서 20 사이의 숫자를 입력하세요: "))
    if 10 <= nums <= 20:
        savenums.append(nums)
        count = count +1
    else: print("Outside the range")
    
print("Thank you!")
for x in savenums:
    print(x)
     
# 091. 다섯 개의 숫자(이 숫자들 중 2개는 반복 되어야 함)를 담고 있는 배열을 생성한다. 사용자에게 배열 전체를 출력한다. 사용자에게 배열 속에 있는 숫자들 중 하나를 입력하라고 요청한 뒤, 입력한 숫자가 리스트에 몇 개 있는지 메시지를 표시하라.
from array import*

arrays = array('i', [2,7,11,9,7])
for i in arrays:
    print(i)
    
pickme = int(input("배열 속에 있는 숫자들 중 하나를 입력하세요: "))
print(arrays.count(pickme)) #배열에 (pickme)몇 개 들어 있는지

# 092. 두 개의 빈 배열을 생성한다. 하나에는 사용자가 입력할 숫자 세 개를 담을 것이고, 다른 하나 에는 다섯 개의 임의의 숫자를 담을 것이다. 두 개의 배열을 큰배열 하나로 결합한다. 결합한 배열을 정렬하고 각 항목을 한 줄에 하나씩 출력한다.
from array import*
import random

from numpy import around, round_

array1 = array('i', [])
array2 = array('i', [])

count = 0
while count < 3:
    three = int(input("숫자 세 개를 담아주세요: "))
    array1.append(three)
    count = count + 1
print(array1)


# count = 0
# while count < 5:
#     fiverandom = random.randint(0,100)
#     array2.append(fiverandom)
#     count = count + 1
# print(array2)

for b in range(0,5):
    fiverandom = random.randint(0,100)
    array2.append(fiverandom)
print(array2)

array1.extend(array2)
array1 = sorted(array1)

for i in array1:
    print(i)

# 093. 사용자에게 숫자 다섯 개를 입력하라고 요청한다. 입력된 숫자를 정렬하고 사용자에게 표시한다. 배열의 숫자들 중 하나를 고르라고 사용자에게 요청한다. 입력된 숫자를 배열에서 삭제하고 새로운 배열에 그 값을 저장하라. 
from array import* 

arr = array('i', [])

for i in range(0,5):
    fivenum = int(input("숫자 다섯 개를 입력하세요: "))
    arr.append(fivenum)
arr = sorted(arr)
print(arr) 

getrid = int(input("배열의 숫자들 중 하나를 고르세요: "))
if getrid in arr:
    arr.remove(getrid)
    print("삭제되고 남은 배열의 값들은", arr, "입니다.")

    newarr = array('i', [])
    newarr.append(getrid)
    print("삭제되어 새로운 배열에 온 값은 ", newarr, "입니다!")

else: print("그런 값은 없습니다...")

# 094. 다섯 개의 숫자들을 가진 배열을 출력한다. 숫자들 중 하나를 고르 라고 사용자에게 요청한다. 사용자 가 숫자를 고르면 그 항목의 위치 (인덱스)를 출력한다. 만약 사용자가 입력한 숫자가 배열 안에 없다면 올바른 숫자를 입력할 때까지 다시 요청하라. 
from array import*

arr = array('i', [])
for i in range(0,5):
    ranarr = random.randint(0,100)
    arr.append(ranarr)
print(arr)

# for i in arr:
#     print(i)
    
picknum = int(input("숫자들 중 하나를 고르세요: "))

tryagain = True
while tryagain == True:
    if picknum in arr:
        print(arr.index(picknum))
        tryagain = False
        
    else: picknum = int(input("올바른 숫자를 다시 입력하세요: "))

# 095. 소수점 이하 두 자리가 있는 10과 100 사이 의 숫자 다섯 개를 포함하는 배열을 생성한다. 사용자에게 2와 5 사이의 정수를 입력하도록 요청한다. 입력한 숫자가 범위에 없는 숫자라면 적절한 에러 메시지를 출력하고 다시 입력하라고 한다. 배열에 있는 각 숫자를 사용자가 입력한 숫자로 나누고 소수점 둘째 자리까지 표시하라.
from array import*
import math

from traceback import print_tb

arr = array('f', [33.12, 22.34, 99.76, 26.31, 44.74])

tryagain = True
while tryagain == True: 
    twofive = int(input("2에서 5사이의 정수를 입력하세요: "))
    if 2 < twofive < 5:
        print("good!")
        tryagain = False
    else: print("try again!")

for i in range(0,5):
    arrtwofive = arr[i] / twofive
    print(round(arrtwofive, 2))