def validate_request_description(description):
    """Return True for a non-empty description of at most 500 characters."""
    if not isinstance(description, str):
        return False
    cleaned = description.strip()
    return 1 <= len(cleaned) == 500
