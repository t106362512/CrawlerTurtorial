from random import randint
 
#規定範圍並產生密碼
lowest = 1
highest = 100
answer = randint(lowest, highest)
 
#重複猜數字，直到猜對為止
while True:
    guess = input('密碼介於 ' + str(lowest) + '-' + str(highest) + ':\n>>')
 
    #檢查輸入的內容是否為數字
    try:
        guess = int(guess)  #把字串轉換成整數
    except ValueError:  #轉換失敗便要求重新輸入數字
        print('格式錯誤，請輸入數字\n')
        continue
 
        #檢查輸入的數字是否介於規定範圍內
    if guess <= lowest or guess >= highest:
        print('請輸入 ' + str(lowest) + '-' + str(highest) + ' 之間的整數\n')
        continue
 
        #判斷有沒有猜中密碼
    if guess == answer:
        print('答對了！')
        break   #猜對才跳脫迴圈
    elif guess < answer:
        lowest = guess
    else:
        highest = guess