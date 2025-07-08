""" write a function to split a string 
of words separated by commas and spaces into two lists, words and separators."""

import sys 
from typing import List, Tuple

def splitter(text: str) -> Tuple[List[str], List[str]]:
    words: list[str] = []
    seps: list[str] = []
    buffer: list[str] = []

    for ch in text:
        if ch == ' ' or ch == ',':
            # end of a word; append and reset buffer
            words.append(''.join(buffer))
            seps.append(ch)
            buffer.clear()
        else:
            buffer.append(ch)

    if buffer:
        words.append(''.join(buffer))

    return words, seps

def main() -> None:
    try:
        user_input = input("Enter text to split (by spaces and commas): ")
    except EOFError:
        print("No input provided. Exiting.", file=sys.stderr)
        sys.exit(1)

    words, seps = splitter(user_input)

    print("\nWords:", words)
    print("Separators:", seps)

if __name__ == '__main__':
    main()

