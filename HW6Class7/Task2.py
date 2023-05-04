# Input data:
# Compute the total price of the stock where the total
# price is the sum of the price of an item multiplied by
# the quantity of this exact item.
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_price = {k: prices[k]*stock[k] for k in prices}
print(total_price)
get_price_values = total_price.values()
print('the total price u need pay is:'+ str(sum(get_price_values))+'$')

