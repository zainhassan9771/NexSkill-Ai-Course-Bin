integer_number=123
float_number= 3.4
total=integer_number + float_number
print("value=" , total)
print ("Data type=",type(total))

string_number="20"
int_number=15
print("Data type before type casting:", type(string_number))
string_number=int(string_number)
print("Data type after type casting:",type (string_number))

num_sum=string_number+int_number
print("Sum:",num_sum)
print(type(num_sum))