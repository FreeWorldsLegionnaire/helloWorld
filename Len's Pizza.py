# Your code below:
#Create kinds of pizzas I sell
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives","anchovies", "mushrooms"]

#Creating a list of prices for each slice
prices = [2, 6, 1, 3, 2, 7, 2]

#Count the number of 2$ slices and print
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#finding and storing length of toppings
num_pizzas = len(toppings)

#print string with num_pizzas
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#create 2D list combining pizza toppings with prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

#Print pizza and prices
print(pizza_and_prices)

#sorting pizza prices by ascending price
pizza_and_prices.sort()
#print(pizza_and_prices)

#store cheapest pizza
cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza)

#store priciest pizza
priciest_pizza = pizza_and_prices[-1]
#print(priciest_pizza)

#remove last slice since it was last of the given anchovy pizza
pizza_and_prices.pop()
#print(pizza_and_prices)

#add peppers pizza in sorted pizza and prices list while keeping it sorted
pizza_and_prices.insert(-2, [2.5, "peppers"])
#print(pizza_and_prices)

#Slice pizza and prices for 3 cheapest
three_cheapest = pizza_and_prices[0:3]

#print three cheapest
print(three_cheapest)
