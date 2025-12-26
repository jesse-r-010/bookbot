def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    lower_text = text.lower()
    letter_collection = {}
    for letter in lower_text:
        if letter in letter_collection:
            letter_collection[letter] += 1
        else:
            letter_collection[letter] = 1
    return letter_collection    

def return_number(dict):
    return dict["num"]

def sorted_list(dict):
    list = []
    for i in dict:
        letter_dict = {"char": i, "num": dict[i]}
        list.append(letter_dict)
    list.sort(reverse=True, key=return_number)
    return list