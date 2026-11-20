"""
if 조건:
    조건이 참일때 실행될 문장1
    조건이 참일때 실행될 문장2
    조건이 참일때 실행될 문장3

----
if 조건:
    조건이 참일때 실행될 문장
else:
    조건이 거짓일때 실행될 문장

----
if 조건1:
    조건1이 참일때 실행될 문장
elif 조건2:
    조건1이 거짓이고, 조건2가 참일때 실행될 문장
else:
    조건1,2 모두 거짓일때 실행될 문장
여기에서 실행되는 문장은 조건의 참 거짓과 상관없이 실행
"""

# score = int(input("점수 입력해(자연수로)"))
# if score >= 60:
#    print("합격")
# else:
#    print("불합격")
# print("조건문과 관련없이 실행되는 문장")
#

# age = int(input("나이:"))
# if age >= 20:
#    print("성인입니다")
# else:
#    print("미성년자입니다")
# print("조건문과 관련없이 실행되는 문장")
# 90 이상 우수
# 70점 이상 보통
# 그 아래 미흡
# score = int(input("점수 입력해(자연수로)"))
# if score >= 90:
#    print("우수")
# elif score >= 70:
#    print("보통")
# else:
#    print("미흡")
#
# score = int(input("점수 입력해(자연수로)"))
score = 90
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
#
temp = 58
vib = 3.5
# 온도 60 초과, 진동 3 초과 -> 위험합니다.
# 온도 60 초과, 진동 3 이하 -> 주의하세요.
# 온도 60 미만 -> 정상입니다.
if temp > 60:
    if vib > 3:
        print("위험합니다")
    else:
        print("주의하세요")
else:
    print("정상입니다.")

# =======================
# 삼항 연산자
# 짝수인지 홀수인지 판단 프로그램
# result= int(input("점수 입력해(자연수로)"))
n = 7
if n % 2 == 0:
    result = "짝수"
else:
    result = "홀수"
print(result)
# 참일때값 if 조건 else 거짓값
result2 = "짝수" if n % 2 == 0 else "홀수"
print(result2)

# match ~ case 문
color = input("red, yellow, green 중 하나 작성").strip()
# red = 퇴장
# yellow = 경고
# green = 통과
# 위 세개 아니면 ->잘못된 값이 들어왔습니다.
match color:
    case "red" | "RED":  # | = or
        print("퇴장입니다.")
    case "yellow":
        print("경고입니다.")
    case "green":
        print("통과입니다.")
    case _:
        print("잘못된 값이 들어왔습니다!")

data = ["PUMP-01", 85, "WARNING"]
# (설비명)name: 온도 ()temp도, 주의 상태입니다.
match data:
    case [name, temp, "WARNING"]:
        print(f"{name}: 온도 {temp}도, 주의상태입니다")
    case [name, temp, "NORMAL"]:
        print(f"{name}: 온도 {temp}도, 정상상태입니다")
#
cid = "admin"
cpas = "1234"
id = input("아이디:")
pas = input("비밀번호:")
if id == cid and pas == cpas:
    print("로그인 성공")
else:
    print("로그인 실패")
"""
match 값에 대한변수:
    case 변수값1:
        변수==변수값1일때 실행할 문장
    case 변수값2:
        변수==변수값2일때 실행할 문장
    case 변수값3:
        변수==변수값3일때 실행할 문장
    case _:
        변수가 변수값1, 변수값2, 변수값3 모두 아닐때 실행할 문장
        if else 문에서 else 해당 조건
"""
#
