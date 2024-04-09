from django.core.exceptions import PermissionDenied

def user_is_host(function):
    def wrap(request, *args, **kwargs):
        print(f"User: {request.user.username}")  # print the username
        print(f"Is host: {request.user.groups.filter(name='מארח').exists()}")  # print if the user is part of the 'Host' group
        if request.user.groups.filter(name='מארח').exists():
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap