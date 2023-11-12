tabs = []

# Function to handle no opened tabs error
def handleNoTabsError():
  if not tabs:
    print("No tabs yet.")
    return
    
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