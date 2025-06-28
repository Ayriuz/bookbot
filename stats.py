# File: stats.py
# --- a/file:///home/nix/codespace/github.com/Ayriuz/bookbot

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    count_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def sort_character_count(char_count):
    alpha_count = []
    for char, num in char_count.items():
        if char.isalpha():
            alpha_count.append((char, num))
    alpha_count.sort(key=lambda x: x[1], reverse=True)
    return alpha_count


