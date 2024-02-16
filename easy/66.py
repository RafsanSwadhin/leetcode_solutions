from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if len(digits) > 1:
            # new = digits[-1] + 1
           # digits.pop()
           # digits.append(new)
            result = int(''.join(map(str, digits)))+1
            return [int(digit) for digit in str(result)]

        elif len(digits) == 1:
            m = digits[0]+1
            result = [int(digit) for digit in str(m)]
            return result