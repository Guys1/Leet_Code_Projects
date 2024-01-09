import re 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #calculating patern of regular expression
        patern = re.compile(r'%s' %p)
        #matching if pattern addresses the regular expression
        match = patern.fullmatch(s)
        if match : 
            return True 
        return False