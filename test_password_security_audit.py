import pytest
from password_security_audit import is_password_secure

def test_secure_password():
    assert is_password_secure("SecurePassword!1") == True

def test_empty_passowrd():
    assert is_password_secure(" ") == False

def test_short_password():
    assert is_password_secure("Short!1") == False

def test_password_with_spaces():
    assert is_password_secure("Password with spaces!1") == False

def test_password_without_special_character():
    assert is_password_secure("NoSpecialCharacter1") == False

def test_password_without_lowercase_letter():
    assert is_password_secure("ALLUPPERCASE!1") == False

def test_password_without_uppercase_letter():
    assert is_password_secure("alllowercase!1") == False
