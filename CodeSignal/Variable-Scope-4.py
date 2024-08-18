# Declare a global list to keep track of visited landmarks
visited_landmarks = []

# Define a function named log_landmark that takes two parameters: landmark and city
def log_landmark(landmark, city):
    # Add the landmark and its city to the global list in the format "landmark in city"
    visited_landmarks.append(landmark + " in " + city)  
    # Call the log_landmark function with examples e.g., "Eiffel Tower" and "Paris"
log_landmark("Eiffel Tower", "Paris")
# Print the list of visited landmarks
print(visited_landmarks)