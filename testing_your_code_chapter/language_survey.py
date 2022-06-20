from survey import AnonymousSurvey

# Define a question and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question
my_survey.show_question()
print("Enter 'q' any time to quit.")
while True:
    response = input("Language: ")
    if response.lower() == "q":
        break
    my_survey.store_response(response)

# Show the survey results
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
