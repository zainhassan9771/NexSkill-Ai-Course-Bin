#Write a program that converts a temperature from Celsius to Fahrenheit. (Formula: Fahrenheit=
# (Celsius * 9/5) + 32)
Celcius=int(input("Enter temperature in Celcius :"))
Farenheit=(Celcius*9/5+32)
print("Temperature in Farenheit :",Farenheit)

#Calculate Area of a Rectangle
#Rectangle= L*W
Length=int(input("Enter Length :"))
Width=int(input("Enter Width :"))
Area=Length*Width
print("Area of a Rectangle :",Area)

#Calculate Compound Interest
#Use the formula: CI = P * (1 + R/100)**T - P
#Where P = principal, R = rate, T = time
P=int(input("Principal :"))
R=int(input("Rate :"))
T=int(input("Time :"))
CI=P*(1+R/100)**T - P
print("Compound Interest :",CI)

#Perimeter of a Rectangle - Take length and width as input and calculate the perimeter.
Length=int(input("Length :"))
Width=int(input("Width :"))
Perimeter=2*(Length+Width)
print("Perimeter :",Perimeter)

#Average of Three Numbers - Input three numbers and print their average.
Num1=int(input("Number 1 :"))
Num2=int(input("Number 2 :"))
Num3=int(input("Number 3 :"))
Average=(Num1+Num2+Num3)/3
print("Average Of 3 Numbers :",Average)

#Square and Cube of a Number - Ask the user for a number and display its square and cube.
Number=int(input("Enter your number :"))
Square=(Number)*2
print("Square of Number :",Square)
Cube=(Number)*3
print("Cube of Number :",Cube)

#Distribute Items Equally - You have n candies and k students.
#Write a program to find:
#how many candies each student gets
#how many are left
Candies=int(input("Number of candies :"))
Students=int(input("Number of students :"))
EachStudentGet=Candies//Students
print("Each Student Get :",EachStudentGet)
CandiesLeft=Candies%Students
print("Total candies and left :",CandiesLeft)

#Calculate Profit or Loss
#Input cost price and selling price. Display either:
#Profit and amount, or
#Loss and amount, or
#No Profit No Loss
CostPrice=int(input("Enter Cost Price :")) 
SellingPrice=int(input("Enter selling price :"))
if SellingPrice>CostPrice:
    Profit=SellingPrice-CostPrice
    print("Profit :",Profit)
elif SellingPrice<CostPrice:
     Loss=CostPrice-SellingPrice
     print("Loss :",Loss)
else:
     print("No Profit No Loss :")

#Total Marks and Percentage
#Input marks of 5 subjects. Print:
# Total marks
# Percentage
# Average  
S1=int(input("Enter marks of subject 1 :"))
S2=int(input("Enter marks of subject 2 :"))
S3=int(input("Enter marks of subject 3 :"))
S4=int(input("Enter marks of subject 4 :"))
S5=int(input("Enter marks of subject 5 :"))
ToatlMarks=S1+S2+S3+S4+S5
print("Total Marks :",ToatlMarks)
Percentage=( ToatlMarks/500 )*100
print("Percentage :",Percentage)
Average=ToatlMarks/5
print("Average :")

#Salary Calculator
#Input basic salary. Calculate:
#HRA = 20% of basic
#DA = 15% of basic
#Total Salary = Basic + HRA + DA
BasicSalary=int(input("Salary :"))
HRA=(BasicSalary)*20/100
DA=(BasicSalary)*15/100
ToatlSalary=BasicSalary+HRA+DA
print("HRA :",HRA)
print("DA :",DA)
print("Total Salary :",ToatlSalary)

#Age in Months and Days
#Input your age in years. Calculate and print age in:
#Months
#Days (approximate)
Age=int(input("Input Your Age :"))
InMonths=Age*12
InDays=Age*365
print("Age in Months :",InMonths)
print("Age in Days :",InDays)

#Currency Converter (USD to PKR)
#Input amount in USD. Convert using a fixed exchange rate.
USD=int(input("Enter Currency in USD : $"))
PKR=USD*280
print("pkr amount=",PKR)

#Sum of First N Natural Numbers
#Input a number n, calculate sum of first n natural numbers.
#Formula: sum = n * (n + 1) / 2
n=int(input("Enter a number :"))
Sum=n*(n+1)/2
print("First n number:",n,"Natural number:",sum)

#Percentage of Correct Answers
#Input total questions and correct answers, and calculate the percentage score
TotalQuestions=int(input("Enter total questions :"))
CorrectQuestions=int(input("Enter correct questions :"))
Percentage=(CorrectQuestions/TotalQuestions)*100
print("Percentage :",Percentage)

#Speed, Distance, and Time
#Input distance and time, and calculate speed.
Distance=int(input("Enter Distance :"))
Time=int(input("Enter Time :"))
Speed=Distance/Time
print("Speed :",Speed)

#Calculate Body Mass Index (BMI)
#Input weight (kg) and height (m), then calculate:
#BMI = weight / (height ** 2)
Weight=int(input(" Enter Weight of mass :"))
Height=int(input("Enter Height of Mass :"))
BMI=Weight/(Height**2)
print("BMI :",BMI)

#Convert Minutes to Hours and Minutes
#Input number of minutes and convert to hours and remaining minutes.
#Example: 130 minutes → 2 hours 10 minutes
Minutes=int(input("Enter minutes :"))
Hours=Minutes/60
RemainingMinutes=Minutes%60
print("Hours :",Hours, "Remaing Minutes :",RemainingMinutes)
