choose = str(input('Выбери действие(пиши так: +,-,*,/,**,%,//):'))
num1 = int(input('первое число:'))
num2 = int(input('Второе число:'))

if(choose == '+'):
    print('Результат:',num1+num2)
elif(choose == '-'):
    print('Результат:',num1-num2)
elif(choose == '*'):
    print('Результат:',num1*num2)
elif(choose == '/'):
    print('Результат:',num1/num2)
elif(choose == '**'):
    print('Результат:',num1**num2)
elif(choose == '%'):
    print('Результат:',num1%num2)
elif(choose == '//'):
    print('Результат:',num1//num2)
else:
    print('Писать научись! Для кого подсказка была')