'''
reverse s == s
raw = s.strip()
letters

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw = "".join(word for word in s if word.isalnum()).lower()
        print(raw)

        if raw[::-1] == raw:
            return True
        else:
            return False


        