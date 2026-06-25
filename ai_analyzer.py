from my_API import my_api
from groq import Groq
import json

client = Groq (api_key=my_api)

def ai_analyzer(profile):
    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages = [
            {
                "role": "user",
                "content": f"""Analyze this GitHub profile.

                                    Give:
                                    1. Summary
                                    2. Strengths
                                    3. Recommendations

                                    Profile:
                                    {profile}

                                    Retuen ONLY JSON 
                                    Do not write explanations.
                                    Do not write markdown.
                                    Do not write ```json.

                                    The response must start with {{
                                    and end with }}

                                    Format example:
                                        
                                        {{
                                        "summary":"...",
                                        "strengths":[
                                        ],
                                        "recommendations" :[
                                        ],
                                        "career_level": "...",
                                        "next_steps": []
                                        }}
                                        and don't make it is very tall summary""",

                                    
            }
        ],
    )
    data =  ((stream.choices[0].message.content))
    return json.loads(data)


