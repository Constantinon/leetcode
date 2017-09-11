class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        str = map(set,["qwertyuiop","asdfghjkl","zxcvbnm"]);
        out = [];
        for i in words:
            smalli = set(i.lower())
            if any(smalli<= strr for strr in str):
                out.append(i);
        return out;
