#things to know 
def remove_spaces_and_punctuation(input_string):
    # Remove spaces and punctuation using a list comprehension
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    return cleaned_string

input_string = "A man, a plan, a canal: Panama"
output_string = remove_spaces_and_punctuation(input_string)
print(output_string)



#things to know 
def remove_spaces_and_punctuation(input_string):
    cleaned_string = ''  # Initialize an empty string to store the cleaned version
    for char in input_string:
        # Check if the character is alphanumeric (a letter or a digit)
        if char.isalnum():
            # If it's alphanumeric, add it to the cleaned string after converting it to lowercase
            cleaned_string += char.lower()
    return cleaned_string

input_string = "A man, a plan, a canal: Panama"
output_string = remove_spaces_and_punctuation(input_string)
print(output_string)



#here is my submitted problem

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = ''.join(char.lower() for char in s if char.isalnum())
        i = 0
        j = len(m)-1
        while i < j:
            if m[i] != m[j] :
                return False
            i = i + 1
            j = j -1
        return True

'''