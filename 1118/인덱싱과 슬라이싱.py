word = "PYTHON"
print(word[0], word[2], word[5])  # P T N
print(word[-6], word[-4], word[-1])  # P T N
print("python"[2])  # t

word = "Strawberry Moon ~!"
# Son!
son = word[0] + word[12] + word[14] + word[17]
print(son)

# 실습1 양수 인덱스로 글자 꺼내기
word1 = "SIGNAL"
print(word1[0])
print(word1[2])
print(word1[5])
# print(word1[6]) # IndexError

word2 = "안녕하세요!"
# 안녕! (음수인덱스)
hi = word2[-6] + word2[-5] + word2[-1]
print(hi)

##### 슬라이싱
word = "PYTHON"
print(word[0:5])  # PYTHO
print(word[:4])  # PYTH
print(word[1:])  # YTHON
print(word[1:100])  # 슬라이싱은 범위 밖으로 번호 지정해도 Error 발생x
print(word[:])  # PYTHON

# 음수 인덱스 통한 슬라이싱
print(word[-3:])  # 뒤에서부터 세글자 HON
print(word[:-1])  # 마지막 글자 빼고 가져와보기 PYTHO

# 문자열[시작:끝:간격] - step으로 건너뛰기
print(word[0::2])  # PTO
print(word[::-1])  # NOHTYP

# 실습3 구간자르기
# SIGNAL 저장 -> 예상결과 동일하게 나오도록 구간자르기
# SIG / GNA
word = "SIGNAL"
print(word[:3], " / ", word[2:5])

# 실습2. ① 'temp_sensor' 저장 → ② 앞 4글자만 추출하기
word = "temp_sensor"
print(word[:4])  # temp
# 실습3. ① 'temp_sensor' 저장 → ② _(언더바) 이후 모든글자 추출
word = "temp_sensor"
print(word[-6:])  # sensor
# 실습4. ① 'icecream' 저장 → ② 슬라이싱만을 이용해서 'crm' 추출
word = "icecream"
print(word[1::3])  # crm
