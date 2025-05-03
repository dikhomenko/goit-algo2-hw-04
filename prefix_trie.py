from trie import Trie


class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError("The pattern must be a string.")

        count = 0

        # Traverse all words in the trie
        for word in self.keys():
            if word.endswith(pattern):
                count += 1

        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("The prefix must be a string.")

        # Start traversal from the root node
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    print("Words ending with 'e':", trie.count_words_with_suffix("e"))  # apple
    print(
        "Words ending with 'ion':", trie.count_words_with_suffix("ion")
    )  # application
    print("Words ending with 'a':", trie.count_words_with_suffix("a"))  # banana
    print("Words ending with 'at':", trie.count_words_with_suffix("at"))  # cat

    # Перевірка наявності префікса
    print("Has prefix 'app':", trie.has_prefix("app"))  # apple, application
    print("Has prefix 'bat':", trie.has_prefix("bat"))
    print("Has prefix 'ban':", trie.has_prefix("ban"))  # banana
    print("Has prefix 'ca':", trie.has_prefix("ca"))  # cat
