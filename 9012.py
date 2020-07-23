N = int(input())

for i in range(N):
    Parentheses = list(input())
    while len(Parentheses) != 0:
        if Parentheses[0] == ')':
            print('NO')
            break
        else:
            if ')' in Parentheses:
                Parentheses.remove(')')
                Parentheses.remove('(')
            else:
                print('NO')
                break
    if len(Parentheses) == 0:
        print('YES')