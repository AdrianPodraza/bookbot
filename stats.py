def count_words(text):
    words = text.split()
    return len(words)

def unique_chars(text):
    counts = {} 
    for char in text:
        c = char.lower()
        counts[c] = counts.get(c, 0) + 1
    return counts
    
def sort_on(items):
    return items["num"]

def final(dictionary):
    list_dictionaries=[]
    for key in dictionary:
        list_dictionaries.append({"char":key, "num":dictionary[key]})
    list_dictionaries.sort(reverse=True, key=sort_on)
    return list_dictionaries