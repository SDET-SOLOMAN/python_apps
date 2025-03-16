from arts import day_8_art as art
print(art.logo)

people = {

}

print("Welcome to the secret auction program")

while True:
    user_name = input("What is your name:\n")
    user_bid = input("What is your bid$:\n")
    people[user_name] = int(user_bid)

    check_user = input("Is there another bidder? y/n: ")
    if check_user.lower() != "y":
        # winner = ["", 0]
        # for k,v in people.items():
        #     if v > winner[1]:
        #         winner = [k, v]
        # print(f"The winner of this auction is {winner[0]} and the bid is ${winner[1]}")
        winner_name, winner_bid = max(people.items(), key=lambda item: item[1])
        print(f"The winner of this auction is {winner_name} and the bid is ${winner_bid}")
        break
    else:
        print("\n" * 100)

