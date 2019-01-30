#dictionaries

prices = {
    'apple': 1.20,
    'orange': 3.45,
    'banana': 8.47,
    'pineapple':23.67,
}

for i in prices:
    print('{} - {:.2f}'.format(i, prices[i]))

for i,j in prices.items():
    print('{} - {:.2f}'.format(i, j))

