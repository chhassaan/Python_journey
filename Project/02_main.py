name=input("Enter your name:")
health=100
coins=50
food=3
weapon="knife"
print("========================")
print(" ===SURVIVAL ISLAND===")
print("========================")
print("Name:",name)
print("Health:",health)
print("Coins:",coins)
print("Food:",food)
print("Weapon:",weapon)
while True:

    print("\n1. Forest")
    print("2. River")
    print("3. Inventory")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("You entered the forest 🌲")

    elif choice == "2":
        print("You went to the river 🌊")

    elif choice == "3":
        print("Your inventory:")
        print("Food:", food)
        print("Weapon:", weapon)
        print("Coins:", coins)

    elif choice == "4":
        print("Game Over. Thanks for playing!")
        break

    else:
        print("Invalid choice!")