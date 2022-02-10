

def keep_win_leader(win, move, name):
    if win:
        try:
            with open("leaderboard_text.txt", "w") as leader:
                self.leader_new_info = [self.Game.move, self.Game.name]
                self.leader_old_info.append(self.leader_new_info)
                self.leader_old_info.sort(key=lambda x: x[0])
                for i in range(len(self.leader_old_info)):
                    leader_board = str(self.leader_old_info[i][0]) + ": " + self.leader_old_info[i][1] + "\n"
                    leader.write(leader_board)
        except IOError:
            print("A file error occurred")


def write_leaderboard(self):
    tt = turtle.Turtle()
    tt.up()
    tt.hideturtle()
    tt.goto(130, 220)
    tt.color("blue")
    for each in self.leader_old_info:
        tt.write(each, font=("Arial", 17, "normal"))

def main():
    keep_win_leader(True, 2, "Keith")
if __name__ == "__main__":
    main()
