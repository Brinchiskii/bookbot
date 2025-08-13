def get_word_count(file_content):
    words = file_content.split()
    
    return len(words)

def get_character_count(file_content):
    characters = list(file_content.lower())
    characters_count = {}

    for c in characters:
        if c in characters_count:
            characters_count[c] += 1
        else: 
            characters_count[c] = 1

    return characters_count

def sort_on(chars):
    return chars["num"]

def get_sorted_dict(char_dict):
    dict_list = []
    
    for char in char_dict:
        count = char_dict[char]
        dict_list.append({"char": char, "num": count})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
