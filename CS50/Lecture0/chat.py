guest_list = ["Alice", "Bob", "Charlie", "David"]
banned_list = ["Kevin", "Malory"]
current_inside = 0
max_capacity = 3

def namecheck():
    global current_inside
    name = input("Enter your name: ")
    if name in banned_list:
        print("Security, take him away!")
    elif name in guest_list:
        if name == guest_list[0]:
            print("Welcome, go to VIP lounge!")
            current_inside += 1
        elif current_inside >= max_capacity:
            bribe = input("Do you want to bribe bouncer? (yes/no): ")
            if bribe == "yes":
                guest_list.remove(name)
                guest_list.insert(0, name)
                print("Success! Enter your name again to get in VIP!")
            else:
                print("Then you can't come in")
        else:
            print("Welcome, " + name + ". Enjoy the party!")
            current_inside += 1
    else:
        print("Sorry, you're not on the list!")

while True:
    namecheck()