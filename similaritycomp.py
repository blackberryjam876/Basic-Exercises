import argparse


def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Compute the Levenshtein distance between two strings.
    Using dynamic programming approach with O(len(s1) * len(s2)) time.
    """
    if s1 == s2:
        return 0
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    # Initialize matrix of zeros
    rows = len(s1) + 1
    cols = len(s2) + 1
    dist = [[0 for _ in range(cols)] for _ in range(rows)]

    # Populate matrix of distances
    for i in range(1, rows):
        dist[i][0] = i
    for j in range(1, cols):
        dist[0][j] = j

    # Compute DP matrix
    for i in range(1, rows):
        for j in range(1, cols):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dist[i][j] = min(
                dist[i - 1][j] + 1,      
                dist[i][j - 1] + 1,      
                dist[i - 1][j - 1] + cost 
            )

    return dist[-1][-1]


def similarity_ratio(s1: str, s2: str) -> float:
    """
    Compute a normalized similarity ratio between 0 and 1 based on Levenshtein distance.
    A ratio of 1 means the strings are identical.
    """
    distance = levenshtein_distance(s1, s2)
    max_len = max(len(s1), len(s2))
    if max_len == 0:
        return 1.0
    return 1.0 - (distance / max_len)


def is_similar(s1: str, s2: str, threshold: float = 0.8) -> bool:
    """
    Determine if 2 strings are similar based on a similarity threshold.
    Returns True if the similarity_ratio >= threshold.
    """
    return similarity_ratio(s1, s2) >= threshold


def main():
    parser = argparse.ArgumentParser(
        description="Compare two strings using Levenshtein distance and similarity ratio."
    )
    parser.add_argument("string1", type=str, help="First input string")
    parser.add_argument("string2", type=str, help="Second input string")
    parser.add_argument(
        "-t", "--threshold", type=float, default=0.8,
        help="Similarity threshold between 0 and 1 (default: 0.8)"
    )
    args = parser.parse_args()

    dist = levenshtein_distance(args.string1, args.string2)
    ratio = similarity_ratio(args.string1, args.string2)
    similar = is_similar(args.string1, args.string2, args.threshold)

    print(f"Levenshtein distance: {dist}")
    print(f"Similarity ratio: {ratio:.2f}")
    print(
        f"Strings are {'similar' if similar else 'not similar'} "
        f"(threshold: {args.threshold})"
    )


if __name__ == "__main__":
    main()
