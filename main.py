import validators

tabs = []

# Function to handle no opened tabs error
def handleNoTabsError():
  if not tabs:
    print("No tabs yet.")
    return

# Function to deal with user entries
def getTabIndex():
  index = input("Enter the index of the tab (press Enter to deal with the last opened tab): " )
  while not index.isdigit() and index != "":
    print("Please enter a valid integer for the tab index.")
    index = input("Enter the index of the tab (press Enter to deal with the last opened tab): ")
  return index

# Function to display the menu
def displayMenu():
  print("Welcome to the Advanced Browser Tabs Simulation!")
  print("Menu:")
  print("1. Open Tab")
  print("2. Close Tab")
  print("3. Switch Tab")
  print("4. Display All Tabs")
  print("5. Open Nested Tab")
  print("6. Clear All Tabs")
  print("7. Save Tabs")
  print("8. Import Tabs")
  print("9. Exit")