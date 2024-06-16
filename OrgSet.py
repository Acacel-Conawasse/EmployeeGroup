import pyautogui
import time
import pyperclip
from PIL import ImageGrab
import pytesseract
import re

# Explicitly specify the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to log processed col0
def log_processed_col0(col0):
    with open('processed_log.txt', 'a') as log_file:
        log_file.write(f"Processed: {col0}\n")

# Function to log already created orgsets
def log_already_created(col0):
    with open('already_created_log.txt', 'a') as log_file:
        log_file.write(f"Commander {col0} orgset is already created Sir~!.\n")

# Function to read and update JavaScript template
def read_and_update_js_template(cost_center):
    with open('js.txt', 'r') as js_file:
        js_template = js_file.read()
    
    # Replace placeholder with the cost center
    updated_js = js_template.replace('Cost_center', cost_center)
    
    # Copy the updated JavaScript to clipboard
    pyperclip.copy(updated_js)

# Function to take screenshot and extract text
def take_screenshot_and_extract_text():
    screenshot = ImageGrab.grab(bbox=(984, 380, 1158, 409))
    screenshot.save('screenshot.png')
    extracted_text = pytesseract.image_to_string(screenshot).strip()
    return extracted_text

# Function to clean text by removing all special characters
def clean_text(text):
    return re.sub(r'\W+', '', text)

# Function to process each line in the input file
def process_line(line):
    cols = line.strip().split('|')
    
    if len(cols) < 3:
        print("Invalid line format")
        return
    
    col0 = cols[0]
    col1 = cols[1]
    col2 = cols[2]

    # Click on Search 1021, 319
    pyautogui.click(1021, 319)
    time.sleep(1)
    pyautogui.write(col0)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.click(1021, 319)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

    # Take screenshot and extract text
    extracted_text = take_screenshot_and_extract_text()
    time.sleep(1)
    
    # Clean extracted text and col0
    cleaned_extracted_text = clean_text(extracted_text)
    time.sleep(1)
    cleaned_col0 = clean_text(col0)
    
    # Print extracted text and col0
    print(f"Extracted text: {cleaned_extracted_text} | Col0: {cleaned_col0}")

    # Check if cleaned extracted text matches cleaned col0
    if cleaned_extracted_text == cleaned_col0:
        print(f"Commander {col0} orgset is already created Sir.")
        log_already_created(col0)
    else:
        # Click on the new button
        pyautogui.click(1011, 286)
        time.sleep(1)

        # Write Col 0
        pyautogui.typewrite(col0)
        time.sleep(1)
        pyautogui.press('tab')

        # Write Col 0 and Col 2
        pyautogui.typewrite(f"{col0},{col2}")
        time.sleep(1)
        pyautogui.press('tab')

        # Process cost centers in Col 1
        cost_centers = col1.split(',')

        for cost_center in cost_centers:
            # Read and update JS template with the current cost center
            read_and_update_js_template(cost_center)
            time.sleep(1)

            # Click on the target location and paste the copied value
            pyautogui.click(57, 125)
            pyautogui.hotkey('ctrl', 'v')  # Paste the JavaScript
            pyautogui.press('enter')  # Press enter
            time.sleep(1)

            # Click on another specified location
            pyautogui.click(44, 68)
            pyautogui.click(44, 68) 
            time.sleep(1)

        # Log the processed col0
        log_processed_col0(col0)
        
        # Save
        time.sleep(1)
        pyautogui.click(999, 249)
        time.sleep(.002)
        pyautogui.click(999, 249)
        time.sleep(1)

# Read input file and process each line
with open('Input1.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    process_line(line)
    time.sleep(2)  # Add delay between processing lines to avoid overwhelming the system
