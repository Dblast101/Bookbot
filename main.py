def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        number = count(file_contents)
        amount = letters(file_contents)
        list_amount = change(amount)
        list_amount.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number} words found in the document\n")
    for item in list_amount:
        print(f"The '{item['Letter']}' character was found {item['num']} times.")
    print("--- End report ---")

def count(amount):
    total = amount.split()
    return len(total)

def letters(words):
    lower_letters = words.lower()
    seperated = list(lower_letters)
    sep_letters = {}
    for letter in seperated:
        if letter in sep_letters:
            sep_letters[letter] += 1
        else:
            sep_letters[letter] = 1
    return sep_letters

def change(group):
    new_list = []
    dump = []
    for i in group:
        if i.isalpha() == False:
            dump.append(i)
        else: 
            temp = {"Letter": i, "num": group[i]}
            new_list.append(temp)
    return new_list

def sort_on(fix):
    return fix["num"]

main()