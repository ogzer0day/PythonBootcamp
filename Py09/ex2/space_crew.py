from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime
from enum import Enum
from typing import List


SPACE_MISSIONS = [
    {
        "mission_id": "M2024_TITAN",
        "mission_name": "Solar Observatory Research Mission",
        "destination": "Solar Observatory",
        "launch_date": "2024-03-30T00:00:00",
        "duration_days": 451,
        "crew": [
            {
                "member_id": "CM001",
                "name": "Sarah Williams",
                "rank": "captain",
                "age": 43,
                "specialization": "Mission Command",
                "years_experience": 19,
                "is_active": True,
            },
            {
                "member_id": "CM002",
                "name": "James Hernandez",
                "rank": "captain",
                "age": 43,
                "specialization": "Pilot",
                "years_experience": 30,
                "is_active": True,
            },
            {
                "member_id": "CM003",
                "name": "Anna Jones",
                "rank": "cadet",
                "age": 35,
                "specialization": "Communications",
                "years_experience": 15,
                "is_active": True,
            },
        ],
        "mission_status": "planned",
        "budget_millions": 2208.1,
    },
    {
        "mission_id": "M2024_TITAN",
        "mission_name": "Solar Observatory Research Mission",
        "destination": "Solar Observatory",
        "launch_date": "2024-03-30T00:00:00",
        "duration_days": 451,
        "crew": [
            {
                "member_id": "CM001",
                "name": "Sarah Williams",
                "rank": "captain",
                "age": 43,
                "specialization": "Mission Command",
                "years_experience": 19,
                "is_active": True,
            },
            {
                "member_id": "CM002",
                "name": "James Hernandez",
                "rank": "ll",
                "age": 43,
                "specialization": "Pilot",
                "years_experience": 30,
                "is_active": True,
            },
            {
                "member_id": "CM003",
                "name": "Anna Jones",
                "rank": "cadet",
                "age": 35,
                "specialization": "Communications",
                "years_experience": 15,
                "is_active": True,
            },
        ],
        "mission_status": "planned",
        "budget_millions": 2208.1,
    },
]


class RankEnum(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: RankEnum
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self):

        if not self.mission_id[0] == "M":
            raise ValueError("Mission ID must start with 'M'")

        if not any(
            member.rank in {RankEnum.captain, RankEnum.commander}
            for member in self.crew
        ):
            raise ValueError("Mission must have at "
                             "least one Commander or Captain")

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        if self.duration_days > 365:
            experienced = [
                member for member in self.crew if member.years_experience >= 5
            ]
            if len(experienced) < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (>365 days)"
                    "require at least 50% experienced crew"
                )

        return self


def main():
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        for data in SPACE_MISSIONS:
            mission = SpaceMission(**data)

            print("Valid mission created:")
            print(f"Mission: {mission.mission_name}")
            print(f"ID: {mission.mission_id}")
            print(f"Destination: {mission.destination}")
            print(f"Duration: {mission.duration_days} days")
            print(f"Budget: ${mission.budget_millions}M")
            print(f"Crew size: {len(mission.crew)}")
            print("Crew members:")

            for member in mission.crew:
                print(
                    f"- {member.name} ({member.rank.value}) - "
                    f"{member.specialization}"
                )

    except ValidationError as e:
        print("\n========================"
              "=================")
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


main()
