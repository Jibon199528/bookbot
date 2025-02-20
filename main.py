letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

contens = main()

def count_words(main):
    main_list = main.split()
    return len(main_list)

number_words  = count_words(contens)

def count_letter(main):
    book_dict = {}
    for letter in main.lower():
        if letter.lower() not in book_dict:
            book_dict[letter.lower()] = 1
        elif letter in book_dict:
            book_dict[letter.lower()] +=1
    return book_dict

number_letters = count_letter(contens)

def sort_dict(dict):
    new_dict = {}
    for key in dict:
        if key in letter_list:
            new_dict[key] = dict[key]
    return new_dict

sorted_dict = sort_dict(number_letters)

def dict_to_list(dict):
    dict_list = []
    for pair in dict:
        dict_list.append({"name": pair,"num": dict[pair]})
    return dict_list

dict_list = dict_to_list(sorted_dict)

def sort_on(dict):
    return dict["num"]



dict_list.sort(reverse= True, key=sort_on)


def report():
    print(f"--- Begin report of books/frankenstein.txt ---")
    
    print(f"{number_words} words found in the dokument")
    print(" ")
    for dict in dict_list:
        print(f"The '{dict["name"]}' character was found {dict["num"]} times")
    print("--- End report ---")

report()
    


    