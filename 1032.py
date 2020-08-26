import sys

n = int(sys.stdin.readline())
commands = []

for i in range(n):
    commands.append(sys.stdin.readline().strip())

pattern = list(commands[0])

for command in commands[1:]:
    for i in range(len(command)):
        if pattern[i] == '?':
            pass
        elif pattern[i] != command[i]:
            pattern[i] = '?'

print(''.join(pattern))
