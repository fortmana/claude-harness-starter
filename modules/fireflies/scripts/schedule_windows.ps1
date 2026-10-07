<#
.SYNOPSIS
  Register (or remove) a Windows scheduled task that runs the Fireflies poll script.

.DESCRIPTION
  OPT-IN. Only run this if the user agreed to scheduled polling. The task runs poll.py as the
  current user, only while logged on, so it can read the OS credential store. It fetches transcripts
  only; processing into notes happens in a Claude Code session.

.EXAMPLE
  .\schedule_windows.ps1 -ScriptDir "$HOME\.claude-harness\fireflies" -IntervalMinutes 60
  .\schedule_windows.ps1 -Remove
#>
param(
    [string]$ScriptDir = "$HOME\.claude-harness\fireflies",
    [int]$IntervalMinutes = 60,
    [string]$TaskName = "ClaudeHarness-FirefliesPoll",
    [string]$Python = "",   # full path to the interpreter recorded in fireflies.toml; defaults to python on PATH
    [switch]$Remove
)

$ErrorActionPreference = "Stop"

if ($Remove) {
    if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
        Write-Host "Removed task '$TaskName'."
    } else {
        Write-Host "Task '$TaskName' not found."
    }
    return
}

$poll = Join-Path $ScriptDir "poll.py"
if (-not (Test-Path $poll)) { throw "poll.py not found in $ScriptDir" }
$python = if ($Python) { $Python } else { (Get-Command python -ErrorAction Stop).Source }

$action  = New-ScheduledTaskAction -Execute $python -Argument "`"$poll`"" -WorkingDirectory $ScriptDir
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) `
           -RepetitionInterval (New-TimeSpan -Minutes $IntervalMinutes)
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopIfGoingOnBatteries `
            -AllowStartIfOnBatteries -ExecutionTimeLimit (New-TimeSpan -Minutes 10)
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings `
    -Description "Polls Fireflies for new transcripts (claude-harness-starter)" | Out-Null

Write-Host "Registered '$TaskName': runs every $IntervalMinutes minutes. Remove with: .\schedule_windows.ps1 -Remove"
