class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c=s.count(letter)
        return int(c/len(s)*100)