from django.http import HttpResponse, JsonResponse
import logging

# Set up logging
logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("This is Home page ")

def hello_world(request):
    """Returns a simple Hello World response"""
    return HttpResponse("Hello, World!")

def bad_request(request):
    """Logs an error and returns a 400 Bad Request response"""
    logger.error("Bad Request encountered")
    return JsonResponse({"error": "Bad Request"}, status=400)
