# main_script.py
from screens import start_screen, end_screen

## Variables
language = "fr" # Set the language (either "eng" or "fr")
image_filename = "openSF.png" # Image filename (should be placed in the same directory as the script)

scores = { # Create a dictionary of example stats and scores
    "total_score": 3275,
    "flight_score": 1200,
    "fortress_score": 500,
    "mine_score": 750,
    "bonus_score": 825,
    "numberofdeath": 13,
    "numberofdestroyedfortress": 2,
    "numberofdestroyedmines": 4,
    "numberofmines": 12,
    "numberofdestroyedbonuses": 1,
    "numberofbonuses": 8
}

# Show screens
start_screen(language, image_filename) # Show the start screen
end_screen(language, scores) # Show the end screen with the game stats
