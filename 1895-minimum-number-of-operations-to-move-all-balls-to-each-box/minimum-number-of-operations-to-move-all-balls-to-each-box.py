from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        # First pass: from left to right
        total_balls = 0
        operations = 0
        
        for i in range(n):
            answer[i] += operations
            if boxes[i] == '1':
                total_balls += 1
            operations += total_balls
        
        # Second pass: from right to left
        total_balls = 0
        operations = 0
        
        for i in range(n - 1, -1, -1):
            answer[i] += operations
            if boxes[i] == '1':
                total_balls += 1
            operations += total_balls
        
        return answer