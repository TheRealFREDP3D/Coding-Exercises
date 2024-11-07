# This function processes astronaut names and planets from a string 
# then prints out a neat summary of who is exploring which planet.
def process_astronaut_data(data):
    """
    Process astronaut names and planets from a string then print out a neat summary of who is exploring which planet.

    Parameters
    ----------
    data : str
        The string containing the astronaut details, each astronaut-planet pair separated by a semicolon (;)
        and each pair separated by a dash (-).

    Returns
    -------
    None

    Examples
    --------
    >>> process_astronaut_data("    Neil-Mars; Buzz-Jupiter; Sally-Venus    ")
    Astronaut Neil is exploring Mars.
    Astronaut Buzz is exploring Jupiter.
    Astronaut Sally is exploring Venus.
    """
    
    if not data:
        print("No data provided.")
        return

    try:
        astronaut_details = data.split(';')
        for detail in astronaut_details:
            if '-' in detail:
                name, planet = detail.split('-')
                name = name.strip()
                planet = planet.strip()
                print(f'Astronaut {name} is exploring {planet}.')
            else:
                print("Invalid data format detected.")
    except Exception as e:
        print(f"An error occurred: {e}")
print(f'Astronaut [name] is exploring [planet].')      
  
# String containing astronaut names and planets, separated by semicolons.
# Each astronaut-planet pair is separated by a dash.
astronaut_data = "    Neil-Mars; Buzz-Jupiter; Sally-Venus    "
process_astronaut_data(astronaut_data)