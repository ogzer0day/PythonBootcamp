
def cast_spell(spell_name: str, targets: list) -> dict:
        key = spell_name
        value = targets

        my_dict_comp = {str(key).replace("'", ""): value}
        return (str(my_dict_comp).replace("{", "").replace("}", ""))

print(cast_spell("Card", ['play', 'get_card_info', 'is_playable']))
