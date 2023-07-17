#Copyright Bail 2021-2023
#com.Bail.daysmatter.gkdjs 高考倒计时 v1.4.3_11
#2021.3.16-2023.7.17

PURPOSE = (6,7) #目标日
HELP = ''

import time,sys,random,os

def getarg():
    '''获取参数
返回值：运行程序时传入的参数(str|bool)'''
    if len(sys.argv) == 1:  #无参数
        return False
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-s': #倒计秒
            return 's'
        elif sys.argv[1] == '-q':   #9秒后退出
            return 'q'
        elif sys.argv[1] == '-n':   #以linux通知形式显示
            return 'n'
        else:   #不认识的参数
            print(HELP)
            exit(1)
def getdate()->tuple:
    '''获取当前日期
返回值：当前日期元组，整型，依次为年，月，日(tuple)
※注意：返回的年份为等效年份：
[1,PURPOSE[0]]月为当前年份，
(PURPOSE[0],12]月为下一年份'''
    year,mon,day = map(int,time.strftime('%Y.%m.%d').split('.'))
    if mon > PURPOSE[0]:
        year += 1
    return year,mon,day
def isrun(year:int)->bool:
    '''判断是否为闰年
year(int):年份
返回值：闰年性(bool)'''
    if year%4 == 0 and year%100 != 0:
        return True
    elif year%400 == 0:
        return True
    else:
        return False
def totday(m:int,d:int,tue:bool)->int:
    '''计算该等效年份内经过的天数
m(int):月
d(int):日
tue(bool):闰年性（即2月的天数为(28+tue)天）
返回值：当前日期（月，日）在当前等效年份所处的等效天数(int)
※后续优化规划：放弃负数'''
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
    else:
        raise ValueError(f'无效的月份: {m}')
def day()->int:
    '''计算距目标日的天数
返回值：距目标日的天数(int)'''
    year,mon,day = getdate()
    now = totday(mon,day,isrun(year))
    pur = totday(*PURPOSE,isrun(year))
    delta = pur-now
    return delta
def sec()->float:
    '''计算距目标日的秒数
返回值：距目标日的秒数(float)'''
    year = getdate()[0]
    now = time.time()
    pur = int(time.mktime(time.strptime('{}.{}.{}'.format(year,PURPOSE[0],PURPOSE[1]),'%Y.%m.%d')))
    delta = pur-now
    return delta
def cheer()->str:
    '''抽取励志名言
返回值：抽取到的励志名言(str)
※强依赖文件：sentences.txt（励志名言库）'''
    with open('sentences.txt',encoding='utf-8') as file:
        sent = random.choice(file.readlines())
    return sent
def output(value,isday:bool):
    '''输出相关信息
value(int|float):相关数值
isday(bool):倒数日性'''
    if isday:
        if getarg() == 'n':
            os.system(f'notify-send -a gkdjs -i python3 -t 3000000 距高考还有{value}天 "{cheer()}"')
            sys.exit(0)
        else:
            print('距高考还有{}天'.format(value))
            print(cheer())
    else:
        print('距高考还有{}秒'.format(value),end='\r')
def close(iswait:bool):
    '''提供倒数日最后的关闭方式
iswait(bool):“9秒后自动关闭”性'''
    if iswait:
        print('9秒后自动关闭',end='\r')
        for i in range(9,0,-1):
            print(i,end='\r')
            time.sleep(1)
        sys.exit(0)
    else:
        input() #保持控制台窗口不自动关闭
def main():
    if getarg() == 's': #倒计秒
        while True:
            value = sec()
            output(value,False)
    else:   #倒数日
        value = day()
        output(value,True)
        close((getarg() == 'q'))
    return 0
if __name__ == '__main__':
    sys.exit(main())
