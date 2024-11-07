from recipes import recipe_nutrition

print("Please review the dietary options below and select the one that best fits your goals:\n")
for i, preference in enumerate(recipe_nutrition, start=1):
    print(f"{i}. {preference['diet']} Diet:")
    for key, value in preference['nutritional_goals'].items():
        print(f"   - {key}: {value} g")
    print()

# Prompt the user for their choice
choice = input("Enter the number corresponding to your preferred diet (1 for Vegetarian, 2 for Vegan, 3 for Keto, 4 for Regular): ")

# Validate and display the choice
try:
    choice = int(choice)
    if 1 <= choice <= 4:
        print(f"\nYou selected the {user_preferences[choice - 1]['diet']} diet.")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
