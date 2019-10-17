# _*_ coding: utf-8 _*_
from robot_base import *
import logging
from map import MapConfig
import time

class GameRobot(RobotBase):
    def __init__(self, host, ip, data):
        RobotBase.__init__(self, host, ip)

        self._data = {}
        self._t = int(time.time())

        #
        self._data["id"] = data["id"]
        self._data["account"] = data["name"]
        self._data["nickname"] = data["name"]
        self._data["session"] = session_t()
        self._data["account_info"] = platform_account_t()
        self._data["account_info"].server_id.value = data["server_id"]
        self._data["account_info"].self_channel.value = data["channel"]
        self._data["account_info"].platform_id.value = data["name"]
        self._data["user_id"] = 0
        self._data["block_id"] = -1
        self._data["region"] = data["region"]

    def set_attr(self, attr, val):
        self._data[attr] = val

    def get_attr(self, attr):
        return self._data[attr]

    def make_login_packet(self, packet):
        packet.account_info = self.get_attr("account_info")
        #packet.s_session.value = self.get_attr("account_info").platform_id.value
        packet.ip.value = str(packet.account_info.server_id)
        packet.device_id.value = 'pc'

    def make_register_packet(self, packet):
        packet.account_info = self.get_attr("account_info")
        packet.session = self.get_attr("session")
        packet.nick_name.value = self.get_attr("nickname")
        packet.region.value = self.get_attr("region")
        packet.region.value = self.get_attr("region")
        packet.head_entry.value = 1

    def make_get_land_info_packet(self, packet):
        packet.session = self.get_attr("session")
        packet.chunk_id.value = MapConfig.blockid_to_chunkid(self.get_attr("block_id"))
        # packet.chunk_id.value = MapConfig.rand_chunk_id()

    def make_get_chunk_events_packet(self, packet):
        packet.session = self.get_attr("session")
        packet.chunk_id.value = MapConfig.blockid_to_chunkid(self.get_attr("block_id"))
        # packet.chunk_id.value = MapConfig.rand_chunk_id()

    def make_get_user_info_packet(self, packet):
        packet.session = self.get_attr("session")

    def make_get_castle_list_packet(self, packet):
        packet.session = self.get_attr("session")

    # def make_gm_command_packet(self, packet):
    #     packet.session = self.get_attr("session")
    def send_gm(self, command):
        packet = cs_gm_command()
        packet.session = self.get_attr("session")
        packet.command.value = command
        self.send_packet(OP_CODE.CS_GM_COMMAND, packet)


    def handle_login(self, packet):
        print "recv_login result %d" % (packet.common_result.result.value.value)

        # print "user_id lld%  key %d" % (packet.res_info.session.user_id.value, packet.res_info.session.key.value)
        self.set_attr("session", packet.res_info.session)
        self.set_attr("user_id", packet.res_info.session.user_id.value)

        if packet.common_result.result.value.value == e_op_result_login_nochar().value:
            self.send_register()
            return
        elif packet.common_result.result.value.value == e_op_result_login_s().value:
            time.sleep(1)
        elif packet.common_result.result.value.value == e_op_result_login_failed().value:
            time.sleep(3)
        elif packet.common_result.result.value.value == e_op_result_ok().value:
            self._t = int(time.time())
            self.on_login()
            logging.error("login ok id:  %s", self.get_attr("id"))
            return
        else:
            logging.error("recv_login %d", packet.common_result.result.value.value)
            print "error"

        self.send_login()

    def handle_register(self, packet):
        print "handle_register %d" % (packet.common_result.result.value.value)
        if packet.common_result.result.value.value == e_op_result_register_success().value:
            self.send_login()
        else:
            time.sleep(2)
            self.send_register()

    def handle_get_user_info(self, packet):
        self.set_attr("region", packet.user.region.value)
        # self.set_attr("block", packet.user.land_coord_list[0].value)

    def handle_get_castle_list(self, packet):
        self.set_attr("block_id", packet.castle_info_list[0].centre_coord.value)

    def on_login(self):
        self.send_get_user_info()
        self.send_get_castle_list()

    def on_idle(self):
        # self.over()
        print "on_idle"
        time.sleep(1)
        # self.send_get_user_info()
        self.send_get_land_info()
        self.send_get_chunk_events()

    def on_start(self):
        self.send_login()

# config
tab_config = [
    ['192.168.44.38', 6380, 2001],  # linux
    ['192.168.44.101', 6380, 2004],  # mine
    ['192.168.44.47', 6380, 2015],  # wenjun
]
idx = 1


def main():
    data = {}
    data['id'] = 1
    data['name'] = 'robot1'
    data['server_id'] = tab_config[idx][2]
    data['channel'] = '425800000'
    data['region'] = 1

    robot = GameRobot(tab_config[idx][0], tab_config[idx][1], data)
    robot.start()
    robot.join()
    # r = CTest()
    # r.start()
    pass


if __name__ == "__main__":
    main()
