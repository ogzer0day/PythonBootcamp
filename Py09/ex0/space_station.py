from pydantic import BaseModel, Field, ValidationError
from datetime import datetime

data = [
    {
        "station_id": "LGW125",
        "name": "Titan Mining Outpost",
        "crew_size": 6,
        "power_level": 76.4,
        "oxygen_level": 95.5,
        "last_maintenance": "2023-07-11T00:00:00",
        "is_operational": True,
        "notes": None
    },
    {
        "station_id": "LGW125",
        "name": "Titan Mining Outpost",
        "crew_size": 21,
        "power_level": 76.4,
        "oxygen_level": 95.5,
        "last_maintenance": "2023-07-11T00:00:00",
        "is_operational": True,
        "notes": None
    }
]

class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(gt=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(description="DateTime field")
    is_operational: bool = Field(default=True)
    notes: str | None = Field(max_length=200)



def main():
    print("Space Station Data Validation")
    print("========================================")

    for data_validation in data:
        try:
            station = SpaceStation(**data_validation)
            print("Valid station created:")
            print(f"ID: {station.station_id}")
            print(f"Name: {station.name}")
            print(f"Crew: {station.crew_size} people")
            print(f"Power: {station.power_level}%")
            print(f"Oxygen: {station.oxygen_level}%")
            print(f"Status: {'Operational' if station.is_operational else 'Non-operational'}\n")
            print("========================================")
        except ValidationError as e:
            print("Expected validation error:")
            for e in e.errors():
                print(e['msg'])

    

if __name__ == "__main__":
    main()
