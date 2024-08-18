# Function to calculate Relax Score
def calculate_relax_score(hours_per_day):
    return hours_per_day * 2

# Function to calculate Social Score
def calculate_social_score(interactions_per_week):
    return interactions_per_week // 2


# Function to calculate Work-Life Balance Score
def calculate_work_life_balance_score(rating):
    return rating * 10


# Function to calculate Happiness Index
def calculate_happiness_index(leisure_score, social_score, work_life_balance_score):
    return (leisure_score + social_score + work_life_balance_score) // 3  # Average of the scores


# Main function
def main():
    # Defines the scores
    relax_hours = 4
    social_interactions = 7
    work_life_balance_rating = 5

    # Calculate each score - Function Calls
    leisure_score = calculate_relax_score(relax_hours)
    social_score = calculate_social_score(social_interactions)
    work_life_balance_score = calculate_work_life_balance_score(work_life_balance_rating)

    # Calculate the Happiness Index - Function Call
    happiness_index = calculate_happiness_index(leisure_score, social_score, work_life_balance_score)

    # Print the Happiness Index with interpretation, demonstrating int to string conversion with f-string
    message = (f"Your Happiness Index is: {happiness_index}. ")
    print(message)
    if happiness_index >= 70:
        print("You are very happy! Keep up the good work!")
    else:
        print("You could be happier. Try to improve your scores in each category.")


# Execute the main function
if __name__ == "__main__":
    main()
