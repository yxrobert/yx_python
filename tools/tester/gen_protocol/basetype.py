import struct

class proto:
    def serialize(self, buff, buff_len):
	return buff, buff_len
    
    def deserialize(self, buff):
	return buff
    
    def get_value(self):
	return self.value
    
    def set_value(self, val):
	self.value = val
    
class cint64(proto):
    def __init__(self):
	self.value = -1
	
    def serialize(self, buff, buff_len):
	return buff + struct.pack("=q", self.value), buff_len + 8
    
    def deserialize(self, buff):
	self.value, = struct.unpack("=q", buff[:8])
	return buff[8:]    
    
class cint32(proto):
    def __init__(self):
	self.value = -1
	
    def serialize(self, buff, buff_len):
	return buff + struct.pack("=i", self.value), buff_len + 4
    
    def deserialize(self, buff):
	self.value, = struct.unpack("=i", buff[:4])
	return buff[4:]   
    
class cbool(proto):
    def __init__(self):
	self.value = False
	
    def serialize(self, buff, buff_len):
	return buff + struct.pack("=?", self.value), buff_len + 1
    
    def deserialize(self, buff):
	self.value, = struct.unpack("=?", buff[:1])
	return buff[1:]   
    
class cstring(proto):
    def __init__(self):
	self.value = ""
	self.str_len = cuint16()
	
    def serialize(self, buff, buff_len):
	self.str_len.value = len(self.value)
	buff,buff_len = self.str_len.serialize(buff, buff_len)
	if self.str_len.value != 0:
	    buff += struct.pack("=" + str(self.str_len.value) + "s", self.value)
	    buff_len += self.str_len.get_value()
	return buff, buff_len
    
    def deserialize(self, buff):
	buff = self.str_len.deserialize(buff)
	if self.str_len.value != 0:
	    self.value, = struct.unpack("=" + str(self.str_len.value) + "s", buff[:self.str_len.get_value()])
	return buff[self.str_len.get_value():]
    
class cbigstring(proto):
    def __init__(self):
	self.value = ""
	self.str_len = cuint16()
	
    def serialize(self, buff, buff_len):
	self.str_len.value = len(self.value)
	buff,buff_len = self.str_len.serialize(buff, buff_len)
	if self.str_len.value != 0:
	    buff += struct.pack("=" + str(self.str_len.value) + "s", self.value)
	    buff_len += self.str_len.get_value()
	return buff, buff_len
    
    def deserialize(self, buff):
	buff = self.str_len.deserialize(buff)
	if self.str_len.value != 0:
	    self.value, = struct.unpack("=" + str(self.str_len.value) + "s", buff[:self.str_len.get_value()])
	return buff[self.str_len.get_value():]
    
class cuint32(proto):
    def __init__(self):
	self.value = 0
	
    def serialize(self, buff, buff_len):
	return buff + struct.pack("=I", self.value), buff_len + 4
    
    def deserialize(self, buff):
	self.value, = struct.unpack("=I", buff[:4])
	return buff[4:]    
    
class cuint8(proto):
    def __init__(self):
	self.value = 0
	
    def serialize(self, buff, buff_len):
	return buff + struct.pack("=B", self.value), buff_len + 1
    
    def deserialize(self, buff):
	self.value, = struct.unpack("=B", buff[:1])
	return buff[1:]  
    
class cuint16(proto):
    def __init__(self):
	self.value = 0
	
    def serialize(self, buff, buff_len):
	return buff + struct.pack("=H", self.value), buff_len + 2
    
    def deserialize(self, buff):
	self.value, = struct.unpack("=H", buff[:2])
	return buff[2:]   

class msghdr(proto):
    def __init__(self):
		self.ver = cuint32()
		self.flags = cuint8()
		self.package_len = cuint32()
		self.protocol = cuint16()
		self.package_len.set_value(11)
        
    def serialize(self, buff, buff_len):
		buff, buff_len = self.ver.serialize(buff, buff_len) 
		buff, buff_len = self.flags.serialize(buff, buff_len) 
		buff, buff_len = self.package_len.serialize(buff, buff_len) 
		buff, buff_len = self.protocol.serialize(buff, buff_len)
		return buff, buff_len
	
	
    def deserialize(self, buff):
		buff = self.ver.deserialize(buff)
		buff = self.flags.deserialize(buff)
		buff = self.package_len.deserialize(buff)
		buff = self.protocol.deserialize(buff)
		return buff
    
class enum(proto):
    def __init__(self):
	self.value = cint32()
    
    def serialize(self, buff, buff_len):
	buff, buff_len = self.value.serialize(buff, buff_len) 
	return buff, buff_len

    def deserialize(self, buff):
	buff = self.value.deserialize(buff)
	print self.value.value
	return buff

