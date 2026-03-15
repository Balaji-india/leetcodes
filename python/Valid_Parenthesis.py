class Solution(object):
    def isValid(self, s):
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (c == ')' and top != '(') or \
                   (c == '}' and top != '{') or \
                   (c == ']' and top != '['):
                    return False

        return stack == []
