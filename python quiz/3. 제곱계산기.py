#3. 제곱 계산기
#정수를 한 개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 ValueError 예외처리를 포함하여 작성
try:
    num = int(input("정수를 입력하세요: "))
    
    for i in range(1, num + 1):
        square = i ** 2
        print(f"{i}의 제곱은 {square}입니다.")

except ValueError:
    print("유효한 정수를 입력해주세요.")






