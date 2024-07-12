from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

print(os.environ.get('GCP_PROJECT_ID'))


def append_to_top_of_log(log_file_path, message):
    """
    Append a message to the top of the log file.
    
    Parameters:
    log_file_path (str): The path to the log file.
    message (str): The message to append to the log file.
    """
    # Read the current content of the log file if it exists
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as log_file:
            old_content = log_file.read()
    else:
        old_content = ""
    
    # Write the new log message followed by the old content
    with open(log_file_path, 'w') as log_file:
        log_file.write(message + old_content)

# Get the current working directory
cwd = os.getcwd()

# Define the new folder name
new_folder_name = 'data'

# Combine the current working directory with the new folder name to get the full path
new_folder_path = os.path.join(cwd, new_folder_name)

# Define the log file path
log_file_path = os.path.join(cwd, 'script.log')

# Get the current time
current_time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

# Create the log message with the current time
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)
    log_message = f"[{current_time}] Folder '{new_folder_name}' created at {new_folder_path}.\n"
else:
    log_message = f"[{current_time}] Folder '{new_folder_name}' already exists at {new_folder_path}.\n"

log_message += f"[{current_time}] Current working directory: {cwd}\n"

# Append the log message to the top of the log file
append_to_top_of_log(log_file_path, log_message)


# Define the text file name with the current time
text_file_name = f"running_time_{current_time.replace(':', ':')}.txt"

# Define the full path for the text file
text_file_path = os.path.join(cwd, new_folder_name, text_file_name)

# Create the content to write
content = f"This script was run at {current_time}\n"

# Write the content to the text file
with open(text_file_path, 'w') as text_file:
    text_file.write(content)



new_log_message = (f"[{current_time}] Text file created at {text_file_path} with content: {content}")

append_to_top_of_log(log_file_path, new_log_message)


