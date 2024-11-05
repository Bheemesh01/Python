from django.http import HttpResponse, JsonResponse
def home_page(request):
    print("Home page requested")
    friends = {
        'ankit':"value",
        'ravi':"value",
        'uttam':"value"
    }
    return JsonResponse(friends , safe=False)
 