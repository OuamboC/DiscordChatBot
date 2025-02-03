## Description of WengBot

1. **Purpose**: 
   The main function of WengBot is to serve as an AI-powered assistant within Discord. It is designed to interact with users by responding to their messages, providing assistance, and engaging in conversation. WengBot helps create a more interactive and enjoyable experience for Discord users by utilising the DeepSeek API for generating responses.

2. **Key Features**
   - **Message Handling**: WengBot listens for incoming messages and can respond to users based on the content of their messages.
     - *Prompt example for a user within Discord*: `@WengBot How to well create and manage MySQL directly on AWS and then use the database file within my SpringBoot Project`
   - **Mentions**: It specifically reacts when mentioned in a message, generating relevant responses using the DeepSeek-R1 model from OpenRouter.
   - **Chat History**: Maintains a chat history to provide context for its responses.
   - **Welcoming Users**: Sends a welcome message to the general channel when the bot is ready, making users feel greeted and informed about its capabilities.
   - **Customizable Responses**: Generates responses based on the chat history and context, making interactions feel more personalized.

3. **Technology Stack**:
   - **Programming Language**: Python
   - **Libraries**: 
     - `discord`: For creating the bot and handling Discord interactions.
     - `dotenv`: For loading environment variables from a `.env` file.
     - `os`: For accessing environment variables.
     - `OpenAI`: For integrating with the DeepSeek API.
   - **APIs**: 
     - `DeepSeek API`: Used for generating AI-powered responses.
     - `OpenRouter API`: Base URL and key management for API access.

4. **Development Process**:
   - **Challenges**:
     1. Integrating the DeepSeek API with the Discord bot.
     2. Handling chat history and ensuring the bot's responses are contextually relevant.
   - **Solutions**:
     1. Successfully set up environment variables for secure API key management.
     2. Implemented a method to maintain and utilise chat history for generating responses.
   - **Exciting Part**: 
     Seeing WengBot come to life and interact with users in real-time was the most thrilling part of the project. The ability to combine Discord's capabilities with AI-generated responses made the bot dynamic and engaging.

## Design Part

### WengBot Logo
To create a logo for WengBot while keeping the development cost-efficient, I used a free logo design tool, FreeLogoDesign. Here are some insights into the process:

- **Tool**: **FreeLogoDesign**
  - **Website**: [FreeLogoDesign](https://www.freelogodesign.org/)
  - **Features**: Allows custom logo creation with various templates, icons, and fonts.
  - **Free Account**: Provides a free option to design and download low-resolution logos. You can upgrade to a paid version for high-resolution files if needed.

#### Steps to Create the Logo:
1. **Conceptualise**: Determine key elements for the logo, such as symbols related to AI, technology, or chatbots.
2. **Choose a Template**: Select a template that aligns with the vision for WengBot.
3. **Customise**: Edit the template by adding the bot's name, selecting appropriate colors, and choosing relevant icons.
4. **Experiment**: Try different designs until finding the perfect one.
5. **Download**: Download the final logo in the desired resolution.

#### Example Ideas:
- **Tech Symbol**: Incorporate symbols like gears, chat bubbles, or robots.
- **Color Scheme**: Choose colors that reflect WengBot's personality, such as whites and blues.

### Logo Creation Screenshot
![WengBot](https://github.com/user-attachments/assets/c7bb412f-f269-4025-89d6-df0a49cbd23a)

By utilising free tools and keeping the process cost-efficient, I was able to create a professional logo for WengBot.



