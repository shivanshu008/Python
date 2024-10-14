#function definition
# Time Complexity: O(n)
def findmaxProfit(price):
    #Initialization
    minPrice=float('inf')
    maxProfit=0
    for i in range(len(price)):
        if price[i] < minPrice:
            minPrice = price[i]
        elif price [i] - minPrice > maxProfit:
            maxProfit = price[i] - minPrice
    return maxProfit

#Driver Code
price = [7,1,5,3,6,4]
maxProfit_value = findmaxProfit(price)
print("The maximum profit of buying and selling the stocks is: ", maxProfit_value)