---
name: fix-loop
description: A loop that enforces high-quality bug fixes by running a strict reviewer agent on proposed fixes, only opening a PR on PASS.
---

# Fix Loop Skill

1.  **Identify Bug:** Review the bug report and locate the bug in the codebase.
2.  **Checkout Branch:** Have the implementer agent checkout a new branch (or worktree) specifically for drafting the fix.
3.  **Draft Fix:** The implementer agent writes the fix and creates a commit.
4.  **Review Loop:**
    -   Generate a diff of the proposed fix.
    -   Invoke the Reviewer Agent (ix_reviewer) providing the original bug context and the proposed diff.
    -   If the Reviewer Agent replies **PASS**, proceed to the next step.
    -   If the Reviewer Agent replies **FAIL** with reasons, the implementer must read the feedback, modify the fix, and repeat the Review Loop (Step 4).
5.  **Open PR:** Once the reviewer replies PASS, open a Pull Request for the fix.
