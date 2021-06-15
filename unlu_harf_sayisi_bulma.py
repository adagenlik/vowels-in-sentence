def text(sentence,number=0):
    letter="aeiouAEIOU"

    for character in sentence:
        if character in letter:
            number+=1
    return number

sentence=input("Type a sentence: ")
print("There is {} vowels in this sentence".format(text(sentence)))