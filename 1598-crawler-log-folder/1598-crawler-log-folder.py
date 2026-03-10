class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for dir in logs:
            if stack and dir == "../":
                stack.pop()
            elif dir == "./" or dir=="../":
                continue
            else:
                stack.append(dir)
        return len(stack)