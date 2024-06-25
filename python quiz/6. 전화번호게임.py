# 6. 전화번호 게임
# 친구들과 함께 어떤 게임을 하고 있습니다.
# 게임의 규칙은 각자의 전화번호 뒷자리 4자리를 뒤집어서 말하는 것입니다.
# ex) 1234 -> 4321 / 파이썬 코드로 구현해 봅시다.
number = 358

rem = rev = 0
while number >= 1:
    rem = number % 10
    rev = rev * 10 + rem
    number = number // 10

print(rev)


try:
    # 사용자에게 전화번호 뒷자리를 입력받습니다.
    number = int(input("전화번호 뒷자리 3~4자리를 입력하세요: "))

    rem = rev = 0
    while number >= 1:
        rem = number % 10  # 10으로 나눈 나머지를 구합니다.
        rev = rev * 10 + rem  # 뒤집힌 숫자를 구성합니다.
        number = number // 10  # 10으로 나눈 몫을 구합니다.

    print(f"뒤집힌 전화번호 뒷자리는 {rev}입니다.")

except ValueError:
    print("유효한 숫자를 입력해주세요.")