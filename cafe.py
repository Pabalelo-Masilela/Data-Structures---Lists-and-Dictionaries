menu = ['powerade','water','sweets','chips']
stock = {'powerade':'15',
         'water':'20',
         'sweets':'10',
         'chips':'10'}
price = {'powerade':'16.5',
         'water':'13.5',
         'sweets':'12.0',
         'chips':'7.0'}
total_stock = 0
for item in menu:
   item_value = float(stock[item]) * float(price[item])
   total_stock += item_value
print(f"Total stock value: R{total_stock}")