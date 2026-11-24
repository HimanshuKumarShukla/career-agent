from pydantic import BaseModel, Field


class CareerPreference(BaseModel):
    """Initial user criteria for future career guidance."""

    target_roles: list[str] = Field(default_factory=list)
    preferred_locations: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    remote_only: bool = False
    experience_years: float | None = Field(default=None, ge=0)
