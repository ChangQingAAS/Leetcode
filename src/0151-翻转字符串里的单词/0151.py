class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split(' ')[::-1]
        string = ""
        for i in range(len(slist)):
            if slist[i] != '':
                string += slist[i] + ' '
        
        return string.strip()
