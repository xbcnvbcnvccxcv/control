x=input("값을 입력하세요")
fruit={"봄":"딸기","여름":"토마토","가을":"사과"}
# in 앞에는 찾고싶은 요소, in 뒤에는 변수를 넣기
if x in fruit.values():
    print("정답입니다.")
else :
    print("오답입니다.")