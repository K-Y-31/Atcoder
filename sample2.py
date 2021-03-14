m = int(input())
m_k = m/1000
if m_k < 0.1:
    print('00')
elif 0.1 <= m_k <= 5:
    if len(str(int(m_k*10))) >= 2:
        print(str(int(m_k*10)))
    elif len(str(int(m_k*10))) <= 1:
        print('0'+str(int(m_k*10)))
elif 6 <= m_k <= 30:
    print(str(int(m_k+50)))
elif 35 <= m_k <= 70:
    print(str(int(((m_k-30)/5)+80)))
else:
    print('89')
