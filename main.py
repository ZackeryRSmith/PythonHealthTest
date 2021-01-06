#Questionaire for wellness
import time

rusername = "****"
rpassword = "****"

HealthPoint = 0
TotalPossible = 24

Question1 = "Do you utilize the oral health care system and abide their guidlines?"
Question2 = "Do you eat items with high sugar counts that could reduce the chance of getting proper nutrients but could give you excessive amounts of calories?"
Question3 = "Do you inject, take, or consume drugs (This excludes Marijuana as it is healthy to take in most cases) of any form?"
Question4 = "Do you consume alcoholic beverages regularly?"
Question5 = "Do you live in a community where you are often subjected or exposed to unhealthy poluted air?"
Question6 = "Do you have any eating disorder such as anorexia or bulimia?"
Question7 = "Do you live in a community or household that has limited access to food which causess starvation among yourself or others?"
Question8 = "Have you recieved your general vaccinations?"
Question9 = "Do you get your influenza vaccination yearly?"
Question10 = "Do you have any STIs such as HIV?"
Question11= "Do you currently have any health conditions?"
Question12 = "Do you suffer mental illness or suffer from suicidal thoughts?"


print("Welcome to the BluSoftware Wellness Test created within python! Please be sure to answer all questions honestly so we can properly gauge your general wellness")
time.sleep(1)
print("Remember, most of these questions have been created out of the Leading Health Indicators that you can find at health.gov/healthypeople")
time.sleep(2)
##userinp = input("Are you an administrator? y/n ")
##if (userinp == "y" or userinp == "Y"):
##    username = input("Username ")
##    password = input("Password ")
##    if (username != rusername):
##        print("Username Incorrect")
##    if(username == rusername):
##        if(password != rpassword):
##            print("Incorrect Password")
array = [Question1, Question2, Question3, Question4, Question5, Question6, Question7, Question8, Question9, Question10, Question11, Question12]
for x in array:
    userin =input(x + " y/n ")
    if(x == Question1):
        if(userin == "Y" or userin == "y"):
            HealthPoint = HealthPoint + 2
    if(x == Question2):
        if(userin == "N" or userin == "n"):
            HealthPoint = HealthPoint + 2
    if(x == Question3):
        if(userin == "N" or userin == "n"):
            HealthPoint = HealthPoint + 2
    if(x == Question4):
        if(userin == "N" or userin == "n"):
            HealthPoint = HealthPoint + 2
    if(x == Question5):
        if(userin == "N" or userin == "n"):
            HealthPoint = HealthPoint + 2
    if(x == Question6):
        if(userin == "N" or userin == "n"):
            HealthPoint = HealthPoint + 2
    if(x == Question7):
        if(userin == "N" or userin == "n"):
            HealthPoint = HealthPoint + 2
    if(x == Question8):
        if(userin == "Y" or userin == "y"):
            HealthPoint = HealthPoint + 2
    if(x == Question9):
        if(userin == "Y" or userin == "y"):
            HealthPoint = HealthPoint + 2
    if(x == Question10):
        if(userin == "N" or userin == "n"):
            HealthPoint = HealthPoint + 2
    if(x == Question11):
        if(userin == "N" or userin == "n"):
            HealthPoint = HealthPoint + 2
    if(x == Question12):
        if(userin == "N" or userin == "n"):
            HealthPoint = HealthPoint + 2

if(HealthPoint <= 6):
    print("With the answers you have provided, we have decided to declare you unhealthy")
elif(HealthPoint <= 12):
    print("With the answers you have provided, we have decided to declare you moderately unhealthy")
elif(HealthPoint <= 18):
    print("With the answers you have provided, we have decided to declare you moderately healthy")
elif(HealthPoint <= 24):
    print("With the answers you have provided, we have decided to declare you healthy")
