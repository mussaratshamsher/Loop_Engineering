# Project 1: A watch Loop

Build a simple Python CLI project called **Long Task Monitor**. Start a long-running task that sleeps for 2–3 minutes and then creates `result.txt`. Run an in-session loop that checks every 60 seconds whether the task has finished. When finished, print a completion message **once** and exit. Support clean stopping with `Ctrl+C`. Keep the implementation minimal and focused only on the project criteria.


# Project 2: Make the test pass, then stop 

Build. Put 2 or 3 small failing tests in your repo. Build a loop that keeps working until the tests pass, but let a command (the test runner), not the agent, decide when it is done. Cap it at, say, 6 tries.

Done when the loop stops because the tests actually passed, not because it hit the cap. If it keeps hitting the cap, your stop condition or your prompt needs work. That is the lesson.

# Project 3: The Morning brief with Memory

Build. Make a scheduled loop that runs once, reads a progress.md, gathers something simple from the repo (open TODO comments, or the last day's commits), writes a short summary, and updates progress.md with what it found and the date.

Done when you run it twice and the second run clearly builds on the first, meaning it does not repeat what it already recorded. That proves your spine works. If the second run starts from nothing, your loop has no memory yet.

# Project 4: A fix loop with real time checker

Build. A smaller version of the Part 5 loop. Write a short skill with your fix steps, and a reviewer agent that replies PASS or FAIL. Take one real bug, have the implementer draft a fix in its own checkout (worktree or branch), and let the reviewer grade it. Open a PR only on PASS.

Done when two things are both true: a good fix gets a PASS and a PR, and a deliberately bad fix you plant gets a FAIL with reasons. If the reviewer passes the bad fix, your checker is too soft, so tighten it. A checker that approves everything is no checker.
 
 ## test by rnning commands

  cd 04-fix-loop
  git log --all --graph --oneline -p

# Project 5: Codify the body

Build. Take the fix loop you built in Project 4 and codify its body. On the Claude Code approach, describe it in plain words: "use a workflow to draft fixes for these three issues in parallel worktrees, and have a reviewer grade each one." Let the runtime write and run the script. When a run does what you want, save it from the /workflows view as a /command. On the OpenCode approach, write the same thing as a shell script: a for loop over the candidates, &/wait for the fan-out, and the reviewer's exit code as the checker. Run it twice.

Done when two things are true. First, one command (or one script) runs the whole draft-and-review body, meaning several candidates, isolated checkouts, and a verdict for each, with no step-by-step prompting from you. Second, you have proved the interlude's warning on your own machine: start a fresh session (or a fresh shell) and confirm the workflow remembers nothing from its last run. Then name what it would need to become a loop: a heartbeat to fire it, and a progress file its agents write. If you can name those two, you understand the difference between an engine and a loop. (Dynamic workflows are a research preview, so where this project and the live docs disagree, the docs win.)

  ### Option 2: Using WSL (Windows Subsystem for Linux)


  1. Open your WSL terminal.
  2. Navigate to the directory:
    cd /mnt/d/Agentic-Hackthon/Loop_Engineering/05-codify-body

  3. Run the script:
    bash workflow.sh

# Project 6: The door bell Loop

Build. Make your throwaway repo review its own pull requests. On the OpenCode approach, run opencode github install and accept the workflow it generates. On the Claude Code approach, create a Routine with a GitHub pull-request trigger (the appendix walks through the filters). Then open a PR that contains one planted bug, such as an off-by-one or a deleted null check, and wait.

Done when the PR gets a review you never asked for, and the review flags the planted bug. If the review misses it, tighten the prompt and push again. The push fires the loop once more through the synchronize event, and that re-fire is the event heartbeat working. With Projects 1 to 3, this completes all four heartbeats: in-session, conditional, scheduled, and event-driven.

# Project 7: Break it on purpose

Build. Take your Project 3 loop. First, measure one beat: note roughly how many tokens a run reads and writes, and multiply by your cadence to get a monthly cost, which is Concept 13's math on your own loop. Then sabotage it: point the prompt at a file that does not exist, or give it a success condition it can never meet (with a limit set). Let it fire on schedule and fail. Now diagnose the failure using only what the loop left behind, meaning the log line and progress.md, without replaying the full run.

Done when three things are true. You can say what failed, and when, from the spine alone. The loop left a clear "needs a human" note instead of failing silently. And you know your loop's monthly cost at its current cadence. If it failed silently, fix that before anything else by adding the log line. You are rehearsing the overnight failure now, while it is cheap and you are watching.

# Proejct 8: Your own daily loop

Build. Pick one real, boring, recurring chore in a project you actually work on: a dependency audit, a docs-freshness check, a changelog draft, a lint sweep. Build the full loop: heartbeat, worktree, skill, maker-checker, connector, and the spine. Add budget guards. Let it run.

Done when it has run unattended for a week and you trust what it ships because you read it, not because you stopped reading. Then answer Concept 15 honestly: did your understanding of the project keep up with what the loop changed? If not, slow the loop down until it does. (When it fails overnight, and it will, work through When an unattended loop fails before you blame the model.)