data = input("숫자 다섯개 입력해주세요.").split()
print(data)

# data.sort()
# print(data)

numbers = [int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4])]
print(numbers)
numbers.sort(reverse=True)
print(numbers)

max_count = numbers.count(numbers[0])  # 두번째 큰 숫자의 인덱스 번호
print("두번째 큰 숫자:", numbers[max_count])
