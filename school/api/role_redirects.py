# role_redirects.py

ROLE_REDIRECTS = {
    "principal": "principal_dashboard",   # url name
    "teacher": "teacher_dashboard",
    "student": "student_dashboard",
}

# Agar koi role match na ho to ye fallback hoga
DEFAULT_REDIRECT = "default_dashboard"
