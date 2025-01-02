from django.contrib.auth.models import User
from chat.models import Chat, Message
from rest_framework.decorators import api_view
from .serializers import MessageSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import google.generativeai as genai
import os
import requests

# Initialize the Gemini API client with your API key
gemini_api_key = os.getenv("GEMINI_API_KEY")


# Initialization prompt for setting context
initialization_prompt = (
    f'your name is Krushak AI and you are here to provide information related to agriculture only and you will work as Assistant to farmers. You will answer questions related to crop cultivation, soil health, irrigation, pest control, marketing, government programs, and regulations  only if any questions asked on other topics then you should respond {"Sorry, I do not have an answer for your question, please ask question related to agriculture."} you should not answer questions anything other than related to agriculture. they should never know your true identity. respond only to questions related to agriculture only'
)

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

@api_view(['GET'])
def getMessages(request, pk):
    user = User.objects.get(username=request.user.username)
    chat = Chat.objects.filter(user=user)[pk-1]
    messages = Message.objects.filter(chat=chat)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@csrf_exempt
def get_prompt_result(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        prompt = data.get('prompt')
        user = User.objects.get(username=request.user.username)
        chat = Chat.objects.filter(user=user)[0]

        # Save the user's prompt message to the database
        message = Message(message=prompt, is_user=True, chat=chat)
        message.save()

        # Check if prompt is present in the request
        if not prompt:
            return JsonResponse({'error': 'Prompt is missing in the request'}, status=400)

        # Interaction with Gemini for agriculture-related questions
        is_agriculture_related = any(keyword in prompt.lower() for keyword in agriculture_keywords)
        if is_agriculture_related:
            question = f'answer the question only if it is related to agriculture and do not respond with extra information unrelated and your question is: {prompt}'
            
            # Configure the Gemini API client
            genai.configure(api_key=gemini_api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(question)
            
            content = response.text # Default to an empty set if images are not present
            
            # If the response contains images, include them in the response
            # if images:
            #     image_urls = list(images)  # Convert the set to a list
            #     image_tags = '\n'.join(f'<img src="{url}" alt="Image" class="image-viewer resized-image">' for url in image_urls)
            #     content += "\n\n\n" + image_tags
            
            # Save the assistant's response message to the database
            assistant_message = Message(message=content, is_user=False, chat=chat)
            assistant_message.save()
            
            return JsonResponse(content, safe=False)
        else:
            return JsonResponse("Sorry, I do not have an answer for your question related to agriculture.", safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def bardResponse(prompt):
    question = f'answer the question only if it is related to agriculture and do not respond with extra information unrelated and your question is: {prompt}'
     
    # Configure the Gemini API client
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(question)
    
    return response.text
