from src import agent, gui

def response_to_gui(input_text):
    response = agent.get_genai_response(input_text)
    return {
        "text": response.text,
        "thought": response.usage_metadata.thoughts_token_count,
        "output": response.usage_metadata.candidates_token_count
    }

if __name__ == "__main__":
    app = gui.GeminiGui(process_callback = response_to_gui)
    app.mainloop()
