def word_count(text):
    words = text.split()
    return len(words)


# takes text from the book as a string and returns the number of times each character appears
# convert any character to lower case with .lower()
# use dictionary  of String -> Integer
# import and call the function in main.py and capture results in new variable
# after printing the word count, print dictionary  of characters and thier counts

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# add new function that takes dictionary of characters and thier counts and returns a sorted list of dictionaries

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

  
        
