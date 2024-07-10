#num= input("임의의 숫자를 입력하세요.")
#num = int(num)
#print(num, type(num), int(num))

num = input("임의의 숫자를 입력하세요.")
num = int(num) +100
if num <= 150 :
    print("값이 부족합니다")
if num > 150 :
    print(num)

#1. 사용자로부터 값을 입력받아. (문자열)
data = input("값을 입력하세요:")
#2. 입력받은 값에 100을 더함 (숫자형)
data_2 = data + 100
#2-1. 입력받은 값에 100을 더할 때, 데이터 타입을 변환 (문자열->숫자형)
data_2 = int(data) +100
#3. 더한 값이 150초과인 경우, 사용자 입력 값을 출력
if data > 150:
    print("값이 부족합니다")
#4. 더한 값이 150이하인 경우, 값이 모자랍니다를 출력
if data <= 150:
    print(data)