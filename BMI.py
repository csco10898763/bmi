height = input('請輸入您的身高：')
weight = input('請輸入您的體重：')
height = float(height)
weight = float(weight)
bmi = round((weight / (height / 100) ** 2),2)
if bmi < 18.5:
    print('BMI：', bmi, '體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('BMI：', bmi, '正常範圍')
elif bmi >=24 and bmi < 27:
    print('BMI：', bmi, '異常範圍：輕度肥胖')
elif bmi >= 27 and bmi < 30:    
    print('BMI：', bmi, '異常範圍：中度肥胖')
else:
    print('BMI', bmi, '異常範圍：重度肥胖')
