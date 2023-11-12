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

# Function to open a new tab
# Made a research to know more about the validators from this website:
# https://medium.com/@miguendes/how-to-check-if-a-string-is-a-valid-url-in-python-fb0584aab549
def openTab():
  title = input("Enter the title of the website: ")
  url = input("Enter the URL: ")
  if validators.url(url):
    new_tab = {'Title': title, 'URL': url, 'NestedTabs': []}
    tabs.append(new_tab)
    print("Tab opened successfully.")
  else:
    print("Please enter a valid URL.")

# Function to close a tab
def closeOneTab():
  handleNoTabsError()
  index = getTabIndex()
  if index:
    index = int(index)
    if 1 <= index <= len(tabs):
      del tabs[index - 1]
      print(f"Tab at index {index} closed.")
    else:
      print("Invalid tab index.")
  else:
    closed_tab = tabs.pop()
    print(f"Closed last opened tab: {closed_tab['Title']}")
    
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