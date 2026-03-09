class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []
        for s in logs:
            if s == "./":
                continue
            elif s == "../":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return len(stack)        