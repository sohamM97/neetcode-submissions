class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for word in strs:
            res+=f"{len(word)}#{word}#"

        return res

    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0

        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j+1: j+1+length]
            strs.append(word)
            i=j+2+length

        return strs

        