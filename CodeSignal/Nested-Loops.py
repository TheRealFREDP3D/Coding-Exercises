""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ Organizing a photo exhibition of iconic landmarks from around the        │
  │ world.                                                                   │
  └──────────────────────────────────────────────────────────────────────────┘
 """

exhibition_landmarks = {
    "France": ["Louvre Museum", "Mont Saint Michel"],
    "Italy": ["Leaning Tower of Pisa", "Venice Canals"],
    "Spain": ["Sagrada Familia", "Royal Palace of Madrid"],
    "Japan": ["Tokyo Tower", "Kiyomizu-dera"],
}
for country, landmarks in exhibition_landmarks.items():
    print(f"Landmarks in {country} to feature:")
    for landmark in landmarks:
        print(f"- {landmark}")


"""
The purpose of this code is to present a list of famous landmarks from different countries that will be featured in the exhibition. It takes no external input, as the data is already defined within the code itself in the form of a dictionary called exhibition_landmarks.

This dictionary contains countries as keys and lists of landmarks as values. For example, "France" is associated with a list containing "Louvre Museum" and "Mont Saint Michel".

The code produces output by printing the information to the console. It displays each country name followed by its associated landmarks, formatted in a readable way.

To achieve its purpose, the code uses nested loops. The outer loop iterates through each country-landmarks pair in the dictionary. For each country, it prints a header line stating which country's landmarks are being listed. Then, an inner loop goes through each landmark for that country, printing it with a dash in front for a bullet-point effect.

The important logic flow here is the use of nested loops to handle the two-level structure of the data (countries containing landmarks). This allows the code to systematically go through all the information and present it in an organized manner.

In simple terms, this code is like creating a tour guide for the photo exhibition. It goes through a list of countries, announces each country, and then lists the landmarks from that country that visitors can expect to see photos of in the exhibition. This gives a clear, structured preview of what the exhibition will feature, organized by country.
"""
