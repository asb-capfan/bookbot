def get_num_words(book_content):
    return len(book_content.split())

def get_char_count(book_content):
    char_list = [char for char in book_content]

    char_count = {}

    for char in char_list:
        lc_char = char.lower()
        if lc_char in char_count:
            char_count[lc_char] += 1
        else:
            char_count[lc_char] = 1  # Ersten Eintrag setzen
    
    return char_count

def sort_char_count(char_dict):
    sorted_dicts = [
        # Each dictionary should have two key-value pairs: one for the character itself and one for that character's count.
        # {'char': 'x', 'count': n}, ...
    ]

    sorted_char_dict = dict(sorted(char_dict.items(), key=lambda x: x[1], reverse=True))
    for char in sorted_char_dict:
        sorted_dicts.append({"char": char, "count": sorted_char_dict[char]})
    
    return sorted_dicts