import random
class MapConfig:
    rows = 128
    cols = 128
    hex_rows_per_terrain = 26
    hex_cols_per_terrain = 23
    key_split = 10000
    chunk_id_max = rows * cols

    @classmethod
    def get_block_row(self, block_id):
        return block_id % 10000

    @classmethod
    def get_block_col(self, block_id):
        return block_id / 10000

    @classmethod
    def blockid_to_chunkid(self, block_id):
        return (block_id % MapConfig.key_split) / MapConfig.hex_rows_per_terrain * \
            MapConfig.cols + ((block_id / MapConfig.key_split) /
                              MapConfig.hex_cols_per_terrain)

    @classmethod
    def rand_chunk_id(cls):
        return random.randint(1, cls.chunk_id_max)


