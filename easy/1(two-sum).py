class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        given_numbers_dict = {}

        for index,value in enumerate(nums):

            required_number = target - value
            if required_number in given_numbers_dict:
                return [given_numbers_dict[required_number],index ]
            
            else:
                given_numbers_dict[value] = index

      


        