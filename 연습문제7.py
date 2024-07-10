x= input("점수를 입력하세요.")
x=int(x)
if 81 < x and x < 100 :
    print("학점은 A입니다.")
if 61 < x and x < 80 :
    print("학점은 B입니다.")
if 41 < x and x < 60 :
    print("학점은 C입니다.")
if 21 < x and x < 40:
    print("학점은 D입니다.")
if 0 < x and x < 20 :
    print("학점은 E입니다.")

#1. 사용자로부터 값을 입력
num= input("점수를 입력하세요")
#2. 문자열을 숫자열로 변형
num= int(num)
#3. 변환된 값을 각 조건에 따라 학점으로 출력
if 81 <= num <= 100:
    print("A")
elif 61<=num <= 80:
    print("B")