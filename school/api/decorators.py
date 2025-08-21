from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from .role_redirects import ROLE_REDIRECTS, DEFAULT_REDIRECT

def role_required(allowed_roles=None):
    """
    Restrict access to certain roles
    Usage:
        @role_required(['teacher', 'principal'])
    """
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')  # agar login nahi hai

            if allowed_roles is None or request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied  # agar role allowed nahi hai
        return wrapper
    return decorator


def auto_redirect(user):
    """Redirect user after login based on role"""
    role = user.role
    url_name = ROLE_REDIRECTS.get(role, DEFAULT_REDIRECT)
    return redirect(url_name)
