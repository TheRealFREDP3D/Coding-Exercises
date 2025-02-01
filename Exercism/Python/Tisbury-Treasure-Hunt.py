"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.
    
    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[-1]
    


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    # Extract the coordinate from azara_record and the combined coordinates from rui_record
    azara_coordinate = azara_record[1]
    rui_coordinates = ''.join(rui_record[1])  

    # Check if the coordinates match
    return azara_coordinate == rui_coordinates

def create_record(azara_record, rui_record):
    
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    azara_coordinate = azara_record[1]
    rui_coordinates = ''.join(rui_record[1])
    
    if azara_coordinate == rui_coordinates:
        return azara_record + rui_record

    else:
        return "not a match"
    


def clean_up(combined_record_group: tuple) -> str:
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """

    # List to store cleaned records
    report = ""
    for record in combined_records:
        if record != "not a match":
            cleaned_record = (record[0], record[2], record[3], record[4])
            report += f"{cleaned_record}\n"
    return report