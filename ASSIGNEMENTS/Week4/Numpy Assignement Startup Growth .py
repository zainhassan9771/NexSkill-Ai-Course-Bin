import numpy as np

Name,Amount,Valuation,Country=np.genfromtxt("Week6/startup_growth_investment_data.csv",delimiter=",",unpack=True,usecols=(0,3,4,6),dtype=None,skip_header=1)

print(Name)
print(Amount)
print(Valuation)
print(Country)

print(np.min(Amount))
print(np.max(Amount))

print("Mean of Amount :",np.mean(Amount))
print("Average of Amount :",np.average(Amount))
print("Median of Amount :",np.median(Amount))
print("Std of Amount :",np.std(Amount))
print("Percentile of 77 =",np.percentile(Amount,77))
print("Percentile of 3=", np.percentile(Amount,3))

print("Square of Amount :",np.square(Amount))
print("Sqrt of Amount:",np.sqrt(Amount))
print("Power of Amount :",np.power(Amount,Amount))

Addition=Amount+Valuation
Substraction=Amount-Valuation
Multiplication=Amount*Valuation
Division=Amount/Valuation

print(Addition)
print(Substraction)
print(Multiplication)
print(Division)

AmountPie=(Amount/np.pi)+1
SinValue=np.sin(AmountPie)
CosineValue=np.cos(AmountPie)
TangentValue=np.tan(AmountPie)
print("Value of Sin :",SinValue)
print("Value of Cos",CosineValue)
print("Value of Tan",TangentValue)

LogArray=np.log(AmountPie)
log10Array=np.log10(AmountPie)
print(log10Array)
print(LogArray)

SinhValues=np.sinh(AmountPie)
print(SinhValues)

CoshValues=np.cosh(AmountPie)
print(CoshValues)

TanhValues=np.cosh(AmountPie)
print(TanhValues)

D2NameAmount = np.array([Name,Amount])
D2NameAmountSlice=  D2NameAmount[0:1:1 , 1:5:1]
print(D2NameAmountSlice)
D2NameAmountSlice2=D2NameAmount[:1,4:15:4]
print(D2NameAmountSlice2)

D2NameAmountSliceItemOnly=D2NameAmountSlice[0,1]
print(D2NameAmountSliceItemOnly)

D2NameAmountSlice2ItemOnly=D2NameAmountSlice2[0,2]
print(D2NameAmountSlice2ItemOnly)

for elem in np.nditer(D2NameAmount):
    print(elem)

for index,elem in np.ndenumerate(D2NameAmount):
    print(index,elem) 


D2NameAmountT0112=np.reshape(D2NameAmount,(1,10000))
print(D2NameAmountT0112)
print(D2NameAmountT0112.size)
print(D2NameAmountT0112.ndim)
print(D2NameAmountT0112.shape)
print()
