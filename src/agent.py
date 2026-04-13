from google import genai
import os
import dotenv
from types import SimpleNamespace
from src.utils import projectConfig

dotenv.load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Create a GenAI client using the API key from the environment variable
client = genai.Client(api_key=GEMINI_API_KEY)
types = genai.types

def get_genai_response(input_text):

    #Project dependent parameters are loaded from projectConfig.yaml using the projectConfig function in utils.py.
    #This keeps the main code clean and makes it easy to adjust parameters without touching the code
    model_name = projectConfig["model_settings"]["name"]
    thinking_budget_val = projectConfig["model_settings"]["thinking_budget"]
    max_output_tokens_val = projectConfig["model_settings"]["max_output_tokens"]
    temperature_val = projectConfig["model_settings"]["temperature"]


    # The debug_mode flag allows you to return a mock response for testing the GUI without making actual API calls.
    if(projectConfig["proj_settings"]["debug_mode"] is True):
        return SimpleNamespace(
            text = "This is a simulated mock response and not an actual API call. \nAdjust the projectConfig.yaml to toggle this",
            usage_metadata=SimpleNamespace(
                thoughts_token_count = 111,
                candidates_token_count = 222 ) )
   #This is where the actual API call happens. The input text and max output tokens are passed in, along with the parameters loaded from the config file.
    response = client.models.generate_content(
        model = model_name,
        contents = input_text,
        config = types.GenerateContentConfig(
            thinking_config = types.ThinkingConfig(thinking_budget = thinking_budget_val),
            max_output_tokens = max_output_tokens_val,
            temperature = temperature_val) )
    return response

