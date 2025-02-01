import discord #import discord library
import os #import os(operating system) library
import dotenv #import dotenv library for loading environment vraiables from a .env file
from openai import OpenAI #import the OpenAI class from the openai library for interacting with the OpenAI API

# Load the environment variables from the .env file
dotenv.load_dotenv()

# Prompt the user to enter the chat name for loading it 
file = input("Enter the chat name for loading it:")
#Open the specified chat file in read mode and read its contents into the 'chat variable
with open(file,'r') as f:
    chat = f.read()
#Initialise the chat variable as an empty string
chat = "" 

# Get the Discord bot token from environment variables
DISCORD_KEY = os.environ['DISCORD_KEY']

# Get the OpenAI key from environment variables
OPENAI_KEY = os.environ['OPENAI_KEY']

# Initialise the OpenAI client with the API key
openai = OpenAI(api_key = OPENAI_KEY)

class MyClient(discord.Client):

    # Create an asynchronous method to handle the bot's readiness event
    # This method will be triggered every time the bot successfully  connect to Discord
    async def on_ready(self):

        # Print a message when the bot has successfully connected to Discord
        print(f'Logged on as {self.user}!')

        # Send a welcome message to the general channel
        channel = discord.utils.get(self.get_all_channels(), name='general')
        if channel:
            await channel.send("Hello everyone! I'm WengBot, your AI-powered assistant. Feel free to mention me if you need help or just want to chat. 😊")
    # Create an asynchronous method to handle incoming messages
    # This method will be triggered every time a message is received in the chat
    async def on_message(self, message):
        #Initialise the global variable 'chat' to store the chat history
        global chat
         # Append the incoming message to the chat history
        chat +=f"{message.author}: {message.content}\n"
        # Print the incoming message to the console
        print(f'Message from {message.author}: {message.content}')
        # Check if the message is not sent by the the bot itself
        if self.user != message.author:
            #Check if the bot is mentioned in the message
            if self.user in message.mentions:
                # Generate a response using the OpenAI API
                response = openai.completions.create(
                    # Specify the OpenAI model to use 
                    model ="gpt-3.5-turbo-instruct",
                    # Use the chat history as the prompt
                    prompt = f"{chat}\nWengBot: ",
                    # Set the temperature for the response ( creativity level)
                    temperature = 1,
                    # Set the maximum number of tokens in the response
                    max_tokens = 256,
                    # Set the top-p value (nucleus sampling)
                    top_p = 1,
                    # Set the frequency penalty
                    frequency_penalty = 0,
                    # Set the presence penalty
                    presence_penalty = 0,
                )
                # Get the generated response text
                messageTosend = response.choices[0].text
                # Get the channel where the message was sent
                channel = message.channel
                # Send the generated response bak to the channel
                await channel.send(messageTosend)

# Define the intents for the bot
intents = discord.Intents.default()
intents.message_content = True

#Create an instance of MyClient with the specified intents
client = MyClient(intents = intents)
#Run the bot with the Discord bot token
client.run(DISCORD_KEY)


