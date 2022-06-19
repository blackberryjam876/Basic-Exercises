"""print the entry with the highest number of unique characters"""
def uniquee(arr):
    k =0
    counts = []
    for i in range(len(arr)):
        y = arr[i]
        #print(y)
        k=0
        for j in range(len(y)):

            if y[j] in (y[:j] or y[(j+1):]):
                k = k+1
            else:
                continue
        if k != None:
            print ("repetion for: " + arr[i] + " with " + str(k) + " repeated chars.")
            counts.append(k)
       
    if k != None:
        indmax = counts.index(max(counts))
        indmin = counts.index(min(counts))
        print("Item with the most repeated chars is: " + arr[indmax])
        print("Item with the most unique chars is: " + arr[indmin])
        
    else:
        print("All content is unique.")


uniquee(["abc", "apple","strawberry", " "])