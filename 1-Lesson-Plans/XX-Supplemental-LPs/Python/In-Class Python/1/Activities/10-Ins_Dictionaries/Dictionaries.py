# Unlike lists, dictionaries store information in pairs
# ---------------------------------------------------------------
# A list of actor's names
actors = ["Tom Cruise",
          "Angelina Jolie",
          "Kristen Stewart",
          "Denzel Washington"]

# A dictionary of an actor
actor = {"name": "Tom Cruise"}
print(actor["name"])

# ---------------------------------------------------------------

# A dictionary can contain multiple pairs of information
actress = {
  "name": "Angelina Jolie",
  "genre": "Action",
  "nationality": "United States"
  }

# ---------------------------------------------------------------

# A dictionary can contain multiple types of information
# Here we have a list as a dictionary value. Remember lists can't be dictionary keys but they can be values
another_actor = {
    "name": "Sylvester Stallone",
    "age": 62,
    "married": True,
    "best movies": [
      "Rocky",
      "Rocky 2",
      "Rocky 3"
      ]
    }

# Notice the concatenation
print(another_actor["name"] + " was in " + another_actor["best movies"][0])
# ---------------------------------------------------------------

# A dictionary can even contain another dictionary
film = {"title": "Interstellar",
        "revenues": {
          "United States": 360, 
          "China": 250, 
          "United Kingdom": 73
          }
        }

print(film["title"] + " made " + str(film["revenues"]["United States"]) + " in the US.")
# ---------------------------------------------------------------
