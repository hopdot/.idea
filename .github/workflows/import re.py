import re

# Example of the generated code (malicious code as per earlier example)
generated_code = """
import os

def delete_files():
    # This is a malicious code snippet that deletes files
    os.remove("important_file.txt")

delete_files()
"""

# Detecting potential threats in the generated code
def detect_threats(generated_code: str):
    # Simple pattern matching to detect potentially harmful code
    threat_patterns = [
        r"exec\(",  # Dangerous use of exec()
        r"eval\(",  # Dangerous use of eval()
        r"os\.",  # Suspicious use of os module (e.g., os.system, os.remove)
        r"subprocess\.",  # Suspicious subprocess use
        r"import .*subprocess",  # Importing subprocess module
        r"import .*os",  # Importing os module
        r"open\(",  # Suspicious use of open() for file handling
        r"shutil\.",  # Use of shutil for file operations (can be risky)
    ]
    
    # Check for these patterns in the generated code
    for pattern in threat_patterns:
        if re.search(pattern, generated_code):
            return True  # Return True if a threat is detected
    return False

# Check if threats are detected
threat_detected = detect_threats(generated_code)

# Print the results
output = ""
if threat_detected:
    output += "Threat detected in generated code!\n"
else:
    output += "No threats detected in generated code.\n"

# Add the generated code
output += "\nGenerated Code:\n"
output += generated_code

# Save the generated code to a file
file_path = 'generated_code.py'
with open(file_path, "w") as file:
    file.write(generated_code)

# Notify the user
print(f"Generated code saved as '{file_path}'.")
