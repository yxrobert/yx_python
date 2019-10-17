import os
import os.path
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

file_dir = "..\\..\\..\\..\\public\\protocol\\"
gen_proto_dir = ""


def write_class_init(keys):
    strproto = "\tdef __init__(self):\n"
    for line in keys:
        if len(line) == 2:
            if(line[0].find("int64") != -1 or line[0].find("int32") != -1
               or line[0].find("bool") != -1
               or line[0].find("string") != -1
               or line[0].find("uint32") != -1
               or line[0].find("uint8") != -1
               or line[0].find("uint16") != -1):
                line[0] = "c" + line[0].strip()
            strproto += "\t\tself." + \
                line[1].strip() + " = " + line[0].strip() + "()\n"
        elif len(line) == 3:
            strproto += "\t\tself." + line[1].strip() + " = []\n"
    if len(keys) == 0:
        strproto += "\t\tpass"
    strproto += "\n"
    return strproto


def write_class_serialize(keys):
    strproto = "\tdef serialize(self, buff, buff_len):\n"
    for line in keys:
        if len(line) == 2:
            strproto += "\t\tbuff, buff_len = self." + \
                line[1].strip() + ".serialize(buff, buff_len)\n"
        elif len(line) == 3:
            strproto += "\t\tfor i in range(self.len_of_" + \
                line[1].strip() + ".value):\n"
            strproto += "\t\t\tbuff, buff_len = self." + \
                line[1].strip() + "[i].serialize(buff, buff_len)\n"

    strproto += "\t\treturn buff, buff_len\n"
    strproto += "\n"
    return strproto


def write_class_deserialize(keys):
    strproto = "\tdef deserialize(self, buff):\n"
    for line in keys:
        if len(line) == 2:
            strproto += "\t\tbuff = self." + \
                line[1].strip() + ".deserialize(buff)\n"
        elif len(line) == 3:
            if(line[0].find("int64") != -1 or line[0].find("int32") != -1
               or line[0].find("bool") != -1
               or line[0].find("string") != -1
               or line[0].find("uint32") != -1
               or line[0].find("uint8") != -1
               or line[0].find("uint16") != -1):
                line[0] = "c" + line[0].strip()
            strproto += "\t\tself." + line[1].strip() + " = []\n"
            strproto += "\t\tfor i in range(self.len_of_" + \
                line[1].strip() + ".value):\n"
            strproto += "\t\t\tself." + \
                line[1].strip() + ".append(" + line[0] + "())\n"
            strproto += "\t\t\tbuff = self." + \
                line[1].strip() + "[i].deserialize(buff)\n"

    strproto += "\t\treturn buff\n"
    strproto += "\n"
    return strproto


def write_class_repeated(keys):
    strproto = ""
    for line in keys:
        if len(line) == 3:
            if(line[0].find("int64") != -1 or line[0].find("int32") != -1
               or line[0].find("bool") != -1
               or line[0].find("string") != -1
               or line[0].find("uint32") != -1
               or line[0].find("uint8") != -1
               or line[0].find("uint16") != -1):
                line[0] = "c" + line[0].strip()
            strproto += "\tdef add_" + line[1].strip() + "():\n"
            strproto += "\t\tif len(" + line[1].strip() + \
                ") >= " + line[2].strip() + ".value:\n"
            strproto += "\t\t\treturn None\n"
            strproto += "\t\t" + line[1].strip() + \
                ".append(" + line[0].strip() + "())\n"
            strproto += "\t\treturn " + \
                line[1].strip() + "[len(" + line[1].strip() + ") - 1]\n"
            strproto += "\n"
    return strproto


def parse_message(messagedef):
    strproto = ""
    messagename = ""
    keys = []
    for line in messagedef:
        if line.find("message") != -1:
            messagename = line.replace("message", "").strip()
        elif line.find("required") != -1 or line.find("optional") != -1:
            keys.append(
                line.replace(
                    "required",
                    "").replace(
                    "optional",
                    "").replace(
                    ";",
                    "").split())
        elif line.find("repeated") != -1:
            arraydef = line.replace("repeated", "").replace(";", "").split()
            arraylen = ['uint16']
            keyname = arraydef[1][:arraydef[1].find("[")]
            arraylen.append("len_of_" + keyname)
            kenlen = arraydef[1][arraydef[1].find(
                "[") + 1:arraydef[1].find("]")]
            keys.append(arraylen)
            del arraydef[1]
            arraydef.append(keyname)
            arraydef.append(kenlen)
            keys.append(arraydef)

    strproto += "class " + messagename + "(proto):\n"
    strproto += write_class_init(keys)
    strproto += write_class_serialize(keys)
    strproto += write_class_deserialize(keys)
    strproto += write_class_repeated(keys)
    return strproto


def write_enum_class(enumname, baseclass, val=None):
    strproto = "class " + enumname + "(" + baseclass + "):\n"
    if val is not None:
        strproto += "\tdef __init__(self):\n"
        strproto += "\t\tself.value=" + str(val) + '\n'
    else:
        strproto += "\tpass\n"
    strproto += '\n'
    return strproto


def write_enum_opcode(enumname, val=None):
    strproto = "\t" + enumname + " = " + str(val) + "\n"
    return strproto


def parse_enum(enumdef):
    strproto = ""
    enumname = ""
    maxenum = -1
    for line in enumdef:
        if line.find("enum") != -1:
            enumname = line.replace("enum", "").strip()
            strproto += write_enum_class(enumname, 'enum')
        elif line.find('{') != -1 or line.find("}") != -1:
            pass
        elif len(line.strip()) == 0:
            pass
        else:
            enuminfo = line.strip().split('=')
            if len(enuminfo) == 1:
                maxenum += 1
                strproto += write_enum_class(
                    enuminfo[0].strip(), enumname, maxenum)
            elif len(enuminfo) == 2:
                maxenum = int(enuminfo[1].strip())
                strproto += write_enum_class(
                    enuminfo[0].strip(), enumname, maxenum)

    return strproto


def parse_opcode(filename):
    outname = gen_proto_dir + 'game_' + filename.replace("txt", "py")
    file = open(file_dir + filename)
    line = file.readline()
    # strproto = "from basetype import *\n"
    strproto = ""
    strproto += "class OP_CODE:\n"
    while(line):
        if(line.find("=") != -1):
            enuminfo = line.strip().split('=')
            # strproto += write_enum_class(enuminfo[0].strip(), 'enum', enuminfo[1].strip())
            strproto += write_enum_opcode(
                enuminfo[0].strip(), enuminfo[1].strip())
        line = file.readline()
    file.close()
    file = open(outname, 'w')
    file.write(strproto)
    file.close()


def gen_message(enumdef):
    if enumdef[:2] == 'CS':
        return '''
    # ''' + enumdef[:-1] + '''
    @CallbackBase.callback(OP_CODE.''' + enumdef[:-1] + ''')
    def send_''' + enumdef[3:-1].lower() + '''_decorate(self, code):
        packet = ''' + enumdef[:-1].lower() + '''()
        self.make_''' + enumdef[3:-1].lower() + '''_packet(packet)
        self.mes_que[code] = packet
    # makeup '''+ enumdef[3:-1].lower() + ''' packet
    def make_''' + enumdef[3:-1].lower() + '''_packet(self, packet):
        return None
    # send '''+ enumdef[3:-1].lower() + '''
    def send_'''+ enumdef[3:-1].lower() + '''(self):
        self.dispatch(OP_CODE.''' + enumdef[:-1] + ''')(OP_CODE.''' + enumdef[:-1] + ''')
    '''
    elif enumdef[:2] == 'SC':
        return '''
    # handle ''' + enumdef[:-1] + '''
    @CallbackBase.callback(OP_CODE.''' + enumdef[:-1] + ''')
    def handle_''' + enumdef[3:-1].lower() + '''_decorate(self, recv_buff):
        packet = ''' + enumdef[:-1].lower() + '''()
        packet.deserialize(recv_buff)
        return self.handle_''' + enumdef[3:-1].lower() + '''(packet)    
    def handle_''' + enumdef[3:-1].lower() + '''(self, packet):
        return None

    '''
    else:
        return ''


def parse_message_file(filename):
    outname = "..//robot//game_message.py"
    file = open(file_dir + filename)
    line = file.readline()
    outstr = '''import sys
sys.path.append("..\\gen_protocol")
from game_opcode import *
from callback import *
from command import *
from collections import OrderedDict

class CMessage(CallbackBase):
    def __init__(self):
        CallbackBase.__init__(self)
        self.mes_que = OrderedDict()       
    def process(self, code, recv_buff):
        self.dispatch(code)(recv_buff)
    def send_msg(self, code):
        self.dispatch(code)(code)
        
    '''
    while line:
        if line.find("=") != -1:
            enuminfo = line.strip().split('=')
            outstr += gen_message(enuminfo[0])
        line = file.readline()

    file.close()
    file = open(outname, 'w')
    file.write(outstr)
    file.close()


def parse_file(filename):
    if(filename.find("proto") == -1):
        return

    outname = gen_proto_dir + filename.replace("proto", "py")

    file = open(file_dir + filename)
    line = file.readline()
    strproto = "from basetype import *\n"
    while(line):
        if(line.find("message") != -1):
            message = []
            message.append(line[:line.find("//")].replace(";", ""))
            while True:
                line = file.readline()
                if(line.find("}") != -1):
                    break

                message.append(line[:line.find("//")].replace(";", ""))
            strproto += parse_message(message)
        elif(line.find("enum") != -1):
            enumlist = []
            enumlist.append(line[:line.find("//")].replace(";", ""))
            while True:
                line = file.readline()
                if(line.find("}") != -1):
                    break

                enumlist.append(line[:line.find("//")].replace(";", ""))
            strproto += parse_enum(enumlist)
        elif line.find("import") != -1:
            strmodulename = line[line.find('"') + 1: line.find(".")]
            strproto += "from " + strmodulename + " import *\n"

        line = file.readline()

    file.close()
    file = open(outname, 'w')
    file.write(strproto)
    file.close()


if __name__ == '__main__':
    for parent, dirnames, filenames in os.walk(file_dir, '.proto'):
        for filename in filenames:
            if filename.find('locojoy') < 0:
                parse_file(filename)
                print filename + ' finish'

    parse_opcode('opcode.txt')
    parse_message_file('opcode.txt')
