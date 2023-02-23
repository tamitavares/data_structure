#Temperature Converter

temp = float(input('Temperature: '))
un = input('Unit of Measurement (F or C): ')

if un == 'C':
    result = (temp*1.8)+32
elif un == 'F':
    result = (temp-32)/1.8
else:
    result = 'Error'

print('Result: ', result)