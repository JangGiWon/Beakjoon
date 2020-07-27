s = list(input().split('-'))

for i in s:
    print(i[0], end='')

# -를 기준으로 리스트에 저장하면 단어 별로 저장됨
# 그것을 end='' 를 붙여서 출력하면 줄바꿈없이 출력할 수 있음
