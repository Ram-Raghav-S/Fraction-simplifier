fraction = input("Enter the improper fraction in the form numerator/denominator. ")
slash_index = fraction.find("/")
numerator = int(fraction[:slash_index])
denominator = int(fraction[slash_index+1:])
smaller_value = min(numerator, denominator)
common_factors = []

while len(common_factors) != 1:
    common_factors = []
    for j in range(1, smaller_value + 1):
        if numerator % j == denominator % j == 0:
            common_factors.append(j)
    for i in range(1, smaller_value+1):
        if denominator % i == 0 and numerator % i == 0:
            numerator = numerator//i
            denominator = denominator//i

print(f"fraction = {numerator}/{denominator}")










