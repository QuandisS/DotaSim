import random

print('Введите никнейм игрока>>')
nick = input()
print('Введите гражданство игрока (три символа)>>')
coutry = input()
print('Введите позицию игрока (Carry/Mid/Offlane/Semi-Sup/Sup')
pos = input()
print('Generation...')

f = open(nick + '.plr', 'w')
f.write(nick + '\n')
f.write(coutry + '\n')
f.write('Farm: ' + str(random.randint(0, 100)) + '\n')
f.write('Fight: ' + str(random.randint(0, 100)) + '\n')
f.write('Team_Work: ' + str(random.randint(0, 100)) + '\n')
f.write('Position: ' + pos)
f.close()

print('DONE!')