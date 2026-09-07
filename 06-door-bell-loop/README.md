# 06-Door-Bell-Loop

This project demonstrates an **event-driven heartbeat** approach by setting up an automated Pull Request (PR) reviewer.

## Overview
- **Objective:** Create an automated loop that triggers on GitHub PR events (`opened`, `synchronize`) to review code.
- **Workflow:** A GitHub Action (`pr-review.yml`) runs whenever a PR is created or updated. It analyzes the PR diff to catch a specific bug (a missing null check).
- **Outcome:** The loop acts as an "event-driven heartbeat", ensuring code quality checks are automatically enforced without manual intervention.
