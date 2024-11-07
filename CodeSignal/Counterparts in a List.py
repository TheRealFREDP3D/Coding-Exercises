def solution(numbers):
    # Create a dictionary to store the numbers and their indices
    num_dict = {num: i for i, num in enumerate(numbers)}
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the numbers
    for num in numbers:
        # Reverse the number
        rev_num = int(str(num)[::-1])
        
        # Check if the reversed number is in the dictionary
        if rev_num in num_dict:
            # Append the tuple to the result
            result.append((num, rev_num))
    
    return result