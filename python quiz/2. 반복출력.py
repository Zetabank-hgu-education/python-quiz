# 2. 반복 출력
#input()으로 사용자로부터 정수를 한 개 입력받아, 그 숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 ValueError 예외처리를 포함하여 작성

#이 때, 출력 앞에 공백을 한 칸 주어서 입력과 출력이 구분되게 합니다.

# num = int(input())

# i = 0
# while i < num:
#     print('', num)
#     i += 1

# 2-1
try:
    num = int(input("정수를 입력하세요: "))
    
    i = 0
    while i < num:
        print('', num)
        i += 1

except ValueError:
    print("유효한 정수를 입력해주세요.")