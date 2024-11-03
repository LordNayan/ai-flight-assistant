from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LANGCHAIN_TRACING_V2: bool
    LANGCHAIN_API_KEY: str
    LANGCHAIN_ENDPOINT: str
    LANGCHAIN_PROJECT: str
    ANTHROPIC_API_KEY: str

    class Config:
        env_file = ".env"


# Initialize the settings
settings = Settings()
