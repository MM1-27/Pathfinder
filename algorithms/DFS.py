import pygame

def dfs(grid):
    start = grid.start
    end = grid.end

    stack = [start]
    visited = set()
    came_from = {} #used to backtrack to the start after finding the end point


    while stack:
        r,c = stack.pop() #LIFO
        visited.add((r,c))

        if grid.cells[r][c] != 2 and grid.cells[r][c] != 3: #mark cell as visited as long as its not start or end
            grid.cells[r][c] = 4

        #update the grid display
        grid.draw(grid.screen)
        pygame.display.flip()
        pygame.time.delay(10)

        #reconstruct the fastest path at the end
        if (r,c) == end:
            current = end
            while current != start:
                r2, c2 = current
                if grid.cells[r2][c2] != 2 and grid.cells[r2][c2] != 3: #don't overwrite start/end
                    grid.cells[r2][c2] = 5 #final path colour
                current = came_from[current]

                # animate path drawing
                grid.draw(grid.screen)
                pygame.display.flip()
                pygame.time.delay(20)
            return

        neighbours = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
        for neighbour in neighbours:
            row = neighbour[0]
            col = neighbour[1]

            if row>=0 and row<grid.rows and col>=0 and col<grid.cols: #if the coords are in range
                if grid.cells[row][col] != 1 and (row,col) not in visited: #if its not a wall and its not been visited yet
                    stack.append((row,col))
                    came_from[(row, col)] = (r, c) #store parent