print(4*5)
print(4%15)
print(3*6*6)
print(279/3)




x1 = 4*5
x2 = 4%15
x3 = 3*6*6
x4 = 279/3

#print separately
print(x1)
print(x2)
print(x3)
print(x4)
#print using text/string statment 
print("The value of x1, x2, x3, and x4 is", x1,",",x2,",",x3,",and",x4,", respectively")



x1, x2, x3, x4 = 4*5, 4%15, 3*6*6, 279/3

#print separately
print(x1)
print(x2)
print(x3)
print(x4)


a = 2 -4*11-(2/4)
print(a)


#c)
import math
a, b, c = 3, 6, -34

x = (-b+math.sqrt(b**2-4*a*c))/(2*a)
print(x)
print(round(x,2))


#d)
# Number of stocks in each industry
energy = 24
metals = 12
telecom = 11

# You can also assign multiple variables in one line:
# energy, metals, telecom = 24, 12, 11

# Total number of stocks
total = energy + metals + telecom

print("I have a total of", total, "stocks.")

# -------------------------------
# Method 1 (inefficient way)
# -------------------------------
print("\nMethod 1 (repeating total calculation):")
print(
    "Percentage of stocks in Energy, Metals, and Telecom is",
    round(energy / (energy + metals + telecom) * 100), "%,",
    round(metals / (energy + metals + telecom) * 100), "%, and",
    round(telecom / (energy + metals + telecom) * 100), "% respectively."
)

'''
NOTE: In Method 1, we calculate (energy+metals+telecom) three times,
which is not efficient. It's better to calculate it once and reuse it.
'''

# -------------------------------
# Method 2 (efficient way)
# -------------------------------
print("\nMethod 2 (using pre-calculated total):")
print(
    "Percentage of stocks in Energy, Metals, and Telecom is",
    round(energy / total * 100), "%,",
    round(metals / total * 100), "%, and",
    round(telecom / total * 100), "% respectively."
)





