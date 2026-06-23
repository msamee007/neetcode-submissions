class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        i=min(len(word1),len(word2))
        j=0
        while j!=i:
            s+=word1[j]+word2[j]
            j+=1
        s+=word1[j:]
        s+=word2[j:]
        return s
        