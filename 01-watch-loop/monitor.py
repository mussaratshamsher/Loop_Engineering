import time
import threading
import sys
import os

def long_task():
    """Simulates a long-running task that takes 2 minutes and creates a result file."""
    time.sleep(120)  # Sleep for 2 minutes
    
    # Ensure it saves in the same folder as the script, no matter where it's run from
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "result.txt")
    
    with open(file_path, "w") as f:
        f.write("Task completed successfully.\n")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "result.txt")
    
    # Clean up previous result file if it exists
    if os.path.exists(file_path):
        os.remove(file_path)

    print("Starting long-running task... (This will take exactly 2 minutes)")
    
    # Run the task in a separate thread so it doesn't block our monitor loop
    task_thread = threading.Thread(target=long_task, daemon=True)
    task_thread.start()

    try:
        task_notified = False
        print("Monitor loop started. Press Ctrl+C at any time to stop.")
        
        # Loop that runs continuously until the user stops it
        while True:
            # Wait for 60 seconds before checking again
            # time.sleep() will catch KeyboardInterrupt (Ctrl+C) smoothly
            time.sleep(60)
            
            if task_thread.is_alive():
                print("Status check: Task is still running...")
            elif not task_notified:
                print("Task finished! 'result.txt' has been created.")
                task_notified = True
                print("Monitor is still active... (Press Ctrl+C to stop)")
            else:
                print("Monitor is still active... (Press Ctrl+C to stop)")
        
    except KeyboardInterrupt:
        # Handle Ctrl+C cleanly
        print("\nMonitor stopped by user (Ctrl+C). Exiting cleanly.")
        sys.exit(0)

if __name__ == "__main__":
    main()
