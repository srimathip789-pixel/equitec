@echo off
echo ========================================================
echo   Testing Job Reply Checker System
echo ========================================================
echo.

cd /d "C:\Users\Sri Mathi\OneDrive\Desktop\RESUME\job_automation\01_email_automation"

echo Step 1: Running Test Suite...
echo --------------------------------------------------------
python test_reply_checker.py
echo.

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ✗ Tests failed! Please check the errors above.
    pause
    exit /b 1
)

echo.
echo ========================================================
echo   Tests Completed Successfully!
echo ========================================================
echo.
echo Press any key to run the actual reply checker...
pause

echo.
echo Step 2: Running Actual Reply Checker...
echo --------------------------------------------------------
python check_job_replies.py

echo.
echo ========================================================
echo   Execution Complete!
echo ========================================================
echo.
echo Check the following locations:
echo   - logs\positive_replies_alerts\ (for alert files)
echo   - data\positive_job_replies.csv (for logged replies)
echo.
pause
