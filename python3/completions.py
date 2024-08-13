import anthropic
from constants import *
import os


class Completions:
    """ 
    Handle integration with Anthropic API for code generation and review tasks

    Methods:
        __get_anthropic()
            private method to get anthropic client object

        __parse_anthropic_response(response)
            private method to parse API response
        
        write_code(request)
            request code generation based on user request

        review_code(code)
            request code review generation based on file content
    """

    def __init__(self):
        self.anthropic_client = None
        return


    def __get_anthropic(self):
        """ 
        Get anthropic client object, create it if not already created

        Returns:
            anthropic client object
        """
        if self.anthropic_client is None:
            self.anthropic_client = anthropic.Anthropic(
                api_key=os.environ['ANTHROPIC_KEY'],
            )   
        return self.anthropic_client

    
    def __parse_anthropic_response(self, response):
        """
        Parse anthropic respnose to get content and token consumption

        Args:
            response (dict): anthropic API response dict

        Returns:
            string containing generated response
            int containing count of tokens consumed
        """

        # parse content from response
        response_text = ''
        if response.content:
            response_text = response.content[0].text
       
        # count tokens used
        tokens_used = response.usage.input_tokens + response.usage.output_tokens 
        return response_text, tokens_used

   
    def write_code(self, request):
        """
        Call API with request from user to generate python code

        Args:
            request (str): user request for code completion

        Returns:
            string containing generated python code
        """
        
        response = self.__get_anthropic().messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=2048,
            system=SYSTEM_PROMPT_CODE,
            messages=[
                {"role": "user", "content": request}
            ]
        ) 
        response_text, tokens_used = self.__parse_anthropic_response(response)
        return response_text, tokens_used


    def review_code(self, code):
        """
        Call API with code from open file to generate review

        Args:
            code (str): code from open file

        Returns:
            string containing the generated python code review
        """
        
        response = self.__get_anthropic().messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=2048,
            system=SYSTEM_PROMPT_REVIEW,
            messages=[
                {"role": "user", "content": code}
            ]
        ) 
        response_text, tokens_used = self.__parse_anthropic_response(response)
        return response_text, tokens_used
        