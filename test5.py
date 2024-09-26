a = int(input('輸入三位數字:'))
a3 = int(a/100)
a2 = int(a%100/10)
a1 = a%10
print(f'{a1}{a2}{a3}')
