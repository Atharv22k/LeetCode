class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping of digits to letters
        digit_to_char = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index: int, current_combination: str):
            # If the combination is complete
            if index == len(digits):
                result.append(current_combination)
                return
            
            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            for char in digit_to_char[current_digit]:
                # Recurse to the next digit
                backtrack(index + 1, current_combination + char)
        
        # Start backtracking from the first digit
        backtrack(0, "")
        return result