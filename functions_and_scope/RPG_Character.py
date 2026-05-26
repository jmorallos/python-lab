full_dot = "●"
empty_dot = "○"


def create_character(character_name, strength, intelligence, charisma):
    # character_name != str
    # "The character name should be a string"
    if not isinstance(character_name, str):
        return "The character name should be a string"

    # character_name == ""
    # "The character should have a name"
    if character_name.strip() == "":
        return "The character should have a name"

    # character_name > 10
    # "The character name is too long"
    if len(character_name) > 10:
        return "The character name is too long"

    # character_name =="Value Value"
    # "The character name should not contain spaces"
    if " " in character_name:
        return "The character name should not contain spaces"

    # statsAll == "int"
    # "All stats should be integers"
    if not all(isinstance(stat, int) for stat in (strength, intelligence, charisma)):
        return "All stats should be integers"

    # statsAll > 0
    # "All stats should be no less than 1"
    if any(stat < 1 for stat in (strength, intelligence, charisma)):
        return "All stats should be no less than 1"

    # statsAll > 4
    # "All stats should be no more than 4"
    if any(stat > 4 for stat in (strength, intelligence, charisma)):
        return "All stats should be no more than 4"

    # statsAll == 7
    # "The character should start with 7 points"
    total_pts = strength + intelligence + charisma
    if total_pts != 7:
        return "The character should start with 7 points"

    # if valid
    # character_name
    # STR
    # INT
    # CHA

    return f"{character_name}\nSTR {full_dot * strength + (empty_dot * (10 - strength))}\nINT {full_dot * intelligence + (empty_dot * (10 - intelligence))}\nCHA {full_dot * charisma + (empty_dot * (10 - charisma))}"


print(create_character("KeneJ", 3, 2, 1))

