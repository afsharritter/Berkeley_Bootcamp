Sub ClassScanner()

    Dim TargetStudent as string

    for i = 1 to  3

        for j = 1 to 5

        Msgbox("Row:" & i & "Column:" & j & Cells(i, j).Value)

        next j

    next i

End Sub

Sub StarCounter()
    Dim I As Integer
    Dim j As Integer
    'what is nested for loop keeping track of?
        'start with rows, because for each row we need to look at each column
        
    'need to figure out how many rows we have??? just look? = 51
    'start at 2nd row, no headers
    For i = 2 to 51
        'need to add a counter
        Dim totalVolume As Integer
        totalVolume = 0

        'now need to check the number of columns; just the ones with star ratings D:H
        For j = 4 to 8

            If Cells(i, j).Value = "Full-Star" Then
                totalVolume = totalVolume + 1
                'every full-star will increment our total-volume by one"        
            End If
        next j
        'to output the count of full-stars in that row
        Cells(i, 9) = totalVolume
    next i 

End Sub




End Sub