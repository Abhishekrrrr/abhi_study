def student_discount(price):
    price = price - (price * 10) / 100
    return price

def additional_discount_regular(rprice):
    rprice = rprice - (rprice * 5) / 100
    return rprice

selling_price = 1000
print(additional_discount_regular(student_discount(selling_price)))

