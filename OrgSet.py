import pyautogui
import time
import pyperclip

# Function to log processed col0
def log_processed_col0(col0):
    with open('processed_log.txt', 'a') as log_file:
        log_file.write(f"Processed: {col0}\n")

# Function to read and update JavaScript template
def read_and_update_js_template(cost_center):
    with open('js.txt', 'r') as js_file:
        js_template = js_file.read()
    
    # Replace placeholder with the cost center
    updated_js = js_template.replace('Cost_center', cost_center)
    
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

    # Click on the new button
    pyautogui.click(3496, 443)
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
        pyautogui.click(4186, -286)
        pyautogui.hotkey('ctrl', 'v')  # Paste the JavaScript
        pyautogui.press('enter')  # Press enter
        time.sleep(1)

        # Click on another specified location
        pyautogui.click(3797, -708)
        time.sleep(1)

    # Log the processed col0
    log_processed_col0(col0)
    #Save
    pyautogui.click(3487, 394)
    time.sleep(1)



# Read input file and process each line
with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    process_line(line)
    time.sleep(2)  # Add delay between processing lines to avoid overwhelming the system
