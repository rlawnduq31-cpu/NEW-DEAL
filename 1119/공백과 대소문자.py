word = "python"
sen = "I Love python"

# upper(), lower() 전체변경
# capitalize(), title() 앞글자만 대문자로 변경
print(word.upper())  # PYTHON
print(sen.upper())  # I LOVE PYTHON
print(word.count("p"))  # 1, 원본 문자열은 변경되지 않음.

print("normal".upper())
print("WARNING".lower())
print("WARNING 경고".lower())  # warning 경고 한글이나 특수문자는 그대로 유지
print("python is good. i have an apple".capitalize())
# Python is good. i have an apple

print("python is good. i have an apple".title())
# Python Is Good. I Have An Apple
print("hong gil-dong".title())
# Hong Gil-Dong
print("apple".lower() == "Apple".lower())
# True

# isupper(), islower()
print("Apple".islower(), "Apple".isupper())
# False False
print("apple".islower())  # False
print("APPLE".isupper())  # True

# 1
print("ready".upper())
print("WARNING".lower())
print("kim chul soo".title())
f1 = "fault"
f2 = "FAULT"
print(f1.upper() == f2.upper())
print("ABC".islower(), "ABC".isupper())
print("abc".islower(), "abc".isupper())
print("Abc".islower(), "Abc".isupper())
sen = "Sensor_LOG.CSV"
sen_low = sen.lower()
print(sen_low.startswith("sensor"), sen_low.endswith(".csv"))

###### 문자열 공백 처리 ######
# strip() 앞 뒤 공백 제거
# lstrip()앞공백제거 , rsrtip() 뒤 공백 제거
sent = "  안녕하세요. 저는 abc입니다.   "
print(sent + "!!")
#  안녕하세요. 저는 abc입니다.   !!
print(sent.strip() + "!!")
# 안녕하세요. 저는 abc입니다.!!
print(sent.lstrip() + "!!")
# 안녕하세요. 저는 abc입니다.   !!
print(sent.rstrip() + "!!")
#  안녕하세요. 저는 abc입니다.!!

print("=========절취선=========".strip("="))

# abc를 대문자로 -> 결과
#  결과 앞뒤 공백 제거
# 문자 개수 제거
print(sent.upper())
print(sent.upper().strip())
print(len(sent.upper().strip()))

# 실습
# 7. '  가동중 ' 변수로 저장 후 -> [가동중] 출력해보기
ga = "  가동중 "
print("[" + ga.strip() + "]")
# 8. ' 대기 ' 변수로 저장 후 -> [대기 ]/[ 대기] 각각 출력
da = " 대기 "
print("[" + da.lstrip() + "]")
print("[" + da.rstrip() + "]")
# 9. ***경고**** 저장, '*' 제거 후 `경고`만 출력
war = "***경고****"
print(war.strip("*"))
# 10. '  WARNING ' -> 'warning' 체이닝으로 출력하기
print("  WARNING ".strip().lower())
#
