from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from chat.models import Chat
import json
import json
import re
from .api.views import bardResponse


@login_required
def chat_main(request):
    try:
        Chat.objects.filter(user = request.user)[0]
    except:
        chat = Chat(user = request.user)
        chat.save()

    return redirect('chat_id', pk=1)



@login_required
def chat(request, pk):
    return render(request, 'chat/chat.html')




def extract_json_from_response(response_content):
    pattern = r'```json(.*?)```'
    match = re.search(pattern, response_content, re.DOTALL)
    if match:
        cleaned_json_content = match.group(1).strip()
        return cleaned_json_content
    return None

def loan_form(request):
    if request.method == 'POST':
        # Process the form data
        place = request.POST.get('name')
        message = f'list all the agriculture schems and loans provided by the government for farmers for a person in {place} and List these schems in table format which include "schemename", "loantype", "interestrate", "loanamount_limit"  Provide in json format'
        response_data = bardResponse(message)

        # Extract and clean the JSON content
        json_content = response_data['content']
        cleaned_json_content = extract_json_from_response(json_content)
        print(cleaned_json_content)
        if cleaned_json_content:
            # Load the JSON data into a dictionary
            json_data = json.loads(cleaned_json_content)

            # Check if 'schemes' key exists
            if 'schemes' in json_data:
                schemes = json_data['schemes']
            else:
                schemes = json_data  # Directly use the scheme objects

            # Render the template with JSON data
            context = {"schemes": schemes}
            return render(request, 'chat/loan_form.html', context)
        else:
            # Handle the case where JSON content is not found
            # Return an appropriate response or error message
            return render(request, 'chat/error.html')
    
    return render(request, 'chat/loan_form.html')



def crop_form(request):
    if request.method == 'POST':
        # Process the form data
        place = request.POST.get('name')
        message = f'list crops that can be grown in {place} and rank them based on profitability, cost, market demand, and ease of growing. Provide in json format'
        response_data = bardResponse(message)

        # Extract and clean the JSON content
        json_content = response_data['content']
        cleaned_json_content = extract_json_from_response(json_content)
        
        if cleaned_json_content:
            # Load the JSON data into a dictionary
            json_data = json.loads(cleaned_json_content)

            # Check if 'crops' key exists
            if 'crops' in json_data:
                crops = json_data['crops']
            else:
                crops = json_data  # Directly use the crop objects

            # Render the template with JSON data
            context = {"crops": crops}
            return render(request, 'chat/crop_form.html', context)
        else:
            # Handle the case where JSON content is not found
            # Return an appropriate response or error message
            return render(request, 'chat/error.html')

    return render(request, 'chat/crop_form.html')
