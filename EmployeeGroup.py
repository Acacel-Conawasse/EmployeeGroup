import pyautogui
import time
import pyperclip

# Function to log processed col0
def log_processed_col0(col0):
    with open('Employee Group processed_log.txt', 'a') as log_file:
        log_file.write(f"Processed Employee Group: {col0}\n")

# Function to read and update JavaScript template
def read_and_update_js_template(col0):
    with open('EEjs.txt', 'r') as js_file:
        js_template = js_file.read()
    
    # Replace placeholder with the cost center
    updated_js = js_template.replace('OrgSet-', col0)
    
    # Copy the updated JavaScript to clipboard
    pyperclip.copy(updated_js)

# Function to process each line in the input file
def process_line(line):
    cols = line.strip().split('|')
    
    if len(cols) < 3:
        print("Invalid line format")
        return
    
    col0 = cols[0]
    col1 = cols[1]
    col2 = cols[2]

    # Click on console
    pyautogui.click(59, 103)
    time.sleep(1)
    read_and_update_js_template(col0)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')  # Paste the JavaScript
    pyautogui.press('enter')  # Press enter
    time.sleep(1)
    pyautogui.click(47, 75)#Clear Console
    time.sleep(1)


# Read input file and process each line
with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    process_line(line)
    time.sleep(2)  # Add delay between processing lines to avoid overwhelming the system
