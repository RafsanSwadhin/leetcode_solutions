class Solution:  
    def twoSum(self, nums, target):   
        visited_numbers = dict()   
        print(visited_numbers)         
        for index, num in enumerate(nums):
            # 1st loop , index = 0 and num = 2
            number_to_be_search = target - num  
            # 1st loop num=2, target=18 and number_to_be_search=16
            if number_to_be_search in visited_numbers:
                # as in 1st loop number_to_be_search=16 is not in visited_numbers  
                return [index, visited_numbers[number_to_be_search]]          
            else:
                visited_numbers[num] = index
                # 1st loop num = 2 
                print("no",index)  
list1 = [2,7,11,15]      
target = 18
obj = Solution()  
print(obj.twoSum(list1, target))
