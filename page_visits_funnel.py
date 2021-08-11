##import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_cart = pd.merge(visits, cart, how="left")
print(visits_cart.head())
visits_cart_length = len(visits_cart)
print(visits_cart_length)
null_cart_time = visits_cart[visits_cart.cart_time.isnull()]
print(null_cart_time.head())

null_cart_time_percent = (len(null_cart_time)/float(visits_cart_length)) * 100
print(null_cart_time_percent)

cart_checkout = pd.merge(visits, cart, how="left")
print(cart_checkout.head())
cart_checkout_length = len(cart_checkout)
null_cart_checkout = cart_checkout[cart_checkout.cart_time.isnull()]

null_cart_checkout_percent = (len(null_cart_time)/float(cart_checkout_length)) * 100
print(null_cart_checkout_percent)

all_data = visits.merge(cart, how="left").merge(checkout, how="left").merge(purchase, how="left")
print(all_data.head())

all_data_length = len(all_data)
null_purchase_percent = (len(all_data[all_data.purchase_time.isnull()])/float(all_data_length)) * 100
print("=======Purchase=======")
print(null_purchase_percent)

null_visit_percent = (len(all_data[all_data.visit_time.isnull()])/float(all_data_length)) * 100
print("=======Visits=======")
print(null_visit_percent)

null_cart_percent = (len(all_data[all_data.cart_time.isnull()])/float(all_data_length)) * 100
print("=======Cart=======")
print(null_cart_percent)

null_checkout_percent = (len(all_data[all_data.checkout_time.isnull()])/float(all_data_length)) * 100
print("======Checkout========")
print(null_checkout_percent)

print(max(null_visit_percent, null_cart_percent, null_checkout_percent, null_purchase_percent))

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data.time_to_purchase)

print(all_data.time_to_purchase.mean())



