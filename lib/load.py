def load(fileName, mainBg, initf):
  vgroups = {}
  with open(fileName, "r") as file:
    # Initialize variables for grouping
    current_group = []
    groups = []

    # Read each line of the file
    for line in file:
      # Strip leading/trailing whitespace
      line = line.strip()

      # Check if the line is empty (indicating a new group)
      if not line:
        if current_group:
            groups.append(current_group)
            current_group = []
        continue  # Skip processing empty lines

      # Split the line into text1, text2, and number
      parts = line.split(',')
      if (len(parts) == 3):
        text1, text2, number_str = parts
        
        try:  
          number = int(number_str)
        except ValueError:
          try:
            number = float(number_str)
          except ValueError:
            continue
        
        # Add the data to the current group
        current_group.append((text1, text2, number))
      
      if (len(parts) == 1):
        # Check if the line indicates the show option
        if line.startswith("show"):
          show_option = int(line.split()[1])
          current_group.append(("show", show_option))
          continue
        if line.startswith("name"):
          name = line.split()[1]
          current_group.append(("name", name))
        if line.startswith("bg"):
          bg = line.split()[1]
          current_group.append(("bg", bg))

    # Add the last group (if any)
    if current_group:
      groups.append(current_group)

    # Create instances of MyClass and process each group
    for i, group in enumerate(groups):

      #First scan of data to get bg (need by the vg init)
      bg = mainBg #default value
      for data in group:
        if data[0] == "bg":
          bg = data[1]
          continue

      vg = initf(bg)

      #Second scan to populate
      for data in group:
        if data[0] == "show":
          show_option = data[1]
          continue
        if data[0] == "name":
          name = data[1]
          continue
        if data[0] == "bg":
          continue
        text1, text2, number = data
        vg.add(text1, text2, number)
      if show_option:
        vg.show()
      vgroups[name] = vg
  return vgroups