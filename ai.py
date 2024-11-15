import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"))


class StructuredResponse(BaseModel):
    title: str
    author: str
    email: str
    company: str
    location: str
    date: str


class Content(BaseModel):
    content_section_title: str
    content_section_text: str


class ColsContent(BaseModel):
    col_results: list[str]
    contents: list[Content]


def system_prompt(additional_prompt):
    return f"""
    System: You are a maximum random table row generator and pdf content creator. 
    Creativity: Be creative with names and places. You can also create new places and names.
    Objective: You need to create data for a row in a table and given text elements for a PDF document." 
    Industry Specific Prompt: f{additional_prompt}
    """


def user_prompt(cols):
    concatenated_string = " | ".join(cols)
    return f"""Create the needed text elements for a PDF document.
    Task 1: First you need to create random values for the following columns: {concatenated_string}
    Task 1 Rules: The values should be fully deterministic and findable.
    Task 2: finally create a random list of content elements for the PDF document. 
    Task 2 Rules: They must be at least 400 words long each, make it as long as you can.
    Task 2 Rules: The first text element is the header the last the footer and the rest are the body of the document.
    Task 2 Rules: Every single column data from Task 1 must be somewhere hidden in the content and deterministic findable.
    Task 2 Rules: It should be written professionally and should include all important details of a well written document. such as summary, header, address, date, etc.
    Task 2 Rules: And if needed the footer should contain references, links or other information.
    Task 1 & 2 Rules: Do not use any emojis in or non unicode characters in the text.
    """


def create_content(cols: list, additional_prompt: str) -> str:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": system_prompt(additional_prompt)
            },
            {
                "role": "user",
                "content": user_prompt(cols)
            },
        ],
        response_format=ColsContent,
    )
    parsed_content = completion.choices[0].message.parsed
    parsed_content_dict = parsed_content.model_dump()
    col_results = parsed_content_dict["col_results"]
    contents = parsed_content_dict["contents"]
    return col_results, contents
