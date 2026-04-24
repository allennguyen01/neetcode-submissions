class Solution:
    global special
    special = '!'

    def encode(self, strs: List[str]) -> str:
        string = ''

        for s in strs:
            length = len(s)
            string += str(length) + special + s

        # [Hello, Cat] -> 5!Hello3!Cat
        return string

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != special:
                j += 1

            length = int(s[i:j])

            startOfWord = j + 1
            word = s[startOfWord:startOfWord+length]

            res.append(word)
            i = startOfWord + length

        return res