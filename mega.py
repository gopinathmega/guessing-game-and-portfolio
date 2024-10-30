import random
import math
import streamlit as st

st.write("=========================================================================")
st.title("WELCOME TO GUESSING GAME")
st.write("=========================================================================")
st.header("Hello User We can play a game.")
st.write("...................................................................................................")
st.subheader("1. User Guessing") 

def optimal_guessing_game():
    st.title("Optimal Number Guessing Game")
    st.write("Try to guess the number I'm thinking of in as few attempts as possible!")

    # Step 1: User sets the range
    lower_bound = st.number_input("Enter the lower bound of the range:", value=1, step=1)
    upper_bound = st.number_input("Enter the upper bound of the range:", value=100, step=1)

    # Validate the range
    if lower_bound >= upper_bound:
        st.error("Invalid range! Ensure the upper bound is greater than the lower bound.")
        return

    # Step 2: Initialize session state variables
    if "target_number" not in st.session_state:
        st.session_state.target_number = random.randint(int(lower_bound), int(upper_bound))
        st.session_state.attempts = 0
        st.session_state.current_lower = int(lower_bound)
        st.session_state.current_upper = int(upper_bound)
        st.session_state.game_over = False

    # Calculate the optimal number of attempts using binary search
    max_attempts = math.ceil(math.log2(st.session_state.current_upper - st.session_state.current_lower + 1))
    st.write(f"Try to guess the number within {max_attempts} attempts!")

    # Step 3: User's guess input
    user_guess = st.number_input(
        "Enter your guess:",
        min_value=st.session_state.current_lower,
        max_value=st.session_state.current_upper
    )

    # Step 4: Button to submit the guess
    if st.button("Submit Guess") and not st.session_state.game_over:
        st.session_state.attempts += 1

        # Check if the guess is correct, too high, or too low
        if user_guess < st.session_state.target_number:
            st.warning("Too low! Try a higher number.")
            st.session_state.current_lower = user_guess + 1  # Narrow down the lower bound
        elif user_guess > st.session_state.target_number:
            st.warning("Too high! Try a lower number.")
            st.session_state.current_upper = user_guess - 1  # Narrow down the upper bound
        else:
            st.success(f"Congratulations! You guessed the number {st.session_state.target_number} in {st.session_state.attempts} attempts.")
            st.balloons()
            st.session_state.game_over = True

    # Display a "Play Again" button once the game is over
    if st.session_state.game_over:
        if st.button("Play Again"):
            del st.session_state.target_number
            del st.session_state.attempts
            del st.session_state.current_lower
            del st.session_state.current_upper
            st.session_state.game_over = False

# Run the game
optimal_guessing_game()

#Machine finding the value

import streamlit as st

# Set up Streamlit application
st.title("Machine Guessing Game with Binary Search")
st.write("Think of a number within the specified range, and I'll try to guess it!")
st.write("...................................................................................................")
st.subheader("2. Machine Guessing") 
# Initialize session state variables
if "low" not in st.session_state:
    st.session_state.low = 1
if "high" not in st.session_state:
    st.session_state.high = 100
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "guess" not in st.session_state:
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
if "guessed" not in st.session_state:
    st.session_state.guessed = False

# Reset the game
if st.button("Reset Game"):
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.attempts = 0
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
    st.session_state.guessed = False
    st.write("Game has been reset. Think of a new number!")

# Game logic
if not st.session_state.guessed:
    st.write(f"My guess is: {st.session_state.guess}")
    
    # Get feedback from the user
    feedback = st.radio("Is my guess too high, too low, or correct?", ("Too High", "Too Low", "Correct"))

    # Adjust range based on feedback
    if feedback == "Too High":
        st.session_state.high = st.session_state.guess - 1
        st.session_state.attempts += 1
    elif feedback == "Too Low":
        st.session_state.low = st.session_state.guess + 1
        st.session_state.attempts += 1
    elif feedback == "Correct":
        st.session_state.guessed = True
        st.session_state.attempts += 1
        st.write(f"I guessed your number! It took me {st.session_state.attempts} attempts.")
        st.balloons()

    # Update the guess using binary search
    if not st.session_state.guessed:
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
else:
    st.write("Press 'Reset Game' to play again.")
