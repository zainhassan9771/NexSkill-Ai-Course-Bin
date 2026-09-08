import numpy as np

Brokkerd_By, Price, Bed, Acre_Lot = np.genfromtxt("Week6/RealEstate-USA.csv",delimiter=",",usecols=(0, 2, 3, 5),unpack=True,dtype=float,skip_header=1)

print(Brokkerd_By)
print(Price)
print(Bed)
print(Acre_Lot)

print(np.min(Price))

print("Average of the price :", np.average(Price))
print("Mean of the price :", np.mean(Price))
print("Median of the of the price :", np.median(Price))
print("Standard deviation of the price :", np.std(Price))
print("Percentile 25 -= ", np.percentile(Price, 25))
print("Percentil 77-= ", np.percentile(Price, 77))
Addition = Price + Bed
Substraction = Price - Bed
Multiplication = Price * Bed
Division = Price / Bed

print(Addition)
print(Substraction)
print(Multiplication)
print(Division)


print("Square of the price :", np.square(Price))
PricePie = (Price / np.pi) + 1
SinValue = np.sin(PricePie)
CosValue = np.cos(PricePie)
TanValue = np.tan(PricePie)
print(SinValue)
print(CosValue)
print(TanValue)
LogArray = np.log(PricePie)
log10Array = np.log10(PricePie)
print(log10Array)
print(LogArray)

SinhValues = np.sinh(PricePie)
print(SinhValues)

CoshValues = np.cosh(PricePie)
print(CoshValues)

TanhValues = np.tanh(PricePie)
print(TanhValues)

D2PriceBed = np.array([Price, Bed])
D2PriceBedSlice = D2PriceBed[0:1:1, 0:5:1]
print(D2PriceBedSlice)
D2PriceBedSlice2 = D2PriceBed[:1, 2:12:1]
print(D2PriceBedSlice2)