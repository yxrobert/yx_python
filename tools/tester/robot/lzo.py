from ctypes import *
import ctypes


class Lzo():
    # lzo = CDLL('./minilzo.dll')
    # ret = lzo.lzo_init_ex()
    # wrkmem = c_byte * (25600 * 2)
    # wrkmem_data = wrkmem()

    @staticmethod
    def lzo_compress(in_data, in_len):

        lzo = CDLL('./minilzo.dll')
        ret = lzo.lzo_init_ex()
        wrkmem = c_byte * (25600 * 2)
        wrkmem_data = wrkmem()

        out_data = ctypes.create_string_buffer(25600)

        outlen = c_int * 1
        outlen_data = outlen()

        ret = lzo.lzo1x_1_compress(
            in_data,
            in_len,
            out_data,
            outlen_data,
            wrkmem_data)
        if ret != 0:
            print 'decompress %d, outlen %d!!' % (
                ret, outlen_data[0])
        return out_data, outlen_data[0]

    @staticmethod
    def lzo_decompress(in_data, in_len):

        lzo = CDLL('./robot/minilzo.dll')
        ret = lzo.lzo_init_ex()
        wrkmem = c_byte * (25600 * 2)
        wrkmem_data = wrkmem()

        # out = c_byte * 25600
        #out_data = out()

        out_data = ctypes.create_string_buffer(25600)

        outlen = c_int * 1
        outlen_data = outlen()

        # ret = lzo.lzo1x_decompress_safe(in_data, len(in_data), out_data, outlen_data, wrkmem_data)
        ret = lzo.lzo1x_decompress(
            in_data,
            in_len,
            out_data,
            outlen_data,
            wrkmem_data)
        if ret != 0:
            print 'decompress %d, outlen %d!!' % (ret, outlen_data[0])
        return out_data, outlen_data[0]

# l = 16
# input = c_byte * l
# input_data = input()
# for i in range(l):
#     input_data[i] = i % 2
#
#
# xl, buff = Lzo.lzo_compress(input_data, l)
# print xl, buff
# xl, buff = Lzo.lzo_decompress(buff, xl)
# print xl, buff
