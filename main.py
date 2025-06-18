food_item = ['Momo','burger','biriyani']
food_item_price = [50,150,300]


def show_menu_item():
    print('welcome to hansle!')
    
    for i in range(0,3):
        print(f"{food_item[i]} - {food_item_price[i]}/-")


show_menu_item()