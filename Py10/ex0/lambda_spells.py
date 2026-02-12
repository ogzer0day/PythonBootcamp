
artifacts = [
        {'name': 'Light Prism', 'power': 102, 'type': 'accessory'},
        {'name': 'Fire Staff', 'power': 120, 'type': 'relic'},
        {'name': 'Crystal Orb', 'power': 91, 'type': 'weapon'},
        {'name': 'Lightning Rod', 'power': 66, 'type': 'focus'}
        ]
    
mages = [
        {'name': 'Ember', 'power': 89, 'element': 'light'},
        {'name': 'Nova', 'power': 81, 'element': 'water'},
        {'name': 'Ash', 'power': 97, 'element': 'wind'},
        {'name': 'Sage', 'power': 63, 'element': 'fire'},
        {'name': 'Casey', 'power': 95, 'element': 'wind'}
        ]
    
spells = ['meteor', 'darkness', 'flash', 'earthquake']


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return (sorted(artifacts, key=lambda x: x.get('power'), reverse = True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x.get('power') >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    most_pow = min(mages, key=lambda x: x.get('power'))
    least_pow = max(mages, key=lambda x: x.get('power'))
    avg_pow = sum(map(lambda x: x["power"], mages)) / len(mages)

    return (
        {
            "most_pow": most_pow['power'],
            "least_pow": least_pow['power'],
            "avg_pow": avg_pow
        }
    )

def main():
    print("Testing artifact sorter...")
    artifact = artifact_sorter(artifacts)
    print(f"{artifact[0]['name']} ({artifact[0]['power']} power) comes before"
          f"{artifact[1]['name']} ({artifact[1]['power']} power)\n")

    print("Testing spell transformer...")
    mage_stat = spell_transformer(spells)
    print(*mage_stat)
    

main()