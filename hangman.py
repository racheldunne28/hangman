import random



def draw_hangman(fails):
    HANGMAN = (
    """
    -----
    |   |
    |
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |  -+-
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |  |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |  | 
    |  | 
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |  | | 
    |  | 
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |  | | 
    |  | | 
    |
    --------
    """)
    print(HANGMAN[fails])
    
    
    
def generate_word(auto_generate = True):
    while auto_generate not in ["auto", "manual"]:
        print("Invalid response")
        auto_generate = input("Type 'auto' for an auto_generated word or type " +
                          "'manual' to enter your own word: ") 
    if auto_generate == "auto":
        word = random.choice(["hello", "goodbye", "kitchen", "platform",
                              "spider", "genie", "mushroom", "orange",
                              "chicken", "box", "squelch", "door",
                              "stiletto", "slippers", "shot",
                              "hangman"])
    elif auto_generate == "manual":
        word = input("Please input your word: ")
    return(word)
    
    

def check_letter_in_word(letter, word, guessed_letters,fails):
    output = str()
    round_successes = 0
    for num in range(len(word)):
        if set(word[num]).issubset(set(guessed_letters)):
            print(word[num])
            output = " ".join([output, word[num]])
        elif word[num] == letter:
            output = " ".join([output, word[num]])
            round_successes = round_successes + 1
            if not letter in guessed_letters:
                guessed_letters.append(word[num])
        else:
            output = " ".join([output, "_"]) 
           
    if round_successes == 0:
        fails = fails + 1
    print(fails)
    return(output, guessed_letters, fails)           
        
        
            
def run_game():
    print("Welcome to hangman")
    auto_generate = input("Type 'auto' for an auto_generated word or type " +
                          "'manual' to enter your own word: ") 
    word = generate_word(auto_generate)  
    output = str()
    for num in range(len(word)):
        output = " ".join([output, "_"])
    print(output)
    guessed_letters = []
    fails = 0
    while "_" in set(output):
        letter = input("Enter your guess: ")
        output, guessed_letters, fails = check_letter_in_word(letter, word, 
                                                              guessed_letters,
                                                              fails)
        draw_hangman(fails)
        print(output)
        if fails == 10:
            break
    if fails < 10:
        print("You win!")
    else:
        print("You lose!")
