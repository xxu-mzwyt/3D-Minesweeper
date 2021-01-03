# 3D Minesweeper

This is a 3-D version of Minesweeper.

Currently, there is no UI or mouse events.

-------------------------------------------------------

To play 3D Minesweeper, you need to run run.py and type commends to control the game.



```
l x y z
```

Left-click cell (x, y, z) to check the number of mines, where 0 <= x, y, z < board_size.

If there is a mine at (x, y, z), you lose.




```
r x y z
```

Right-click cell (x, y, z) to mark it as a mine.

If all the mines are marked, you win.

-------------------------------------------------------

Variables:

``` Python
# The size of the board.
board_size = 5
# Currently: 5*5*5

# The number of the mines.
mine_num = 10
# Currently: 10 mines
```
