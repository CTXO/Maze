from components import Maze
import os

def clear():
    os.system("cls")


def game_over():
    clear()
    print("Game over, press enter to leave")





easy_maze = Maze(1)
medium_maze = Maze(2)
hard_maze = Maze(3)


def movement(maze_num):

    if maze_num == 1:
        maze = easy_maze
    elif maze_num == 2:
        maze = medium_maze
    else:
        maze = hard_maze

    while True:

        clear()
        print("Level", maze_num)
        for b in range(5):
            print()
        print(maze.cmaze)
        print(f"{maze.moves} moves left")
        direction = input('\n')

        if direction == "w":
            try:
                maze.up()
            except IndexError:
                maze.hit_wall=True

        elif direction == "s":
            try:
                maze.down()
            except IndexError:
                maze.hit_wall = True

        elif direction == "a":
            maze.left()

        elif direction == "d":
            maze.right()

        if maze.out_of_moves or maze.hit_wall:
            maze.won=False
            choice = input("You lost it! Please type 'c' to try again\n")
            if choice == 'c':
                maze.keep_playing = True
            else:
                maze.keep_playing = False
            break

        elif maze.found_exit:
            maze.won=True

        if maze.found_exit:
            if maze_num != 3:
                clear()
                choice = input("Congratulations!!! Type 'c' to go to the next level\n")
                if choice == 'c':
                    maze.keep_playing = True
                else:
                    maze.keep_playing = False
                break
            else:
                choice=input("CONGRATULATIONS, YOU HAVE WON THE GAME!!!")
                input()
                os.system("exit")
                break


print("Welcome to the aMazeing game")
for i in range(5):
    print()

print("Instructions:\n"
      "- Get to the exit(S) to go to the next level\n"
      "- Don't hit the walls(X)\n"
      "- Do not go beyond the screen limits\n"
      "- Watch out your moves left")

input("Hit enter to start")
movement(1)
while not easy_maze.won :
    if easy_maze.keep_playing:
        easy_maze=Maze(1)
        movement(1)
    else:
        break
    
if easy_maze.keep_playing:
    movement(2)
    while not medium_maze.won:
        if medium_maze.keep_playing:
            medium_maze=Maze(2)
            movement(2)
        else:
            break
    if easy_maze.keep_playing:
        movement(3)
        while not hard_maze.won:
            if hard_maze.keep_playing:
                hard_maze=Maze(3)
                movement(3)
            else:
                break
        else:
            game_over()

    else:
        game_over()

else:
    game_over()





