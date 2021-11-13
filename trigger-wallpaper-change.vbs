Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "<Path to Python script>" & Chr(34), 0
Set WinScriptHost = Nothing
