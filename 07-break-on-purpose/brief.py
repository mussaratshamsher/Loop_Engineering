import os
import glob
import datetime
import re

PROGRESS_FILE = "D:/Agentic-Hackthon/Loop_Engineering/06-break-on-purpose/progress.md"
SEARCH_DIR = "D:\Agentic-Hackthon\Loop_Engineering"

def get_recorded_todos():
    if not os.path.exists(PROGRESS_FILE):
        return set()
    
    with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract todos already recorded
    # We will format them as "- TODO: <text>"
    recorded = set()
    for line in content.splitlines():
        if line.startswith("- [x] TODO:") or line.startswith("- [ ] TODO:"):
            # just get the text part
            text = line.split("TODO:", 1)[1].strip()
            recorded.add(text)
    return recorded

def find_todos():
    todos = set()
    # Let's search some common text/code files, avoiding .git or binaries or progress.md itself
    for root, dirs, files in os.walk(SEARCH_DIR):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'node_modules', '.gemini']]
        
        for file in files:
            if file.endswith(('.py', '.txt', '.md', '.js')):
                filepath = os.path.join(root, file)
                
                # skip the progress file itself to avoid infinite loop of finding its own todos
                if os.path.abspath(filepath) == os.path.abspath(PROGRESS_FILE):
                    continue
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        for line in f:
                            if 'TODO' in line:
                                # extract the todo part
                                parts = line.split('TODO', 1)
                                if len(parts) > 1:
                                    todo_text = parts[1].strip(' :-\n')
                                    if todo_text:
                                        todos.add(todo_text)
                except Exception:
                    pass
    return todos

def main():
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        if not os.path.exists(SEARCH_DIR):
            raise FileNotFoundError(f"Directory {SEARCH_DIR} not found.")

        recorded = get_recorded_todos()
        current_todos = find_todos()
        
        new_todos = current_todos - recorded
        
        with open(PROGRESS_FILE, 'a', encoding='utf-8') as f:
            f.write(f"\n## Morning Brief - {now_str}\n")
            
            if not new_todos:
                f.write("No new TODOs found.\n")
                print("No new TODOs found.")
            else:
                f.write(f"Found {len(new_todos)} new TODOs:\n")
                for t in sorted(new_todos):
                    f.write(f"- [ ] TODO: {t}\n")
                print(f"Recorded {len(new_todos)} new TODOs.")
    except Exception as e:
        with open(PROGRESS_FILE, 'a', encoding='utf-8') as f:
            f.write(f"\n## FAILED - {now_str}\n")
            f.write(f"**needs a human**: The loop failed due to error: {str(e)}\n")
        print(f"Failed. Wrote needs a human to {PROGRESS_FILE}.")

if __name__ == '__main__':
    main()
