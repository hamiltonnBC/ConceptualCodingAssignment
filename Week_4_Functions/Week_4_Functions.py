# Create a program that calculates a Happiness Level based on a person's daily activities.

# IMPORT STATEMENTS GO HERE


# Function to calculate Social Score
def calculate_social_score(hours_socializing):
    return hours_socializing * 3


# Function to calculate Relax Score
def calculate_relax_score(hours_per_day):
    return hours_per_day * 2


# Function to determine Work Score
def determine_work_score(work_hours):
    return work_hours * -2


# Function to calculate Work-Life Balance Score
def calculate_work_life_balance_score(work_hours, relax_score):
    work_score = determine_work_score(work_hours)
    return work_score + relax_score


# Function to calculate Happiness Level
def calculate_happiness_level(relax_score, social_score, work_life_balance_score):
    return (relax_score + social_score + work_life_balance_score) // 3  # Average of the scores


def main():
    # Defines the scores
    scotts_socializing_hours = 2  # how many hours socializing per day
    scotts_relax_hours = 5  # how many hours of relaxing per day
    scotts_work_hours = 8  # how many hours of work per day

    # Calculate each score - Function Calls
    scotts_social_score = calculate_social_score(scotts_socializing_hours)
    scotts_relax_score = calculate_relax_score(scotts_relax_hours)
    scotts_work_life_balance_score = calculate_work_life_balance_score(scotts_work_hours, scotts_relax_score)

    # Calculate the Happiness Level - Function Call
    scotts_happiness_level = calculate_happiness_level(scotts_relax_score, scotts_social_score, scotts_work_life_balance_score)

    # Print the Happiness Level
    print(f"Scott's Happiness Level is: {scotts_happiness_level}.")
    if scotts_happiness_level >= 10:
        print("You are very happy! Keep up the good work!")
    elif scotts_happiness_level >= 5:
        print("You're doing well, but there's room for improvement in your daily routine.")
    else:
        print("You could be happier. Try to improve your scores in each category.")


if __name__ == "__main__":
    main()


# Expected Output:
# Social Score: 2 * 3 = 6
# Relax Score: 5 * 2 = 10
# Work Score: 8 * -2 = -16
# Work-Life Balance Score: -16 + 10 = -6
# Happiness Level: (6 + 10 + (-6)) // 3 = 10 // 3 = 3