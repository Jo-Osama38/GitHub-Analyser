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
                "content": f"""You are a senior software engineering recruiter and GitHub expert.

                                    Analyze the following GitHub profile.
                                    profile : {profile}

                                    Evaluate:

                                    1. Overall summary.
                                    2. Career level.
                                    3. Strongest technical skills.
                                    4. Weaknesses.
                                    5. Repository quality.
                                    6. Documentation quality.
                                    7. Community engagement.
                                    8. Suggestions to improve the GitHub profile.
                                    9. Next learning roadmap.

                                    Return ONLY valid JSON.
                                    Do not write markdown.
                                    Do not write ```json.
                                    Do not write any explanation.
                                    The first character must be {{
                                    The last character must be }}
                                    Every key and string must use double quotes.

                                    Format:

                                    {{
                                    "summary":"",
                                    "career_level":"",
                                    "strengths":[],
                                    "weaknesses":[],
                                    "next_steps":[],
                                    "Tips_To_improve":[]
        
                                    }}
                                    Rules for "Tips_To_improve" only :
                                        - Return exactly 6 tips
                                        - Each tip must contain between 7 and 11 words
                                        - Do not repeat the same idea
                                    """,}],
                                    
                                response_format={"type": "json_object"},
    )
    data =  ((stream.choices[0].message.content))
    return json.loads(data)


