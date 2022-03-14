# Questionaire for wellness
# Quicky fixed and simplified by https://github.com/ZackeryRSmith

# Developer note: Hey TristanCanDev/Blu! It seems you may be new to python (Granted this was last updated 12 months ago), which is just fine! I tried commenting this code with the best explanations I can. Please, just please don't use so many if statements like you did. 

import time

# Multi-line variable declaration
health_points, total_possible = 0, 24


print("Welcome to the BluSoftware Wellness Test created within python! Please be sure to answer all questions honestly so we can properly gauge your general wellness")
time.sleep(1)

print("Remember, most of these questions have been created out of the Leading Health Indicators that you can find at health.gov/healthypeople")
time.sleep(2)

# Allows declaration in one line, but looks a bit chunky
questions = ["Do you utilize the oral health care system and abide their guide lines?", "Do you eat items with high sugar counts that could reduce the chance of getting proper nutrients but could give you excessive amounts of calories?", "Do you inject, take, or consume drugs (This excludes Marijuana as it is healthy to take in most cases) of any form?", "Do you consume alcoholic beverages regularly?", "Do you live in a community where you are often subjected or exposed to unhealthy polluted air?", "Do you have any eating disorder such as anorexia or bulimia?", "Do you live in a community or household that has limited access to food which causess starvation among yourself or others?", "Have you received your general vaccinations?", "Do you get your influenza vaccination yearly?", "Do you have any STIs such as HIV?", "Do you currently have any health conditions?", "Do you suffer mental illness or suffer from suicidal thoughts?"]

# There is a better way to do this.. But, this will simplify all the if statements in the for loop
best_answer = ["y", "n", "n", "n", "n", "n", "n", "y", "y", "n", "n", "n"]

# For loop, gets the index of the current question along with the question.
for index, question in enumerate(questions):
    while True:  # While loop, allows us to repeat a question if [Y or N] format was not met
        userin = input(question + " [y/n] ")
        
        # Let me explain this if.
        # First we lowercase the input an example would be taking "HELLO" into "hello"
        # We then check if the input is NOT in a list. This is the same thing as writing
        # `if userin.lower() != "y" or userin.lower != "n"`
        # As you can see it's cleaner. If the input is not y or n we repeat the while loop (essentially repeating the question)
        if userin.lower() not in ["y", "n"]:  # lower() lowercases any string I.e. "HELLO" -> "hello"
            print("Not 'y' or 'n'")
            continue
        # Check if the input is the best answer possible
        elif userin.lower() == best_answer[index]:
            health_points += 2
            break
        # If input is NOT the best answer possible
        else:
            break

# Kept your old system, just removed the un-needed braces
if health_points <= 6:
    print("With the answers you have provided, we have decided to declare you unhealthy")
elif health_points <= 12:
    print("With the answers you have provided, we have decided to declare you moderately unhealthy")
elif health_points <= 18:
    print("With the answers you have provided, we have decided to declare you moderately healthy")
elif health_points <= 24:
    print("With the answers you have provided, we have decided to declare you healthy")
