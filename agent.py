class AIAgent:
    def __init__(self, model):
        self.model = model

    def get_response(self, user_input):
        # Preprocess the input
        processed_input = self.preprocess_input(user_input)
        
        # Generate a reply using the model
        reply = self.model.generate_reply(processed_input)
        
        # Postprocess the output
        final_reply = self.postprocess_output(reply)
        
        return final_reply

    def preprocess_input(self, user_input):
        # Implement input preprocessing logic here
        return user_input.strip()

    def postprocess_output(self, reply):
        # Implement output postprocessing logic here
        return reply.strip()