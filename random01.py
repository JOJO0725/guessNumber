import random

num1 = input('請輸入1~100範圍內一數字:')
num2 = input('請輸入1~100範圍內一數字:')
num1 = int(num1)
num2 = int(num2)

ans = random.randint(num1,num2)
count = 0
while True: 
    guess = input('請猜一數字:')
    guess = int(guess)
    count += 1
    if guess == ans:
        print('恭喜你!猜對了!')
        print('你猜了',count,'次!')    
        break    
    elif guess < ans:
        print('再猜大一點!')
        if guess <1:
            print('你輸入的數字超出範圍,請輸入1~100的數字!')                
    elif guess > ans:
        print('再猜小一點!')    
        if guess > 100 :
            print('你輸入的數字超出範圍,請輸入1~100的數字!')
    print('你猜了',count,'次!')        