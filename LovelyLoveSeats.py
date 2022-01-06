# 2022Regaining-skills
#Step 1 describe product
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

#Step 2 set price of loveseat
lovely_loveseat_price = 254.00

#Step 3 add another product description
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."


#Step 4 set price of Settee
stylish_settee_price = 180.50

#Step 5 One more item to add description
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade"

#Step 6 add price of product
luxurious_lamp_price = 52.15

#Step 7 Sales tax
sales_tax = 0.088

#Step 8 keep tabs on customer 1 total
customer_one_total = 0

#Step 9 string list of descrption of items that the customer buys
customer_one_itemization = ""

#Step 10 customer one purchases love seat
customer_one_total += lovely_loveseat_price
#Step 11 keep track of item description
customer_one_itemization += lovely_loveseat_description

#Steps 12 and 13 same as 10 and 11 but for luxurious lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += " " + luxurious_lamp_description

#Step 14 customer one check out with added sales tax
customer_one_tax = customer_one_total * sales_tax
#Step 15 add sales tax to total
customer_one_total += customer_one_tax

#Step 16 and 17 printing out itemization of customer one
print("Cusstomer One Items: " + customer_one_itemization)

#Step 18 and 19 print total cost

print("Customer One Total: " + str(customer_one_total))


