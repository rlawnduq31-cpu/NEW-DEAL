print("안녕하세요!!!")
print(100)

# 메모를 하고 싶어요 (주석)
# 주석 단축키는 ctrl + / (cmd + /)
# 쓰고 싶은 말을 쓸 수 있어요.

# 숫자 출력해보기
print(75)
print(2.33)
print(-100)

# 문자 출력해보기
print("파이썬 배우기")
print("python is good")


# 여러 값 함께 출력 -> 글자 숫자 자유롭게 섞을 수 있음.
print("온도:", 75)
print("설비", 1, "번 상태:", "정상")

# 숫자 연산 해보기
print(75 + 5)  # 80
print(75 - 5)  # 70
print(10 * 3)  # 30
print(10 / 4)  # 2.5
print((75 + 80) / 2)  # 77.5

print("=== 1번 설비 측정값 ===")
print("온도(℃):", 75)
print("진동(mm/s):", 2.3)

# 에러 발생시켜 보기
# 1) NameError : 정의하지 않은 이름 썼을 때
# print(안녕하세요)
# NameError: name '안녕하세요' is not defined
print("안녕하세요")  # -> 따옴표로 감싸서 해결 가능

# 2) SyntaxError :문법이 어긋났을때발생 ( 따옴표, 괄호의 짝이 안맞을 때)
# print("온도(): ", 82 -> SyntaxError, 괄호가 안닫혔음
# SyntaxError: '(' was never closed
print("온도(): ", 82)  # 괄호를 닫아서 에러 해결

print("온도", 75)
print("진동", 2.3)
print("압력:", 4.0)
