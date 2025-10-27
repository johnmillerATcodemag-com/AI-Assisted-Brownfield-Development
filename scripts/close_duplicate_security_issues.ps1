# PowerShell script to close duplicate security issues
# This script identifies and closes duplicate security issues created by the security scanner

param(
    [switch]$DryRun = $false,
    [switch]$Verbose = $false
)

# Define the duplicate issues to close and their canonical issues
$duplicateIssues = @{
    # Mailgun API Key Detection
    471 = @{ canonical = 458; reason = "Duplicate Mailgun API key detection in same file" }

    # Insecure HTTP Connections (keep #452 as canonical - MEDIUM severity)
    453 = @{ canonical = 452; reason = "Duplicate HTTP insecurity detection" }
    466 = @{ canonical = 452; reason = "Duplicate HTTP insecurity detection (INFO level)" }
    467 = @{ canonical = 452; reason = "Duplicate HTTP insecurity detection (INFO level)" }

    # XSS/Template Vulnerabilities (keep #463 as canonical - Flask specific)
    462 = @{ canonical = 463; reason = "Duplicate XSS vulnerability (Django variant)" }
    464 = @{ canonical = 463; reason = "Duplicate template injection vulnerability" }
    465 = @{ canonical = 463; reason = "Duplicate Flask XSS vulnerability" }

    # Weak Cryptographic Algorithms (keep specific ones: #460 MD5, #461 SHA1)
    454 = @{ canonical = 460; reason = "Duplicate weak crypto - covered by specific MD5 issue" }
    455 = @{ canonical = 461; reason = "Duplicate weak crypto - covered by specific SHA1 issue" }

    # Weak Random Number Generation
    457 = @{ canonical = 456; reason = "Duplicate weak random number generator detection" }
}

Write-Host "Security Issue Duplicate Cleanup Script" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""

if ($DryRun) {
    Write-Host "DRY RUN MODE - No issues will be actually closed" -ForegroundColor Yellow
    Write-Host ""
}

Write-Host "Duplicate issues to be closed:" -ForegroundColor Green
foreach ($issueNumber in $duplicateIssues.Keys | Sort-Object) {
    $info = $duplicateIssues[$issueNumber]
    Write-Host "  Issue #$issueNumber -> Duplicate of #$($info.canonical)" -ForegroundColor White
    if ($Verbose) {
        Write-Host "    Reason: $($info.reason)" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "Canonical issues to keep open:" -ForegroundColor Green
$canonicals = $duplicateIssues.Values | ForEach-Object { $_.canonical } | Sort-Object -Unique
foreach ($canonical in $canonicals) {
    Write-Host "  Issue #$canonical (keeping as canonical)" -ForegroundColor White
}

Write-Host ""
Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "  Total duplicate issues to close: $($duplicateIssues.Count)" -ForegroundColor White
Write-Host "  Canonical issues to keep: $($canonicals.Count)" -ForegroundColor White
Write-Host "  Net reduction: $($duplicateIssues.Count) issues" -ForegroundColor White

if (-not $DryRun) {
    Write-Host ""
    $confirm = Read-Host "Do you want to proceed with closing these duplicate issues? (y/N)"

    if ($confirm -eq 'y' -or $confirm -eq 'Y') {
        Write-Host ""
        Write-Host "Closing duplicate issues..." -ForegroundColor Yellow

        foreach ($issueNumber in $duplicateIssues.Keys | Sort-Object) {
            $info = $duplicateIssues[$issueNumber]
            $closeComment = "Closing as duplicate of #$($info.canonical). $($info.reason)."

            try {
                Write-Host "  Closing issue #$issueNumber..." -ForegroundColor White

                # Add comment explaining the closure
                gh issue comment $issueNumber --body $closeComment

                # Close the issue
                gh issue close $issueNumber --reason "not planned"

                Write-Host "    ✓ Issue #$issueNumber closed successfully" -ForegroundColor Green

            }
            catch {
                Write-Host "    ✗ Failed to close issue #$issueNumber`: $_" -ForegroundColor Red
            }

            Start-Sleep -Milliseconds 500  # Rate limiting
        }

        Write-Host ""
        Write-Host "Duplicate cleanup completed!" -ForegroundColor Green

    }
    else {
        Write-Host "Operation cancelled." -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "GitHub CLI Commands (for manual execution):" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
foreach ($issueNumber in $duplicateIssues.Keys | Sort-Object) {
    $info = $duplicateIssues[$issueNumber]
    $closeComment = "Closing as duplicate of #$($info.canonical). $($info.reason)."
    Write-Host "gh issue comment $issueNumber --body `"$closeComment`"" -ForegroundColor Gray
    Write-Host "gh issue close $issueNumber --reason `"not planned`"" -ForegroundColor Gray
    Write-Host ""
}
