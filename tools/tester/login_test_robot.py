from robot_game import GameRobot
import time

class LoginRobot(GameRobot):

    def on_login(self):
        GameRobot.on_login(self)
        # self.send_get_user_info()

    def on_idle(self):
        # self.over()
        print "on_idle"
        time.sleep(1)
        # self.send_get_user_info()
        self.send_get_land_info()
        self.send_get_chunk_events()
