from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()

def main():
    try:
        api_key = os.environ["ANTHROPIC_API_KEY"]
    except KeyError:
        raise RuntimeError(
            "ANTHROPIC_API_KEY not set. Copy .env.example to .env and add your key from console.anthropic.com"
        )
    
    client = Anthropic(api_key=api_key)


if __name__ == "__main__":
    main()
