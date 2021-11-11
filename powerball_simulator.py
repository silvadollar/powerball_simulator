from random import choice

def get_winning_ticket(possibilities, power):
    winning_ticket = []
    pulled_power = choice(power)

    while len(winning_ticket) < 5:
        pulled_item = choice(possibilities)

        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    winning_ticket.append(pulled_power)

    return winning_ticket


def get_my_ticket(possibilities, power):
    my_ticket = []
    pulled_power = choice(power)

    while len(my_ticket) < 5:
        pulled_item = choice(possibilities)

        if pulled_item not in my_ticket:
            my_ticket.append(pulled_item)

    my_ticket.append(pulled_power)

    return my_ticket


def check_ticket(mine, winner):
    """This checks if my ticket matches the winning ticket."""
    mine_power_check = []

    pulled_mine_power = mine.pop()
    mine_power_check.append(pulled_mine_power)

    for element in mine:
        if element not in winner:
            return False

    for powerball in mine_power_check:
        if powerball not in winner_power:
            return False

    return True


def main():

    print(f"Welcome to the Powerball simulator where you can choose to \"buy\" as many tickets as you want. "
          f"This program will create one winning ticket and check every one of your new tickets to see if you won. "
          f"Then we will let you know how much you won. Hopefully you get the GRAND PRIZE! \n")
    possibilities = [x for x in range(1, 70)]
    power = [x for x in range(1, 27)]

    winner = get_winning_ticket(possibilities, power)
    # below is just to test a winner
    # winner = [1, 11, 31, 3, 5, 11]
    winner_power = []
    pulled_winner_power = winner.pop()
    winner_power.append(pulled_winner_power)

    plays = 0
    payout = 0
    payout1mil = 0
    payout50k = 0
    payout100 = 0
    payout7 = 0
    payout4 = 0
    won = False

    max_attempts = eval(input("How many Powerball tickets would you like to buy: "))

    while not won:
        mine = get_my_ticket(possibilities, power)
        # below is just to test a winner
        # mine = [1, 31, 3, 11, 5, 11]
        won = check_ticket(mine[:], winner)

        mine_power = []
        pulled_mine_power = mine.pop()
        mine_power.append(pulled_mine_power)

        plays += 1
        solution = set(mine).intersection(winner)

        if plays >= max_attempts:
            print("\nReached max attempts...")
            print(f"Winning ticket: {winner}:{winner_power}")
            print(f"You won ${payout:,d}.00 in total.")
            print(f"You won {payout1mil:,d} $1,000,000 prizes")
            print(f"You won {payout50k:,d} $50,000 prizes")
            print(f"You won {payout100:,d} $100 prizes")
            print(f"You won {payout7:,d} $7 prizes")
            print(f"You won {payout4:,d} $4 prizes")
            break

        if won:
            print("\nGRAND PRIZE WINNER!!!!")
            print(f"Your ticket: {mine}:{mine_power}")
            print(f"Winning ticket: {winner}:{winner_power}")
            print(f"It took {plays} tries.")
            print(f"You won ${payout:,d}.00 in total")
            print(f"You won {payout1mil:,d} $1,000,000 prizes")
            print(f"You won {payout50k:,d} $50,000 prizes")
            print(f"You won {payout100:,d} $100 prizes")
            print(f"You won {payout7:,d} $7 prizes")
            print(f"You won {payout4:,d} $4.00 prizes")
        else:
            # print(f"Your ticket: {mine}:{mine_power}")
            # print(f"Winning ticket: {winner}:{winner_power}")
            if len(solution) == 5 and mine_power != winner_power:
                payout += 1_000_000
                payout1mil += 1
            elif len(solution) == 4 and mine_power == winner_power:
                payout += 50_000
                payout50k += 1
            elif len(solution) == 4 and mine_power != winner_power:
                payout += 100
                payout100 += 1
            elif len(solution) == 3 and mine_power == winner_power:
                payout += 100
                payout100 += 1
            elif len(solution) == 3 and mine_power != winner_power:
                payout += 7
                payout7 += 1
            elif len(solution) == 2 and mine_power == winner_power:
                payout += 7
                payout7 += 1
            elif len(solution) == 1 and mine_power == winner_power:
                payout += 4
                payout4 += 1
            elif len(solution) == 2 and mine_power == winner_power:
                payout += 4
                payout4 += 1
            else:
                payout += 0


if __name__ == '__main__':
    main()
