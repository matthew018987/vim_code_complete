import anthropic
import os
from constants import *


class Completions:
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.environ['ANTHROPIC_KEY'],
        )

    
    def do(self, request):
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=2048,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": request}
            ]
        ) 

        response_text = ''
        if len(response.content) > 0:
            response_text = response.content[0].text
       
        tokens_used = response.usage.input_tokens + response.usage.output_tokens 
        return response_text, tokens_used

