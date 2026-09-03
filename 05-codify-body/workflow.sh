#!/bin/bash

# Candidates representing issues to fix
candidates=("issue-1" "issue-2" "issue-3")

# Function to simulate draft and review
draft_and_review() {
    local candidate=$1
    echo "[$candidate] Drafting fix in isolated checkout (worktree)..."
    sleep $((RANDOM % 3 + 1))
    
    # Reviewer's verdict (0 = PASS, 1 = FAIL)
    local exit_code=$((RANDOM % 2))
    
    if [ $exit_code -eq 0 ]; then
        echo "[$candidate] Reviewer verdict: PASS (exit code 0). Opening PR."
    else
        echo "[$candidate] Reviewer verdict: FAIL (exit code 1). Rejecting fix."
    fi
    
    return $exit_code
}

# For loop over the candidates
for candidate in "${candidates[@]}"; do
    # Run in background (fan-out)
    draft_and_review "$candidate" &
done

# Wait for all background jobs to finish
wait

echo "Workflow run complete."
