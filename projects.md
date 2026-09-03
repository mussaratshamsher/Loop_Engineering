# Project 1

Build a simple Python CLI project called **Long Task Monitor**. Start a long-running task that sleeps for 2–3 minutes and then creates `result.txt`. Run an in-session loop that checks every 60 seconds whether the task has finished. When finished, print a completion message **once** and exit. Support clean stopping with `Ctrl+C`. Keep the implementation minimal and focused only on the project criteria.


# Project 2

Build. Put 2 or 3 small failing tests in your repo. Build a loop that keeps working until the tests pass, but let a command (the test runner), not the agent, decide when it is done. Cap it at, say, 6 tries.

Done when the loop stops because the tests actually passed, not because it hit the cap. If it keeps hitting the cap, your stop condition or your prompt needs work. That is the lesson.

# Project 3

Build. Make a scheduled loop that runs once, reads a progress.md, gathers something simple from the repo (open TODO comments, or the last day's commits), writes a short summary, and updates progress.md with what it found and the date.

Done when you run it twice and the second run clearly builds on the first, meaning it does not repeat what it already recorded. That proves your spine works. If the second run starts from nothing, your loop has no memory yet.