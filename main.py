#Copyright Bail 2020
#daysmatter 倒数日 v1.0.3

from time import strftime
main = {}    #使用项目
dic = {}
def day(lst,mode=28):
    if int(strftime('%Y'))%4 == 0:
        mode = 29
    else:
        mode = 28 
    for i,j in enumerate(lst):
        lst[i] = int(j)
    if lst[0] == 1:
        return lst[1]
    elif lst[0] == 2:
        return lst[1]+31
    elif lst[0] == 3:
        return lst[1]+31+mode
    elif lst[0] == 4:
        return lst[1]+62+mode
    elif lst[0] == 5:
        return lst[1]+92+mode 
    elif lst[0] == 6:
        return lst[1]+123+mode 
    elif lst[0] == 7:
        return lst[1]+153+mode 
    elif lst[0] == 8:
        return lst[1]+184+mode 
    elif lst[0] == 9:
        return lst[1]+215+mode 
    elif lst[0] == 10:
        return lst[1]+245+mode 
    elif lst[0] == 11:
        return lst[1]+276+mode 
    elif lst[0] == 12:
        return lst[1]+306+mode 

for i,j in main.items():
    mainlst = j.split('.')
    dic[i] = day(mainlst)
date = strftime('%m.%d')
daylst = date.split('.')
days = day(daylst)
print('今天是',date,'，今年第',days,'天')
for i,j in dic.items():
	print('距',i,'(',main[i],') 还有',j-days,'天')
	
