import sys
import math


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    data: str = sys.argv[1]
    list_to_convert: list[str] = data.split(',')
    new_tuple: tuple = tuple(list_to_convert)

    try:
        x1, y1, z1 = int(new_tuple[0]), int(new_tuple[1]), int(new_tuple[2])
        x2, y2, z2 = 0, 0, 0
        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{data}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: ({e},)")
    else:
        print(f"Parsing coordinates: \"{data}\"")
        print(f"Parsed position: ({x1}, {y1}, {z1})")
        print(f"Distance between ({x2}, {y2}, {z2}) and ({x1}, {y1}, {z1}):"
              f"{distance:.2f}")
        print()
        print("Unpacking demonstration:")
        print(f"Player at x={x1}, y={y1}, z={z1}\nCoordinates: "
              f"X={x1}, Y={y1}, Z={z1}")
