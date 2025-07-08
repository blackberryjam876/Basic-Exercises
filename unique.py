"""print the entry with the highest number of unique characters"""
def uniquee(arr):
    if not arr:
        print("Input list is empty.")
        return
    
    non_empty = [s for s in arr if s != ""]

    if not non_empty:
        print("No non‐empty strings in the input.")
        return
    
    repeat_counts = []
    unique_counts = []
    for s in non_empty:
        rep = sum(1 for ch in s if s.count(ch) > 1)
        repeat_counts.append(rep)
        unique_counts.append(len(set(s)))

    idx_most_repeats = repeat_counts.index(max(repeat_counts))
    idx_most_unique  = unique_counts.index(max(unique_counts))
    print(f"Item with the most repeated chars is: {non_empty[idx_most_repeats]!r}")
    print(f"Item with the most unique chars is:  {non_empty[idx_most_unique]!r}")
        
#Examples
uniquee(["abc", "apple","strawberry", " "])

uniquee(["", "a", "aa", "abcd", "aabbcc","aabbccghjkl"])