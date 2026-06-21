is_member = True
purchase_total = 90

if is_member == True and purchase_total >= 100:
    print("You get a discount!")

else:
    print("Discount Unavailable")

has_coupon = False
is_vip = False

if has_coupon or is_vip:
    print("You get a discount!")
else:
    print("Discount Unavailable")