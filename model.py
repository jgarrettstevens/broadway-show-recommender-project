def get_show_recommendation(show_type, location, genre):
  if show_type == "Musical" and location == "Broadway" and genre == "Uplifting and Funny":
    return "MJ: The Musical"
  elif show_type == "Musical" and location == "Broadway" and genre == "Emotional and Thought-Provoking":
    return "A Strange Loop"
  elif show_type == "Musical" and location == "Off-Broadway" and genre == "Uplifting and Funny":
    return "Little Shop of Horrors"
  elif show_type == "Musical" and location == "Off-Broadway" and genre == "Emotional and Thought-Provoking":
    return "SUFFS"
  elif show_type == "Play" and location == "Broadway" and genre == "Uplifting and Funny":
    return "POTUS"
  elif show_type == "Play" and location == "Broadway" and genre == "Emotional and Thought-Provoking":
    return "Slave Play"
  elif show_type == "Play" and location == "Off-Broadway" and genre == "Uplifting and Funny":
    return "Fat Ham"
  else:
    return "...what the end will be"