import random

dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

def parse_input(input_string): # validate correct input

    while True:
        if input_string.strip() in {"1", "2", "3", "4" , "5", "6"}:
            return int(input_string)
        else:
            input_string = input("Invalid value. How many dice would you like to roll? [1-6]: ")

def roll_dice(dice_roll): # Generate random numbers of dices

    dices_numbers = []

    for _ in range(dice_roll):
        dices_numbers.append(random.randint(1,6))
    
    return dices_numbers

def generate_roll_dices_diagram(result_numbers):
    #Add all the values of the result numbers
    dice_values = []
    for i in result_numbers:
        dice_values.append(dice_art[i])

    dice_format = []
    for row_idx in range(len(dice_art[1])): # rows of dice_art (5)
        dice_component = [] # reset list every time
        for i in dice_values:
            dice_component.append(i[row_idx]) # add each dice line together -> ['1[0]','2[0]'] -> [] -> ['1[1]','2[1]'] -> [] etc.. -> ['1[4]','2[4]']
        dice_rows = " ".join(dice_component) # convert to string  --> 1[0] 2[0] -> 1[1] 2[1] -> etc.. -> 1[4] 1[4]
        dice_format.append(dice_rows) # append it to the list -> [1[0] 2[0]] -> [1[0] 2[0], 1[1] 2[1]] -> [1[0] 2[0], 1[1] 2[1], 1[2] 1[2]]....

        # add diagram header 
        width = len(dice_format[0]) # total width of the dices
        header = " RESULT ".center(width, "~")

        dice_faces_diagram = "\n".join([header] + dice_format)  # Join Header + dice format
                                                                
    return dice_faces_diagram                                   
"""
                ~~  RESULT  ~~
                1[0]      2[0] (DICE)
                1[1]      2[1]
                1[2]      2[1]
"""


# ~~~~~ App's Main Code ~~~~~

dice_input = input("How many dice would you like to roll? [1-6]: ")
dice_validation = parse_input(dice_input)
dice_result = roll_dice(dice_validation)
dice_diagram = generate_roll_dices_diagram(dice_result)

print(f"\n{dice_diagram}")
