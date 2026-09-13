full_dot = '●'
empty_dot = '○'

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name ==  "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if ' ' in name:
        return 'The character name should not contain spaces'
    stats = {'STR': strength, 'INT': intelligence, 'CHA': charisma}
    for value in stats.values():
        if not isinstance(value, int):
            return 'All stats should be integers'
    for value in stats.values():
        if value < 1:
            return 'All stats should be no less than 1'
        if value > 4:
            return 'All stats should be no more than 4'
    if sum(stats.values()) != 7:
        return 'The character should start with 7 points'
    
    str_line = "STR " + (full_dot * strength) + (empty_dot * (10 - strength))
    int_line = "INT " + (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    cha_line = "CHA " + (full_dot * charisma) + (empty_dot * (10 - charisma))
    return name + "\n" + str_line + "\n" + int_line + "\n" + cha_line

create_character("ren", 3, 3, 1)
print(create_character("ren", 3, 3, 1))
