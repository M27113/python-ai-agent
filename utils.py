def preprocess_input(user_input):
    # Clean and format the user input
    cleaned_input = user_input.strip().lower()
    return cleaned_input

def postprocess_output(ai_response):
    # Refine the AI's response
    refined_response = ai_response.strip()
    return refined_response