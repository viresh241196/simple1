class Solution:
    def longestCommonPrefix(self, List):
        if not List:
            return ""
        first = List[0]
        var =''
        for item in List:
            for i,j in zip(first,item):
                if i==j:
                    var = var + i
            first = var
            var = ''       
        return first

s1 = Solution()
result =s1.longestCommonPrefix(["dogc","dracecar","dcar"])
print(result)