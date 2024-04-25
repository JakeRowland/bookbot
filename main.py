def main():
    with open("books/frankenstein.txt") as f:
        file_contents=f.read()
        #add code here if you want to process or print file_contents
        number_of_words=wordcount(file_contents)
    print (f"{number_of_words} words found in document")

#This splits file_contents into words and the counts/outputs the number of words
def wordcount(file_contents):
    words=file_contents.split()
    count=len(words)
    return count

#This spilts the file_contents into letters and returns the count for each letter
def lettercount(file_contents):
    letters_dict={}
    lower_case=file_contents.lower()
    for letter in lower_case:
        if letter in letters_dict:
            letters_dict[letter]=letters_dict[letter]+1
        else:
            letters_dict[letter]=1
    return letters_dict


#This calls the main function
if __name__ == "__main__":
    main()
