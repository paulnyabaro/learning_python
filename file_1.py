groups = [['Newton', 'Isaac'], ['John', 'Bianca'], ['Ciara', 'Clara', 'Beth']]

for group in groups:
    for name in group:
        print(name)


big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# Print only positive numbers:
for i in big_number_list:
  if i < 0:
    continue
  print(i)

# Recursion 
def recursion(value):
    if value == 0:
        print("Done")
    else:
        print(f'Loop {value}')
        recursion(value - 1)

recursion(10)