@echo off
echo ==========================================
echo       HAFIZA OYUNU BASLATILIYOR...
echo ==========================================
echo.
echo 1. Sistemin rahatlamasi icin Java islemleri temizleniyor...
taskkill /F /IM java.exe 2>nul
taskkill /F /IM javaw.exe 2>nul
taskkill /F /IM gradle.exe 2>nul
echo.
echo 2. OneDrive kilitleri ve eski dosyalar siliniyor...
rmdir /s /q app\build 2>nul
rmdir /s /q .gradle 2>nul
rmdir /s /q "C:\Users\Casper\.android_build_cache" 2>nul
echo.
echo 3. Oyun telefona yukleniyor...
echo    Bu islem biraz surebilir, lutfen bekleyin.
call ./gradlew installDebug --no-daemon

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ==========================================
    echo      BASARILI! OYUN YUKLENDI. :)
    echo ==========================================
) else (
    echo.
    echo ==========================================
    echo      BIR HATA OLUSTU! :(
    echo ==========================================
)
pause
