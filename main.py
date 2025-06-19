food_item = ['Momo','burger','biriyani']
food_item_price = [50,150,300]


def show_menu_item():
    print('welcome to hansle!')
    
    for i in range(0,3):
        print(f"{food_item[i]} - {food_item_price[i]}/-")

def take_order():
    num_items = int(input("how many items you want to buy?"))
    for i in range(num_items):
        item = input(f"Enter item name:")
        quantity = int(input("Enter quantity"))

def generate_bill():
     item = input(f"Enter item name:")
     quantity = int(input("Enter quantity"))
    
     if item in food_item:
            price = food_item_price[item]
            total = price * quantity
            gst = total * 0.05
            final_amount = total + gst
            print("Bill")
            print(f"{total}/-")
            print(f"{gst:}")
            print(f"{final_amount}")
             

show_menu_item()
take_order()
generate_bill()


