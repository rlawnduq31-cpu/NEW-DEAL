# 실습4 세값
"""
temp = int(input("온도:"))
 vib = float(input("진동:"))
 el = int(input("전류:"))
 if temp > 80 or vib > 4.0:
  print("위험: 즉시 정지")
 elif el > 60 and temp > 70:
    print("주의: 부하 점검")
 elif vib > 2.5:
   print("주의: 진동 관찰")
 else:
   print("정상")
"""

# 실습 1. 두번째로 큰 숫자 찾기
# data = [30 50 20 50 40]
"""
data = input().split()
 a = int(data[0])
 b = int(data[1])
 c = int(data[2])
 d = int(data[3])
 e = int(data[4])
 list = [a, b, c, d, e]
 list.sort(reverse=True)  # [50,50,40,30,20]
 if list[0] == list[1]:
    print(list[2])
 elif list[1] == list[2]:
    print(list[3])
 else:
   print(list[1])
"""

# 실습2 사칙연산 계산기 case match
"""first = int(input("첫 번째 숫자:"))
second = int(input("두 번째 숫자:"))
tool = input("연산자(+,-,*,/):")
match tool:
    case "+":
        print(f"계산 결과:{float(first + second)}")
    case "-":
        print(f"계산 결과:{float(first - second)}")
    case "*":
        print(f"계산 결과:{float(first * second)}")
    case "/":
    if second == 0:
    print("0으로 나눌 수 없습니다.")
    else:
        print(f"계산 결과:{float(first / second)}")
    case _:
    print("알수없는 연산자")
"""

"""
tot = int(input("현재 잔액:"))
cc = int(input("출금 금액:"))
rr = tot - cc  # 남은잔액
if cc % 1000 != 0:
    print("단위가 1000원이 아닙니다")
elif cc > 100000:
    print("출금 실패![100000원 초과입니다]")
elif cc < 1000:
    print("출금 실패![1000원 미만입니다]")
elif cc > tot:
    print("출금 실패![출금 잔액 부족!]")
else:
    print("출금 성공!")
    print(f"남은 잔액: {rr}원")
"""
# 실습19 1120 심화4 숫자 5개 중앙값 찾기
# num = input("숫자 5개 입력:").sort().split()
# print(f"정렬 결과: {num}")
# mid = num[2]
# print(f"중앙값: {mid}")
num = input("숫자 5개 입력:").split()
a = int(num[0])
b = int(num[1])
c = int(num[2])
d = int(num[3])
e = int(num[4])
list = [a, b, c, d, e]
ls = list
ls.sort()
mid = ls[2]
print(f"정렬 결과: {ls}")
print(f"중앙값: {mid}")
