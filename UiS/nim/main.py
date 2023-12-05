def calculate_nim_sum(cards):
    xor_sum = 0
    for card in cards:
        xor_sum ^= card
    return xor_sum

def make_move(cards, is_player1, opponent_move=None):
    nim_sum = calculate_nim_sum(cards)
    print("Current board:", cards)

    if nim_sum == 0:
        if is_player1:
            print("You won!")
        else:
            print("Player 1 won!")
        return None

    if is_player1:
        move = int(input("1, 2, or 3\n"))
        if move not in [1, 2, 3] or move > max(cards):
            print("feil")
            return make_move(cards, is_player1, opponent_move)
    else:
        # Player 2's turn
        move = nim_sum ^ max(cards)
        print("Player 2 removed", move)

    cards.pop()
    return move

# Main game loop
def nim_game():
    
    is_player1 = input("Do you want to be Player 1? (yes/no): ").lower() == 'yes'

            
    cards_on_board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    while True:
        move = make_move(cards_on_board, is_player1)
        if move is None:
            break
        
        
        is_player1 = not is_player1

# Run the game
nim_game()
