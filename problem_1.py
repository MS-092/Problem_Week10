def find_linking_subword(word1, word2):
    len_word1 = len(word1)
    len_word2 = len(word2)

    max_length = min(len_word1, len_word2)

    # Initialize variables to store the linking subword and its length
    linking_subword = ""
    linking_length = 0

    # iterate the letters of the words
    for i in range(1, max_length + 1):
        
        # last letter of first word == first letter of second word
        if word1[-i:] == word2[:i] :
            linking_subword = word1[-i:]

    return linking_subword



word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")


linking_subword = find_linking_subword(word1, word2)

if linking_subword:
    print(f"Both words can be linked with the subword '{linking_subword}'.")
else:
    print("Both words cannot be linked.")
