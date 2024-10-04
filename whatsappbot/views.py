
from django.http import HttpResponse
from bardapi import Bard
import os
from django.views.decorators.csrf import csrf_exempt
import requests
from twilio.twiml.messaging_response import MessagingResponse

# Create a session object using the requests library
session = requests.Session()

# Set the headers for the session
session.headers = {
    "Host": "bard.google.com",
    "X-Same-Domain": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://bard.google.com",
    "Referer": "https://bard.google.com/",
}

# Set the "__Secure-1PSID" cookie with the Bard API key
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))

# Create a Bard object with the session and a timeout of 30 seconds
bard = Bard(session=session, timeout=90)

# Agriculture-related keywords
agriculture_keywords = [
    "agriculture",
    "crop",
    "soil",
    "fertilizer",
    "irrigation",
    "pest",
    "disease",
    "marketing",
    "government",
    "regulation",
    "hello",
    "hi",
    "what",
    " ",
]

@csrf_exempt
def whatsapp_incoming(request):
    if request.method == 'POST':
        # Get the incoming message and sender's phone number
        incoming_message = request.POST.get('Body', '')

        question = f'answer the question only if it is related to agriculture and do not respond with extra information unrelated and answer in a whatsapp message format only. your question is: {incoming_message}'
        
        response = bard.get_answer(question)
    
        content = response['content']
        images = response.get('images', set())  # Default to an empty set if images are not present
        
        # If the response contains images, include them in the response
        if images:
            image_urls = list(images)  # Convert the set to a list
            content += "\n\nImage URLs:\n" + "\n".join(image_urls)

        # Create a Twilio response with the chatbot's response
        twilio_response = MessagingResponse()
        twilio_response.message(content)

        return HttpResponse(str(twilio_response))





