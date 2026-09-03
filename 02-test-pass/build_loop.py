import subprocess
import sys

MAX_TRIES = 6

def run_tests():
    print("Running tests...")
    result = subprocess.run(["pytest", "test_math_funcs.py"], capture_output=True, text=True)
    return result.returncode == 0, result.stdout

def fix_code(error_output):
    print("Tests failed. Asking agent to fix...")
    prompt = f"The tests in test_math_funcs.py failed with the following output:\n\n{error_output}\n\nPlease fix the implementation in math_funcs.py to make the tests pass. You must edit math_funcs.py directly using your tools. Do not just print the code, actually modify the file."
    
    # Call agy to fix it
    result = subprocess.run(["agy", "-p", prompt, "--dangerously-skip-permissions"], capture_output=True, text=True)
    print("Agent finished fixing.")
    # Print the last few lines of the agent's response to keep it clean
    lines = result.stdout.split('\n')
    print('\n'.join(lines[-15:]))

def main():
    for i in range(MAX_TRIES):
        print(f"--- Attempt {i+1} ---")
        passed, output = run_tests()
        if passed:
            print("Tests passed! Loop finished successfully.")
            sys.exit(0)
        else:
            fix_code(output)
            
    print("Hit max tries. Tests still fail.")
    sys.exit(1)

if __name__ == "__main__":
    main()
