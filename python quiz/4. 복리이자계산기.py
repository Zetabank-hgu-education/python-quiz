#4. 복리 이자 계산기
#1년에 10%의 이자를 주는 예금이 있습니다.
#각 년도별로 초기 투자금이 얼마나 증가하는지를 보여주는 프로그램을 작성해 봅시다
try:
    years = int(input("몇 년 동안 투자하실 예정인가요?: "))
    initial_investment = float(input("초기 투자 금액을 입력하세요: "))
    interest_rate = float(input("연 이자율을 입력하세요 (%): "))
    
    for year in range(1, years + 1):
        investment_value = initial_investment * (1 + interest_rate / 100) ** year
        print(f"{year}년 후 투자 금액: {investment_value:.2f}")

except ValueError:
    print("유효한 숫자를 입력해주세요.")