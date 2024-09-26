a = int(input('請輸入一個三位數:'))
a1 = a%10
a2 = int(a%100/10)
a3 = int(a/100)
print('每位數字的總和:',a1 + a2 +a3)