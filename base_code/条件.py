# -*- coding: utf-8 -*-

weight=float(input('请输入你的体重（/kg）:'))
high=float(input('请输入你的身高（/m）:'))

bmi=weight/(high**2)
print('你的BMI指数是：%.1f'%bmi)

if bmi<18.5:
     print('你的体重过轻')
elif bmi<25:
     print('你的体重正常')
elif bmi<28:
     print("你的体重过重")
elif bmi<32:
     print('你属于肥胖')
else:
     print('你属于严重肥胖')
