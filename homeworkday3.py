# grades = [72, 76, 78, 80, 85, 88, 89, 90, 93, 95 ]
# print(grades)
# average = sum(grades)/len(grades)
# print(average)


# temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
# print(temperatures)
# week2 = (temperatures[7:13])
# print(week2)
# print(temperatures[-6:])
# print(temperatures[4], temperatures[9])


# days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# range(len(days_of_week))
# for i in range(0, len(days_of_week)):
#     if i % 2 == 0:
#         print(days_of_week[i])

#trying different conditions with while loops
# i = 0
# while i < 12:
#     i += 2
#     if i == 4:
#         continue
#     print(i)

# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")
#exit after 5
# i = 1
# while i < 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1 


from random import random


#def main():
items = ["stick", "$4", "dagger", "bottle", "chicken sandwich"]
import random
random.choice(items)
    
while True:
    user = input("Guess the item that was selected ")
    if user == random.choice(items):
        print("Good!")
        break
    else:
        print("Try again ")

                    
            






   

    










