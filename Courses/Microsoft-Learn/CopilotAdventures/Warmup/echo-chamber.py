# -----------------------------------------------------------------------------------
# echo-chamber.py
# https://microsoft.github.io/CopilotAdventures/Adventures/StartHere.html
# -----------------------------------------------------------------------------------
# A program that predicts the next number in the sequence by finding the difference
# between the first two numbers and adding that difference to the last number in the
# sequence.
# ------------------------------------------------------------------------------------
# Input: A list of numbers that includes the first two numbers in the sequence
# Output: A list of numbers that includes the next number in the sequence
# ------------------------------------------------------------------------------------

memories = []

def predict_next(echoes):

    # Calculate the difference between the first two numbers in the sequence
    # and add that difference to the last number in the sequence
    # to predict the next number in the sequence
    # Store the full sequence including the predicted number in memories
    # Return the predicted next value
    difference = echoes[1] - echoes[0]
    next_value = echoes[-1] + difference

    # Store the full sequence including the predicted number in memories
    memories.extend(echoes + [next_value])

    # Return the predicted next value
    return next_value

# Print results

print('***************************************************')
print(f'Prediction: {(predict_next([3, 6, 9, 12]))}')
print('***************************************************')
print(f'Memories: {memories}')
print('***************************************************')
