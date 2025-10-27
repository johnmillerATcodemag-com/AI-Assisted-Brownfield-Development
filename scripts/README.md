# Branch Change Tracking Scripts

This directory contains scripts to help identify branches with changes that haven't been merged to the main branch.

## Available Scripts

### Bash Script (Linux/Mac/WSL)

**File:** `check_unmerged_branches.sh`

**Usage:**
```bash
# Basic usage
./scripts/check_unmerged_branches.sh

# Configure via environment variables
MAIN_BRANCH=main REMOTE=origin ./scripts/check_unmerged_branches.sh

# Show less detail
SHOW_DETAILS=false ./scripts/check_unmerged_branches.sh

# Show more commits
MAX_COMMITS_TO_SHOW=20 ./scripts/check_unmerged_branches.sh
```

### PowerShell Script (Windows/PowerShell Core)

**File:** `check_unmerged_branches.ps1`

**Usage:**
```powershell
# Basic usage
.\scripts\check_unmerged_branches.ps1

# Specify parameters
.\scripts\check_unmerged_branches.ps1 -MainBranch "main" -Remote "origin"

# Show less detail
.\scripts\check_unmerged_branches.ps1 -ShowDetails $false

# Show more commits
.\scripts\check_unmerged_branches.ps1 -MaxCommitsToShow 20
```

## Configuration Options

Both scripts support the same configuration options:

| Option | Default | Description |
|--------|---------|-------------|
| `MAIN_BRANCH`/`-MainBranch` | `main` | The main branch to compare against |
| `REMOTE`/`-Remote` | `origin` | The remote repository name |
| `SHOW_DETAILS`/`-ShowDetails` | `true` | Whether to show detailed commit and file information |
| `MAX_COMMITS_TO_SHOW`/`-MaxCommitsToShow` | `10` | Maximum number of commits to display per branch |

## Output

The scripts provide:

1. **Branch Information:** List of all branches with unmerged changes
2. **Commit Count:** Number of commits ahead of and behind main
3. **Commit Details:** List of unmerged commits (up to configured maximum)
4. **File Changes:** Files that differ from main
5. **Last Commit Date:** When the branch was last updated
6. **Summary:** Total branches checked and number with unmerged changes

## Example Output

```
=== Branch Change Tracking Report ===

Checking for branches with changes not merged to main...

Fetching latest changes from remote...
Main branch (main) at commit: bb338919

Branch: feature/new-functionality
  ✓ Commits ahead of main: 5
  ↓ Commits behind main: 0
  Unmerged commits:
    - a1b2c3d Add new feature implementation
    - e4f5g6h Update documentation
    - i7j8k9l Add tests
    - m0n1o2p Fix linting issues
    - q3r4s5t Update dependencies
  Files changed:
    M	src/feature.js
    M	docs/README.md
    A	tests/feature.test.js
    M	package.json
  Last commit: 2 hours ago

=== Summary ===
Total branches checked: 5
Branches with unmerged changes: 1

Tip: Review these branches to determine if they should be merged or deleted
```

## Use Cases

1. **Branch Cleanup:** Identify old branches that can be deleted
2. **Code Review:** Find branches that need review before merging
3. **Release Planning:** See what changes are pending for the next release
4. **Team Coordination:** Understand what work is in progress across the team
5. **CI/CD Integration:** Automate branch tracking in workflows

## Integration with CI/CD

You can run these scripts as part of your CI/CD pipeline:

**GitHub Actions Example:**
```yaml
name: Branch Report
on:
  schedule:
    - cron: '0 9 * * 1'  # Every Monday at 9 AM
  workflow_dispatch:

jobs:
  branch-report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - name: Check unmerged branches
        run: |
          chmod +x scripts/check_unmerged_branches.sh
          ./scripts/check_unmerged_branches.sh
```

## Related Scripts

This directory also contains other utility scripts:

- `close_duplicate_security_issues.ps1` - Close duplicate security issues
- `close_latest_security_issues.ps1` - Close latest security issues
- `close_new_security_issues.ps1` - Close new security issues
- `close_resolved_security_issues.ps1` - Close resolved security issues
- `emergency_security_cleanup.ps1` - Emergency security cleanup

## Contributing

When adding new scripts to this directory:

1. Provide both Bash and PowerShell versions when possible
2. Use consistent naming conventions
3. Add configuration options for flexibility
4. Update this README with usage documentation
5. Include example output
6. Make scripts executable (Bash) or properly signed (PowerShell)

## License

See the repository LICENSE file for details.
