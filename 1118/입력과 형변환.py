#### 입력함수 input()
# name = input("이름을 입력해주세요.")
# age = input("나이를 입력해주세요.")
# print("제 이름은", name, "입니다.")
# print("제 나이는" + age + "입니다.")

# number_A = input("덧셈 연산을 할 첫번째 숫자를 입력해주세요")
# number_B = input("덧셈 연산을 할 두번째 숫자를 입력해주세요")
# print(number_A + number_B)  # 10 + 5 = 105
# number_A, number_B 자료형확인 해보기
# print("입력되는 숫자의 데이터 타입(자료형):", type(number_A)) #<class 'str'>
# -> 실제 숫자 연산 하기 위해 형변환 해야함

# ====== 형변환 =======
# int(), float(), str()
print("int->float", float(25))  # 25.0
print("정수형 str->float", float("25"))  # 25.0
print("실수형 str->float", float("25.5"))  # 25.5
print("==== int() 확인 =====")
print("float->int", int(25.8))  # 25
print("정수형 str -> int", int("25"))  # 25
# print("실수형 str -> int", int("25.8")) #ValueError
print("==== str()확인 ====")
print("int -> str", str(25))
print("float -> str", str(25.2))

# 형변환 입력 같이 써보기!!
# number_A = input("첫번째 숫자를 입력해주세요")
# number_B = input("두번째 숫자를 입력해주세요")
# number_A = int(number_A)
# number_B = int(number_B)
# print("덧셈 결과:", number_A + number_B)

# 위에꺼 한줄에 뺄셈
# n1 = int(input("숫자 입력해주시오(1)"))
# n2 = int(input("숫자 입력해주시오(2)"))
# print("n1, n2 자료형 확인", type(n1)) #<class 'int'>
# print("뺄셈 결과:", n1 - n2)

# heigth = float(input("당신의 키를 입력해주세요.:"))  # float("188.5")
# age = int(input("당신의 나이를 입력해주세요"))
# print("당신의 키는", heigth, "입니다.", "나이는", age, "입니다.")

# 실습-이름 입력받아 인사말 출력
name = input("당신의 이름을 입력해주세요 ")
print("안녕하세요", name, "님!")
