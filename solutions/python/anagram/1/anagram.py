def find_anagrams(word, candidates):
    lower_word = word.lower()
    sorted_word = sorted(lower_word)
    is_anagram = []

    for canditate in candidates:
        canditate_lower = canditate.lower()
        if canditate_lower != lower_word and sorted(canditate_lower) == sorted_word:
            is_anagram.append(canditate)

    return is_anagram

