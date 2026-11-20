# +(문자열 이어주기) *(문자열 반복)
print("설비" + "점검")  # 설비점검
print("설비" + " " + "점검")  # 설비점검
line = "-" * 20  # 구분선 만들어주기
print(line)

##### 문자열과 관련된 함수
# len(문자열): 문자열의 길이를 변환
print(len("PYTHON"))  # 6
print(len("Strawberry Moon ~!"))  # 18
phone = "01012345678"
phoneLength = len(phone)
print(phoneLength)

# in, not in < 함수는 아님
hasWord = "고장" in "설비 고장을 예측하는~~"
hasWord2 = "고장" not in "설비 고장을 예측하는~~"
print(hasWord, hasWord2)

# 실습2 포함확인하기
msg = "설비 고장 발생"
print("고장" in msg)
print("정상" in msg)

# count(), find(), index()
# 문자열A.count(문자열B) : 문자열A에 문자열B가 몇 개나 들어있는지 -> 숫자값 반환
# 문자열A.find(문자열B) :
# - 문자열A에 문자열B가 언제 처음 등장하는지 -> 인덱스 반환
# - 문자열B가 등장하지 않으면 -1 반환
# 문자열A.index(문자열B):
# - 문자열A에 문자열B가 언제 처음 등장하는지 -> 인덱스 반환
# - 문자열B가 등장하지 않으면 Error!
print("banana".count("a"))  # 3
print("banana".count("na"))  # 2

email = "hong@company.com"
print("@의 인덱스번호", email.find("@"))  # 4
print("@의 인덱스번호", email.find("!"))  # -1 (찾고자 하는 문자열(!) 존재하지 않음)

print("@의 인덱스번호", email.index("@"))  # 4
# print("@의 인덱스번호", email.index("!"))  # ValueError: substring not found

# 실습문제 1. ① 'sensor-01-temp' 저장 → ② count('-') 로 하이픈 개수 출력
ex = "sensor-01-temp"
print(ex.count("-"))
# 실습문제 2. ① 'temp_2024' 저장 → ② find('_') 로 첫 위치, 없는 글자(z)는 -1 확인
ex = "temp_2024"
print(ex.find("_"))
print(ex.find("z"))

# startswith / endswith
# 문자열A.startswith(문자열B) : 문자열A가 문자열B로 시작하는지 검사 -> T/F
# 문자열A.endswith(문자열B): 문자열A가 문자열B로 끝나는지 검사 -> T/F
print("EQP-001".startswith("EQP"))  # True
print("data.csv".endswith(".csv"))  # True
print("" == " ")  # False
print("normal" == "Normal")  # False
print("AAaaBB" == "AAaaBB")  # True
