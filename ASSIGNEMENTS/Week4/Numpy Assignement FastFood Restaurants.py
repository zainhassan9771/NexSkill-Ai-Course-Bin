
import numpy as np

Latitude,Longitude,PostalCode,Latitude2 = np.genfromtxt("Week6/FastFoodRestaurants.csv",delimiter=",",usecols=(4, 5, 7, 4),unpack=True,dtype=float,skip_header=1,invalid_raise=False)

print(Latitude)
print(Longitude)
print(PostalCode)
print(Latitude2)

print(np.min(Latitude))
print("Average of the latitude :", np.average(Latitude))
print("Mean of the latitude :", np.mean(Latitude))
print("Median of the latitude :", np.median(Latitude))
print("Standard deviation of the latitude :", np.std(Latitude))
print("Percentile 25 -= ", np.percentile(Latitude, 25))
print("Percentil 77-= ", np.percentile(Latitude, 77))

Addition = Latitude + Longitude
Substraction = Latitude - Longitude
Multiplication = Latitude * Longitude
Division = Latitude / Longitude
print(Addition)
print(Substraction)
print(Multiplication)
print(Division)

print("Square of the latitude :", np.square(Latitude))
LatitudePie = (Latitude / np.pi) + 1

SinValue = np.sin(LatitudePie)
CosValue = np.cos(LatitudePie)
TanValue = np.tan(LatitudePie)
print(SinValue)
print(CosValue)
print(TanValue)

LogArray = np.log(LatitudePie)
log10Array = np.log10(LatitudePie)
print(log10Array)
print(LogArray)

SinhValues = np.sinh(LatitudePie)
print(SinhValues)

CoshValues = np.cosh(LatitudePie)
print(CoshValues)

TanhValues = np.tanh(LatitudePie)
print(TanhValues)

D2LatitudeLongitude = np.array([Latitude, Longitude])
D2LatitudeLongitudeSlice = D2LatitudeLongitude[0:1:1, 0:5:1]
print(D2LatitudeLongitudeSlice)

D2LatitudeLongitudeSlice2 = D2LatitudeLongitude[:1, 2:12:1]
print(D2LatitudeLongitudeSlice2)