def determine_shortest_longest_moving_distance(excavation_map, element_locations):
    # In the excavation map, 0 represents a path, and 1
    # represents a road.
    #
    # The element_locations parameter represents the
    # coordinates of elements that can be mined.
    #
    # The objective is to determine the best location on
    # the map to build a research station.
    #
    # The research station must be built on a road (1).
    #
    # The distance from the research station to each
    # element location is called the "moving distance."
    #
    # For example, if there are 3 element locations and
    # their moving distances are 3, 4, and 5, then the
    # longest moving distance is 5.
    #
    # Among all possible locations for the research
    # station, find the one that minimizes the longest
    # moving distance.

    # Change the excavation_map so that it denotes the
    # location of the elements with number 2 and so on.

    rows, cols = len(excavation_map), len(excavation_map[0])

    # Change the excavation_map so that it denotes the
    # location of the elements with number 2 and so on.
    for i, element_location in enumerate(element_locations, start=2):
        excavation_map[element_location[0] - 1][element_location[1] - 1] = i

    # Possible moves from the current location
    surroundings = [
        [-1, 0],
        [0, -1],
        [0, 1],
        [1, 0],
    ]

    def calculate_longest_distance_from_center(center_y, center_x):
        longest_distance = 0
        queue = [(center_y, center_x)]

        # Create a new 2D array to store the distances from the center
        distances = []
        for _ in range(rows):
            row = []
            for _ in range(cols):
                row.append(-1)
            distances.append(row)
        distances[center_y][center_x] = 0

        while queue:
            y, x = queue.pop(0)

            for dy, dx in surroundings:
                new_y, new_x = y + dy, x + dx

                # Check if the new position is valid
                if 0 <= new_y < rows and 0 <= new_x < cols and distances[new_y][new_x] == -1:
                    # We can only move on roads
                    if excavation_map[new_y][new_x] == 1:
                        distances[new_y][new_x] = distances[y][x] + 1
                        queue.append((new_y, new_x))
                    # We can also move to element locations
                    elif excavation_map[new_y][new_x] >= 2:
                        distances[new_y][new_x] = distances[y][x] + 1
                        longest_distance = max(
                            longest_distance, distances[new_y][new_x])
                        queue.append((new_y, new_x))

        # Check if all roads have been reached
        for i, loc in enumerate(element_locations, start=2):
            y, x = loc[0] - 1, loc[1] - 1

            if distances[y][x] == -1:
                return -1

        return longest_distance

    shortest_longest_distance_from_center = float('inf')

    for y in range(rows):
        for x in range(cols):
            # Skip if not a road
            if excavation_map[y][x] != 1:
                continue

            distances_to_elements = calculate_longest_distance_from_center(
                y,
                x,
            )

            shortest_longest_distance_from_center = min(
                shortest_longest_distance_from_center,
                distances_to_elements,
            )

    # Checking for invalid location
    if shortest_longest_distance_from_center == -1:
        return -1

    return shortest_longest_distance_from_center


if __name__ == '__main__':
    # Test Case 1
    excavation_map = [
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0]
    ]

    # element_locations represents the coordinates of the elements to be mined.
    # Coordinates are given as [y, x], starting from 1.
    element_locations = [
        [1, 2],
        [8, 2],
        [3, 8],
    ]

    result = determine_shortest_longest_moving_distance(
        excavation_map,
        element_locations,
    )

    print(f"Test Case 1 - Shortest longest moving distance: {result}")

    # Test Case 2
    excavation_map = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0]
    ]

    # element_locations represents the coordinates of the elements to be mined.
    # Coordinates are given as [y, x], starting from 1.
    element_locations = [
        [1, 5],
        [9, 5],
        [5, 1],
        [5, 9],
    ]

    result = determine_shortest_longest_moving_distance(
        excavation_map,
        element_locations,
    )

    print(f"Test Case 2 - Shortest longest moving distance: {result}")

    # Test Case 3
    excavation_map = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    ]

    # element_locations represents the coordinates of the elements to be mined.
    # Coordinates are given as [y, x], starting from 1.
    element_locations = [
        [1, 1],
        [10, 10],
        [5, 5],
    ]

    result = determine_shortest_longest_moving_distance(
        excavation_map,
        element_locations,
    )

    print(f"Test Case 3 - Shortest longest moving distance: {result}")

    # Test Case 4: Circular road with elements at opposite ends
    excavation_map = [
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0, 0]
    ]

    # element_locations represents the coordinates of the elements to be mined.
    # Coordinates are given as [y, x], starting from 1.
    element_locations = [
        [1, 3],
        [7, 5],
        [4, 7],
    ]

    result = determine_shortest_longest_moving_distance(
        excavation_map,
        element_locations,
    )

    print(f"Test Case 4 - Shortest longest moving distance: {result}")

    # Test Case 5
    excavation_map = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ]

    # element_locations represents the coordinates of the elements to be mined.
    # Coordinates are given as [y, x], starting from 1.
    element_locations = [
        [4, 1],
        [3, 3],
        [8, 8],
    ]

    result = determine_shortest_longest_moving_distance(
        excavation_map,
        element_locations,
    )

    print(f"Test Case 5 - Shortest longest moving distance: {result}")
