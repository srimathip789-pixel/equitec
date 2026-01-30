@echo off
echo ========================================================
echo   AUTOMATED TEST, COMMIT & PUSH - Job Reply Checker
echo ========================================================
echo.

REM Step 1: Run Tests
echo.
echo [1/4] Running Tests...
echo --------------------------------------------------------
cd /d "C:\Users\Sri Mathi\OneDrive\Desktop\RESUME\job_automation\01_email_automation"
python test_reply_checker.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ✗ Tests failed! Aborting commit and push.
    pause
    exit /b 1
)

echo.
echo ✓ Tests passed successfully!
echo.

REM Step 2: Run Actual Reply Checker (Optional)
echo.
echo [2/4] Running Reply Checker on Your Inbox...
echo --------------------------------------------------------
python check_job_replies.py

echo.
echo ✓ Reply checker completed!
echo.

REM Step 3: Commit Changes
echo.
echo [3/4] Committing Changes to Git...
echo --------------------------------------------------------
cd /d "C:\Users\Sri Mathi\OneDrive\Desktop\RESUME\job_automation"

git status

echo.
echo Adding files...
git add 01_email_automation/check_job_replies.py
git add 01_email_automation/whatsapp_notifier.py
git add 01_email_automation/test_reply_checker.py
git add 01_email_automation/README_JOB_REPLY_CHECKER.md
git add run_morning_automation.bat
git add config/config.py
git add IMPLEMENTATION_SUMMARY_JOB_REPLY_CHECKER.md

echo.
echo Committing...
git commit -m "feat: Add automated job reply checker with positive response detection and auto-reply - Added check_job_replies.py to monitor Gmail for job application replies - Implemented positive/negative response detection using keyword analysis - Created auto-reply system for positive responses - Added whatsapp_notifier.py for multiple notification methods - Integrated reply checker as Step 3 in daily automation workflow - Created comprehensive documentation and test suite - Updated config.py with MY_WHATSAPP_NUMBER setting - Notifications saved to logs/positive_replies_alerts/ as text files"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ✗ Commit failed! Please check the error above.
    pause
    exit /b 1
)

echo.
echo ✓ Changes committed successfully!
echo.

REM Step 4: Push to Remote
echo.
echo [4/4] Pushing to Remote Repository...
echo --------------------------------------------------------
git push

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ✗ Push failed! You may need to specify the branch.
    echo.
    echo Please run manually:
    echo   cd "C:\Users\Sri Mathi\OneDrive\Desktop\RESUME\job_automation"
    echo   git push origin YOUR_BRANCH_NAME
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================================
echo   ✅ ALL STEPS COMPLETED SUCCESSFULLY!
echo ========================================================
echo.
echo Summary:
echo   ✓ Tests passed
echo   ✓ Reply checker executed
echo   ✓ Changes committed to Git
echo   ✓ Changes pushed to remote repository
echo.
echo Your job reply checker is now live! 🚀
echo.
echo Check:
echo   - GitHub for the pushed changes
echo   - logs\positive_replies_alerts\ for any positive replies
echo.
pause
