# It evaluates unit price to sell for a stock given assuming that the total money will increase by 2 percent
def stock(unit_price_to_buy, total_number_of_stock):
    purchase_price = unit_price_to_buy * total_number_of_stock
    print("purchase price : {}".format(purchase_price))
    estimated_price = (102 * purchase_price) / 100
    print("estimated price : {}".format(estimated_price))
    unit_price_to_sell = (estimated_price * unit_price_to_buy) / purchase_price
    print(unit_price_to_sell)


stock(16.98, 74)
#####
