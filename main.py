from stats import word_count, character_count, sorted_list

def get_book_text(filepath):
    with open(filepath, encoding='UTF8') as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    sorted=sorted_list(character_count(book_text))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    for i in sorted:
        if i["char"].isalpha() == False:
            continue
        else:
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()