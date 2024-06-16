import pyautogui
import time
import pyperclip
import logging

# Configure logging
logging.basicConfig(filename='Employee_Group_processed_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Function to log processed col0
def log_processed_col0(col0):
    logging.info(f"Processed Employee Group: {col0}")

# Function to read and update JavaScript template
def read_and_update_js_template(col0):
    try:
        with open('EEjs.txt', 'r') as js_file:
            js_template = js_file.read()
        
        # Replace placeholder with the cost center
        updated_js = js_template.replace('OrgSet-', col0)
        
        # Copy the updated JavaScript to clipboard
        pyperclip.copy(updated_js)
    except FileNotFoundError:
        logging.error("JavaScript template file not found")
    except Exception as e:
        logging.error(f"Error reading or updating JavaScript template: {e}")

# Function to process each line in the input file
def process_line(line):
    cols = line.strip().split('|')
    
    if len(cols) < 3:
        logging.error("Invalid line format")
        return
    
    col0 = cols[0]
    col1 = cols[1]
    col2 = cols[2]

    try:
        # Click on console
        pyautogui.click(59, 103)
        time.sleep(1)
        read_and_update_js_template(col0)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')  # Paste the JavaScript
        pyautogui.press('enter')  # Press enter
        time.sleep(8)
        pyautogui.click(45, 71)  # Clear Console
        time.sleep(1)
        log_processed_col0(col0)
        print(f"Processed Employee Group: {col0}")
    except Exception as e:
        logging.error(f"Error processing Employee Group {col0}: {e}")

# Read input file and process each line
def main():
    try:
        with open('inp2.txt', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        logging.error("Input file not found")
        return
    except Exception as e:
        logging.error(f"Error reading input file: {e}")
        return

    for line in lines:
        process_line(line)
        time.sleep(2)  # Add delay between processing lines to avoid overwhelming the system

if __name__ == "__main__":
    main()
