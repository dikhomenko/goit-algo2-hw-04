from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list):
            raise ValueError("Input must be a list of strings.")

        for i in range(len(strings[0])):
            char = strings[0][i]
            for string in strings[1:]:
                if i >= len(string) or string[i] != char:
                    return strings[0][:i]
        return strings[0]


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"
    print("Longest common prefix:", trie.find_longest_common_word(strings))  # "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"
    print("Longest common prefix:", trie.find_longest_common_word(strings))  # "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
    print(
        "Longest common prefix:", trie.find_longest_common_word(strings)
    )  # empty string
