def time_after_1s(_h, _m, _s):
    #处理秒
    if _s + 1 == 60:
        _s = 0
        s_is_carried = True
    else:
        _s += 1
        s_is_carried = False
    #处理分
    if s_is_carried:
        if _m + 1 == 60:
            m_is_carried = True
            _m = 0
        else:
            m_is_carried = False
            _m += 1
    else:
        m_is_carried = False
    #处理时
    if m_is_carried:
        if _h + 1 == 24:
            h_is_carried = True
            _h = 0
        else:
            h_is_carried = False
            _h += 1
    else:
        h_is_carried = False
    #输出
    print("下一秒是：",end = '')
    if h_is_carried:
        print("第二天的", end = '')
    print(_h,'时', _m,'分', _s, '秒')
if __name__ == '__main__':
    judge = False#判断输入是否符合要求
    while not judge:
        h = int(input("Please input the hous:"))
        m = int(input("Please input the minute:"))
        s = int(input("Please input the second:"))
        judge_h = h < 24 and h >= 0
        judge_m = m < 60 and m >= 0
        judge_s = s < 60 and s >= 0
        judge = judge_h and judge_m and judge_s
        if not judge:
            print("Please input the correct time！")
    time_after_1s(h, m, s)
    
        
    
    
