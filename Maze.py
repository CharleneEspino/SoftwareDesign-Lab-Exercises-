from pymaze import maze, agent
def BFS(m):
        global childCell
        start=(m.rows,m.cols)
        frontier=[start]
        explored=[start]
        bfsPath={}
        while len(frontier)>0:
            currCell = frontier.pop(0)
            if currCell == (1,1):
                break
            for j in 'ESPN':
                if m.maze_map[currCell][j]== True:
                    if j == 'E':
                        childCell=(currCell[0],currCell[1]+1)
                elif j == 'S':
                    childCell=(currCell[0],currCell[1]-1)
                elif j == 'P':
                    childCell=(currCell[0]-1,currCell[1])
                elif j == 'N':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue

                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell

fwdPath={}
cell = (1,1)
while cell!=start:
    fwdPath[bfsPath[cell]]=cell
    cell=bfsPath[cell]

m = maze(20,30)
m.CreateMaze()
path=BFS(m)

a=agent(m,footprints =True)
m.tracePath({a:path})
m.run()