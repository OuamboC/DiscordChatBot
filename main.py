import discord  # Import discord library
import os  # Import os (operating system) library
import dotenv  # Import dotenv library for loading environment variables from a .env file
from openai import OpenAI  # Import OpenAI from the openai library

# Load the environment variables from the .env file
dotenv.load_dotenv()

# Prompt the user to enter the chat name for loading it
file = input("Enter the chat name for loading it:")
try:
    # Open the specified chat file in read mode and read its contents into the 'chat' variable
    with open(file, 'r') as f:
        chat = f.read()
except FileNotFoundError:
    print(f"File '{file}' not found. Starting with an empty chat history.")
    chat = ""

# Get the Discord bot token from environment variables
DISCORD_KEY = os.getenv('DISCORD_KEY')

# Get the OpenRouter API key from environment variables
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

# Initialize the OpenAI client with the API key and base URL for OpenRouter
openai = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    default_headers={
        "HTTP-Referer": "https://example.com",  # Optional. Replace with your site URL.
        "X-Title": "MySite",  # Optional. Replace with your site title.
    }
)

# Define the intents your bot needs
intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

# Create a subclass of Client and override its event handlers
class MyClient(discord.Client):

    # Create an asynchronous method to handle the bot's readiness event
    async def on_ready(self):
        # Print a message when the bot has successfully connected to Discord
        print(f'Logged on as {self.user}!')
        # Send a welcome message to the general channel
        channel = discord.utils.get(self.get_all_channels(), name='general')
        if channel:
            await channel.send("Hello everyone! I'm WengBot, your AI-powered assistant. Feel free to mention me if you need help or just want to chat. 😊")

    # Create an asynchronous method to handle incoming messages
    async def on_message(self, message):
        # Initialize the global variable 'chat' to store the chat history
        global chat
        # Append the incoming message to the chat history
        chat += f"{message.author}: {message.content}\n"
        # Print the incoming message to the console
        print(f'Message from {message.author}: {message.content}')
        # Check if the message is not sent by the bot itself
        if self.user != message.author:
            # Check if the bot is mentioned in the message
            if self.user in message.mentions:
                # Generate a response using the OpenRouter API and DeepSeek-R1 model
                response = openai.completions.create(
                    model = "deepseek/deepseek-r1:free",
                    prompt = chat,
                    max_tokens = 256,
                    temperature = 1.0
                )
                # Get the generated response text
                #message_to_send = response['choices'][0]['message']['content'].strip()
                message_to_send = response.choices[0].text.strip()
                # Get the channel where the message was sent
                channel = message.channel
                # Send the generated response back to the channel
                await channel.send(message_to_send)

# Create an instance of MyClient with the specified intents
client = MyClient(intents=intents)
# Run the bot with the Discord bot token
client.run(DISCORD_KEY)
