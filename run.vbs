Set oShell = CreateObject("WScript.Shell")
Dim arg0 : arg0 = WScript.Arguments(0)
Dim arg1 : arg1 = WScript.Arguments(1)
Dim str : str = "cmd /c run.bat -n " & arg0 & " -op " & arg1
' str = "cmd /c run.bat -n " & arg0 & " -op " & arg1
oShell.Run str, 0, True
