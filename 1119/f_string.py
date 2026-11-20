name = "홍길동"
age = 25
# 홍길동님은 25살입니다.
sen = name + "님은 " + str(age) + "살입니다."
print(sen)
sen2 = f"{name}님은 {age}살입니다."
print(sen2)

code = "EQP-001"

print(f"설비 코드 {code} 점검 완료: 온도 {25}도")
hours = 3
print(f"총 가동 시간(분): {hours*60}분")

value = 3.141592
print(f"PI 소수점둘째자리까지: {value:.2f}")
print(f"PI 소수점넷째자리까지: {value:.4f}")

# ① 설비명·온도를 변수로 저장 → ② f-string을 사용해서 예상 결과와 같이 출력
sul = "전기"
on = 25
print(f"설비명:{sul}, 온도:{on}")
# ① 세 점수를 변수로 저장 → ② f-string을 사용하여 평균을 구하는 계산식을 사용해 출력
score1 = 100
score2 = 90
score3 = 80
print(f"평균: {(score1+score2+score3)/3}")
# ① 측정값 87.456 저장 → ② 소수점 첫 번째 자리와 두 번째 자리까지 각각 출력
value = 87.456
print(f"측정값 소수점 첫 번째 자리: {value:.1f}")
print(f"측정값소수점 두 번째 자리: {value:.2f}")
# ① 문자열 '  5 , sensor_2 , WARNING , 0.78912  ' 저장
# ② strip·split 후 각 조각 정리, 소수점은 두 번째 자리까지
sen = "  5 , sensor_2 , WARNING , 0.78912  "
sen = sen.strip().split(" , ")
print(sen)
print(f"{sen[0]} {sen[1]} {sen[2]} {float(sen[3]):.2f}")

# 11-19 실습
# log = " [WARNing] " →"WARNING"
log = " [WARNing] "
print(log.upper()[2:9])
# sensors = "temp,pressure,vibration"  → "VIBRATION / PRESSURE / TEMP"
sen = "temp,pressure,vibration"
print(" / ".join(sen.split(",")[::-1]).upper())
# data = " EQP-01 , NORMAL , 85.5 " → "normal"
data = " EQP-01 , NORMAL , 85.5 "
data = data.split(" , ")
print(f"{data[1].lower()}")
# text = " ###[ PUMP-07 ]### " → "pump_07"
text = " ###[ PUMP-07 ]### "
text = text.lower().strip().replace("-", "_").split()
print(f"{text[1]}")
# data = " TEMP / Pressure | vibration " → "temp,pressure,vibration"
data = " TEMP / Pressure | vibration "
data = data.replace(" / ", ",").replace(" | ", ",").lower().strip()
print(data)
# 문자열 심화 실습 1
data = "pump-07|08:30|TEMP=85.5C|STATUS=normal"
data2 = "PUMP_07,09:00,92.0C,WARNING"
data = (
    data.upper()
    .replace("-", "_")
    .replace("C", "")
    .replace("TEMP=", "")
    .replace("STATUS=", "")
    .split("|")
)
data2 = data2.upper().replace("-", "_").replace("C", "").split(",")
print(data)
print(data2)
print("=====센서 데이터 비교=====")
print("설비코드:" + data[0])
print("최초 측정:" + f"{data[1]} / {data[2]}℃ / {data[3].lower()}")
print("최근 측정:" + f"{data2[1]} / {data2[2]}℃ / {data2[3].capitalize()}")
print("                         ")
print("동일 설비 여부:", data[0] == data2[0])
print("온도 변화량:" + f"{float(data2[2])-float(data[2])}℃")
print(
    "온도 상승률:" + f"{float(float(data2[2])-float(data[2]))/float(data[2])*100:.2f}%"
)
print("온도 급상승 여부:", (float(data2[2]) - float(data[2])) > float(6.0))

# 실습2 설비 작업 완료 예정 시간
log = "2026/11/19 23:58:45|DELAY=135s|EQP-09"
log1 = log[0:11]  # 2026/11/19
log2 = log[11:]  # 23:58:45|DELAY=135s|EQP-09"
log2 = log2.split("|")
print(log1)
print(log2)
print("=====설비 작업 정보=====")
print("설비코드:" + log2[2])
print("작업날짜:" + log1)
clock = log2[0]
hour = clock[:2]
min = clock[3:5]
sec = clock[-2:]
print("작업시작시간:" + f"{hour}시 {min}분 {sec}초")
soyo = log2[1]
print("소요시간:" f"{soyo[-4:-1]}초")
print("                        ")
print("완료시각:")

# 심화3
line1 = "LOT-A|1,200|36|8h"
line2 = "lot_a,850,17,5h"
# (두 변수 모두 - 생산라인코드, 생산량, 불량품수, 가동시간 순)
