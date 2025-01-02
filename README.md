# Krushak-Ai-Chatbot

**Krushak-Ai-Chatbot** is an intelligent agricultural chatbot designed to assist farmers with a variety of tasks and queries. Powered by **Google Gemini**, the chatbot offers a ChatGPT-like interface with robust multi-language communication, voice interaction, and WhatsApp integration. This ensures a seamless and accessible experience for farmers across different regions and languages. The chatbot is powered by Django on the backend and Bootstrap for a responsive user interface.

---

## Overview

Farmers often struggle to find the information they need because it is scattered across many websites and platforms. Many farmers are not even aware of government portals where they can get details about subsidies, loans, or farming equipment. Even when they know about these portals, the information is not well-organized in one place.

**Krushak-Ai-Chatbot** solves this problem by acting as a one-stop solution for all agriculture-related queries. It provides all the information farmers need and allows them to find answers quickly. To make things even easier, Krushak-Ai-Chatbot is deployed on WhatsApp, a platform many farmers are familiar with. This eliminates the need for browsing the internet, making data more accessible to those who prefer WhatsApp.

---

## Features

- **ChatGPT-like Interface**: A user-friendly and intuitive interface for effortless communication.
- **Google Gemini Integration**: Harnesses the power of Google Gemini for advanced, real-time agricultural assistance.
- **WhatsApp and Website Integration**: Users can interact with the chatbot directly through WhatsApp and a website, ensuring easy access for farmers.
- **Multi-language Support**: Supports multiple languages, enabling farmers to converse in their native tongues.
- **Voice Interaction**: Allows users to communicate via voice commands and receive voice responses, improving accessibility for farmers who may have limited literacy skills.
- **Weather Updates**: Provides real-time weather information to help farmers plan their agricultural activities effectively.
- **Region-Based Schemes and Subsidies**: By simply providing the name of their region, farmers can access a table with all relevant schemes, subsidies, and loan details.
- **Crop Information by Name**: Farmers can get detailed information about any vegetable just by providing its name.
- **Web Scraping for Comprehensive Data**: Krushak-Ai-Chatbot scrapes and consolidates information from across the internet, ensuring farmers receive all the relevant data in one place.
- **Django Framework**: Utilizes Django for the backend, ensuring scalability and robust performance.
- **Responsive Design**: Frontend built using Bootstrap, providing an easy-to-use interface across devices, including smartphones and tablets.

---

## How It Works

1. **User Interaction**: Farmers interact with the chatbot either through the web interface or WhatsApp.
2. **Multi-Language Communication**: The chatbot detects the user's language and provides responses in their preferred language.
3. **Voice Input and Output**: Users can speak their queries, and the chatbot responds via voice, enabling hands-free communication.
4. **Agricultural Assistance**: The chatbot offers real-time information on crop management, weather forecasts, pest control, and other agriculture-related queries.
5. **WhatsApp Support**: Farmers can receive responses directly on WhatsApp, ensuring accessibility without needing a web browser.

---

## Use Cases

- **Crop Management**: Guidance on best practices for growing, watering, and harvesting crops.
- **Pest Control**: Information on pest identification and prevention measures.
- **Weather Forecasts**: Localized weather updates to help farmers plan their activities.
- **Market Prices**: Real-time updates on the prices of agricultural produce.
- **Government Schemes**: Details about government assistance and schemes available for farmers.

---

## Technology Stack

- **Backend**: Django (Python framework)
- **Frontend**: Bootstrap for responsive design
- **AI Integration**: Google Gemini for intelligent and contextual responses
- **Voice Support**: Speech-to-text and text-to-speech functionalities
- **WhatsApp Integration**: Direct messaging support via WhatsApp API

---

## Installation

Follow these steps to set up and run the Krushak AI project locally:

### Prerequisites

1. Ensure you have Python installed (version 3.10 or later).
2. Install Django by running:
   
bash
   pip install django


### Steps

1. **Clone the Repository**  
   Clone the Git repository to your local system:

   
bash
   git clone https://github.com/astronova001/Krushak-Ai-Chatbot.git


2. **Create and Activate a Virtual Environment**

Create a virtual environment:

bash
python -m venv env


Activate the environment:

- On Windows:
  
bash
  env\Scripts\activate

- On macOS/Linux:
  
bash
  source env/bin/activate


3. Install Dependencies
   Use the requirements.txt file to install all required dependencies:

bash
pip install -r requirements.txt


4.Set Up the Environment File

- Create an .env file in the project directory.
- Obtain the session ID for Bard (Google’s previous model of Gemini) by following the guide at [dsdanielpark/Bard-API](https://github.com/dsdanielpark/Bard-API).

- Add the session ID to the .env file as follows:

makefile
SESSION_ID=<your_session_id>


5. Run the Server
   Change to the project directory and start the Django development server:

bash
cd krushak


bash
python manage.py runserver


6. Access the Application
   Open a browser and go to:

http://127.0.0.1:8000/


## Usage

1. Home Page

After starting the server, you’ll land on the home page. This page introduces you to Krushak AI and its features.

2. Navigation
   Use the navigation bar to switch between different pages, such as:

- **Chatbot**: Access the AI chatbot for agriculture-related queries.
- **Weather**: Check real-time weather updates.
- **Schemes**: View region-based schemes and subsidies.
- **Crop Info**: Get detailed information about vegetables by name.

## Results
  <img src="https://github.com/subhashbs36/Krushak-Ai-Chatbot/blob/main/Results/krushak%20.gif" width="550" /> 
  
  <img src="https://github.com/subhashbs36/Krushak-Ai-Chatbot/blob/main/Results/chat.png" width="400" />  
  <img src="https://github.com/subhashbs36/Krushak-Ai-Chatbot/blob/main/Results/gov1.png" width="400" />  
  <img src="https://github.com/subhashbs36/Krushak-Ai-Chatbot/blob/main/Results/gov2.png" width="400" /> 
