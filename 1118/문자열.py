name = "홍길동"
status = "정상"
code = "EQP-001"
print(name, status, code)

sentence = "It's normal"
sentence2 = '이 장비는 "정상" 입니다.'
print(sentence)
print(sentence2)

sentence3 = "'장비1'은 \"정상\"이고, '장비2'는 \"비정상\"입니다."
sentence4 = "'장비1'은 \"정상\"이고, '장비2'는 \"비정상\"입니다."
print(sentence3)
print(sentence4)

# test="여러줄로
# 작성하면
# 에러가 나는군요!"

삼중_따옴표 = """여러줄로
작성했을 때
에러가 나지 않습니다!!"""
print(삼중_따옴표)

#### 이스케이프 문자 \n \t \\
guide = "설비점검 하는 방법 \n1. 전원켜기 \n2. 센서 확인"
print(guide)

print("이름\t상태")
print("설비1\t정상")

print("C:\\Users\\SAMSUNG\\Desktop\\New deal")
print("\\")  # \

print("2025", "01", "15", sep="-")

# 실습1 여러줄 문자열 만들기
exam = """가동 점검표\n1.\t온도확인\n2.\t입력확인"""
print(exam)

# 실습2 설비 라벨 이어 붙이기
code = "PUMP_A"
status = "정상"
date = "2025-01-15"
# PUMP_A / 정상 / 2025-01-15
print(code + " / " + status + " / " + date)
print(code, status, date, sep=" / ")
print("처리중", end="...")
