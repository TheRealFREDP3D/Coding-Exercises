# Space exploration crew members' data, containing their names, missions, and roles
crew_data = "Neil,Armstrong,Apollo 11,C;Buzz,Aldrin,Apollo 11,P;Michael,Collins,Apollo 11,CM"

# Split the crew_data string into a list of individual crew member information using the appropriate delimiter
crew_list = crew_data.split(";")

# Iterate over the list of crew member data
for crew_member in crew_list:
    # For each member, split their data string using commas as delimiters
    name, surname, mission, role = crew_member.split(",")
    
    # Print the crew member's details in a formatted string
    print(f"{name} {surname} {mission} {role}")
    
# Expected output:
# Neil Armstrong Apollo 11 C
# Buzz Aldrin Apollo 11 P
# Michael Collins Apollo 11 CM
