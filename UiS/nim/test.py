def calculate_nim_sum(cards):
    nim_sum = 0
    for card in cards:
        nim_sum ^= card
    return nim_sum

def find_best_move(cards):
    nim_sum = calculate_nim_sum(cards)

    # If nim_sum is already zero, play in a way to keep it zero
    if nim_sum == 0:
        for i, card in enumerate(cards):
            if card > 0:
                return min(card, 3)  # Take 1, 2, or 3 cards from the i-th pile

    # Otherwise, find a move that results in nim_sum of zero
    for i, card in enumerate(cards):
        if (card ^ nim_sum) < card:
            return card - (card ^ nim_sum)  # Ensure the computer chooses 1, 2, or 3

    # If nim_sum is not zero and no optimal move found, take 1 card
    return 1

def play_nim():
    total_cards = 13

    while total_cards > 0:
        print(f"Remaining cards: {total_cards}")
        
        # Opponent's move
        opponent_move = int(input("Enter your opponent's move (1, 2, or 3): "))
        if opponent_move < 1 or opponent_move > 3 or opponent_move > total_cards:
            print("Invalid move. Please enter a valid move.")
            continue
        total_cards -= opponent_move

        # Check if Opponent has won
        if total_cards == 0:
            print("Opponent wins!")
            break

        # Calculate and print the recommended move
        computer_move = find_best_move([total_cards])
        computer_move = min(computer_move, total_cards)
        computer_move = max(1, min(computer_move, 3))  # Ensure computer move is 1, 2, or 3
        print(f"Recommended move for you: {computer_move}")

        # Make the move
        total_cards -= computer_move

        # Check if Computer drew the last card
        if total_cards == 0:
            print("Computer wins!")
            break

    print("You win!")

# Uncomment the line below to start the game
play_nim()
