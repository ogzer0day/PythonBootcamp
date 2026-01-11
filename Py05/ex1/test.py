from typing import Any, List


def process_batch(data_batch: List[Any]) -> str:
    new_lst = [f"{key}: {val}" for key, val in data_batch[0].items()]
    return (str(new_lst).replace("'", ""))


# process_batch([{'temp': 22.5, 'humidity': 65, 'pressure': 1013}])

res = process_batch([{"temp": 22.5, "humidity": 65, "pressure": 1013}])
print(res)
