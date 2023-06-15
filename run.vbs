Set oShell = CreateObject("WScript.Shell")
Dim arg0 : arg0 = WScript.Arguments(0)
Dim arg1 : arg1 = WScript.Arguments(1)
Dim str : str = "cmd /c python main.py -n " & arg0 & " -op " & arg1
oShell.Run str, 0, True
