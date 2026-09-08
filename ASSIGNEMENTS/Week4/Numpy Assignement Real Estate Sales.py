import numpy as np

SerialNumber, Town, Address, SaleAmount = np.genfromtxt("Week6/Real_Estate_Sales_2001-2022_GL-Short.csv",delimiter=",",unpack=True,usecols=(0, 3, 4, 6),dtype=None,skip_header=1)

print(SerialNumber)
print(Town)
print(Address)
print(SaleAmount)

print(min(SaleAmount))
print(max(SaleAmount))
print("Mean of SaleAmount :", np.mean(SaleAmount))
print("Median of SaleAmount :", np.median(SaleAmount))
print("Average of SaleAmount :", np.average(SaleAmount))
print("std of SaleAmount :", np.std(SaleAmount))
print("Percetile of 77 :", np.percentile(SaleAmount, 77))
print("Percentile of 3 :", np.percentile(SaleAmount, 3))
print("Square of SaleAmount :", np.square(SaleAmount))
print("Sqrt of Saleamount :", np.sqrt(SaleAmount))
print("Power of SaleAmount :", np.power(SaleAmount, SaleAmount))
Addition = SaleAmount + SerialNumber
Substraction = SaleAmount - SerialNumber
Multiplication = SaleAmount * SerialNumber
Division = SaleAmount / SerialNumber
print(Addition)
print(Substraction)
print(Multiplication)
print(Division)
SaleAmountPie = (SaleAmount / np.pi) + 1
SinValue = np.sin(SaleAmountPie)
CosineValue = np.cos(SaleAmountPie)
TangentValue = np.tan(SaleAmountPie)
print("Value of Sin :", SinValue)
print("Value of Cos", CosineValue)
print("Value of Tan", TangentValue)
LogArray = np.log(SaleAmountPie)
log10Array = np.log10(SaleAmountPie)
print(log10Array)
print(LogArray)
SinhValues = np.sinh(SaleAmountPie)
print(SinhValues)
CoshValues = np.cosh(SaleAmountPie)
print(CoshValues)
TanhValues = np.tanh(SaleAmountPie)
print(TanhValues)
D2SaleAmountSerialNumber = np.array([SaleAmount, SerialNumber])

D2SaleAmountSerialNumberSlice = D2SaleAmountSerialNumber[0:1:1, 1:5:1]
print(D2SaleAmountSerialNumberSlice)

D2SaleAmountSerialNumberSlice2 = D2SaleAmountSerialNumber[:1, 4:15:4]
print(D2SaleAmountSerialNumberSlice2)
D2SaleAmountSerialNumberSliceItemsOnly = D2SaleAmountSerialNumberSlice[0, 1]
print(D2SaleAmountSerialNumberSliceItemsOnly)
D2SaleAmountSerialNumberSlice2ItemsOnly = D2SaleAmountSerialNumberSlice2[0, 2]
print(D2SaleAmountSerialNumberSlice2ItemsOnly)
for elem in np.nditer(D2SaleAmountSerialNumber):
    print(elem)

for index, elem in np.ndenumerate(D2SaleAmountSerialNumber):
    print(index, elem)

D2SaleAmountSerialNumberT0149 = np.reshape(D2SaleAmountSerialNumber, (1, 278))
print(D2SaleAmountSerialNumberT0149)
print(D2SaleAmountSerialNumberT0149.size)
print(D2SaleAmountSerialNumberT0149.ndim)
print(D2SaleAmountSerialNumberT0149.shape)
print()