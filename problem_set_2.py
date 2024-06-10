"""
Your job is to complete the definition of the function so that it achieves its indicated behavior.

Do not run this file directly.
Rather, call whichever functions defined in this file that you want to run from within the file named main.py and run that file directly.
"""
def true(yes):
  if yes[0] == "y" or yes[0] == "Y":
      return True 
  else:
      return False





 
def weather_helper():
  """
  Make suggestions based on current weather conditions.

  Program logic - indentations indicate nested logic:
  - Ask the user to enter in the current temperature in degrees Farenheit (i.e. an integer between  -70 and 134, inclusive).
    - If the user enters an invalid temperature (i.e. an integer that is not within the given range), print the text "Invalid temperature!" and do not print or input anything else.
    - If the temperature the user enters is below 40, ask them whether it is snowing.
      - If it is snowing, ask the user whether they are wearing a warm jacket.
        - If the user is wearing a jacket, print the output: "Glad to hear you're dressed appropriately!"
        - If the user is not wearing a jacket, print the output: "What were you thinking when you left home today?!"
      - If it is not snowing, ask the user whether it is raining.
        - If it is raining, ask the user whether they have an umbrella.
          - If the user has an umbrella, print the output: "Good job staying dry!"
          - If the user does not have an umbrella, print the output: "You must enjoy getting wet!"
    - If the temperature is above 90, ask the user whether they have air conditioning.
      - If the user has air conditioning, print the output: "Stay cool indoors."
      - If the user does not have air conditioning, print the output: "I hope you have a fan."

  Additional requirements:
    1. You can assume the user will enter an integer for the temperature.
    3. Assume the user will respond to any yes/no question with an affirmative response such as "yes", "yeah", "yup"; or a negative response such as "no", "nah", or "nope".
    2. Do not print anything more than what is requested in the instructions.
    4. The capitalization of the user's responses must not matter to the outcome of the program.
  """

  temperature = int(input("Enter the current temperature in degrees Fahrenheit: "))

  if temperature < -70 or temperature > 134:
        print("Invalid temperature!")
        return

  if temperature < 40:
        snowing = input("Is it snowing (yes/no)? ").lower()
        if snowing == "yes" or snowing == "yup" or snowing == "yeah":
            jacket = input("Are you wearing a warm jacket (yes/no)? ").lower()
            if true(jacket):
                print("Glad to hear you're dressed appropriately!")
            else:
                print("What were you thinking when you left home today?!")
        elif snowing == "no" or snowing == "nah" or snowing == "nope":
            raining = input("Is it raining (yes/no)? ").lower()
            if true(raining):
                umbrella = input("Do you have an umbrella (yes/no)? ").lower()
                if true(umbrella):
                    print("Good job staying dry!")
                else:
                    print("You must enjoy getting wet!")
  elif temperature > 90:
        ac = input("Do you have air conditioning (yes/no)? ").lower()
        if true(ac):
            print("Stay cool indoors.")
        else:
            print("I hope you have a fan.")
  