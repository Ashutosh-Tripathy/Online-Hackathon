class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []
        if len(strs) > 0:
            prefix, i = list(strs[0]), 1
            while len(prefix) > 0 and i < len(strs):
                if len(prefix) > len(strs[i]):
                    prefix = prefix[:len(strs[i])]
                item = list(strs[i][:len(prefix)])
                while prefix != item and len(prefix) > 0:
                    prefix.pop()
                    item.pop()
                i += 1
        return "".join(prefix)
