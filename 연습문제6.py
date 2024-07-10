x=input("문자메세지를 입력하세요.:")

if len(x)<=20:
    print("요금은 50원입니다.")
elif len(x)>20:
    print("요금은 100원입니다.")

#1. 사용자로부터 문자 메세지 입력받기
data = input("문자메세지를 입력하세요.")
#2. 입력받은 문자메세지의 길이
len_data = len(data)
#3. 20글자 초과 시 100원 출력
if len_data > 20 :
    print("요금은 100원입니다.")
#4. 20글자 이하 시 50원 출력
elif len_data <= 20:
    print("요금은 50원입니다.")