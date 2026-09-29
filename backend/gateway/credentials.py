"""Shared administrator credential policy for CLI and HTTP entry points."""

from pydantic import BaseModel, ConfigDict, Field, field_validator

USERNAME_MAX_LENGTH = 128
PASSWORD_MAX_LENGTH = 1024
PASSWORD_MIN_LENGTH = 12


class LoginBody(BaseModel):
    model_config = ConfigDict(extra="forbid", hide_input_in_errors=True)

    # Existing identities are exact, case-sensitive strings, including email-shaped IDs.
    # Never silently strip or case-fold an existing administrator's identity/password.
    username: str = Field(min_length=1, max_length=USERNAME_MAX_LENGTH)
    password: str = Field(min_length=1, max_length=PASSWORD_MAX_LENGTH)


class AdminCredentials(LoginBody):
    password: str = Field(min_length=PASSWORD_MIN_LENGTH, max_length=PASSWORD_MAX_LENGTH)

    @field_validator("username")
    @classmethod
    def valid_username(cls, value: str) -> str:
        if any(c.isspace() or not c.isprintable() for c in value):
            raise ValueError("Username must not contain whitespace or control characters")
        return value
