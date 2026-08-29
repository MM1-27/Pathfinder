import pygame

def dijkstra(grid):
    start = grid.start
    end = grid.end

    unvisited = [start]
    distances = {start: 0}
    came_from = {}
    visited = set()

    while unvisited:
        #selecting which of the unvisited nodes to go down
        smallest_node = unvisited[0]
        smallest_distance = distances[smallest_node]
        for node in unvisited:
            if distances[node] < smallest_distance:
                smallest_node = node
                smallest_distance = distances[node]
        
        unvisited.remove(smallest_node)

        r, c = smallest_node
        visited.add((r, c))

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
                if grid.cells[row][col] != 1:  # not a wall
                    new_dist = distances[(r, c)] + 1

                    # If this path is better, update it
                    if (row,col) not in distances or new_dist < distances[(row, col)]:
                        distances[(row, col)] = new_dist
                        came_from[(row, col)] = (r, c)

                        if (row, col) not in visited:
                            unvisited.append((row, col))