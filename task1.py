slices = party_pizza_mini + large + medium
print(f'Total number of slices: {slices}')

people = people + 1
share = slices // people
leftover = share % people
print(f'Each person gets: {share}')
print(f'Leftover slices: {leftover}')

people = people + 2 #Eric and Brandon are coming too.
share = round(slices // people)
leftover = share % people
print(f'Each person gets: {share}')
print(f'Leftover slices: {leftover}')



slices = slices + party_pizza_mini
share = slices // people
leftover = share % people
print(f'Each person gets: {share}')
print(f'Leftover slices: {leftover}')
print("...for Mr. Hollow Leg")
