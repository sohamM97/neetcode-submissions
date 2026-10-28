class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}

        for word in strs:
            counts_in_word = [0]*26
            for letter in word:
                letter_pos = ord(letter) - ord('a')
                counts_in_word[letter_pos] += 1

            counts_in_word = tuple(counts_in_word)
            if counts.get(counts_in_word):
                counts[counts_in_word].append(word)
            else:
                counts[counts_in_word] = [word]

        result = []
        for anagrams in counts.values():
            result.append(anagrams)

        return result