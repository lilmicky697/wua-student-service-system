from request_validation import validate_request_description

def test_valid_description():
    assert validate_request_description("Wi-Fi is not working in the lab.") is True

def test_empty_description():
    assert validate_request_description("") is False

def test_spaces_only():
    assert validate_request_description("   ") is False

def test_maximum_length_is_accepted():
    assert validate_request_description("a" * 500) is True

def test_too_long_is_rejected():
    assert validate_request_description("a" * 501) is Fals

def test_non_string_is_rejected():
    assert validate_request_description(None) is False
