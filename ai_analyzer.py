from my_API import my_api
from groq import Groq

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
                                    Format example:
                                        
                                        "summary":"...",
                                        "strengths":[
                                            "...",
                                            "..."
                                        ],
                                        "recommendations" :[
                                            "...",
                                            "..."
                                        ]
                                        
                                        and don't make it is very tall summary""",

                                    
            }
        ],
    )
    return (stream.choices[0].message.content)


