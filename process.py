import xml.etree.ElementTree as ET


INPUT_PROPERTY_FILE_PATH = 'properties/colors/dark_theme.xml'
DOUBLE_COMMANDER_SETTING_FILE_PATH = 'doublecmd.xml'
STRING_COLORS = 'Colors'
STRING_LAYOUT = 'Layout'
STRING_FONTS = 'Fonts'
STRING_ICONS = 'Icons'

# Open the file and read its contents into a variable
#with open(INPUT_PROPERTY_FILE_PATH, 'r') as file:
 #   icons_section = file.read()

def read_prop_from_file(input_file_path, property_to_read):
  # Parse the XML file
  tree = ET.parse(input_file_path)

  # Find the Icons element
  root = tree.getroot()
  property = root.find(property_to_read)

  if(property == None):
     return None

  # Convert the Icons element to a string
  return ET.tostring(property).decode()

def add_xml_child(root, section_name, new_xml):
  # Check if the Icons element already exists
  icons_exist = False
  for child in root:
      if child.tag == section_name:
          icons_exist = True
          # Replace the existing Icons element with the new one
          root.remove(child)
          root.append(ET.fromstring(new_xml))

  # If the Icons element doesn't exist, append it to the root
  if not icons_exist:
      root.append(ET.fromstring(new_xml))

def add_property(root, input_file_path, section_name):
  input_property = read_prop_from_file(input_file_path, section_name)

  if (input_property == None):
     return
  
  add_xml_child(root, section_name, input_property)

def apply_changes():
  # Parse the existing XML
  tree = ET.parse(DOUBLE_COMMANDER_SETTING_FILE_PATH)
  root = tree.getroot()

  add_property(root, INPUT_PROPERTY_FILE_PATH, STRING_COLORS)
  add_property(root, INPUT_PROPERTY_FILE_PATH, STRING_LAYOUT)
  add_property(root, INPUT_PROPERTY_FILE_PATH, STRING_FONTS)
  add_property(root, INPUT_PROPERTY_FILE_PATH, STRING_ICONS)

  # Write the modified XML to a new file
  tree.write(DOUBLE_COMMANDER_SETTING_FILE_PATH)
  print("Processing changes has been completed")