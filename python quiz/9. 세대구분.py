# 9. 세대 구분
# input()으로 사용자의 나이를 입력받은 후, 다음 표의 어느 세대에 속하는지 출력하는 코드를 작성해 봅시다. 
y = int(input('What year were you born? '))

gen = None

if y <= 1924:
    gen = 'the Greatest Generation'
elif y <= 1945:
    gen = 'the Silent Generation'
elif y <= 1964:
    gen = 'a baby boomer'
elif y <= 1980:
    gen = 'a Gen X'
elif y <= 1996:
    gen = 'a millennial'
else:
    gen = 'a Gen Z'

print(f"You're {gen}.")