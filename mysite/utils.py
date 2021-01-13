def is_active(path):
    if request.get_full_path == url(path):
        return "active"
    return ""
