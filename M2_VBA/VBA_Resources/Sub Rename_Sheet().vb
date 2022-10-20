Sub Rename_Sheet()
    Sheets("Sheet1").Name = "Calendar"
End Sub

Private Sub

Sub Format_Headers()
Dim i As Integer 
For i = 1 to 1000
    Cells(1, i).Select
    With Selection
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlBottom
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    Selection.Font.Bold = True  
    Selection.Font.Size = 14
Next i 
End Sub

Sub AddValue_Headers()
    Range("C1").Value = "Academia1"
    Range("D1").Value = "Academia2"
    Range("E1").Value = "Academia2"
    Range("F1").Value = "Work"
    Range("G1").Value= "Degree"
    Range("H1").Value = "Hourly"
    Range("I1").Value = "Yearly"
    Range("J1").Value = "CAB"
End Sub

Sub Format_DataTable()
Dim i As Integer  
For i = 1 to 1000
    Cells(i + 1, i + 2).Select
    With Selection
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlBottom
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
Next i 
End Sub


Sub Bootcamp()

If Column("B").Value = "Sep-22" Then
    For i = 1 to 6
    Cells(i + 1, 3).Value = "Bootcamp"
    Next i  
End If  
End Sub
Sub





















