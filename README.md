# Krushak-Ai-Chatbot

**Krushak-Ai-Chatbot** is an intelligent agricultural chatbot designed to assist farmers with a variety of tasks and queries. Built using the Bard API, the chatbot offers a ChatGPT-like interface with additional support for multi-language communication, voice interaction, and WhatsApp integration. This ensures a seamless, accessible experience for farmers across different regions and languages. The chatbot is powered by Django on the backend and Bootstrap for a responsive user interface.

## Features

- **ChatGPT-like Interface**: A user-friendly and intuitive interface similar to ChatGPT for easy communication.
- **Bard API Integration**: Leverages the power of Bard API for contextual, real-time agricultural assistance.
- **WhatsApp Integration**: Users can interact with the chatbot directly through WhatsApp for added convenience.
- **Multi-language Support**: Supports multiple languages, enabling farmers from different regions to converse in their native languages.
- **Voice Interaction**: Allows users to communicate via voice commands and responses, improving accessibility for farmers who may have limited literacy skills.
- **Django Framework**: Utilizes Django for the backend, ensuring scalability and robust performance.
- **Responsive Design**: Frontend built using Bootstrap, providing an easy-to-use interface across devices, including smartphones and tablets.

## How It Works

1. **User Interaction**: The farmer interacts with the chatbot either through the web interface or WhatsApp.
2. **Multi-Language Communication**: The chatbot detects the language of the user and responds in the appropriate language.
3. **Voice Input and Output**: Users can speak their queries, and the chatbot can respond via voice, ensuring hands-free communication.
4. **Agricultural Assistance**: The chatbot provides real-time information about crop management, weather forecasts, pest control, and other agriculture-related inquiries.
5. **WhatsApp Support**: Farmers can receive responses directly on WhatsApp, making the platform accessible even without the need to access a web browser.

## Use Cases

- **Crop Management**: Guidance on best practices for growing, watering, and harvesting crops.
- **Pest Control**: Information on pest identification and prevention measures.
- **Weather Forecasts**: Localized weather updates to help farmers plan their activities.
- **Market Prices**: Real-time updates on the prices of agricultural produce.
- **Government Schemes**: Information on government assistance and schemes available for farmers.

## Technology Stack

- **Backend**: Django (Python framework)
- **Frontend**: Bootstrap for responsive design
- **API**: Bard API for intelligent responses
- **Voice Support**: Speech-to-text and text-to-speech functionalities
- **WhatsApp Integration**: Direct messaging support via WhatsApp API

## Installation

To set up the chatbot locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/krushak-ai-chatbot.git
2. Navigate to the project directory:
   
   ```bash
    cd krushak-ai-chatbot

3. Install the required dependencies:

   ```bash
    pip install -r requirements.txt

4. Set up the Django server:

    ```bash
    python manage.py migrate
    python manage.py runserver

# Update:
Due to change in the API by google now bard is now officially unavailable. 

# Future Improvements

1. Integration with IoT Devices: Connect with smart sensors for real-time field data.
2. Enhanced AI Models: Further optimization of Bard API for specific agricultural advice.
3. Offline Support: Developing an offline mode for areas with limited internet access.
4. Mobile App: Extend the chatbot’s functionality to a dedicated mobile application.
5. Future Integration with Google Gemini: Plans to integrate the chatbot with Google Gemini for enhanced capabilities.