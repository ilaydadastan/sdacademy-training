"""
Customer Feedback System
Problem:
Design a customer feedback system for a business. Customers can rate their experience and leave feedback. The system should allow the business to analyze the feedback and calculate the average rating, showing both positive and negative feedback.

Criteria:
Feedback Details:

Each feedback contains a rating (1-5) and a text message.
Actions:

Submit Feedback: Customers can submit their feedback, including the rating and message.
View All Feedback: View all feedback submitted by customers.
Calculate Average Rating: Calculate the average rating of all feedback.
Categorize Feedback: Sort feedback into positive, neutral, and negative categories.
Edge Cases:

Handle customers submitting feedback with invalid ratings (e.g., outside the 1-5 range).
Handle empty feedback or feedback with missing information.
"""

# Initialize an empty list for feedbacks
feedbacks = []

# Submit feedback manually
rating = int(input("Enter rating (1-5): "))
message = input("Enter your feedback message: ")

# Check for valid rating
if 1 <= rating <= 5 and message:
    feedbacks.append([rating, message])  # Store as a list: [rating, message]
    print("Feedback submitted successfully.")
else:
    print("Invalid input. Rating must be between 1 and 5, and message cannot be empty.")

# Show all feedbacks
print("\nAll Feedbacks:")
for feedback in feedbacks:
    print(f"Rating: {feedback[0]}, Message: {feedback[1]}")

# Calculate average rating
if feedbacks:
    total_rating = sum([feedback[0] for feedback in feedbacks])
    average_rating = total_rating / len(feedbacks)
    print(f"\nAverage Rating: {average_rating:.2f}")
else:
    print("No feedback available to calculate average.")

# Categorize feedbacks into positive, neutral, or negative
positive = []
neutral = []
negative = []

for feedback in feedbacks:
    if feedback[0] >= 4:
        positive.append(feedback)
    elif feedback[0] == 3:
        neutral.append(feedback)
    else:
        negative.append(feedback)

# Display categorized feedbacks
print("\nCategorized Feedbacks:")
print("Positive Feedbacks:")
for feedback in positive:
    print(f"Rating: {feedback[0]}, Message: {feedback[1]}")

print("\nNeutral Feedbacks:")
for feedback in neutral:
    print(f"Rating: {feedback[0]}, Message: {feedback[1]}")

print("\nNegative Feedbacks:")
for feedback in negative:
    print(f"Rating: {feedback[0]}, Message: {feedback[1]}")
