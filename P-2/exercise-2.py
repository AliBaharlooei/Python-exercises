# برنامه ای بنویسید که 5 نمره از ورودی دریافت کرده اگر نمره بین 0 تا 5 بود پیغام دهد خسته نباشید اگر نمره بین 5 تا 8 بود با ارفاق پاس اگر نمره 8 تا 12 بود مردی نمره گرفتی اگر نمره 12 تا 15 بود خوبه بد نیست اگر 15 تا 20 بود وظیفته در غیر این صورت خودتو اذیت نکن مسیر دیگه برو جلو.
userScore1 = int(input("Enter your score 1 : "))
userScore2 = int(input("Enter your score 2 : "))
userScore3 = int(input("Enter your score 3 : "))
userScore4 = int(input("Enter your score 4 : "))
userScore5 = int(input("Enter your score 5 : "))

userScore = (userScore1 + userScore2 + userScore3 + userScore4 + userScore5) / 5

if userScore <= 5 :
    print("خسته نباشید" , userScore)
elif userScore <= 8 :
    print("با ارفاق پاس", userScore)
elif userScore <= 12 :
    print("مردی نمره گرفتی", userScore)
elif userScore <= 15 :
    print("خوبه بد نیست", userScore)
elif userScore <=20 :
    print("وظیفته", userScore)
else :
    print("خودتو اذیت نکن مسیر دیگه برو جلو")