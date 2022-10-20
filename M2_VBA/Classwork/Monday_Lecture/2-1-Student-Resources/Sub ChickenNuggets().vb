Sub ChickenNuggets()

for i = 1 to 10
    'Write I will eat
    Cells(i, 1).Value = "I will eat"
    Cells(i, 2).Value = 10 + i 
    Cells(i, 3).Value = "Chicken Nuggets"

Next i

End Sub




Sub DayDateColumn()

for i = 1 to 7
    Cells(1, i).Value = i
    Cells(2, i).Value = i + 2
Next I

End Sub