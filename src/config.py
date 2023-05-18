from pydantic import BaseSettings


class Settings(BaseSettings):
    
    class Config:
        # `.env.prod` takes priority over `.env`
        env_file = ".env"
        


def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading Settings")
    return settings
