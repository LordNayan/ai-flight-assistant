from fastapi import FastAPI
from langchain_anthropic import ChatAnthropic
from config import settings

app = FastAPI()

# Initialize ChatAnthropic with the API key from settings
llm = ChatAnthropic(model="claude-3-haiku-20240307",
                    api_key=settings.ANTHROPIC_API_KEY)

# Function to process the travel plan query


def parse_travel_plan(query: str):
    try:
        response = llm.invoke(query)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}


@app.get("/")
async def root():
    return {"message": "Flight assistant is up and running!"}


@app.post("/parse-travel-plan/")
async def get_travel_plan(query: str):
    parsed_data = parse_travel_plan(query)
    return parsed_data
