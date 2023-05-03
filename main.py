def count_words(txt): 
    count = 0 
    for str in txt: 
        count+=1 
    return count




def count_letters(txt): 
    count_letters =  {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 
                      'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 
                      's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for str in txt:
        str = str.lower()
        for char in str: 
            if char in count_letters: 
                count_letters[char]+=1 
    return count_letters






print("-- Begin report of books/frankenstein.txt --")
with open("/home/ckindred/workspace/github.com/CarterK33/bookbot/books/frankenstein.txt") as f: 
    file_contents = f.read() 
    file_contents = file_contents.split()
    word_count = count_words(file_contents)
    ans_dict = count_letters(file_contents)

print(f"{word_count} words found in the document")

for key in ans_dict: 
    print(f"The '{key}' character was found {ans_dict[key]} times")

print("-- End Report --")










