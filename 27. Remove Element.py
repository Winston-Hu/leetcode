ls = [0, 1, 2, 2, 3, 0, 4, 2]
ls2 = ls
for i, item in enumerate(ls2):
    print(ls2)
    if item == 2:
        ls.remove(item)

print(ls)

#########
# 注意面向对象的问题，上面的代码会随着for循环，改变ls2，因为上面代码的ls2和ls是一个对象
# #######

ls = [0, 1, 2, 2, 3, 0, 4, 2]
ls2 = []
for i in range(len(ls)):
    ls2.append(ls[i])

for i, item in enumerate(ls2):
    print(ls2)
    if item == 2:
        ls.remove(item)

print(ls)
