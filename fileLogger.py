import os
from datetime import datetime

def log(msg, filename="log.txt"):
    """Log a message to a file with timestamp.
    
    Args:
        msg: Message to log
        filename: Output log file path (default: log.txt)
    
    Raises:
        TypeError: If msg is not a string
        IOError: If file cannot be written
    """
    if not isinstance(msg, str):
        raise TypeError(f"Message must be a string, got {type(msg).__name__}")
    
    try:
        # Create directory if it doesn't exist
        log_dir = os.path.dirname(filename)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {msg}\n"
        
        with open(filename, "a") as f:
            f.write(log_entry)
    except IOError as e:
        raise IOError(f"Failed to write to {filename}: {e}")


if __name__ == "__main__":
    log("Program started")
    log("Test message")
    print("Logs written successfully")