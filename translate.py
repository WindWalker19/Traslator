# The translate function converts all the vowels to a. Just for fun to look how the words look like if i convert the vowel letter
# present in them.

#first we want to ask the user for an input text.
def translate(phrase):
    #get an empty string where we could store the letters.
    new_phrase = ""
    #Then we want to loop through every letter.
    for letters in phrase:
        #Check if any of the letter consists of the vowel letter.
        #converts all the letters to lowercase and check for vowels.
        if letters.lower() in "aeiou":
            #check if letter is upper case. Helps solve caps issues.
            if letters.isupper():
                new_phrase += "A"
            else:
        # if letters == "a" or letters == "e" or letters == "i" or letters == "o" or letters == "u":
        #convert the vowel letter to a.
                new_phrase += "a"
        else:
            new_phrase += letters
    return(new_phrase)

print(translate("Umbrella"))
