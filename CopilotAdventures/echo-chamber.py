# Echo Chamber
# https://microsoft.github.io/CopilotAdventures/Adventures/StartHere.html
#
# A program that predicts the next number in the sequence by finding the difference 
# between the first two numbers and adding that difference to the last number in the sequence.
# 
# Input: A list of numbers that includes the first two numbers in the sequence
# Output: A list of numbers that includes the next number in the sequence   
# ---------------------------------------------------------------------------------

echoes = [3, 6, 9, 12]
memories = []

def predict_next(echoes):
    """
    Calculates the next value in a sequence of echoes.

    Args:
        echoes (List[int]): A list of integers representing the sequence of echoes.

    Returns:
        int: The predicted next value in the sequence.

    Raises:
        IndexError: If the input list is empty or has only one element.

    Examples:
        >>> predict_next([1, 3, 5, 7])
        11
        >>> predict_next([0, 2, 4, 6])
        8
    """
    difference = echoes[1] - echoes[0]
    next_value = echoes[-1] + difference
    
    # Store the full sequence including the predicted number in memories
    memories.extend(echoes + [next_value])
    
    # Return the predicted next value
    return next_value

print("*******************")
print("Prediction: " + str(predict_next(echoes)))
print("*******************")
# print memories
print("Memories: " + str(memories))
print("********************")
