class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                curr_num = curr_str = ""
                
                while stack and stack[-1] != "[":
                    curr_str = stack.pop() + curr_str
                if stack:
                    stack.pop()
                
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num

                curr_num = int(curr_num)
                stack.append(curr_str * curr_num)

        return "".join(stack)