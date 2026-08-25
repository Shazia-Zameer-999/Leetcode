class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or word==word.capitalize():
            return True
        else:
            return False
        
        