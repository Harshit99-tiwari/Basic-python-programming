print(3**4)
print(2**2)
print(5**2)

def power_by(base_number , powered_number):
     result=1
     for index in range(powered_number):
          result = result * base_number
     return result
     

print(power_by(5,2))
