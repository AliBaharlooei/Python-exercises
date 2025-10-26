# برنامه ای بنوسید که مشخصات یک دانشجو از ورودی دریافت کرده که شامل نام و نام خانوادگی کد ملی سن می باشد. 
# اگر سن دانشجو بیشتر از 18 بود مشخصات وارد شده چاپ شود.

userFullName = input("Please write your full name : ")
print("-----------------------------")
userNationalCode = int(input("Please write your National code : "))
print("-----------------------------")
userAge = int(input("Please write your age : "))

userPermission = 18

if userAge >= userPermission :
    print("Hi ",userFullName)
    print("Your national code is : ", userNationalCode)
    print(userFullName, ", you are ", userAge, " years old :)")
elif userAge < userPermission:
    print("You are not of legal age !")
else :
    print("Please enter a number")