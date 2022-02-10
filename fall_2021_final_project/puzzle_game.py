'''
    CS5001
    Fall 2021
    Final project
    RUIHAN DING
    Sliding puzzle game
'''
import random
import turtle
import time
import math

class Game:
    '''
    create a class about the game control area
    '''
    def __init__(self):
        self.add_image()
        self.file_image("mario.puz")
        self.prompt()
        self.rectangle()
        self.pa = PlayArea(self)
        self.ld = Leader(self)
        self.set_reset_button()
        self.set_load_button()
        self.set_quit_button()
        self.move = 0
        self.text_player_moves()
        turtle.Screen().mainloop()

    def file_image(self, image_name):
        '''
        :param image_name: input the image_name to load the game.puz
        :return: the side length of the game
                 the thumbnail of the game
                 all the game pictures and shaffle them
        '''
        info = []
        try:
            image_puz = open(image_name, "r")
        except IOError:
            print("A file error occurred")

        for line in image_puz.readlines():
            line = line.split()
            for i in range(len(line)):
                line[i] = line[i].strip(": ")
            info.append(line)
        self.side_len = int(math.sqrt(int(info[1][1])))
        self.number = int(info[1][1])
        self.thumbnail = info[3][1]
        self.original_block = []
        for i in range(4, len(info)):
            self.original_block.append(info[i][1])
        self.block_images = self.original_block.copy()
        random.shuffle(self.block_images)

    def add_image(self):
        '''
        put all the reminder picture in a dictionary
        :return: a button picture dictionary
        '''
        screen = turtle.Screen()
        self.images = dict()
        self.images["screen_image"] = "Resources/splash_screen.gif"
        self.images["reset_image"] = "Resources/resetbutton.gif"
        self.images["quit_image"] = "Resources/quitbutton.gif"
        self.images["load_image"] = "Resources/loadbutton.gif"
        self.images["win_image"] = "Resources/winner.gif"
        self.images["lose_image"] = "Resources/lose.gif"
        self.images["credits"] = "Resources/credits.gif"
        self.images["f_error"] = "Resources/file_error.gif"
        self.images["quitmsg"] = "Resources/quitmsg.gif"
        screen.addshape(self.images["screen_image"])
        screen.addshape(self.images["reset_image"])
        screen.addshape(self.images["quit_image"])
        screen.addshape(self.images["load_image"])
        screen.addshape(self.images["win_image"])
        screen.addshape(self.images["lose_image"])
        screen.addshape(self.images["credits"])
        screen.addshape(self.images["f_error"])
        screen.addshape(self.images["quitmsg"])

    def prompt(self):
        '''
        :return: the player name and the move
        '''
        turtle.shape(self.images["screen_image"])
        time.sleep(2)
        turtle.clearscreen()
        self.name, self.move_limit = None, None
        while self.name is None or self.name == "":
            self.name = turtle.textinput("CS5001 Puzzle Slide", "Your name:")
        while self.move_limit == None:
            self.move_limit = turtle.numinput("CS5001 Puzzle Slide - moves",
                                        "Enter the number of moves(chances) you want(5-200)",
                                              50, minval=5, maxval=200)
    def add_move(self, win):
        '''
        :param win: win is boolean
        if win, the picture of win will show and if not,the move will add one
        '''
        if win:
            self.move += 1
            self.text_player_moves()
            tt = turtle.Turtle()
            tt.up()
            tt.goto(20, 50)
            tt.down()
            tt.shape(self.images["win_image"])
            self.ld.keep_win_leader(win, self.move, self.name)
            turtle.exitonclick()
        else:
            self.move += 1
            self.text_player_moves()
            if self.move >= self.move_limit:
                tt = turtle.Turtle()
                tt.up()
                tt.goto(20, 50)
                tt.down()
                tt.shape(self.images["lose_image"])
                time.sleep(2)
                tt.clear()
                tt.up()
                tt.goto(-20, 30)
                tt.down()
                tt.shape(self.images["credits"])
                turtle.exitonclick()

    def rectangle(self):
        '''
        :return: draw the rectangle area of the game
        '''
        tt = turtle.Turtle()
        tt.up()
        tt.hideturtle()
        tt.pensize(5)
        tt.speed(10)
        tt.goto(-310, -170)
        tt.down()
        i = 0
        while i < 2:
            tt.forward(600)
            tt.right(90)
            tt.forward(110)
            tt.right(90)
            i += 1

    def text_player_moves(self):
        '''
        :return: create the text of the move reminder
        '''
        turtle.clear()
        turtle.hideturtle()
        turtle.up()
        turtle.goto(-280, -240)
        turtle.down()
        move_text = "Player Moves: " + str(self.move)
        turtle.write(move_text, font=("Arial", 25, "normal"))

    def set_reset_button(self):
        '''
        :return: add the reset button picture
        '''
        tt = turtle.Turtle()
        tt.up()
        tt.goto(50, -225)
        tt.down()
        tt.shape(self.images["reset_image"])
        tt.onclick(self.reset_button)

    def reset_button(self, x, y):
        '''
        :return:set the function of the reset button
        '''
        self.pa.reset_image()
        self.move = 0
        self.text_player_moves()

    def set_load_button(self):
        '''
        :return: add the load button picture
        '''
        tt = turtle.Turtle()
        tt.up()
        tt.goto(140, -225)
        tt.down()
        tt.shape(self.images["load_image"])
        tt.onclick(self.load_button)

    def load_button(self, x, y):
        '''
        :return: set the function of load button
        '''
        self.game_name = turtle.textinput("Load Puzzle",
                                          "Enter the name of the puzzle you wish to load. Choices are:\n"
                                          "luigi.puz\n"
                                          "smiley.puz\n"
                                          "fifteen.puz\n"
                                          "mario.puz\n"
                                          "yoshi.puz")
        if self.game_name != "luigi.puz" and self.game_name != "smiley.puz" and \
                self.game_name != "mario.puz" and self.game_name != "fifteen.puz" and self.game_name != "yoshi.puz":
            tt = turtle.Turtle()
            tt.up()
            tt.goto(-10, 10)
            tt.down()
            tt.shape(self.images["f_error"])
            time.sleep(2)
            tt.hideturtle()

        self.pa.change_image(self.game_name)
        self.ld.change_image(self.game_name)

    def set_quit_button(self):
        '''
        :return: add the quit button picture
        '''
        tt = turtle.Turtle()
        tt.up()
        tt.goto(230, -225)
        tt.down()
        tt.shape(self.images["quit_image"])
        tt.onclick(self.quit_button)

    def quit_button(self, x, y):
        '''
        :return: set the quit button function
        '''
        tt = turtle.Turtle()
        tt.up()
        tt.goto(-10, 10)
        tt.down()
        tt.shape(self.images["quitmsg"])
        time.sleep(2)
        turtle.bye()

    def quit(self, x, y):
        '''
        :return: quit the game
        '''
        tt = turtle.Screen()
        tt.bye()

class PlayArea:
    '''
    create the game play area's class
    '''
    def __init__(self, Game):
        self.Game = Game
        self.turtles = []
        self.rectangle()
        self.change_image("mario.puz")

    def change_image(self, image_name):
        '''
        :param image_name: the name of changing game
        :return: change the game
        '''
        self.Game.file_image(image_name)
        self.turtle()
        self.load_image()

    def rectangle(self):
        '''
        :return: draw the rectangle play area
        '''
        tt = turtle.Turtle()
        tt.up()
        tt.hideturtle()
        tt.pensize(5)
        tt.speed(10)
        tt.goto(-310, 280)
        tt.down()
        i = 0
        while i < 2:
            tt.forward(420)
            tt.right(90)
            tt.forward(420)
            tt.right(90)
            i += 1

    def turtle(self):
        '''
        :return: set the turtle at each of the picture's position in order to draw the picture
        '''
        for tt in self.turtles:
            tt.hideturtle()
        self.turtles = []
        for i in range(self.Game.number):
            tt = turtle.Turtle()
            tt.hideturtle()
            x = i % self.Game.side_len
            y = math.floor(i / self.Game.side_len)
            tt.up()
            tt.goto(-250 + (x * 100), 220 - (y * 100))
            tt.down()
            self.turtles.append(tt)
        for i in range(self.Game.number):
            self.turtles[i].showturtle()

    def load_image(self):
        '''
        :return: add the game image to the position and set the blank image's position
        '''
        for i in range(len(self.Game.block_images)):
            if self.Game.block_images[i] == self.Game.original_block[-1]:
                self.blank = i
        for i in range(len(self.Game.block_images)):
            screen = turtle.Screen()
            screen.addshape(self.Game.block_images[i])
            tt = self.turtles[i]
            tt.shape(self.Game.block_images[i])
        self.set_blank_button()

    def reset_image(self):
        '''
        :return: reset the game image
        '''
        for i in range(len(self.Game.original_block)):
            screen = turtle.Screen()
            screen.addshape(self.Game.original_block[i])
            tt = self.turtles[i]
            tt.shape(self.Game.original_block[i])
            self.Game.block_images[i] = self.Game.original_block[i]
        self.blank = len(self.Game.original_block) - 1
        self.set_blank_button()

    def isValid(self, x, y):
        '''
        :return: judge the blank's surrounding picture if in the rectangle area
        '''
        if -1 < x < self.Game.side_len and -1 < y < self.Game.side_len:
            return True
        return False

    def set_blank_button(self):
        '''
        set the picture's position as number and set the blank's surrounding picture as the one can click and move
        '''
        change = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        x = self.blank / self.Game.side_len
        y = self.blank % self.Game.side_len
        for dx, dy in change:
            newx = int(x + dx)
            newy = int(y + dy)
            if not self.isValid(newx, newy):
                continue
            new_position = newx * self.Game.side_len + newy
            button_turtle = self.turtles[new_position]
            button_turtle.onclick(self.create_onclick_function(new_position))

    def create_onclick_function(self, new_position):
        '''
        :return: create the function can click and return another function
        '''
        return lambda x, y: self.switch_blank_with_new_position(new_position)

    def switch_blank_with_new_position(self, new_position):
        '''
        :param new_position: the blank picture's position
        switch the blank's position with the clicked picture
        '''
        change = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        x = self.blank / self.Game.side_len
        y = self.blank % self.Game.side_len
        for dx, dy in change:
            newx = int(x + dx)
            newy = int(y + dy)
            if not self.isValid(newx, newy):
                continue
            self.turtles[newx * self.Game.side_len + newy].onclick(None)
        self.Game.block_images[self.blank], self.Game.block_images[new_position] = self.Game.block_images[new_position], self.Game.block_images[self.blank]
        self.turtles[self.blank].shape(self.Game.block_images[self.blank])
        self.turtles[new_position].shape(self.Game.block_images[new_position])
        self.blank = new_position
        self.set_blank_button()
        # when all the pictures move to the right position, set the win as True
        if self.Game.block_images == self.Game.original_block:
            win = True
        else:
            win = False
        self.Game.add_move(win)

class Leader:
    '''
    create the leaderboard's class
    '''
    def __init__(self, Game):
        self.Game = Game
        self.add_image()
        self.rectangle()
        self.init_turtle()
        self.change_image("mario.puz")
        self.read_old_win(True)
        self.write_leaderboard()

    def add_image(self):
        '''
        :return: add the leaderboard error picture
        '''
        screen = turtle.Screen()
        self.images = dict()
        self.images["ldb_error"] = "Resources/leaderboard_error.gif"
        screen.addshape(self.images["ldb_error"])

    def read_old_win(self, win):
        '''
        :param win: win is a boolean variable
        open the file to read the former win leader
        '''
        if win:
            self.leader_old_info = []
            try:
                with open("leaderboard.txt", "r") as leader:
                    for line in leader:
                        line = line.split()
                        for i in range(len(line)):
                            line[i] = line[i].strip(":")
                        self.leader_old_info.append(line)

            except IOError:
                tt = turtle.Turtle()
                tt.up()
                tt.goto(-10, 10)
                tt.down()
                tt.shape(self.images["ldb_error"])
                time.sleep(2)
                tt.hideturtle()

    def keep_win_leader(self, win, move, name):
        '''
        :param win: the boolean variable
        :param move: if the player wins, keep the move
        :param name: the player name
        :return: write the new winner in the file and sort these names in order
        '''
        if win:
            try:
                with open("leaderboard.txt", "w") as leader:
                    self.leader_new_info = [str(self.Game.move), self.Game.name]
                    self.leader_old_info.append(self.leader_new_info)
                    self.leader_old_info.sort(key=lambda x: x[0])
                    for i in range(len(self.leader_old_info)):
                        leader_board = str(self.leader_old_info[i][0]) + ": " + self.leader_old_info[i][1] + "\n"
                        leader.write(leader_board)
            except IOError:
                print("A file error occurred")

    def write_leaderboard(self):
        '''
        write the previous winner at the leaderboard place
        '''
        for i in range(len(self.leader_old_info)):
            content = str(self.leader_old_info[i][0]) + ": " + self.leader_old_info[i][1] + "\n"
            tt = turtle.Turtle()
            tt.up()
            tt.hideturtle()
            tt.goto(130, 180 - 25 * i)
            tt.color("blue")
            tt.write(content, font=("Arial", 17, "normal"))

    def rectangle(self):
        '''
        draw the rectangle area of the leaderboard
        '''
        tt = turtle.Turtle()
        tt.up()
        tt.hideturtle()
        tt.pensize(5)
        tt.color("blue")
        tt.speed(10)
        tt.goto(120, 280)
        tt.down()
        i = 0
        while i < 2:
            tt.forward(170)
            tt.right(90)
            tt.forward(420)
            tt.right(90)
            i += 1
        tt.up()
        tt.hideturtle()
        tt.goto(130, 240)
        tt.write("Leaders:", font=("Arial", 17, "normal"))

    def init_turtle(self):
        '''
        set the turtle at the right place
        :return:
        '''
        self.tt = turtle.Turtle()
        self.tt.up()
        self.tt.goto(250, 270)
        self.tt.down()

    def change_image(self, image_name):
        '''
        :param image_name: the game name that load
        :return: draw the thumbnail image
        '''
        screen = turtle.Screen()
        screen.addshape(self.Game.thumbnail)
        self.tt.shape(self.Game.thumbnail)

def main():
    game = Game()

if __name__ == "__main__":
    main()
