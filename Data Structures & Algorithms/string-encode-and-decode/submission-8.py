class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for word in strs:
            res+=f"{len(word)}#{word}#"

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        word_ctr = 0
        ctr = 0
        
        cur_str = ""

        # Edge cases:
        # Empty string
        # Multiple digit counts

        # True if the current string is the word, 
        # False if it is the word length
        is_word = False

        # True if # is at the end of the word length
        is_count_end = False
        

        while ctr < len(s):
            letter = s[ctr]
            print(f"Processing letter: {letter}")

            if letter == "#":
                if is_word:
                    # Whenever we encounter a #, need two conditions - 
                    # word_ctr is 0 or not
                    if word_ctr == 0 and not is_count_end:
                        is_word = False
                        strs.append(cur_str)
                        cur_str = ""     
                    else:
                        # This is for case where # is part of the word.
                        # But need to handle where is the # just after
                        # the count.
                        cur_str += letter
                        word_ctr -= 1
                        print(f"Word ctr: {word_ctr}")
                else:
                    # If it is the # right after the count, 
                    # start new word
                    word_ctr = int(cur_str)
                    print(f"Next count: {word_ctr}")
                    cur_str = ""
                    is_word = True
                    is_count_end = False

            else:
                # No processing related to stopping here, 
                # simple processing of words/counts.
                cur_str += letter
                if is_word:
                    word_ctr -= 1
                    print(f"Word ctr: {word_ctr}")
                else:
                    next_letter = s[ctr + 1]
                    if next_letter == "#":
                        is_count_end = True
                        print(f"Count ends here.")

            ctr += 1
            print(f"Current str: {cur_str}")

        return strs

        