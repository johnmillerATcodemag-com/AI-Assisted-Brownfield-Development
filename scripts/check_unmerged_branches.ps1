# Script to identify branches with changes not merged to main
# This helps track which branches have pending work that needs to be reviewed or merged

param(
    [string]$MainBranch = "main",
    [string]$Remote = "origin",
    [bool]$ShowDetails = $true,
    [int]$MaxCommitsToShow = 10
)

$ErrorActionPreference = "Stop"

# Color functions
function Write-ColorOutput {
    param(
        [string]$Message,
        [string]$Color = "White"
    )
    Write-Host $Message -ForegroundColor $Color
}

function Write-Header {
    param([string]$Message)
    Write-ColorOutput $Message "Cyan"
}

function Write-Success {
    param([string]$Message)
    Write-ColorOutput $Message "Green"
}

function Write-Warning {
    param([string]$Message)
    Write-ColorOutput $Message "Yellow"
}

function Write-Error {
    param([string]$Message)
    Write-ColorOutput $Message "Red"
}

Write-Header "=== Branch Change Tracking Report ==="
Write-Host ""
Write-Host "Checking for branches with changes not merged to $MainBranch..."
Write-Host ""

# Fetch latest changes
Write-Host "Fetching latest changes from remote..."
try {
    git fetch --all --quiet 2>$null
} catch {
    Write-Error "Error: Failed to fetch from remote"
    exit 1
}

# Check if main branch exists - try remote first, then local
$mainRef = $null
$mainRefName = ""

$remoteMainExists = $false
try {
    $null = git rev-parse "$Remote/$MainBranch" 2>$null
    if ($LASTEXITCODE -eq 0) {
        $remoteMainExists = $true
    }
} catch {
    $remoteMainExists = $false
}

if ($remoteMainExists) {
    $mainRef = "$Remote/$MainBranch"
    $mainRefName = $mainRef
} else {
    $localMainExists = $false
    try {
        $null = git rev-parse $MainBranch 2>$null
        if ($LASTEXITCODE -eq 0) {
            $localMainExists = $true
        }
    } catch {
        $localMainExists = $false
    }
    
    if ($localMainExists) {
        $mainRef = $MainBranch
        $mainRefName = $MainBranch
        Write-Warning "Note: Using local $MainBranch branch (no remote tracking branch found)"
    } else {
        Write-Error "Error: Branch $MainBranch not found (tried $Remote/$MainBranch and $MainBranch)"
        exit 1
    }
}

$mainCommit = git rev-parse $mainRef
$shortCommit = $mainCommit.Substring(0, 8)
Write-Success "Main branch ($mainRefName) at commit: $shortCommit"
Write-Host ""

# Counter for branches with unmerged changes
$unmergedCount = 0
$totalBranches = 0

# Get all remote branches except main
$remoteBranches = git branch -r | Where-Object { 
    $_ -notmatch 'HEAD' -and $_ -notmatch "/$MainBranch$" 
} | ForEach-Object { $_.Trim() }

foreach ($remoteBranch in $remoteBranches) {
    $totalBranches++
    
    # Extract branch name without remote prefix
    $branchName = $remoteBranch -replace "^$Remote/", ""
    
    # Check if branch is ahead of main
    try {
        $ahead = (git rev-list --count "$mainRef..$remoteBranch" 2>$null)
        $behind = (git rev-list --count "$remoteBranch..$mainRef" 2>$null)
        
        if ([string]::IsNullOrEmpty($ahead)) { $ahead = 0 }
        if ([string]::IsNullOrEmpty($behind)) { $behind = 0 }
    } catch {
        $ahead = 0
        $behind = 0
    }
    
    # Only report branches that have changes not in main
    if ($ahead -gt 0) {
        $unmergedCount++
        
        Write-Warning "Branch: $branchName"
        Write-Success "  ✓ Commits ahead of main: $ahead"
        Write-ColorOutput "  ↓ Commits behind main: $behind" "Cyan"
        
        if ($ShowDetails) {
            Write-Host "  Unmerged commits:"
            $commits = git log --oneline "$mainRef..$remoteBranch" 2>$null | Select-Object -First $MaxCommitsToShow
            foreach ($commit in $commits) {
                Write-Host "    - $commit"
            }
            
            # Show if there are more commits
            $totalAheadCommits = (git rev-list --count "$mainRef..$remoteBranch" 2>$null)
            if ($totalAheadCommits -gt $MaxCommitsToShow) {
                $remaining = $totalAheadCommits - $MaxCommitsToShow
                Write-Host "    ... and $remaining more commit(s)"
            }
            
            # Show files changed
            Write-Host "  Files changed:"
            $filesChanged = git diff --name-status "$mainRef..$remoteBranch" 2>$null | Select-Object -First 5
            foreach ($file in $filesChanged) {
                Write-Host "    $file"
            }
            
            $totalFilesChanged = (git diff --name-only "$mainRef..$remoteBranch" 2>$null | Measure-Object).Count
            if ($totalFilesChanged -gt 5) {
                $remaining = $totalFilesChanged - 5
                Write-Host "    ... and $remaining more file(s)"
            }
        }
        
        # Get last commit date
        $lastCommitDate = git log -1 --format=%cd --date=relative $remoteBranch 2>$null
        Write-Host "  Last commit: $lastCommitDate"
        
        Write-Host ""
    }
}

# Summary
Write-Header "=== Summary ==="
Write-Host "Total branches checked: $totalBranches"
if ($unmergedCount -eq 0) {
    Write-Success "All branches are up to date with $MainBranch"
} else {
    Write-Warning "Branches with unmerged changes: $unmergedCount"
}
Write-Host ""

# Exit with status based on unmerged count
if ($unmergedCount -gt 0) {
    Write-Warning "Tip: Review these branches to determine if they should be merged or deleted"
}

exit 0
