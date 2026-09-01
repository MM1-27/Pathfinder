import pygame

def a_star(grid):
    start = grid.start
    end = grid.end

    unvisited = [start]
    g_scores = {start: 0} #storing distances from the start point - g(n)
    f_scores = {start: heuristic(start, end)} #storing estimated total cost - g(n) + h(n)
    came_from = {}
    visited = set()

    while unvisited:
        #selecting which of the unvisited nodes to go down
        smallest_node = unvisited[0]
        smallest_f = f_scores[smallest_node]
        for node in unvisited:
            if f_scores[node] < smallest_f:
                smallest_node = node
                smallest_f = f_scores[node]
        
        unvisited.remove(smallest_node)

        visited.add(smallest_node)
        r, c = smallest_node

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
            if 0 <= row < grid.rows and 0 <= col < grid.cols:
                if grid.cells[row][col] != 1:  #not a wall
                    potential_new_g = g_scores[(r,c)] + 1 #potential because we're only gonna use it if it is a better score than what we already have
                    #if this path is better, update it
                    if (row,col) not in g_scores or potential_new_g < g_scores[(row, col)]:
                        g_scores[(row,col)] = potential_new_g
                        came_from[(row,col)] = (r, c)

                        f_scores[(row,col)] = potential_new_g + heuristic((row,col), end)

                        if (row, col) not in visited and (row, col) not in unvisited:
                            unvisited.append((row, col))

def heuristic(a,b): #Manhattan heuristic
    (r1,c1) = a
    (r2,c2) = b
    return abs(r1-r2) + abs(c1-c2)