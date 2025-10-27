#!/bin/bash

# Script to identify branches with changes not merged to main
# This helps track which branches have pending work that needs to be reviewed or merged

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
MAIN_BRANCH="${MAIN_BRANCH:-main}"
REMOTE="${REMOTE:-origin}"
SHOW_DETAILS="${SHOW_DETAILS:-true}"
MAX_COMMITS_TO_SHOW="${MAX_COMMITS_TO_SHOW:-10}"

echo -e "${BLUE}=== Branch Change Tracking Report ===${NC}"
echo ""
echo "Checking for branches with changes not merged to $MAIN_BRANCH..."
echo ""

# Fetch latest changes
echo "Fetching latest changes from remote..."
git fetch --all --quiet 2>/dev/null || {
    echo -e "${RED}Error: Failed to fetch from remote${NC}"
    exit 1
}

# Check if main branch exists - try remote first, then local
MAIN_REF=""
if git rev-parse $REMOTE/$MAIN_BRANCH >/dev/null 2>&1; then
    MAIN_REF="$REMOTE/$MAIN_BRANCH"
elif git rev-parse $MAIN_BRANCH >/dev/null 2>&1; then
    MAIN_REF="$MAIN_BRANCH"
    echo -e "${YELLOW}Note: Using local $MAIN_BRANCH branch (no remote tracking branch found)${NC}"
else
    echo -e "${RED}Error: Branch $MAIN_BRANCH not found (tried $REMOTE/$MAIN_BRANCH and $MAIN_BRANCH)${NC}"
    exit 1
fi

MAIN_COMMIT=$(git rev-parse $MAIN_REF)
echo -e "Main branch ($MAIN_REF) at commit: ${GREEN}${MAIN_COMMIT:0:8}${NC}"
echo ""

# Counter for branches with unmerged changes
UNMERGED_COUNT=0
TOTAL_BRANCHES=0

# List all remote branches except main
for remote_branch in $(git branch -r | grep -v 'HEAD' | grep -v "/$MAIN_BRANCH$" | sed 's/^[[:space:]]*//'); do
    TOTAL_BRANCHES=$((TOTAL_BRANCHES + 1))
    
    # Extract branch name without remote prefix
    branch_name=$(echo "$remote_branch" | sed "s|^$REMOTE/||")
    
    # Check if branch is ahead of main
    AHEAD=$(git rev-list --count $MAIN_REF..$remote_branch 2>/dev/null || echo "0")
    BEHIND=$(git rev-list --count $remote_branch..$MAIN_REF 2>/dev/null || echo "0")
    
    # Only report branches that have changes not in main
    if [ "$AHEAD" != "0" ] && [ -n "$AHEAD" ]; then
        UNMERGED_COUNT=$((UNMERGED_COUNT + 1))
        
        echo -e "${YELLOW}Branch: ${branch_name}${NC}"
        echo -e "  ${GREEN}✓${NC} Commits ahead of main: ${GREEN}$AHEAD${NC}"
        echo -e "  ${BLUE}↓${NC} Commits behind main: ${BLUE}$BEHIND${NC}"
        
        if [ "$SHOW_DETAILS" = "true" ]; then
            echo "  Unmerged commits:"
            git log --oneline $MAIN_REF..$remote_branch 2>/dev/null | head -n $MAX_COMMITS_TO_SHOW | while read line; do
                echo "    - $line"
            done
            
            # Show if there are more commits
            TOTAL_AHEAD_COMMITS=$(git rev-list --count $MAIN_REF..$remote_branch 2>/dev/null)
            if [ "$TOTAL_AHEAD_COMMITS" -gt "$MAX_COMMITS_TO_SHOW" ]; then
                REMAINING=$((TOTAL_AHEAD_COMMITS - MAX_COMMITS_TO_SHOW))
                echo "    ... and $REMAINING more commit(s)"
            fi
            
            # Show files changed
            echo "  Files changed:"
            git diff --name-status $MAIN_REF..$remote_branch 2>/dev/null | head -n 5 | while read line; do
                echo "    $line"
            done
            FILES_CHANGED=$(git diff --name-only $MAIN_REF..$remote_branch 2>/dev/null | wc -l)
            if [ "$FILES_CHANGED" -gt 5 ]; then
                REMAINING=$((FILES_CHANGED - 5))
                echo "    ... and $REMAINING more file(s)"
            fi
        fi
        
        # Get last commit date
        LAST_COMMIT_DATE=$(git log -1 --format=%cd --date=relative $remote_branch 2>/dev/null)
        echo -e "  Last commit: ${LAST_COMMIT_DATE}"
        
        echo ""
    fi
done

# Summary
echo -e "${BLUE}=== Summary ===${NC}"
echo "Total branches checked: $TOTAL_BRANCHES"
if [ "$UNMERGED_COUNT" -eq 0 ]; then
    echo -e "${GREEN}All branches are up to date with $MAIN_BRANCH${NC}"
else
    echo -e "${YELLOW}Branches with unmerged changes: $UNMERGED_COUNT${NC}"
fi
echo ""

# Exit with status based on unmerged count
if [ "$UNMERGED_COUNT" -gt 0 ]; then
    echo -e "${YELLOW}Tip: Review these branches to determine if they should be merged or deleted${NC}"
    exit 0
else
    exit 0
fi
