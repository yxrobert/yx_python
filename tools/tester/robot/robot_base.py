import time
import socket
import threading
import random
from lzo import Lzo
from game_message import *



recv_buff_len = 64 * 1024
packet_head_len = 11


def do_connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        # s.setblocking(0)
    except BaseException:
        pass
    return s


class RobotBase(threading.Thread, CMessage):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        CMessage.__init__(self)

        self._host = host
        self._port = port
        self._is_alive = False


    def get_ver(self):
        return MT_MajorVer().value << 24 | MT_ProtoVer(
        ).value << 16 | MT_MinorVer().value << 8 | MT_ReserVer().value

    def get_protocol_key(self):
        return random.randint(0, 100000)

    def send_packet(self, code, packet):
        self.mes_que[code] = packet

    def send_packet(self, s, code, packet):
        #
        packet.session.protocol_key.value = self.get_protocol_key()
        print "send " + str(code)

        #
        header = msghdr()
        header.protocol.set_value(code)
        header.ver.set_value(self.get_ver())
        buff = ""
        buff_len = 0
        buff, buff_len = packet.serialize(buff, buff_len)
        header.package_len.value = buff_len + packet_head_len
        headerstr = ""
        headerlen = 0
        headerstr, headerlen = header.serialize(headerstr, headerlen)
        s.sendall(headerstr + buff)

    def recv_packet(self, s):
        recv_buff = s.recv(recv_buff_len)
        if len(recv_buff) < packet_head_len:
            return -1, None
        head = msghdr()
        head_buff = recv_buff[:packet_head_len]
        head.deserialize(head_buff)

        print 'recv_packet %d:%d' % (head.protocol.value, head.flags.value)
        #
        if head.flags.value == 1:
            real_len = cint32()
            real_len.deserialize(recv_buff[packet_head_len:])
            buff, buff_len = Lzo.lzo_decompress(recv_buff[packet_head_len + 4:], len(recv_buff) - 15)
            if real_len != buff_len:
                print "unzip head %d len %d!" % (head.protocol.value, buff_len)
            return head.protocol.value, buff[:buff_len]
        else:
            return head.protocol.value, recv_buff[packet_head_len:]

    def tick(self, s):
        if len(self.mes_que) <= 0:
            self.on_idle()

        if len(self.mes_que) > 0:
            k, v = self.mes_que.popitem(False)
            self.send_packet(s, k, v)
        else:
            self.over()


    def over(self):
        self._is_alive = False

    def on_idle(self):
        pass

    def on_start(self):
        pass

    def run(self):
        self._is_alive = True
        s = do_connect(self._host, self._port)
        self.on_start()
        while True:
            try:
                while self._is_alive:
                    self.tick(s)
                    code, buff = self.recv_packet(s)
                    # print 'code ' + str(code)
                    if code > 0:
                        self.process(code, buff)
                    time.sleep(1)

                #
                s.close()
                time.sleep(0.1)
                break
            except socket.error:
                s = do_connect(self._host, self._port)
            except Exception as e:
                print e.message


def main():
    # t = CTest()
    # t.start()
    # m = RobotBase("192.168.44.101", 6380)
    # m.run()
    # m.handle_adventure_step("2222")
    pass


if __name__ == "__main__":
    main()
