import os

os.system('C:\\Users\\student\\Desktop\\mystem -nl C:\\Users\\student\\Desktop\\g.txt C:\\Users\\student\\Desktop\\h.txt')
f = open('h.txt', 'r', encoding = 'UTF-8')
s = f.read()
f.close()
print(s)
