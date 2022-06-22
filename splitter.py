""" write a function to split a string 
of words separated by commas and spaces into two lists, words and separators."""


def splitter(text):
    listword = []
    listsep = []
    for i in range(len(text)):
        if text[i] == " " or text[i] == ",":
            
            listsep.append(text[i])
            listword.append(text[:i])
            listword.append(text[(i+1):])
            break

        else:
            continue
    for i in range(len(text)):
        if text[i] == ",":
            listsep.append(",")
            for j in range(len(listword)):
                if "," in listword[j]:
                    temp = str(listword[j])
                    for k in range(len(temp)):
                        if temp[k] == ",":    
                            t = temp[:k] + temp[(k+1):]
                            listword[j] = t



    print("Your separator is " + str(listsep) + "and the words are: " + str(listword))
         

splitter("apple, orange  blue,")

