#Copyright Bail 2021-2023
#com.Bail.daysmatter.zkdjs 高考倒计时 v1.4_8
#2021.3.16-2023.6.28

PURPOSE = (6,7)
HELP = ''

import time,sys,random,os

def getarg():
    if len(sys.argv) == 1:
        return False
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-s':
            return 's'
        elif sys.argv[1] == '-q':
            return 'q'
        elif sys.argv[1] == '-n':
            return 'n'
        else:
            print(HELP)
            exit(1)
def isrun():
    year = int(time.strftime('%Y'))
    if year%4 == 0 and year%100 != 0:
        return True
    elif year%400 == 0:
        return True
    else:
        return False
def totday(m,d,tue):
    m = int(m)
    d = int(d)
    if m == 7:
        return d-184
    elif m == 8:
        return d-153
    elif m == 9:
        return d-122
    elif m == 10:
        return d-92
    elif m == 11:
        return d-61
    elif m == 12:
        return d-31
    elif m == 1:
        return d
    elif m == 2:
        return 31+d
    elif m == 3:
        return 59+tue+d
    elif m == 4:
        return 90+tue+d
    elif m == 5:
        return 120+tue+d
    elif m == 6:
        return 151+tue+d
def day():
    mon,day = time.strftime('%m.%d').split('.')
    now = totday(mon,day,isrun())
    mon,day = PURPOSE
    pur = totday(mon,day,isrun())
    delta = pur-now
    return delta
def sec():
    print('功能暂未开放')
    sys.exit(1)
    def year():
        if int(time.strftime('%m')) > 6:
            year = int(time.strftime('%Y'))+1
        else:
            year = int(time.strftime('%Y'))
        return year
    now = time.time()
    pur = int(time.mktime(time.strptime('{}.{}.{}'.format(year(),PURPOSE[0],PURPOSE[1]),'%Y.%m.%d')))
    delta = pur-now
    return delta
def close(iswait):
    if iswait:
        print('9秒后自动关闭',end='\r')
        for i in range(9,0,-1):
            print(i,end='\r')
            time.sleep(1)
        sys.exit(0)
    else:
        input()
def output(value,isday):
    if isday:
        if getarg() == 'n':
            os.system(f'notify-send -a gkdjs -i python3 -t 3000000 距高考还有{value}天 "{cheer()}"')
            sys.exit(0)
        else:
            print('距高考还有{}天'.format(value))
            print(cheer())
    else:
        print('距高考还有{}秒'.format(value),end='\r')
def cheer():
    with open('sentences.txt',encoding='utf-8') as file:
        sent = random.choice(file.readlines())
    return sent
def main():
    if getarg() == 's':
        while True:
            value = sec()
            output(value,False)
    else:
        value = day()
        output(value,True)
        close((getarg() == 'q'))
    return 0
if __name__ == '__main__':
    main()
