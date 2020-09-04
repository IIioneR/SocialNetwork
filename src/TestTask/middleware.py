from rest_framework import status

from posts.models import Profile


class CatchUserRequest:
    '''
    Creating a new user automatility, 
    without use admin for create user
    '''

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 200 and not request.user.is_anonymous:
            obj, _ = Profile.objects.update_or_create(user=request.user)
            obj.update_last_request()
        return response
