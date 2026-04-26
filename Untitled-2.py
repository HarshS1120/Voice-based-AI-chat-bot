pip install exa-py cerebras-cloud-sdk

from exa_py import Exa
from cerebras.cloud.sdk import Cerebras

# Add your API keys here
EXA_API_KEY = ""
CEREBRAS_API_KEY = ""

client = Cerebras(api_key = CEREBRAS_API_KEY)
exa = Exa(api_key = EXA_API_KEY)

print("✅ Setup complete")

