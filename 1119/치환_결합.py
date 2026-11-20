# replace -> 문자열 바꾸기, 지우기
print(" 정 상 가 동".replace(" ", "-"))
print(" 정 상 가 동".replace(" ", ""))  # 공백제거
print("falut".replace("falut", "고장"))  # 고장

# 3,000 -> 숫자 3000
print(int("3,000".replace(",", "")))  # int형 3000
# 010-1234 5678 ->01012345678
print("010-1234 5678".replace("-", "").replace(" ", ""))  # 01012345678

# 문자열.split(생략가능구분자)
list = [10, 20, 30, "hello", False]
print(list[3])  # hello
print(list[1])  # 20

coffe = "에스프레소 카페라떼 아메리카노"
print(coffe.split())  # ['에스프레소', '카페라떼', '아메리카노']
coffe_list = coffe.split()
print(coffe_list[2])

print("사과,배,감".split(","))
print("사과,배,감".split(",")[2])
date = "2025-01-15"
day = date.split("-")[2]
print(day)

print(coffe.split(" ", 1))
# ① '설비 정상 가동' 저장 → ② '정상'을 '점검'으로 바꿔 출력
sul = "설비 정상 가동"
print(sul.replace("정상", "점검"))
# ① 'PUMP A 03' 저장 → ② 공백 기준 분리하여 리스트 출력
ex = "PUMP A 03"
print(ex.split(" "))
# ① 'a,b,c,d' 저장 → ② ','을 기준으로 분리
ex = "a,b,c,d"
print(ex.split(","))
# ① 'a,b,c,d' 저장 → ② 첫 번째 ','을 기준으로 한 번만 나누기
ex = "a,b,c,d"
print(ex.split(",", 1))

# 구분자가될문자열.join([리스트])
list = ["2026", "11", "19"]
# 2026-11-19, 2026.11.19
print("-".join(list))
print(".".join(list))
# 1. ① ['2025','01','15'] 준비 → ② '-'으로 연결하여 합치기
list = ["2025", "01", "15"]
print("-".join(list))
# 2. 2025·1·15 를 '-' 와 ','로 총 2가지 방법을 사용해 이어서 출력
list = "2025·1·15"
print(list.replace("·", "-"))
print(",".join(list.split("·")))
# 3. ① '2025/01/15' 저장 → ② '/'을 기준으로 나눈 후 '-' 으로 합치기
list = "2025/01/15"
list1 = list.split("/")
print("-".join(list1))
# 4. ① '1, NORMAL ,25.3' 저장
# ② ',' 기준으로 나누어 1번 인덱스를 공백 제거와 소문자로 변환해 출력
list = "1, NORMAL ,25.3"
list = list.split(",")
print(list[1].strip().lower())
# 1. text = "   PyThOn   " ->"python"
text = "   PyThOn   "
print(text.strip().lower())
# 2. phone = "  010 - 1234 - 5678  " -> "01012345678"
phone = "  010 - 1234 - 5678  "
phone = phone.replace(" - ", "")
print(phone.strip())
# 3. name = "   kIM    cHUL   sOO   " -> "Kim Chul Soo"
name = "   kIM    cHUL   sOO   "
# name = name.strip().lower()
# print(name.title())
print(" ".join(name.split()).title())
# 4. filename = "  Sensor Data 2026.CSV  " -> "sensor_data_2026.csv"
filename = "  Sensor Data 2026.CSV  "
filename = filename.lstrip().rstrip().replace(" ", "_")
print(filename.lower())
# 5. data = "TEMP----PRESSURE----STATUS" -> "TEMP-PRESSURE-STATUS"
data = "TEMP----PRESSURE----STATUS"
print(data.replace("----", "-"))
