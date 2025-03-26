class Solution:
    def countAndSay(self, n: int) -> str:
         # Base case
        if n == 1:
            return "1"
        
        # Recursive call for previous sequence
        previous = self.countAndSay(n - 1)
        result = ""
        count = 1
        
        # Process previous result using run-length encoding
        for i in range(1, len(previous)):
            if previous[i] == previous[i - 1]:
                count += 1
            else:
                result += str(count) + previous[i - 1]
                count = 1
        
        # Append the last group
        result += str(count) + previous[-1]
        return result