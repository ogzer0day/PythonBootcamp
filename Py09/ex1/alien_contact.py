from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


data = [
    {
        "contact_id": "AC_2024_001",
        "timestamp": "2024-01-20T00:00:00",
        "location": " Area 51, Nevada",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 11,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False,
    },
    {
        "contact_id": "AC_2024_001",
        "timestamp": "2024-01-20T00:00:00",
        "location": "Atacama Desert, Chile",
        "contact_type": "visual",
        "signal_strength": 9.6,
        "duration_minutes": 99,
        "witness_count": 2,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False,
    },
]


class ContactType(str, Enum):
    """
    Enumeration of supported alien contact types.

    Defines the possible modes of extraterrestrial contact
    for classification and validation purposes.
    """

    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """
    Represents a validated record of an alien contact event.

    This model enforces constraints on contact metadata such as
    contact type, signal strength, witness count, and verification
    requirements using Pydantic field validation and model-level rules.
    """

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_contact_id(self):
        """
        Ensure the contact ID follows the expected prefix convention.

        Contact IDs must begin with 'AC' to denote an Alien Contact record.
        """
        if self.contact_id[0:2] != "AC":
            raise ValueError(
                "Contact ID must start with 'AC' (Alien Contact)"
            )
        return self

    @model_validator(mode="after")
    def check_physical_verified(self):
        """
        Require verification for physical contact events.

        Physical encounters are considered high-risk and must
        be explicitly verified.
        """
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contacts must be verified")
        return self

    @model_validator(mode="after")
    def check_witness_count(self):
        """
        Validate minimum witness requirements.

        Ensures that contact events meet the required number of
        witnesses to be considered credible.
        """
        if self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        return self

    @model_validator(mode="after")
    def check_signal_strength(self):
        """
        Ensure strong signals include a received message.

        High signal strength readings (> 7.0) are expected to
        contain an intelligible transmitted message.
        """
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def main():
    """
    Entry point for validating alien contact records.

    Iterates through sample contact data, attempts model validation,
    and prints either validated contact details or validation errors.
    """

    print("Alien Contact Log Validation")
    print("======================================")

    for verf_data in data:
        try:
            contact = AlienContact(**verf_data)
            print("Valid contact report:")
            print(f"ID: {contact.contact_id}")
            print(f"Type: {contact.contact_type.value}")
            print(f"Location: {contact.location}")
            print(f"Signal: {contact.signal_strength}/10")
            print(f"Duration: {contact.duration_minutes} minutes")
            print(f"Witnesses: {contact.witness_count}")
            print(f"Message: {contact.message_received}\n")

        except ValidationError as e:
            print("Expected validation error:")
            print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
