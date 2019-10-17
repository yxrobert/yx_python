from basetype import *
from game import *
from err_code import *
class cs_register(proto):
	def __init__(self):
		self.session = session_t()
		self.account_info = platform_account_t()
		self.device_info = device_info_t()
		self.nick_name = cstring()
		self.region = cint32()
		self.head_entry = cint32()
		self.language = cint32()
		self.head_url = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.account_info.serialize(buff, buff_len)
		buff, buff_len = self.device_info.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		buff, buff_len = self.region.serialize(buff, buff_len)
		buff, buff_len = self.head_entry.serialize(buff, buff_len)
		buff, buff_len = self.language.serialize(buff, buff_len)
		buff, buff_len = self.head_url.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.account_info.deserialize(buff)
		buff = self.device_info.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		buff = self.region.deserialize(buff)
		buff = self.head_entry.deserialize(buff)
		buff = self.language.deserialize(buff)
		buff = self.head_url.deserialize(buff)
		return buff

class sc_register(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.res_info = login_register_res_t()
		self.nick_name = cstring()
		self.login_device_id = cstring()
		self.is_charge_channel = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.res_info.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		buff, buff_len = self.login_device_id.serialize(buff, buff_len)
		buff, buff_len = self.is_charge_channel.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.res_info.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		buff = self.login_device_id.deserialize(buff)
		buff = self.is_charge_channel.deserialize(buff)
		return buff

class cs_login(proto):
	def __init__(self):
		self.session = session_t()
		self.account_info = platform_account_t()
		self.access_token = cstring()
		self.device_info = device_info_t()
		self.ip = cstring()
		self.device_id = cstring()
		self.login_device_id = cstring()
		self.language = cint32()
		self.head_url = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.account_info.serialize(buff, buff_len)
		buff, buff_len = self.access_token.serialize(buff, buff_len)
		buff, buff_len = self.device_info.serialize(buff, buff_len)
		buff, buff_len = self.ip.serialize(buff, buff_len)
		buff, buff_len = self.device_id.serialize(buff, buff_len)
		buff, buff_len = self.login_device_id.serialize(buff, buff_len)
		buff, buff_len = self.language.serialize(buff, buff_len)
		buff, buff_len = self.head_url.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.account_info.deserialize(buff)
		buff = self.access_token.deserialize(buff)
		buff = self.device_info.deserialize(buff)
		buff = self.ip.deserialize(buff)
		buff = self.device_id.deserialize(buff)
		buff = self.login_device_id.deserialize(buff)
		buff = self.language.deserialize(buff)
		buff = self.head_url.deserialize(buff)
		return buff

class sc_login(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.res_info = login_register_res_t()
		self.len_of_state_status_list = cuint16()
		self.state_status_list = []
		self.is_charge_channel = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.res_info.serialize(buff, buff_len)
		buff, buff_len = self.len_of_state_status_list.serialize(buff, buff_len)
		for i in range(self.len_of_state_status_list.value):
			buff, buff_len = self.state_status_list[i].serialize(buff, buff_len)
		buff, buff_len = self.is_charge_channel.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.res_info.deserialize(buff)
		buff = self.len_of_state_status_list.deserialize(buff)
		self.state_status_list = []
		for i in range(self.len_of_state_status_list.value):
			self.state_status_list.append(state_status_t())
			buff = self.state_status_list[i].deserialize(buff)
		buff = self.is_charge_channel.deserialize(buff)
		return buff

	def add_state_status_list():
		if len(state_status_list) >= MAX_STATE_NUM.value:
			return None
		state_status_list.append(state_status_t())
		return state_status_list[len(state_status_list) - 1]

class cs_get_user_info(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_user_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user = user_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user.deserialize(buff)
		return buff

class cs_get_castle_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_castle_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_castle_info_list = cuint16()
		self.castle_info_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_castle_info_list.serialize(buff, buff_len)
		for i in range(self.len_of_castle_info_list.value):
			buff, buff_len = self.castle_info_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_castle_info_list.deserialize(buff)
		self.castle_info_list = []
		for i in range(self.len_of_castle_info_list.value):
			self.castle_info_list.append(castle_info_t())
			buff = self.castle_info_list[i].deserialize(buff)
		return buff

	def add_castle_info_list():
		if len(castle_info_list) >= MAX_CASTLE_NUM.value:
			return None
		castle_info_list.append(castle_info_t())
		return castle_info_list[len(castle_info_list) - 1]

class cs_get_building_data(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()
		self.build_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.build_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.build_id.deserialize(buff)
		return buff

class sc_get_building_data(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.castle_id = cint64()
		self.build_id = cint32()
		self.len_of_building_data_list = cuint16()
		self.building_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.build_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_building_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_building_data_list.value):
			buff, buff_len = self.building_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.build_id.deserialize(buff)
		buff = self.len_of_building_data_list.deserialize(buff)
		self.building_data_list = []
		for i in range(self.len_of_building_data_list.value):
			self.building_data_list.append(building_date_t())
			buff = self.building_data_list[i].deserialize(buff)
		return buff

	def add_building_data_list():
		if len(building_data_list) >= MAX_BUILDING_COUNT.value:
			return None
		building_data_list.append(building_date_t())
		return building_data_list[len(building_data_list) - 1]

class cs_building_lvup(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()
		self.build_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.build_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.build_id.deserialize(buff)
		return buff

class sc_building_lvup(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.building_data = building_date_t()
		self.resources = user_resource_t()
		self.new_event = game_event_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.building_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.new_event.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.building_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.new_event.deserialize(buff)
		return buff

class cs_accelerate_building_lvup(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()
		self.build_id = cint32()
		self.item_entry = cint32()
		self.item_num = cint32()
		self.at_once = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.build_id.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.item_num.serialize(buff, buff_len)
		buff, buff_len = self.at_once.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.build_id.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.item_num.deserialize(buff)
		buff = self.at_once.deserialize(buff)
		return buff

class sc_accelerate_building_lvup(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.resources = user_resource_t()
		self.event_data = game_event_data_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []
		self.at_once = cbool()
		self.item_entry = cint32()
		self.item_num = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.event_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.at_once.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.item_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.event_data.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		buff = self.at_once.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.item_num.deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_get_hero_list(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		return buff

class sc_get_hero_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_entry = cint32()
		self.len_of_hero_data_list = cuint16()
		self.hero_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_hero_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_hero_data_list.value):
			buff, buff_len = self.hero_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.len_of_hero_data_list.deserialize(buff)
		self.hero_data_list = []
		for i in range(self.len_of_hero_data_list.value):
			self.hero_data_list.append(hero_data_t())
			buff = self.hero_data_list[i].deserialize(buff)
		return buff

	def add_hero_data_list():
		if len(hero_data_list) >= MAX_HERO_COUNT.value:
			return None
		hero_data_list.append(hero_data_t())
		return hero_data_list[len(hero_data_list) - 1]

class cs_get_single_hero_data(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		return buff

class sc_get_single_hero_data(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_data = hero_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		return buff

class cs_accelerate_hero_train(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()
		self.item_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		return buff

class sc_accelerate_hero_train(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_data = hero_data_t()
		self.resources = user_resource_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_hero_train(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()
		self.entry = cint32()
		self.train_scheme_idx = cint32()
		self.train_slot_idx = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.train_scheme_idx.serialize(buff, buff_len)
		buff, buff_len = self.train_slot_idx.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.entry.deserialize(buff)
		buff = self.train_scheme_idx.deserialize(buff)
		buff = self.train_slot_idx.deserialize(buff)
		return buff

class sc_hero_train(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.castle_id = cint64()
		self.hero_data = hero_data_t()
		self.resources = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		return buff

class cs_cancel_hero_train(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()
		self.entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.entry.deserialize(buff)
		return buff

class sc_cancel_hero_train(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.castle_id = cint64()
		self.hero_data = hero_data_t()
		self.resources = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		return buff

class cs_get_corps_info(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_corps_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_corps_data_list = cuint16()
		self.corps_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_corps_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_corps_data_list.value):
			buff, buff_len = self.corps_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_corps_data_list.deserialize(buff)
		self.corps_data_list = []
		for i in range(self.len_of_corps_data_list.value):
			self.corps_data_list.append(corps_data_t())
			buff = self.corps_data_list[i].deserialize(buff)
		return buff

	def add_corps_data_list():
		if len(corps_data_list) >= MAX_CORPS_COUNT.value:
			return None
		corps_data_list.append(corps_data_t())
		return corps_data_list[len(corps_data_list) - 1]

class cs_get_game_event_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_game_event_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

class cs_query_game_event_result(proto):
	def __init__(self):
		self.session = session_t()
		self.event_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		return buff

class sc_query_game_event_result(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.event_id = cint64()
		self.len_of_game_event_result_data_list = cuint16()
		self.game_event_result_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_result_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_result_data_list.value):
			buff, buff_len = self.game_event_result_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.len_of_game_event_result_data_list.deserialize(buff)
		self.game_event_result_data_list = []
		for i in range(self.len_of_game_event_result_data_list.value):
			self.game_event_result_data_list.append(game_event_result_data_t())
			buff = self.game_event_result_data_list[i].deserialize(buff)
		return buff

	def add_game_event_result_data_list():
		if len(game_event_result_data_list) >= MAX_GAME_EVENT_RESULT_NUM.value:
			return None
		game_event_result_data_list.append(game_event_result_data_t())
		return game_event_result_data_list[len(game_event_result_data_list) - 1]

class cs_get_battle_result(proto):
	def __init__(self):
		self.session = session_t()
		self.battle_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.battle_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.battle_id.deserialize(buff)
		return buff

class sc_get_battle_result(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_battle_result_list = cuint16()
		self.battle_result_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_battle_result_list.serialize(buff, buff_len)
		for i in range(self.len_of_battle_result_list.value):
			buff, buff_len = self.battle_result_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_battle_result_list.deserialize(buff)
		self.battle_result_list = []
		for i in range(self.len_of_battle_result_list.value):
			self.battle_result_list.append(battle_result_t())
			buff = self.battle_result_list[i].deserialize(buff)
		return buff

	def add_battle_result_list():
		if len(battle_result_list) >= MAX_BATTLE_RESULT_NUM.value:
			return None
		battle_result_list.append(battle_result_t())
		return battle_result_list[len(battle_result_list) - 1]

class cs_gm_command(proto):
	def __init__(self):
		self.session = session_t()
		self.command = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.command.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.command.deserialize(buff)
		return buff

class sc_gm_command(proto):
	def __init__(self):
		self.common_result = common_result_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		return buff

class cs_corps_move(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()
		self.e_event_type = E_EVENT_TYPE()
		self.block_id = cint32()
		self.use_token = cbool()
		self.smash_times = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.e_event_type.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.use_token.serialize(buff, buff_len)
		buff, buff_len = self.smash_times.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.e_event_type.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.use_token.deserialize(buff)
		buff = self.smash_times.deserialize(buff)
		return buff

class sc_corps_move(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.e_event_type = E_EVENT_TYPE()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []
		self.len_of_corps_data_list = cuint16()
		self.corps_data_list = []
		self.use_token = cbool()
		self.token = cint32()
		self.smash_times = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.e_event_type.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_corps_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_corps_data_list.value):
			buff, buff_len = self.corps_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.use_token.serialize(buff, buff_len)
		buff, buff_len = self.token.serialize(buff, buff_len)
		buff, buff_len = self.smash_times.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.e_event_type.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		buff = self.len_of_corps_data_list.deserialize(buff)
		self.corps_data_list = []
		for i in range(self.len_of_corps_data_list.value):
			self.corps_data_list.append(corps_data_t())
			buff = self.corps_data_list[i].deserialize(buff)
		buff = self.use_token.deserialize(buff)
		buff = self.token.deserialize(buff)
		buff = self.smash_times.deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

	def add_corps_data_list():
		if len(corps_data_list) >= MAX_CORPS_COUNT.value:
			return None
		corps_data_list.append(corps_data_t())
		return corps_data_list[len(corps_data_list) - 1]

class cs_game_event_discard(proto):
	def __init__(self):
		self.session = session_t()
		self.event_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		return buff

class sc_game_event_discard(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.event_id = cint64()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

class cs_block_discard(proto):
	def __init__(self):
		self.session = session_t()
		self.block_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		return buff

class sc_block_discard(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.block_id = cint32()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

class cs_get_chunk_events(proto):
	def __init__(self):
		self.session = session_t()
		self.chunk_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.chunk_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.chunk_id.deserialize(buff)
		return buff

class sc_get_chunk_events(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.chunk_id = cint32()
		self.len_of_chunk_events = cuint16()
		self.chunk_events = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.chunk_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_chunk_events.serialize(buff, buff_len)
		for i in range(self.len_of_chunk_events.value):
			buff, buff_len = self.chunk_events[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.chunk_id.deserialize(buff)
		buff = self.len_of_chunk_events.deserialize(buff)
		self.chunk_events = []
		for i in range(self.len_of_chunk_events.value):
			self.chunk_events.append(game_event_data_t())
			buff = self.chunk_events[i].deserialize(buff)
		return buff

	def add_chunk_events():
		if len(chunk_events) >= MAX_GAME_CHUNK_NUM.value:
			return None
		chunk_events.append(game_event_data_t())
		return chunk_events[len(chunk_events) - 1]

class cs_conscript_soldier(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()
		self.troop_index = cint32()
		self.soldier_entry = cint32()
		self.soldier_count = cint32()
		self.type = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.troop_index.serialize(buff, buff_len)
		buff, buff_len = self.soldier_entry.serialize(buff, buff_len)
		buff, buff_len = self.soldier_count.serialize(buff, buff_len)
		buff, buff_len = self.type.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.troop_index.deserialize(buff)
		buff = self.soldier_entry.deserialize(buff)
		buff = self.soldier_count.deserialize(buff)
		buff = self.type.deserialize(buff)
		return buff

class sc_conscript_soldier(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.troop_index = cint32()
		self.troop_data = troops_data_t()
		self.resources = user_resource_t()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []
		self.reserver_soldier = reserver_soldier_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.troop_index.serialize(buff, buff_len)
		buff, buff_len = self.troop_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.reserver_soldier.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.troop_index.deserialize(buff)
		buff = self.troop_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		buff = self.reserver_soldier.deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

class cs_cancel_conscript_soldier(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()
		self.troop_index = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.troop_index.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.troop_index.deserialize(buff)
		return buff

class sc_cancel_conscript_soldier(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.troop_index = cint32()
		self.troop_data = troops_data_t()
		self.resources = user_resource_t()
		self.event_id = cint64()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.troop_index.serialize(buff, buff_len)
		buff, buff_len = self.troop_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.troop_index.deserialize(buff)
		buff = self.troop_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

class cs_sync_troop_data(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()
		self.troop_index = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.troop_index.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.troop_index.deserialize(buff)
		return buff

class sc_sync_troop_data(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.troop_index = cint32()
		self.troop_data = troops_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.troop_index.serialize(buff, buff_len)
		buff, buff_len = self.troop_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.troop_index.deserialize(buff)
		buff = self.troop_data.deserialize(buff)
		return buff

class cs_dismiss_soldier(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()
		self.troop_index = cint32()
		self.soldier_entry = cint32()
		self.soldier_count = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.troop_index.serialize(buff, buff_len)
		buff, buff_len = self.soldier_entry.serialize(buff, buff_len)
		buff, buff_len = self.soldier_count.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.troop_index.deserialize(buff)
		buff = self.soldier_entry.deserialize(buff)
		buff = self.soldier_count.deserialize(buff)
		return buff

class sc_dismiss_soldier(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.troop_index = cint32()
		self.troop_data = troops_data_t()
		self.resources = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.troop_index.serialize(buff, buff_len)
		buff, buff_len = self.troop_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.troop_index.deserialize(buff)
		buff = self.troop_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		return buff

class cs_corp_change_battle_pos(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()
		self.len_of_troops_pos_list = cuint16()
		self.troops_pos_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.len_of_troops_pos_list.serialize(buff, buff_len)
		for i in range(self.len_of_troops_pos_list.value):
			buff, buff_len = self.troops_pos_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.len_of_troops_pos_list.deserialize(buff)
		self.troops_pos_list = []
		for i in range(self.len_of_troops_pos_list.value):
			self.troops_pos_list.append(cint32())
			buff = self.troops_pos_list[i].deserialize(buff)
		return buff

	def add_troops_pos_list():
		if len(troops_pos_list) >= MAX_CORPS_TROOPS_NUM.value:
			return None
		troops_pos_list.append(ccint32())
		return troops_pos_list[len(troops_pos_list) - 1]

class sc_corp_change_battle_pos(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.len_of_troops_pos_list = cuint16()
		self.troops_pos_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.len_of_troops_pos_list.serialize(buff, buff_len)
		for i in range(self.len_of_troops_pos_list.value):
			buff, buff_len = self.troops_pos_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.len_of_troops_pos_list.deserialize(buff)
		self.troops_pos_list = []
		for i in range(self.len_of_troops_pos_list.value):
			self.troops_pos_list.append(cint32())
			buff = self.troops_pos_list[i].deserialize(buff)
		return buff

	def add_troops_pos_list():
		if len(troops_pos_list) >= MAX_CORPS_TROOPS_NUM.value:
			return None
		troops_pos_list.append(ccint32())
		return troops_pos_list[len(troops_pos_list) - 1]

class cs_hero_assign_point(proto):
	def __init__(self):
		self.session = session_t()
		self.entry = cint32()
		self.assign_liliang = cint32()
		self.assign_naili = cint32()
		self.assign_moulue = cint32()
		self.assign_minjie = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.assign_liliang.serialize(buff, buff_len)
		buff, buff_len = self.assign_naili.serialize(buff, buff_len)
		buff, buff_len = self.assign_moulue.serialize(buff, buff_len)
		buff, buff_len = self.assign_minjie.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.entry.deserialize(buff)
		buff = self.assign_liliang.deserialize(buff)
		buff = self.assign_naili.deserialize(buff)
		buff = self.assign_moulue.deserialize(buff)
		buff = self.assign_minjie.deserialize(buff)
		return buff

class sc_hero_assign_point(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_data = hero_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		return buff

class cs_reset_hero_point(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		return buff

class sc_reset_hero_point(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_data = hero_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		return buff

class cs_corps_change_hero(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()
		self.change_pos = cint32()
		self.hero_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.change_pos.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.change_pos.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		return buff

class sc_corps_change_hero(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_data = corps_data_t()
		self.resources = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		return buff

class cs_get_item_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_item_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_GET_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_recruit_hero(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		return buff

class sc_recruit_hero(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_data = hero_data_t()
		self.resources = user_resource_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_land_build(proto):
	def __init__(self):
		self.session = session_t()
		self.block_id = cint32()
		self.building_entry = cint32()
		self.name = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.building_entry.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.building_entry.deserialize(buff)
		buff = self.name.deserialize(buff)
		return buff

class sc_land_build(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.block_id = cint32()
		self.building_entry = cint32()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []
		self.len_of_castle_info_list = cuint16()
		self.castle_info_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.building_entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_castle_info_list.serialize(buff, buff_len)
		for i in range(self.len_of_castle_info_list.value):
			buff, buff_len = self.castle_info_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.building_entry.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		buff = self.len_of_castle_info_list.deserialize(buff)
		self.castle_info_list = []
		for i in range(self.len_of_castle_info_list.value):
			self.castle_info_list.append(castle_info_t())
			buff = self.castle_info_list[i].deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

	def add_castle_info_list():
		if len(castle_info_list) >= MAX_CASTLE_NUM.value:
			return None
		castle_info_list.append(castle_info_t())
		return castle_info_list[len(castle_info_list) - 1]

class cs_block_building_discard(proto):
	def __init__(self):
		self.session = session_t()
		self.block_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		return buff

class sc_block_building_discard(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.block_id = cint32()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

class cs_castle_move(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		return buff

class sc_castle_move(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.castle_id = cint64()
		self.len_of_castle_info_list = cuint16()
		self.castle_info_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_castle_info_list.serialize(buff, buff_len)
		for i in range(self.len_of_castle_info_list.value):
			buff, buff_len = self.castle_info_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.len_of_castle_info_list.deserialize(buff)
		self.castle_info_list = []
		for i in range(self.len_of_castle_info_list.value):
			self.castle_info_list.append(castle_info_t())
			buff = self.castle_info_list[i].deserialize(buff)
		return buff

	def add_castle_info_list():
		if len(castle_info_list) >= MAX_CASTLE_NUM.value:
			return None
		castle_info_list.append(castle_info_t())
		return castle_info_list[len(castle_info_list) - 1]

class cs_hero_change_equip(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()
		self.item_entry = cint32()
		self.e_equip_slot = E_EQUIP_SLOT()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.e_equip_slot.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.e_equip_slot.deserialize(buff)
		return buff

class sc_hero_change_equip(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_data = hero_data_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_corps_guard_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_corps_guard_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_corps_guard_list = cuint16()
		self.corps_guard_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_corps_guard_list.serialize(buff, buff_len)
		for i in range(self.len_of_corps_guard_list.value):
			buff, buff_len = self.corps_guard_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_corps_guard_list.deserialize(buff)
		self.corps_guard_list = []
		for i in range(self.len_of_corps_guard_list.value):
			self.corps_guard_list.append(corps_guard_t())
			buff = self.corps_guard_list[i].deserialize(buff)
		return buff

	def add_corps_guard_list():
		if len(corps_guard_list) >= MAX_CORPS_COUNT.value:
			return None
		corps_guard_list.append(corps_guard_t())
		return corps_guard_list[len(corps_guard_list) - 1]

class cs_corps_guard_back(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		return buff

class sc_corps_guard_back(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.len_of_corps_guard_list = cuint16()
		self.corps_guard_list = []
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []
		self.len_of_corps_data_list = cuint16()
		self.corps_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.len_of_corps_guard_list.serialize(buff, buff_len)
		for i in range(self.len_of_corps_guard_list.value):
			buff, buff_len = self.corps_guard_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_corps_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_corps_data_list.value):
			buff, buff_len = self.corps_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.len_of_corps_guard_list.deserialize(buff)
		self.corps_guard_list = []
		for i in range(self.len_of_corps_guard_list.value):
			self.corps_guard_list.append(corps_guard_t())
			buff = self.corps_guard_list[i].deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		buff = self.len_of_corps_data_list.deserialize(buff)
		self.corps_data_list = []
		for i in range(self.len_of_corps_data_list.value):
			self.corps_data_list.append(corps_data_t())
			buff = self.corps_data_list[i].deserialize(buff)
		return buff

	def add_corps_guard_list():
		if len(corps_guard_list) >= MAX_CORPS_COUNT.value:
			return None
		corps_guard_list.append(corps_guard_t())
		return corps_guard_list[len(corps_guard_list) - 1]

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

	def add_corps_data_list():
		if len(corps_data_list) >= MAX_CORPS_COUNT.value:
			return None
		corps_data_list.append(corps_data_t())
		return corps_data_list[len(corps_data_list) - 1]

class cs_change_medal(proto):
	def __init__(self):
		self.session = session_t()
		self.medal_entry = cint32()
		self.slot_index = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.medal_entry.serialize(buff, buff_len)
		buff, buff_len = self.slot_index.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.medal_entry.deserialize(buff)
		buff = self.slot_index.deserialize(buff)
		return buff

class sc_change_medal(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_medal_list = cuint16()
		self.medal_list = []
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []
		self.slot_index = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_medal_list.serialize(buff, buff_len)
		for i in range(self.len_of_medal_list.value):
			buff, buff_len = self.medal_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.slot_index.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_medal_list.deserialize(buff)
		self.medal_list = []
		for i in range(self.len_of_medal_list.value):
			self.medal_list.append(cint32())
			buff = self.medal_list[i].deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		buff = self.slot_index.deserialize(buff)
		return buff

	def add_medal_list():
		if len(medal_list) >= MAX_EQUIP_MEDAL_NUM.value:
			return None
		medal_list.append(ccint32())
		return medal_list[len(medal_list) - 1]

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_levy_tax(proto):
	def __init__(self):
		self.session = session_t()
		self.tax_type = E_RESOURCE_TYPE()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.tax_type.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.tax_type.deserialize(buff)
		return buff

class sc_levy_tax(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.resources = user_resource_t()
		self.tax_info = tax_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.tax_info.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.tax_info.deserialize(buff)
		return buff

class cs_get_tax_info(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_tax_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.tax_info = tax_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.tax_info.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.tax_info.deserialize(buff)
		return buff

class cs_get_fort_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_fort_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_fort_list = cuint16()
		self.fort_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_fort_list.serialize(buff, buff_len)
		for i in range(self.len_of_fort_list.value):
			buff, buff_len = self.fort_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_fort_list.deserialize(buff)
		self.fort_list = []
		for i in range(self.len_of_fort_list.value):
			self.fort_list.append(fort_data_t())
			buff = self.fort_list[i].deserialize(buff)
		return buff

	def add_fort_list():
		if len(fort_list) >= MAX_FORT_NUM.value:
			return None
		fort_list.append(fort_data_t())
		return fort_list[len(fort_list) - 1]

class cs_garrison_fort(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()
		self.block_id = cint32()
		self.use_token = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.use_token.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.use_token.deserialize(buff)
		return buff

class sc_garrison_fort(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.block_id = cint32()
		self.len_of_fort_list = cuint16()
		self.fort_list = []
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []
		self.len_of_corps_data_list = cuint16()
		self.corps_data_list = []
		self.use_token = cbool()
		self.token = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_fort_list.serialize(buff, buff_len)
		for i in range(self.len_of_fort_list.value):
			buff, buff_len = self.fort_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_corps_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_corps_data_list.value):
			buff, buff_len = self.corps_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.use_token.serialize(buff, buff_len)
		buff, buff_len = self.token.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.len_of_fort_list.deserialize(buff)
		self.fort_list = []
		for i in range(self.len_of_fort_list.value):
			self.fort_list.append(fort_data_t())
			buff = self.fort_list[i].deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		buff = self.len_of_corps_data_list.deserialize(buff)
		self.corps_data_list = []
		for i in range(self.len_of_corps_data_list.value):
			self.corps_data_list.append(corps_data_t())
			buff = self.corps_data_list[i].deserialize(buff)
		buff = self.use_token.deserialize(buff)
		buff = self.token.deserialize(buff)
		return buff

	def add_fort_list():
		if len(fort_list) >= MAX_FORT_NUM.value:
			return None
		fort_list.append(fort_data_t())
		return fort_list[len(fort_list) - 1]

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

	def add_corps_data_list():
		if len(corps_data_list) >= MAX_CORPS_COUNT.value:
			return None
		corps_data_list.append(corps_data_t())
		return corps_data_list[len(corps_data_list) - 1]

class cs_leave_fort(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()
		self.block_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		return buff

class sc_leave_fort(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.block_id = cint32()
		self.len_of_fort_list = cuint16()
		self.fort_list = []
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []
		self.len_of_corps_data_list = cuint16()
		self.corps_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_fort_list.serialize(buff, buff_len)
		for i in range(self.len_of_fort_list.value):
			buff, buff_len = self.fort_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_corps_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_corps_data_list.value):
			buff, buff_len = self.corps_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.len_of_fort_list.deserialize(buff)
		self.fort_list = []
		for i in range(self.len_of_fort_list.value):
			self.fort_list.append(fort_data_t())
			buff = self.fort_list[i].deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		buff = self.len_of_corps_data_list.deserialize(buff)
		self.corps_data_list = []
		for i in range(self.len_of_corps_data_list.value):
			self.corps_data_list.append(corps_data_t())
			buff = self.corps_data_list[i].deserialize(buff)
		return buff

	def add_fort_list():
		if len(fort_list) >= MAX_FORT_NUM.value:
			return None
		fort_list.append(fort_data_t())
		return fort_list[len(fort_list) - 1]

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

	def add_corps_data_list():
		if len(corps_data_list) >= MAX_CORPS_COUNT.value:
			return None
		corps_data_list.append(corps_data_t())
		return corps_data_list[len(corps_data_list) - 1]

class cs_market_exchange(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()
		self.from_type = E_RESOURCE_TYPE()
		self.to_type = E_RESOURCE_TYPE()
		self.from_count = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.from_type.serialize(buff, buff_len)
		buff, buff_len = self.to_type.serialize(buff, buff_len)
		buff, buff_len = self.from_count.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.from_type.deserialize(buff)
		buff = self.to_type.deserialize(buff)
		buff = self.from_count.deserialize(buff)
		return buff

class sc_market_exchange(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.castle_id = cint64()
		self.resources = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.resources.deserialize(buff)
		return buff

class cs_market_buy(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()
		self.resource_type = E_RESOURCE_TYPE()
		self.count = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.resource_type.serialize(buff, buff_len)
		buff, buff_len = self.count.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.resource_type.deserialize(buff)
		buff = self.count.deserialize(buff)
		return buff

class sc_market_buy(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.castle_id = cint64()
		self.resources = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.resources.deserialize(buff)
		return buff

class cs_build_trap(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()
		self.trap_entry = cint32()
		self.count = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.trap_entry.serialize(buff, buff_len)
		buff, buff_len = self.count.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.trap_entry.deserialize(buff)
		buff = self.count.deserialize(buff)
		return buff

class sc_build_trap(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.castle_id = cint64()
		self.resources = user_resource_t()
		self.len_of_trap_list = cuint16()
		self.trap_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_trap_list.serialize(buff, buff_len)
		for i in range(self.len_of_trap_list.value):
			buff, buff_len = self.trap_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_trap_list.deserialize(buff)
		self.trap_list = []
		for i in range(self.len_of_trap_list.value):
			self.trap_list.append(trap_data_t())
			buff = self.trap_list[i].deserialize(buff)
		return buff

	def add_trap_list():
		if len(trap_list) >= MAX_TRAP_COUNT.value:
			return None
		trap_list.append(trap_data_t())
		return trap_list[len(trap_list) - 1]

class cs_get_trap_list(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		return buff

class sc_get_trap_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.castle_id = cint64()
		self.len_of_trap_list = cuint16()
		self.trap_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_trap_list.serialize(buff, buff_len)
		for i in range(self.len_of_trap_list.value):
			buff, buff_len = self.trap_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.len_of_trap_list.deserialize(buff)
		self.trap_list = []
		for i in range(self.len_of_trap_list.value):
			self.trap_list.append(trap_data_t())
			buff = self.trap_list[i].deserialize(buff)
		return buff

	def add_trap_list():
		if len(trap_list) >= MAX_TRAP_COUNT.value:
			return None
		trap_list.append(trap_data_t())
		return trap_list[len(trap_list) - 1]

class cs_cancel_build_trap(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()
		self.trap_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.trap_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.trap_entry.deserialize(buff)
		return buff

class sc_cancel_build_trap(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.castle_id = cint64()
		self.resources = user_resource_t()
		self.len_of_trap_list = cuint16()
		self.trap_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_trap_list.serialize(buff, buff_len)
		for i in range(self.len_of_trap_list.value):
			buff, buff_len = self.trap_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_trap_list.deserialize(buff)
		self.trap_list = []
		for i in range(self.len_of_trap_list.value):
			self.trap_list.append(trap_data_t())
			buff = self.trap_list[i].deserialize(buff)
		return buff

	def add_trap_list():
		if len(trap_list) >= MAX_TRAP_COUNT.value:
			return None
		trap_list.append(trap_data_t())
		return trap_list[len(trap_list) - 1]

class cs_accelerate_build_trap(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()
		self.trap_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.trap_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.trap_entry.deserialize(buff)
		return buff

class sc_accelerate_build_trap(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.castle_id = cint64()
		self.resources = user_resource_t()
		self.len_of_trap_list = cuint16()
		self.trap_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_trap_list.serialize(buff, buff_len)
		for i in range(self.len_of_trap_list.value):
			buff, buff_len = self.trap_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_trap_list.deserialize(buff)
		self.trap_list = []
		for i in range(self.len_of_trap_list.value):
			self.trap_list.append(trap_data_t())
			buff = self.trap_list[i].deserialize(buff)
		return buff

	def add_trap_list():
		if len(trap_list) >= MAX_TRAP_COUNT.value:
			return None
		trap_list.append(trap_data_t())
		return trap_list[len(trap_list) - 1]

class cs_demolish_trap(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()
		self.trap_entry = cint32()
		self.count = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.trap_entry.serialize(buff, buff_len)
		buff, buff_len = self.count.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.trap_entry.deserialize(buff)
		buff = self.count.deserialize(buff)
		return buff

class sc_demolish_trap(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.castle_id = cint64()
		self.len_of_trap_list = cuint16()
		self.trap_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_trap_list.serialize(buff, buff_len)
		for i in range(self.len_of_trap_list.value):
			buff, buff_len = self.trap_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.len_of_trap_list.deserialize(buff)
		self.trap_list = []
		for i in range(self.len_of_trap_list.value):
			self.trap_list.append(trap_data_t())
			buff = self.trap_list[i].deserialize(buff)
		return buff

	def add_trap_list():
		if len(trap_list) >= MAX_TRAP_COUNT.value:
			return None
		trap_list.append(trap_data_t())
		return trap_list[len(trap_list) - 1]

class cs_get_one_corps_info(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		return buff

class sc_get_one_corps_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.len_of_corps_data_list = cuint16()
		self.corps_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.len_of_corps_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_corps_data_list.value):
			buff, buff_len = self.corps_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.len_of_corps_data_list.deserialize(buff)
		self.corps_data_list = []
		for i in range(self.len_of_corps_data_list.value):
			self.corps_data_list.append(corps_data_t())
			buff = self.corps_data_list[i].deserialize(buff)
		return buff

	def add_corps_data_list():
		if len(corps_data_list) >= MAX_CORPS_COUNT.value:
			return None
		corps_data_list.append(corps_data_t())
		return corps_data_list[len(corps_data_list) - 1]

class cs_get_land_info(proto):
	def __init__(self):
		self.session = session_t()
		self.chunk_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.chunk_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.chunk_id.deserialize(buff)
		return buff

class sc_get_land_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.chunk_id = cint32()
		self.len_of_block_data_list = cuint16()
		self.block_data_list = []
		self.len_of_user_summary_data = cuint16()
		self.user_summary_data = []
		self.len_of_mark_list = cuint16()
		self.mark_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.chunk_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_block_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_block_data_list.value):
			buff, buff_len = self.block_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_user_summary_data.serialize(buff, buff_len)
		for i in range(self.len_of_user_summary_data.value):
			buff, buff_len = self.user_summary_data[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_mark_list.serialize(buff, buff_len)
		for i in range(self.len_of_mark_list.value):
			buff, buff_len = self.mark_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.chunk_id.deserialize(buff)
		buff = self.len_of_block_data_list.deserialize(buff)
		self.block_data_list = []
		for i in range(self.len_of_block_data_list.value):
			self.block_data_list.append(block_data_t())
			buff = self.block_data_list[i].deserialize(buff)
		buff = self.len_of_user_summary_data.deserialize(buff)
		self.user_summary_data = []
		for i in range(self.len_of_user_summary_data.value):
			self.user_summary_data.append(user_summary_data_t())
			buff = self.user_summary_data[i].deserialize(buff)
		buff = self.len_of_mark_list.deserialize(buff)
		self.mark_list = []
		for i in range(self.len_of_mark_list.value):
			self.mark_list.append(user_mark_t())
			buff = self.mark_list[i].deserialize(buff)
		return buff

	def add_block_data_list():
		if len(block_data_list) >= MAX_GET_LAND_NUM.value:
			return None
		block_data_list.append(block_data_t())
		return block_data_list[len(block_data_list) - 1]

	def add_user_summary_data():
		if len(user_summary_data) >= MAX_BLOCK_USER_NUM.value:
			return None
		user_summary_data.append(user_summary_data_t())
		return user_summary_data[len(user_summary_data) - 1]

	def add_mark_list():
		if len(mark_list) >= MAX_BLOCK_USER_MARK.value:
			return None
		mark_list.append(user_mark_t())
		return mark_list[len(mark_list) - 1]

class cs_get_more_block_info(proto):
	def __init__(self):
		self.session = session_t()
		self.block_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		return buff

class sc_get_more_block_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.block_id = cint32()
		self.block_data = block_data_t()
		self.city_data = guild_city_rank_t()
		self.len_of_user_summary_data = cuint16()
		self.user_summary_data = []
		self.len_of_guard_list = cuint16()
		self.guard_list = []
		self.len_of_corps_list = cuint16()
		self.corps_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.block_data.serialize(buff, buff_len)
		buff, buff_len = self.city_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_user_summary_data.serialize(buff, buff_len)
		for i in range(self.len_of_user_summary_data.value):
			buff, buff_len = self.user_summary_data[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_guard_list.serialize(buff, buff_len)
		for i in range(self.len_of_guard_list.value):
			buff, buff_len = self.guard_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_corps_list.serialize(buff, buff_len)
		for i in range(self.len_of_corps_list.value):
			buff, buff_len = self.corps_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.block_data.deserialize(buff)
		buff = self.city_data.deserialize(buff)
		buff = self.len_of_user_summary_data.deserialize(buff)
		self.user_summary_data = []
		for i in range(self.len_of_user_summary_data.value):
			self.user_summary_data.append(user_summary_data_t())
			buff = self.user_summary_data[i].deserialize(buff)
		buff = self.len_of_guard_list.deserialize(buff)
		self.guard_list = []
		for i in range(self.len_of_guard_list.value):
			self.guard_list.append(block_guard_brief_data_t())
			buff = self.guard_list[i].deserialize(buff)
		buff = self.len_of_corps_list.deserialize(buff)
		self.corps_list = []
		for i in range(self.len_of_corps_list.value):
			self.corps_list.append(block_fort_corps_brief_data_t())
			buff = self.corps_list[i].deserialize(buff)
		return buff

	def add_user_summary_data():
		if len(user_summary_data) >= MAX_BLOCK_USER_NUM.value:
			return None
		user_summary_data.append(user_summary_data_t())
		return user_summary_data[len(user_summary_data) - 1]

	def add_guard_list():
		if len(guard_list) >= MAX_BLOCK_GUARD_NUM.value:
			return None
		guard_list.append(block_guard_brief_data_t())
		return guard_list[len(guard_list) - 1]

	def add_corps_list():
		if len(corps_list) >= MAX_FORT_CORPS_NUM.value:
			return None
		corps_list.append(block_fort_corps_brief_data_t())
		return corps_list[len(corps_list) - 1]

class cs_get_summary_user_info(proto):
	def __init__(self):
		self.session = session_t()
		self.user_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		return buff

class sc_get_summary_user_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_id = cint64()
		self.user_summary_data = user_summary_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.user_summary_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.user_summary_data.deserialize(buff)
		return buff

class cs_get_battle_record(proto):
	def __init__(self):
		self.session = session_t()
		self.battle_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.battle_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.battle_id.deserialize(buff)
		return buff

class sc_get_battle_record(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.battle_id = cint64()
		self.record = battle_record()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.battle_id.serialize(buff, buff_len)
		buff, buff_len = self.record.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.battle_id.deserialize(buff)
		buff = self.record.deserialize(buff)
		return buff

class cs_get_battle_record_list(proto):
	def __init__(self):
		self.session = session_t()
		self.page = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.page.deserialize(buff)
		return buff

class sc_get_battle_record_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.amount = cint32()
		self.page = cint32()
		self.len_of_brief_record = cuint16()
		self.brief_record = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.amount.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		buff, buff_len = self.len_of_brief_record.serialize(buff, buff_len)
		for i in range(self.len_of_brief_record.value):
			buff, buff_len = self.brief_record[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.amount.deserialize(buff)
		buff = self.page.deserialize(buff)
		buff = self.len_of_brief_record.deserialize(buff)
		self.brief_record = []
		for i in range(self.len_of_brief_record.value):
			self.brief_record.append(brief_battle_record())
			buff = self.brief_record[i].deserialize(buff)
		return buff

	def add_brief_record():
		if len(brief_record) >= MAX_BATTLE_RECORD_NUM.value:
			return None
		brief_record.append(brief_battle_record())
		return brief_record[len(brief_record) - 1]

class cs_syn_user_resource(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_syn_user_resource(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.resource_info = user_resource_t()
		self.resource_icr = user_resource_increase_t()
		self.seize_times = cint32()
		self.token = cint32()
		self.token_buy_times = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.resource_info.serialize(buff, buff_len)
		buff, buff_len = self.resource_icr.serialize(buff, buff_len)
		buff, buff_len = self.seize_times.serialize(buff, buff_len)
		buff, buff_len = self.token.serialize(buff, buff_len)
		buff, buff_len = self.token_buy_times.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.resource_info.deserialize(buff)
		buff = self.resource_icr.deserialize(buff)
		buff = self.seize_times.deserialize(buff)
		buff = self.token.deserialize(buff)
		buff = self.token_buy_times.deserialize(buff)
		return buff

class cs_syn_user_resource_limit(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_syn_user_resource_limit(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.resource_limit = user_resource_limit_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.resource_limit.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.resource_limit.deserialize(buff)
		return buff

class cs_change_head_entry(proto):
	def __init__(self):
		self.session = session_t()
		self.head_entry = cint32()
		self.head_type = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.head_entry.serialize(buff, buff_len)
		buff, buff_len = self.head_type.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.head_entry.deserialize(buff)
		buff = self.head_type.deserialize(buff)
		return buff

class sc_change_head_entry(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.head_entry = cint32()
		self.head_type = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.head_entry.serialize(buff, buff_len)
		buff, buff_len = self.head_type.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.head_entry.deserialize(buff)
		buff = self.head_type.deserialize(buff)
		return buff

class cs_change_signature(proto):
	def __init__(self):
		self.session = session_t()
		self.signature = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.signature.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.signature.deserialize(buff)
		return buff

class sc_change_signature(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.signature = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.signature.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.signature.deserialize(buff)
		return buff

class cs_pay_for_free(proto):
	def __init__(self):
		self.session = session_t()
		self.res_data = resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.res_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.res_data.deserialize(buff)
		return buff

class sc_pay_for_free(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.invaded_max = cint32()
		self.invaded_progress = cint32()
		self.invaded_id = cint64()
		self.user_res = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.invaded_max.serialize(buff, buff_len)
		buff, buff_len = self.invaded_progress.serialize(buff, buff_len)
		buff, buff_len = self.invaded_id.serialize(buff, buff_len)
		buff, buff_len = self.user_res.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.invaded_max.deserialize(buff)
		buff = self.invaded_progress.deserialize(buff)
		buff = self.invaded_id.deserialize(buff)
		buff = self.user_res.deserialize(buff)
		return buff

class cs_liberate(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_liberate(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.invaded_max = cint32()
		self.invaded_progress = cint32()
		self.invaded_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.invaded_max.serialize(buff, buff_len)
		buff, buff_len = self.invaded_progress.serialize(buff, buff_len)
		buff, buff_len = self.invaded_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.invaded_max.deserialize(buff)
		buff = self.invaded_progress.deserialize(buff)
		buff = self.invaded_id.deserialize(buff)
		return buff

class cs_get_invader_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_invader_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_invader_list = cuint16()
		self.invader_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_invader_list.serialize(buff, buff_len)
		for i in range(self.len_of_invader_list.value):
			buff, buff_len = self.invader_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_invader_list.deserialize(buff)
		self.invader_list = []
		for i in range(self.len_of_invader_list.value):
			self.invader_list.append(invader_data_t())
			buff = self.invader_list[i].deserialize(buff)
		return buff

	def add_invader_list():
		if len(invader_list) >= MAX_INVADER_NUM.value:
			return None
		invader_list.append(invader_data_t())
		return invader_list[len(invader_list) - 1]

class cs_change_nick_name(proto):
	def __init__(self):
		self.session = session_t()
		self.nick_name = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		return buff

class sc_change_nick_name(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.nick_name = cstring()
		self.resources = user_resource_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []
		self.nick_name_change = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.nick_name_change.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		buff = self.nick_name_change.deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_user_power_data(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_user_power_data(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.power_data = user_power_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.power_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.power_data.deserialize(buff)
		return buff

class cs_go_home_immediately(proto):
	def __init__(self):
		self.session = session_t()
		self.event_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		return buff

class sc_go_home_immediately(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.event_id = cint64()
		self.len_of_corps_data_list = cuint16()
		self.corps_data_list = []
		self.user_res = user_resource_t()
		self.event_data = game_event_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_corps_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_corps_data_list.value):
			buff, buff_len = self.corps_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.user_res.serialize(buff, buff_len)
		buff, buff_len = self.event_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.len_of_corps_data_list.deserialize(buff)
		self.corps_data_list = []
		for i in range(self.len_of_corps_data_list.value):
			self.corps_data_list.append(corps_data_t())
			buff = self.corps_data_list[i].deserialize(buff)
		buff = self.user_res.deserialize(buff)
		buff = self.event_data.deserialize(buff)
		return buff

	def add_corps_data_list():
		if len(corps_data_list) >= MAX_CORPS_COUNT.value:
			return None
		corps_data_list.append(corps_data_t())
		return corps_data_list[len(corps_data_list) - 1]

class cs_guild_data_req(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_guild_data_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.guild_data = guild_t()
		self.len_of_guild_member_list = cuint16()
		self.guild_member_list = []
		self.user_guild_data = guild_member_t()
		self.len_of_invitation_list = cuint16()
		self.invitation_list = []
		self.len_of_mark_list = cuint16()
		self.mark_list = []
		self.len_of_application_list = cuint16()
		self.application_list = []
		self.len_of_city_list = cuint16()
		self.city_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.guild_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_guild_member_list.serialize(buff, buff_len)
		for i in range(self.len_of_guild_member_list.value):
			buff, buff_len = self.guild_member_list[i].serialize(buff, buff_len)
		buff, buff_len = self.user_guild_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_invitation_list.serialize(buff, buff_len)
		for i in range(self.len_of_invitation_list.value):
			buff, buff_len = self.invitation_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_mark_list.serialize(buff, buff_len)
		for i in range(self.len_of_mark_list.value):
			buff, buff_len = self.mark_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_application_list.serialize(buff, buff_len)
		for i in range(self.len_of_application_list.value):
			buff, buff_len = self.application_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_city_list.serialize(buff, buff_len)
		for i in range(self.len_of_city_list.value):
			buff, buff_len = self.city_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.guild_data.deserialize(buff)
		buff = self.len_of_guild_member_list.deserialize(buff)
		self.guild_member_list = []
		for i in range(self.len_of_guild_member_list.value):
			self.guild_member_list.append(brief_guild_member())
			buff = self.guild_member_list[i].deserialize(buff)
		buff = self.user_guild_data.deserialize(buff)
		buff = self.len_of_invitation_list.deserialize(buff)
		self.invitation_list = []
		for i in range(self.len_of_invitation_list.value):
			self.invitation_list.append(guild_invitation_t())
			buff = self.invitation_list[i].deserialize(buff)
		buff = self.len_of_mark_list.deserialize(buff)
		self.mark_list = []
		for i in range(self.len_of_mark_list.value):
			self.mark_list.append(guild_mark_t())
			buff = self.mark_list[i].deserialize(buff)
		buff = self.len_of_application_list.deserialize(buff)
		self.application_list = []
		for i in range(self.len_of_application_list.value):
			self.application_list.append(guild_application_t())
			buff = self.application_list[i].deserialize(buff)
		buff = self.len_of_city_list.deserialize(buff)
		self.city_list = []
		for i in range(self.len_of_city_list.value):
			self.city_list.append(guild_city_t())
			buff = self.city_list[i].deserialize(buff)
		return buff

	def add_guild_member_list():
		if len(guild_member_list) >= MAX_GUILD_MEMBER.value:
			return None
		guild_member_list.append(brief_guild_member())
		return guild_member_list[len(guild_member_list) - 1]

	def add_invitation_list():
		if len(invitation_list) >= MAX_GUILD_INVITATION.value:
			return None
		invitation_list.append(guild_invitation_t())
		return invitation_list[len(invitation_list) - 1]

	def add_mark_list():
		if len(mark_list) >= MAX_GUILD_MARK.value:
			return None
		mark_list.append(guild_mark_t())
		return mark_list[len(mark_list) - 1]

	def add_application_list():
		if len(application_list) >= MAX_GUILD_APPLICATION.value:
			return None
		application_list.append(guild_application_t())
		return application_list[len(application_list) - 1]

	def add_city_list():
		if len(city_list) >= MAX_GUILD_CITY_NUM.value:
			return None
		city_list.append(guild_city_t())
		return city_list[len(city_list) - 1]

class cs_guild_create(proto):
	def __init__(self):
		self.session = session_t()
		self.nick_name = cstring()
		self.icon = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		buff, buff_len = self.icon.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		buff = self.icon.deserialize(buff)
		return buff

class sc_guild_create(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.guild_data = guild_t()
		self.len_of_guild_member_list = cuint16()
		self.guild_member_list = []
		self.resource_info = user_resource_t()
		self.user_guild_data = guild_member_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.guild_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_guild_member_list.serialize(buff, buff_len)
		for i in range(self.len_of_guild_member_list.value):
			buff, buff_len = self.guild_member_list[i].serialize(buff, buff_len)
		buff, buff_len = self.resource_info.serialize(buff, buff_len)
		buff, buff_len = self.user_guild_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.guild_data.deserialize(buff)
		buff = self.len_of_guild_member_list.deserialize(buff)
		self.guild_member_list = []
		for i in range(self.len_of_guild_member_list.value):
			self.guild_member_list.append(brief_guild_member())
			buff = self.guild_member_list[i].deserialize(buff)
		buff = self.resource_info.deserialize(buff)
		buff = self.user_guild_data.deserialize(buff)
		return buff

	def add_guild_member_list():
		if len(guild_member_list) >= MAX_GUILD_MEMBER.value:
			return None
		guild_member_list.append(brief_guild_member())
		return guild_member_list[len(guild_member_list) - 1]

class cs_guild_contribute(proto):
	def __init__(self):
		self.session = session_t()
		self.res_data = resource_t()
		self.gold = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.res_data.serialize(buff, buff_len)
		buff, buff_len = self.gold.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.res_data.deserialize(buff)
		buff = self.gold.deserialize(buff)
		return buff

class sc_guild_contribute(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.guild_data = guild_t()
		self.len_of_guild_member_list = cuint16()
		self.guild_member_list = []
		self.user_guild_data = guild_member_t()
		self.resource_info = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.guild_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_guild_member_list.serialize(buff, buff_len)
		for i in range(self.len_of_guild_member_list.value):
			buff, buff_len = self.guild_member_list[i].serialize(buff, buff_len)
		buff, buff_len = self.user_guild_data.serialize(buff, buff_len)
		buff, buff_len = self.resource_info.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.guild_data.deserialize(buff)
		buff = self.len_of_guild_member_list.deserialize(buff)
		self.guild_member_list = []
		for i in range(self.len_of_guild_member_list.value):
			self.guild_member_list.append(brief_guild_member())
			buff = self.guild_member_list[i].deserialize(buff)
		buff = self.user_guild_data.deserialize(buff)
		buff = self.resource_info.deserialize(buff)
		return buff

	def add_guild_member_list():
		if len(guild_member_list) >= MAX_GUILD_MEMBER.value:
			return None
		guild_member_list.append(brief_guild_member())
		return guild_member_list[len(guild_member_list) - 1]

class cs_guild_apply(proto):
	def __init__(self):
		self.session = session_t()
		self.guild_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		return buff

class sc_guild_apply(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.guild_id = cint64()
		self.len_of_application_list = cuint16()
		self.application_list = []
		self.is_pass = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_application_list.serialize(buff, buff_len)
		for i in range(self.len_of_application_list.value):
			buff, buff_len = self.application_list[i].serialize(buff, buff_len)
		buff, buff_len = self.is_pass.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		buff = self.len_of_application_list.deserialize(buff)
		self.application_list = []
		for i in range(self.len_of_application_list.value):
			self.application_list.append(guild_application_t())
			buff = self.application_list[i].deserialize(buff)
		buff = self.is_pass.deserialize(buff)
		return buff

	def add_application_list():
		if len(application_list) >= MAX_USER_APPLICATION.value:
			return None
		application_list.append(guild_application_t())
		return application_list[len(application_list) - 1]

class cs_guild_application_req(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_guild_application_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_application_list = cuint16()
		self.application_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_application_list.serialize(buff, buff_len)
		for i in range(self.len_of_application_list.value):
			buff, buff_len = self.application_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_application_list.deserialize(buff)
		self.application_list = []
		for i in range(self.len_of_application_list.value):
			self.application_list.append(guild_user_application_t())
			buff = self.application_list[i].deserialize(buff)
		return buff

	def add_application_list():
		if len(application_list) >= MAX_GUILD_APPLICATION.value:
			return None
		application_list.append(guild_user_application_t())
		return application_list[len(application_list) - 1]

class cs_guild_application_process(proto):
	def __init__(self):
		self.session = session_t()
		self.user_id = cint64()
		self.typed = E_APPLICATION_PROCESS_TYPE()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.typed.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.typed.deserialize(buff)
		return buff

class sc_guild_application_process(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_id = cint64()
		self.typed = E_APPLICATION_PROCESS_TYPE()
		self.len_of_application_list = cuint16()
		self.application_list = []
		self.len_of_guild_member_list = cuint16()
		self.guild_member_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.typed.serialize(buff, buff_len)
		buff, buff_len = self.len_of_application_list.serialize(buff, buff_len)
		for i in range(self.len_of_application_list.value):
			buff, buff_len = self.application_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_guild_member_list.serialize(buff, buff_len)
		for i in range(self.len_of_guild_member_list.value):
			buff, buff_len = self.guild_member_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.typed.deserialize(buff)
		buff = self.len_of_application_list.deserialize(buff)
		self.application_list = []
		for i in range(self.len_of_application_list.value):
			self.application_list.append(guild_application_t())
			buff = self.application_list[i].deserialize(buff)
		buff = self.len_of_guild_member_list.deserialize(buff)
		self.guild_member_list = []
		for i in range(self.len_of_guild_member_list.value):
			self.guild_member_list.append(brief_guild_member())
			buff = self.guild_member_list[i].deserialize(buff)
		return buff

	def add_application_list():
		if len(application_list) >= MAX_GUILD_APPLICATION.value:
			return None
		application_list.append(guild_application_t())
		return application_list[len(application_list) - 1]

	def add_guild_member_list():
		if len(guild_member_list) >= MAX_GUILD_MEMBER.value:
			return None
		guild_member_list.append(brief_guild_member())
		return guild_member_list[len(guild_member_list) - 1]

class cs_guild_expel_member(proto):
	def __init__(self):
		self.session = session_t()
		self.user_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		return buff

class sc_guild_expel_member(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_id = cint64()
		self.len_of_guild_member_list = cuint16()
		self.guild_member_list = []
		self.len_of_group_data_list = cuint16()
		self.group_data_list = []
		self.free_group = guild_group_info()
		self.my_group = my_group_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_guild_member_list.serialize(buff, buff_len)
		for i in range(self.len_of_guild_member_list.value):
			buff, buff_len = self.guild_member_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_group_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_group_data_list.value):
			buff, buff_len = self.group_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.free_group.serialize(buff, buff_len)
		buff, buff_len = self.my_group.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.len_of_guild_member_list.deserialize(buff)
		self.guild_member_list = []
		for i in range(self.len_of_guild_member_list.value):
			self.guild_member_list.append(brief_guild_member())
			buff = self.guild_member_list[i].deserialize(buff)
		buff = self.len_of_group_data_list.deserialize(buff)
		self.group_data_list = []
		for i in range(self.len_of_group_data_list.value):
			self.group_data_list.append(guild_group_t())
			buff = self.group_data_list[i].deserialize(buff)
		buff = self.free_group.deserialize(buff)
		buff = self.my_group.deserialize(buff)
		return buff

	def add_guild_member_list():
		if len(guild_member_list) >= MAX_GUILD_MEMBER.value:
			return None
		guild_member_list.append(brief_guild_member())
		return guild_member_list[len(guild_member_list) - 1]

	def add_group_data_list():
		if len(group_data_list) >= MAX_GUILD_GROUP.value:
			return None
		group_data_list.append(guild_group_t())
		return group_data_list[len(group_data_list) - 1]

class cs_guild_quit(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_guild_quit(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_guild_data = guild_member_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_guild_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_guild_data.deserialize(buff)
		return buff

class cs_guild_transfer(proto):
	def __init__(self):
		self.session = session_t()
		self.user_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		return buff

class sc_guild_transfer(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.guild_data = guild_t()
		self.len_of_guild_member_list = cuint16()
		self.guild_member_list = []
		self.user_guild_data = guild_member_t()
		self.len_of_group_data_list = cuint16()
		self.group_data_list = []
		self.free_group = guild_group_info()
		self.my_group = my_group_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.guild_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_guild_member_list.serialize(buff, buff_len)
		for i in range(self.len_of_guild_member_list.value):
			buff, buff_len = self.guild_member_list[i].serialize(buff, buff_len)
		buff, buff_len = self.user_guild_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_group_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_group_data_list.value):
			buff, buff_len = self.group_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.free_group.serialize(buff, buff_len)
		buff, buff_len = self.my_group.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.guild_data.deserialize(buff)
		buff = self.len_of_guild_member_list.deserialize(buff)
		self.guild_member_list = []
		for i in range(self.len_of_guild_member_list.value):
			self.guild_member_list.append(brief_guild_member())
			buff = self.guild_member_list[i].deserialize(buff)
		buff = self.user_guild_data.deserialize(buff)
		buff = self.len_of_group_data_list.deserialize(buff)
		self.group_data_list = []
		for i in range(self.len_of_group_data_list.value):
			self.group_data_list.append(guild_group_t())
			buff = self.group_data_list[i].deserialize(buff)
		buff = self.free_group.deserialize(buff)
		buff = self.my_group.deserialize(buff)
		return buff

	def add_guild_member_list():
		if len(guild_member_list) >= MAX_GUILD_MEMBER.value:
			return None
		guild_member_list.append(brief_guild_member())
		return guild_member_list[len(guild_member_list) - 1]

	def add_group_data_list():
		if len(group_data_list) >= MAX_GUILD_GROUP.value:
			return None
		group_data_list.append(guild_group_t())
		return group_data_list[len(group_data_list) - 1]

class cs_guild_commission(proto):
	def __init__(self):
		self.session = session_t()
		self.user_id = cint64()
		self.position = E_GUILD_POSITION()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.position.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.position.deserialize(buff)
		return buff

class sc_guild_commission(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_id = cint64()
		self.position = E_GUILD_POSITION()
		self.len_of_guild_member_list = cuint16()
		self.guild_member_list = []
		self.len_of_group_data_list = cuint16()
		self.group_data_list = []
		self.free_group = guild_group_info()
		self.my_group = my_group_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.position.serialize(buff, buff_len)
		buff, buff_len = self.len_of_guild_member_list.serialize(buff, buff_len)
		for i in range(self.len_of_guild_member_list.value):
			buff, buff_len = self.guild_member_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_group_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_group_data_list.value):
			buff, buff_len = self.group_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.free_group.serialize(buff, buff_len)
		buff, buff_len = self.my_group.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.position.deserialize(buff)
		buff = self.len_of_guild_member_list.deserialize(buff)
		self.guild_member_list = []
		for i in range(self.len_of_guild_member_list.value):
			self.guild_member_list.append(brief_guild_member())
			buff = self.guild_member_list[i].deserialize(buff)
		buff = self.len_of_group_data_list.deserialize(buff)
		self.group_data_list = []
		for i in range(self.len_of_group_data_list.value):
			self.group_data_list.append(guild_group_t())
			buff = self.group_data_list[i].deserialize(buff)
		buff = self.free_group.deserialize(buff)
		buff = self.my_group.deserialize(buff)
		return buff

	def add_guild_member_list():
		if len(guild_member_list) >= MAX_GUILD_MEMBER.value:
			return None
		guild_member_list.append(brief_guild_member())
		return guild_member_list[len(guild_member_list) - 1]

	def add_group_data_list():
		if len(group_data_list) >= MAX_GUILD_GROUP.value:
			return None
		group_data_list.append(guild_group_t())
		return group_data_list[len(group_data_list) - 1]

class cs_guild_dismiss(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_guild_dismiss(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_guild_data = guild_member_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_guild_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_guild_data.deserialize(buff)
		return buff

class cs_guild_set_noitce(proto):
	def __init__(self):
		self.session = session_t()
		self.notice = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.notice.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.notice.deserialize(buff)
		return buff

class sc_guild_set_noitce(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.guild_data = guild_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.guild_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.guild_data.deserialize(buff)
		return buff

class cs_guild_search(proto):
	def __init__(self):
		self.session = session_t()
		self.name = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.name.deserialize(buff)
		return buff

class sc_guild_search(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.guild_data = guild_t()
		self.len_of_city_list = cuint16()
		self.city_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.guild_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_city_list.serialize(buff, buff_len)
		for i in range(self.len_of_city_list.value):
			buff, buff_len = self.city_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.guild_data.deserialize(buff)
		buff = self.len_of_city_list.deserialize(buff)
		self.city_list = []
		for i in range(self.len_of_city_list.value):
			self.city_list.append(guild_city_t())
			buff = self.city_list[i].deserialize(buff)
		return buff

	def add_city_list():
		if len(city_list) >= MAX_GUILD_CITY_NUM.value:
			return None
		city_list.append(guild_city_t())
		return city_list[len(city_list) - 1]

class cs_guild_list_req(proto):
	def __init__(self):
		self.session = session_t()
		self.page = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.page.deserialize(buff)
		return buff

class sc_guild_list_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.amount = cint32()
		self.page = cint32()
		self.len_of_guild_list = cuint16()
		self.guild_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.amount.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		buff, buff_len = self.len_of_guild_list.serialize(buff, buff_len)
		for i in range(self.len_of_guild_list.value):
			buff, buff_len = self.guild_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.amount.deserialize(buff)
		buff = self.page.deserialize(buff)
		buff = self.len_of_guild_list.deserialize(buff)
		self.guild_list = []
		for i in range(self.len_of_guild_list.value):
			self.guild_list.append(guild_brief_t())
			buff = self.guild_list[i].deserialize(buff)
		return buff

	def add_guild_list():
		if len(guild_list) >= MAX_GUILD_LIST.value:
			return None
		guild_list.append(guild_brief_t())
		return guild_list[len(guild_list) - 1]

class cs_guild_invite(proto):
	def __init__(self):
		self.session = session_t()
		self.user_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		return buff

class sc_guild_invite(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		return buff

class cs_guild_invitation_req(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_guild_invitation_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_invitation_list = cuint16()
		self.invitation_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_invitation_list.serialize(buff, buff_len)
		for i in range(self.len_of_invitation_list.value):
			buff, buff_len = self.invitation_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_invitation_list.deserialize(buff)
		self.invitation_list = []
		for i in range(self.len_of_invitation_list.value):
			self.invitation_list.append(guild_invitation_t())
			buff = self.invitation_list[i].deserialize(buff)
		return buff

	def add_invitation_list():
		if len(invitation_list) >= MAX_GUILD_INVITATION.value:
			return None
		invitation_list.append(guild_invitation_t())
		return invitation_list[len(invitation_list) - 1]

class cs_guild_invitation_process(proto):
	def __init__(self):
		self.session = session_t()
		self.guild_id = cint64()
		self.typed = E_APPLICATION_PROCESS_TYPE()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.typed.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		buff = self.typed.deserialize(buff)
		return buff

class sc_guild_invitation_process(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.guild_id = cint64()
		self.typed = E_APPLICATION_PROCESS_TYPE()
		self.len_of_invitation_list = cuint16()
		self.invitation_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.typed.serialize(buff, buff_len)
		buff, buff_len = self.len_of_invitation_list.serialize(buff, buff_len)
		for i in range(self.len_of_invitation_list.value):
			buff, buff_len = self.invitation_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		buff = self.typed.deserialize(buff)
		buff = self.len_of_invitation_list.deserialize(buff)
		self.invitation_list = []
		for i in range(self.len_of_invitation_list.value):
			self.invitation_list.append(guild_invitation_t())
			buff = self.invitation_list[i].deserialize(buff)
		return buff

	def add_invitation_list():
		if len(invitation_list) >= MAX_GUILD_INVITATION.value:
			return None
		invitation_list.append(guild_invitation_t())
		return invitation_list[len(invitation_list) - 1]

class cs_get_mission_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_mission_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.tasks = fame_task_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.tasks.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.tasks.deserialize(buff)
		return buff

class cs_get_mission_rewards(proto):
	def __init__(self):
		self.session = session_t()
		self.mission_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.mission_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.mission_entry.deserialize(buff)
		return buff

class sc_get_mission_rewards(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.tasks = fame_task_t()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.tasks.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.tasks.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

class cs_get_achievement_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_achievement_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_achievement_list = cuint16()
		self.achievement_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_achievement_list.serialize(buff, buff_len)
		for i in range(self.len_of_achievement_list.value):
			buff, buff_len = self.achievement_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_achievement_list.deserialize(buff)
		self.achievement_list = []
		for i in range(self.len_of_achievement_list.value):
			self.achievement_list.append(achievement_t())
			buff = self.achievement_list[i].deserialize(buff)
		return buff

	def add_achievement_list():
		if len(achievement_list) >= MAX_ACHIEVEMENT_NUM.value:
			return None
		achievement_list.append(achievement_t())
		return achievement_list[len(achievement_list) - 1]

class cs_get_achievement_rewards(proto):
	def __init__(self):
		self.session = session_t()
		self.achievement_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.achievement_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.achievement_entry.deserialize(buff)
		return buff

class sc_get_achievement_rewards(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.achievement_data = achievement_t()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.achievement_data.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.achievement_data.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

class cs_guild_get_relationship(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_guild_get_relationship(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_relationship_list = cuint16()
		self.relationship_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_relationship_list.serialize(buff, buff_len)
		for i in range(self.len_of_relationship_list.value):
			buff, buff_len = self.relationship_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_relationship_list.deserialize(buff)
		self.relationship_list = []
		for i in range(self.len_of_relationship_list.value):
			self.relationship_list.append(guild_relationship_t())
			buff = self.relationship_list[i].deserialize(buff)
		return buff

	def add_relationship_list():
		if len(relationship_list) >= MAX_GUILD_RELATIONSHIP.value:
			return None
		relationship_list.append(guild_relationship_t())
		return relationship_list[len(relationship_list) - 1]

class cs_guild_set_relationship(proto):
	def __init__(self):
		self.session = session_t()
		self.guild_id = cint64()
		self.typed = E_GUILD_RELATIONSHIP()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.typed.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		buff = self.typed.deserialize(buff)
		return buff

class sc_guild_set_relationship(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.guild_id = cint64()
		self.len_of_relationship_list = cuint16()
		self.relationship_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_relationship_list.serialize(buff, buff_len)
		for i in range(self.len_of_relationship_list.value):
			buff, buff_len = self.relationship_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		buff = self.len_of_relationship_list.deserialize(buff)
		self.relationship_list = []
		for i in range(self.len_of_relationship_list.value):
			self.relationship_list.append(guild_relationship_t())
			buff = self.relationship_list[i].deserialize(buff)
		return buff

	def add_relationship_list():
		if len(relationship_list) >= MAX_GUILD_RELATIONSHIP.value:
			return None
		relationship_list.append(guild_relationship_t())
		return relationship_list[len(relationship_list) - 1]

class cs_shop_buy(proto):
	def __init__(self):
		self.session = session_t()
		self.item_entry = cint32()
		self.price = cint32()
		self.currency_type = cint32()
		self.buy_num = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.price.serialize(buff, buff_len)
		buff, buff_len = self.currency_type.serialize(buff, buff_len)
		buff, buff_len = self.buy_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.price.deserialize(buff)
		buff = self.currency_type.deserialize(buff)
		buff = self.buy_num.deserialize(buff)
		return buff

class sc_shop_buy(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.resources = user_resource_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_SHOP_BUY_ITEM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_free_man_list(proto):
	def __init__(self):
		self.session = session_t()
		self.page = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.page.deserialize(buff)
		return buff

class sc_free_man_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.page = cint32()
		self.amount = cint32()
		self.len_of_user_summary_data = cuint16()
		self.user_summary_data = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		buff, buff_len = self.amount.serialize(buff, buff_len)
		buff, buff_len = self.len_of_user_summary_data.serialize(buff, buff_len)
		for i in range(self.len_of_user_summary_data.value):
			buff, buff_len = self.user_summary_data[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.page.deserialize(buff)
		buff = self.amount.deserialize(buff)
		buff = self.len_of_user_summary_data.deserialize(buff)
		self.user_summary_data = []
		for i in range(self.len_of_user_summary_data.value):
			self.user_summary_data.append(user_summary_data_t())
			buff = self.user_summary_data[i].deserialize(buff)
		return buff

	def add_user_summary_data():
		if len(user_summary_data) >= MAX_FREEMAN_LIST.value:
			return None
		user_summary_data.append(user_summary_data_t())
		return user_summary_data[len(user_summary_data) - 1]

class cs_equip_combine(proto):
	def __init__(self):
		self.session = session_t()
		self.item_entry = cint32()
		self.combine_num = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.combine_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.combine_num.deserialize(buff)
		return buff

class sc_equip_combine(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.resources = user_resource_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_equip_resolve(proto):
	def __init__(self):
		self.session = session_t()
		self.item_entry = cint32()
		self.resolve_num = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.resolve_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.resolve_num.deserialize(buff)
		return buff

class sc_equip_resolve(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.resources = user_resource_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_hero_equip_slot_strengthen(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()
		self.e_equip_slot = E_EQUIP_SLOT()
		self.strengthen_to_lv = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.e_equip_slot.serialize(buff, buff_len)
		buff, buff_len = self.strengthen_to_lv.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.e_equip_slot.deserialize(buff)
		buff = self.strengthen_to_lv.deserialize(buff)
		return buff

class sc_hero_equip_slot_strengthen(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.resources = user_resource_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []
		self.hero_data = hero_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_guildlog_list(proto):
	def __init__(self):
		self.session = session_t()
		self.typed = cint32()
		self.page = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.typed.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.typed.deserialize(buff)
		buff = self.page.deserialize(buff)
		return buff

class sc_guildlog_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.typed = cint32()
		self.page = cint32()
		self.amount = cint32()
		self.len_of_guildlog_list = cuint16()
		self.guildlog_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.typed.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		buff, buff_len = self.amount.serialize(buff, buff_len)
		buff, buff_len = self.len_of_guildlog_list.serialize(buff, buff_len)
		for i in range(self.len_of_guildlog_list.value):
			buff, buff_len = self.guildlog_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.typed.deserialize(buff)
		buff = self.page.deserialize(buff)
		buff = self.amount.deserialize(buff)
		buff = self.len_of_guildlog_list.deserialize(buff)
		self.guildlog_list = []
		for i in range(self.len_of_guildlog_list.value):
			self.guildlog_list.append(guildlog_t())
			buff = self.guildlog_list[i].deserialize(buff)
		return buff

	def add_guildlog_list():
		if len(guildlog_list) >= MAX_GUILDLOG_NUM.value:
			return None
		guildlog_list.append(guildlog_t())
		return guildlog_list[len(guildlog_list) - 1]

class cs_guild_mark_req(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_guild_mark_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_mark_list = cuint16()
		self.mark_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mark_list.serialize(buff, buff_len)
		for i in range(self.len_of_mark_list.value):
			buff, buff_len = self.mark_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_mark_list.deserialize(buff)
		self.mark_list = []
		for i in range(self.len_of_mark_list.value):
			self.mark_list.append(guild_mark_t())
			buff = self.mark_list[i].deserialize(buff)
		return buff

	def add_mark_list():
		if len(mark_list) >= MAX_GUILD_MARK.value:
			return None
		mark_list.append(guild_mark_t())
		return mark_list[len(mark_list) - 1]

class cs_guild_mark(proto):
	def __init__(self):
		self.session = session_t()
		self.block_id = cint32()
		self.name = cstring()
		self.notice = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		buff, buff_len = self.notice.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.name.deserialize(buff)
		buff = self.notice.deserialize(buff)
		return buff

class sc_guild_mark(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.block_id = cint32()
		self.len_of_mark_list = cuint16()
		self.mark_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mark_list.serialize(buff, buff_len)
		for i in range(self.len_of_mark_list.value):
			buff, buff_len = self.mark_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.len_of_mark_list.deserialize(buff)
		self.mark_list = []
		for i in range(self.len_of_mark_list.value):
			self.mark_list.append(guild_mark_t())
			buff = self.mark_list[i].deserialize(buff)
		return buff

	def add_mark_list():
		if len(mark_list) >= MAX_GUILD_MARK.value:
			return None
		mark_list.append(guild_mark_t())
		return mark_list[len(mark_list) - 1]

class cs_guild_del_mark(proto):
	def __init__(self):
		self.session = session_t()
		self.block_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		return buff

class sc_guild_del_mark(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.block_id = cint32()
		self.len_of_mark_list = cuint16()
		self.mark_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mark_list.serialize(buff, buff_len)
		for i in range(self.len_of_mark_list.value):
			buff, buff_len = self.mark_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.len_of_mark_list.deserialize(buff)
		self.mark_list = []
		for i in range(self.len_of_mark_list.value):
			self.mark_list.append(guild_mark_t())
			buff = self.mark_list[i].deserialize(buff)
		return buff

	def add_mark_list():
		if len(mark_list) >= MAX_GUILD_MARK.value:
			return None
		mark_list.append(guild_mark_t())
		return mark_list[len(mark_list) - 1]

class cs_get_lottery_data_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_lottery_data_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.lottery_info = lottery_info_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.lottery_info.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.lottery_info.deserialize(buff)
		return buff

class cs_lottery_draw(proto):
	def __init__(self):
		self.session = session_t()
		self.lottery_id = cint32()
		self.draw_index = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.lottery_id.serialize(buff, buff_len)
		buff, buff_len = self.draw_index.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.lottery_id.deserialize(buff)
		buff = self.draw_index.deserialize(buff)
		return buff

class sc_lottery_draw(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.draw_lottery_index = cint32()
		self.lottery_info = lottery_info_t()
		self.resources = user_resource_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.draw_lottery_index.serialize(buff, buff_len)
		buff, buff_len = self.lottery_info.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.draw_lottery_index.deserialize(buff)
		buff = self.lottery_info.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_lottery_reset(proto):
	def __init__(self):
		self.session = session_t()
		self.lottery_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.lottery_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.lottery_id.deserialize(buff)
		return buff

class sc_lottery_reset(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.lottery_info = lottery_info_t()
		self.resources = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.lottery_info.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.lottery_info.deserialize(buff)
		buff = self.resources.deserialize(buff)
		return buff

class cs_get_shop_buy_count(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_shop_buy_count(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.surplus_refresh_time = cint32()
		self.len_of_shop_item_list = cuint16()
		self.shop_item_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.surplus_refresh_time.serialize(buff, buff_len)
		buff, buff_len = self.len_of_shop_item_list.serialize(buff, buff_len)
		for i in range(self.len_of_shop_item_list.value):
			buff, buff_len = self.shop_item_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.surplus_refresh_time.deserialize(buff)
		buff = self.len_of_shop_item_list.deserialize(buff)
		self.shop_item_list = []
		for i in range(self.len_of_shop_item_list.value):
			self.shop_item_list.append(shop_item_t())
			buff = self.shop_item_list[i].deserialize(buff)
		return buff

	def add_shop_item_list():
		if len(shop_item_list) >= MAX_SHOP_ITEM_NUM.value:
			return None
		shop_item_list.append(shop_item_t())
		return shop_item_list[len(shop_item_list) - 1]

class cs_block_reap_req(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_block_reap_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_data = user_res_reap_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		return buff

class cs_block_reap(proto):
	def __init__(self):
		self.session = session_t()
		self.typed = E_RESOURCE_TYPE()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.typed.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.typed.deserialize(buff)
		return buff

class sc_block_reap(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.typed = E_RESOURCE_TYPE()
		self.add_res = user_resource_t()
		self.user_data = user_res_reap_data_t()
		self.user_res = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.typed.serialize(buff, buff_len)
		buff, buff_len = self.add_res.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		buff, buff_len = self.user_res.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.typed.deserialize(buff)
		buff = self.add_res.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		buff = self.user_res.deserialize(buff)
		return buff

class cs_get_effect_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_effect_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_effect_list = cuint16()
		self.effect_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_effect_list.serialize(buff, buff_len)
		for i in range(self.len_of_effect_list.value):
			buff, buff_len = self.effect_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_effect_list.deserialize(buff)
		self.effect_list = []
		for i in range(self.len_of_effect_list.value):
			self.effect_list.append(effect_t())
			buff = self.effect_list[i].deserialize(buff)
		return buff

	def add_effect_list():
		if len(effect_list) >= e_effect_type_global_max.value:
			return None
		effect_list.append(effect_t())
		return effect_list[len(effect_list) - 1]

class cs_get_chat_info(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_chat_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.ip = cstring()
		self.port = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.ip.serialize(buff, buff_len)
		buff, buff_len = self.port.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.ip.deserialize(buff)
		buff = self.port.deserialize(buff)
		return buff

class cs_get_chat_channel_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_chat_channel_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_channel_list = cuint16()
		self.channel_list = []
		self.remain_world_chat_count = cint32()
		self.world_chat_cd_time = cint32()
		self.remain_season_chat_count = cint32()
		self.season_chat_cd_time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_channel_list.serialize(buff, buff_len)
		for i in range(self.len_of_channel_list.value):
			buff, buff_len = self.channel_list[i].serialize(buff, buff_len)
		buff, buff_len = self.remain_world_chat_count.serialize(buff, buff_len)
		buff, buff_len = self.world_chat_cd_time.serialize(buff, buff_len)
		buff, buff_len = self.remain_season_chat_count.serialize(buff, buff_len)
		buff, buff_len = self.season_chat_cd_time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_channel_list.deserialize(buff)
		self.channel_list = []
		for i in range(self.len_of_channel_list.value):
			self.channel_list.append(chat_channel_t())
			buff = self.channel_list[i].deserialize(buff)
		buff = self.remain_world_chat_count.deserialize(buff)
		buff = self.world_chat_cd_time.deserialize(buff)
		buff = self.remain_season_chat_count.deserialize(buff)
		buff = self.season_chat_cd_time.deserialize(buff)
		return buff

	def add_channel_list():
		if len(channel_list) >= MAX_CHAT_CHANNEL_NUM.value:
			return None
		channel_list.append(chat_channel_t())
		return channel_list[len(channel_list) - 1]

class cs_guild_group_req(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_guild_group_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.free_group = guild_group_info()
		self.len_of_group_data_list = cuint16()
		self.group_data_list = []
		self.my_group = my_group_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.free_group.serialize(buff, buff_len)
		buff, buff_len = self.len_of_group_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_group_data_list.value):
			buff, buff_len = self.group_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.my_group.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.free_group.deserialize(buff)
		buff = self.len_of_group_data_list.deserialize(buff)
		self.group_data_list = []
		for i in range(self.len_of_group_data_list.value):
			self.group_data_list.append(guild_group_t())
			buff = self.group_data_list[i].deserialize(buff)
		buff = self.my_group.deserialize(buff)
		return buff

	def add_group_data_list():
		if len(group_data_list) >= MAX_GUILD_GROUP.value:
			return None
		group_data_list.append(guild_group_t())
		return group_data_list[len(group_data_list) - 1]

class cs_guild_group_info(proto):
	def __init__(self):
		self.session = session_t()
		self.group_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.group_id.deserialize(buff)
		return buff

class sc_guild_group_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.group_data = guild_group_info()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.group_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.group_data.deserialize(buff)
		return buff

class cs_guild_group_mod(proto):
	def __init__(self):
		self.session = session_t()
		self.group_id = cint64()
		self.name = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.group_id.deserialize(buff)
		buff = self.name.deserialize(buff)
		return buff

class sc_guild_group_mod(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.group_data = guild_group_info()
		self.len_of_group_data_list = cuint16()
		self.group_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.group_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_group_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_group_data_list.value):
			buff, buff_len = self.group_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.group_data.deserialize(buff)
		buff = self.len_of_group_data_list.deserialize(buff)
		self.group_data_list = []
		for i in range(self.len_of_group_data_list.value):
			self.group_data_list.append(guild_group_t())
			buff = self.group_data_list[i].deserialize(buff)
		return buff

	def add_group_data_list():
		if len(group_data_list) >= MAX_GUILD_GROUP.value:
			return None
		group_data_list.append(guild_group_t())
		return group_data_list[len(group_data_list) - 1]

class cs_guild_group_create(proto):
	def __init__(self):
		self.session = session_t()
		self.name = cstring()
		self.len_of_user_list = cuint16()
		self.user_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		buff, buff_len = self.len_of_user_list.serialize(buff, buff_len)
		for i in range(self.len_of_user_list.value):
			buff, buff_len = self.user_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.name.deserialize(buff)
		buff = self.len_of_user_list.deserialize(buff)
		self.user_list = []
		for i in range(self.len_of_user_list.value):
			self.user_list.append(cint64())
			buff = self.user_list[i].deserialize(buff)
		return buff

	def add_user_list():
		if len(user_list) >= MAX_GUILD_GROUP_MEMBER.value:
			return None
		user_list.append(ccint64())
		return user_list[len(user_list) - 1]

class sc_guild_group_create(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_group_data_list = cuint16()
		self.group_data_list = []
		self.free_group = guild_group_info()
		self.my_group = my_group_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_group_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_group_data_list.value):
			buff, buff_len = self.group_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.free_group.serialize(buff, buff_len)
		buff, buff_len = self.my_group.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_group_data_list.deserialize(buff)
		self.group_data_list = []
		for i in range(self.len_of_group_data_list.value):
			self.group_data_list.append(guild_group_t())
			buff = self.group_data_list[i].deserialize(buff)
		buff = self.free_group.deserialize(buff)
		buff = self.my_group.deserialize(buff)
		return buff

	def add_group_data_list():
		if len(group_data_list) >= MAX_GUILD_GROUP.value:
			return None
		group_data_list.append(guild_group_t())
		return group_data_list[len(group_data_list) - 1]

class cs_guild_group_del(proto):
	def __init__(self):
		self.session = session_t()
		self.group_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.group_id.deserialize(buff)
		return buff

class sc_guild_group_del(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.group_id = cint64()
		self.len_of_group_data_list = cuint16()
		self.group_data_list = []
		self.free_group = guild_group_info()
		self.my_group = my_group_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_group_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_group_data_list.value):
			buff, buff_len = self.group_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.free_group.serialize(buff, buff_len)
		buff, buff_len = self.my_group.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.group_id.deserialize(buff)
		buff = self.len_of_group_data_list.deserialize(buff)
		self.group_data_list = []
		for i in range(self.len_of_group_data_list.value):
			self.group_data_list.append(guild_group_t())
			buff = self.group_data_list[i].deserialize(buff)
		buff = self.free_group.deserialize(buff)
		buff = self.my_group.deserialize(buff)
		return buff

	def add_group_data_list():
		if len(group_data_list) >= MAX_GUILD_GROUP.value:
			return None
		group_data_list.append(guild_group_t())
		return group_data_list[len(group_data_list) - 1]

class cs_guild_group_add(proto):
	def __init__(self):
		self.session = session_t()
		self.group_id = cint64()
		self.len_of_user_list = cuint16()
		self.user_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_user_list.serialize(buff, buff_len)
		for i in range(self.len_of_user_list.value):
			buff, buff_len = self.user_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.group_id.deserialize(buff)
		buff = self.len_of_user_list.deserialize(buff)
		self.user_list = []
		for i in range(self.len_of_user_list.value):
			self.user_list.append(cint64())
			buff = self.user_list[i].deserialize(buff)
		return buff

	def add_user_list():
		if len(user_list) >= MAX_GUILD_GROUP_MEMBER.value:
			return None
		user_list.append(ccint64())
		return user_list[len(user_list) - 1]

class sc_guild_group_add(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.free_group = guild_group_info()
		self.group_data = guild_group_info()
		self.len_of_group_data_list = cuint16()
		self.group_data_list = []
		self.my_group = my_group_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.free_group.serialize(buff, buff_len)
		buff, buff_len = self.group_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_group_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_group_data_list.value):
			buff, buff_len = self.group_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.my_group.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.free_group.deserialize(buff)
		buff = self.group_data.deserialize(buff)
		buff = self.len_of_group_data_list.deserialize(buff)
		self.group_data_list = []
		for i in range(self.len_of_group_data_list.value):
			self.group_data_list.append(guild_group_t())
			buff = self.group_data_list[i].deserialize(buff)
		buff = self.my_group.deserialize(buff)
		return buff

	def add_group_data_list():
		if len(group_data_list) >= MAX_GUILD_GROUP.value:
			return None
		group_data_list.append(guild_group_t())
		return group_data_list[len(group_data_list) - 1]

class cs_guild_group_remove(proto):
	def __init__(self):
		self.session = session_t()
		self.group_id = cint64()
		self.len_of_user_list = cuint16()
		self.user_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_user_list.serialize(buff, buff_len)
		for i in range(self.len_of_user_list.value):
			buff, buff_len = self.user_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.group_id.deserialize(buff)
		buff = self.len_of_user_list.deserialize(buff)
		self.user_list = []
		for i in range(self.len_of_user_list.value):
			self.user_list.append(cint64())
			buff = self.user_list[i].deserialize(buff)
		return buff

	def add_user_list():
		if len(user_list) >= MAX_GUILD_GROUP_MEMBER.value:
			return None
		user_list.append(ccint64())
		return user_list[len(user_list) - 1]

class sc_guild_group_remove(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.group_id = cint64()
		self.free_group = guild_group_info()
		self.group_data = guild_group_info()
		self.len_of_group_data_list = cuint16()
		self.group_data_list = []
		self.my_group = my_group_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		buff, buff_len = self.free_group.serialize(buff, buff_len)
		buff, buff_len = self.group_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_group_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_group_data_list.value):
			buff, buff_len = self.group_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.my_group.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.group_id.deserialize(buff)
		buff = self.free_group.deserialize(buff)
		buff = self.group_data.deserialize(buff)
		buff = self.len_of_group_data_list.deserialize(buff)
		self.group_data_list = []
		for i in range(self.len_of_group_data_list.value):
			self.group_data_list.append(guild_group_t())
			buff = self.group_data_list[i].deserialize(buff)
		buff = self.my_group.deserialize(buff)
		return buff

	def add_group_data_list():
		if len(group_data_list) >= MAX_GUILD_GROUP.value:
			return None
		group_data_list.append(guild_group_t())
		return group_data_list[len(group_data_list) - 1]

class cs_guild_group_leader(proto):
	def __init__(self):
		self.session = session_t()
		self.group_id = cint64()
		self.leader_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		buff, buff_len = self.leader_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.group_id.deserialize(buff)
		buff = self.leader_id.deserialize(buff)
		return buff

class sc_guild_group_leader(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.free_group = guild_group_info()
		self.len_of_group_data_list = cuint16()
		self.group_data_list = []
		self.my_group = my_group_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.free_group.serialize(buff, buff_len)
		buff, buff_len = self.len_of_group_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_group_data_list.value):
			buff, buff_len = self.group_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.my_group.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.free_group.deserialize(buff)
		buff = self.len_of_group_data_list.deserialize(buff)
		self.group_data_list = []
		for i in range(self.len_of_group_data_list.value):
			self.group_data_list.append(guild_group_t())
			buff = self.group_data_list[i].deserialize(buff)
		buff = self.my_group.deserialize(buff)
		return buff

	def add_group_data_list():
		if len(group_data_list) >= MAX_GUILD_GROUP.value:
			return None
		group_data_list.append(guild_group_t())
		return group_data_list[len(group_data_list) - 1]

class cchat_herat_beat(proto):
	def __init__(self):
		pass
	def serialize(self, buff, buff_len):
		return buff, buff_len

	def deserialize(self, buff):
		return buff

class chatc_herat_beat(proto):
	def __init__(self):
		pass
	def serialize(self, buff, buff_len):
		return buff, buff_len

	def deserialize(self, buff):
		return buff

class cs_get_sign_config(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_sign_config(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.sign_day = cint32()
		self.sign_time = cint32()
		self.len_of_sign_data_list = cuint16()
		self.sign_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.sign_day.serialize(buff, buff_len)
		buff, buff_len = self.sign_time.serialize(buff, buff_len)
		buff, buff_len = self.len_of_sign_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_sign_data_list.value):
			buff, buff_len = self.sign_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.sign_day.deserialize(buff)
		buff = self.sign_time.deserialize(buff)
		buff = self.len_of_sign_data_list.deserialize(buff)
		self.sign_data_list = []
		for i in range(self.len_of_sign_data_list.value):
			self.sign_data_list.append(sign_data_t())
			buff = self.sign_data_list[i].deserialize(buff)
		return buff

	def add_sign_data_list():
		if len(sign_data_list) >= MAX_SIGN_DAY.value:
			return None
		sign_data_list.append(sign_data_t())
		return sign_data_list[len(sign_data_list) - 1]

class cs_sign(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_sign(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.sign_day = cint32()
		self.sign_time = cint32()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.sign_day.serialize(buff, buff_len)
		buff, buff_len = self.sign_time.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.sign_day.deserialize(buff)
		buff = self.sign_time.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

class cs_get_active_open(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_active_open(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.sever_open_time = cint32()
		self.user_create_time = cint32()
		self.len_of_active_open_data_list = cuint16()
		self.active_open_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.sever_open_time.serialize(buff, buff_len)
		buff, buff_len = self.user_create_time.serialize(buff, buff_len)
		buff, buff_len = self.len_of_active_open_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_active_open_data_list.value):
			buff, buff_len = self.active_open_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.sever_open_time.deserialize(buff)
		buff = self.user_create_time.deserialize(buff)
		buff = self.len_of_active_open_data_list.deserialize(buff)
		self.active_open_data_list = []
		for i in range(self.len_of_active_open_data_list.value):
			self.active_open_data_list.append(activity_status())
			buff = self.active_open_data_list[i].deserialize(buff)
		return buff

	def add_active_open_data_list():
		if len(active_open_data_list) >= MAX_ACTIVE_OPEN.value:
			return None
		active_open_data_list.append(activity_status())
		return active_open_data_list[len(active_open_data_list) - 1]

class cs_get_activity_detail(proto):
	def __init__(self):
		self.session = session_t()
		self.activityid = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.activityid.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.activityid.deserialize(buff)
		return buff

class sc_get_activity_detail(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.activityid = cint32()
		self.times = cint32()
		self.len_of_activity_data_list = cuint16()
		self.activity_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.activityid.serialize(buff, buff_len)
		buff, buff_len = self.times.serialize(buff, buff_len)
		buff, buff_len = self.len_of_activity_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_activity_data_list.value):
			buff, buff_len = self.activity_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.activityid.deserialize(buff)
		buff = self.times.deserialize(buff)
		buff = self.len_of_activity_data_list.deserialize(buff)
		self.activity_data_list = []
		for i in range(self.len_of_activity_data_list.value):
			self.activity_data_list.append(activity_data_t())
			buff = self.activity_data_list[i].deserialize(buff)
		return buff

	def add_activity_data_list():
		if len(activity_data_list) >= MAX_ACTIVE_DAY.value:
			return None
		activity_data_list.append(activity_data_t())
		return activity_data_list[len(activity_data_list) - 1]

class cs_get_activity_reward(proto):
	def __init__(self):
		self.session = session_t()
		self.activityid = cint32()
		self.itemid = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.activityid.serialize(buff, buff_len)
		buff, buff_len = self.itemid.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.activityid.deserialize(buff)
		buff = self.itemid.deserialize(buff)
		return buff

class sc_get_activity_reward(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.activityid = cint32()
		self.len_of_activity_data_list = cuint16()
		self.activity_data_list = []
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.activityid.serialize(buff, buff_len)
		buff, buff_len = self.len_of_activity_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_activity_data_list.value):
			buff, buff_len = self.activity_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.activityid.deserialize(buff)
		buff = self.len_of_activity_data_list.deserialize(buff)
		self.activity_data_list = []
		for i in range(self.len_of_activity_data_list.value):
			self.activity_data_list.append(activity_data_t())
			buff = self.activity_data_list[i].deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

	def add_activity_data_list():
		if len(activity_data_list) >= MAX_ACTIVE_DAY.value:
			return None
		activity_data_list.append(activity_data_t())
		return activity_data_list[len(activity_data_list) - 1]

class schat_login(proto):
	def __init__(self):
		self.user_id = cint64()
		self.guild_id = cint64()
		self.token = cint32()
		self.nick_name = cstring()
		self.guild_name = cstring()
		self.group_name = cstring()
		self.open_id = cstring()
		self.state = cint32()
		self.position = cint32()
		self.language = cint32()
		self.server_serial_number = cint32()
		self.len_of_channel_list = cuint16()
		self.channel_list = []
		self.title = cint32()
		self.forbid_time = cint32()
		self.os_version = cstring()
		self.ip = cstring()
		self.version_code = cstring()
		self.did = cstring()
		self.iid = cstring()
		self.channel = cstring()
		self.device_platform = cstring()
		self.device_type = cstring()
		self.channel_op = cstring()
		self.head_entry = cint32()
		self.head_type = cint32()
		self.head_url = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.token.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		buff, buff_len = self.guild_name.serialize(buff, buff_len)
		buff, buff_len = self.group_name.serialize(buff, buff_len)
		buff, buff_len = self.open_id.serialize(buff, buff_len)
		buff, buff_len = self.state.serialize(buff, buff_len)
		buff, buff_len = self.position.serialize(buff, buff_len)
		buff, buff_len = self.language.serialize(buff, buff_len)
		buff, buff_len = self.server_serial_number.serialize(buff, buff_len)
		buff, buff_len = self.len_of_channel_list.serialize(buff, buff_len)
		for i in range(self.len_of_channel_list.value):
			buff, buff_len = self.channel_list[i].serialize(buff, buff_len)
		buff, buff_len = self.title.serialize(buff, buff_len)
		buff, buff_len = self.forbid_time.serialize(buff, buff_len)
		buff, buff_len = self.os_version.serialize(buff, buff_len)
		buff, buff_len = self.ip.serialize(buff, buff_len)
		buff, buff_len = self.version_code.serialize(buff, buff_len)
		buff, buff_len = self.did.serialize(buff, buff_len)
		buff, buff_len = self.iid.serialize(buff, buff_len)
		buff, buff_len = self.channel.serialize(buff, buff_len)
		buff, buff_len = self.device_platform.serialize(buff, buff_len)
		buff, buff_len = self.device_type.serialize(buff, buff_len)
		buff, buff_len = self.channel_op.serialize(buff, buff_len)
		buff, buff_len = self.head_entry.serialize(buff, buff_len)
		buff, buff_len = self.head_type.serialize(buff, buff_len)
		buff, buff_len = self.head_url.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_id.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		buff = self.token.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		buff = self.guild_name.deserialize(buff)
		buff = self.group_name.deserialize(buff)
		buff = self.open_id.deserialize(buff)
		buff = self.state.deserialize(buff)
		buff = self.position.deserialize(buff)
		buff = self.language.deserialize(buff)
		buff = self.server_serial_number.deserialize(buff)
		buff = self.len_of_channel_list.deserialize(buff)
		self.channel_list = []
		for i in range(self.len_of_channel_list.value):
			self.channel_list.append(chat_channel_t())
			buff = self.channel_list[i].deserialize(buff)
		buff = self.title.deserialize(buff)
		buff = self.forbid_time.deserialize(buff)
		buff = self.os_version.deserialize(buff)
		buff = self.ip.deserialize(buff)
		buff = self.version_code.deserialize(buff)
		buff = self.did.deserialize(buff)
		buff = self.iid.deserialize(buff)
		buff = self.channel.deserialize(buff)
		buff = self.device_platform.deserialize(buff)
		buff = self.device_type.deserialize(buff)
		buff = self.channel_op.deserialize(buff)
		buff = self.head_entry.deserialize(buff)
		buff = self.head_type.deserialize(buff)
		buff = self.head_url.deserialize(buff)
		return buff

	def add_channel_list():
		if len(channel_list) >= MAX_CHAT_CHANNEL_NUM.value:
			return None
		channel_list.append(chat_channel_t())
		return channel_list[len(channel_list) - 1]

class chats_login(proto):
	def __init__(self):
		self.result = e_op_result()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.result.deserialize(buff)
		return buff

class cs_get_user_force_rank(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_user_force_rank(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_data = cuint16()
		self.data = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_data.serialize(buff, buff_len)
		for i in range(self.len_of_data.value):
			buff, buff_len = self.data[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_data.deserialize(buff)
		self.data = []
		for i in range(self.len_of_data.value):
			self.data.append(force_rank_t())
			buff = self.data[i].deserialize(buff)
		return buff

	def add_data():
		if len(data) >= MAX_FORCE_RANK.value:
			return None
		data.append(force_rank_t())
		return data[len(data) - 1]

class cs_get_guild_force_rank(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_guild_force_rank(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_data = cuint16()
		self.data = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_data.serialize(buff, buff_len)
		for i in range(self.len_of_data.value):
			buff, buff_len = self.data[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_data.deserialize(buff)
		self.data = []
		for i in range(self.len_of_data.value):
			self.data.append(guild_brief_t())
			buff = self.data[i].deserialize(buff)
		return buff

	def add_data():
		if len(data) >= MAX_GUILD_RANK.value:
			return None
		data.append(guild_brief_t())
		return data[len(data) - 1]

class cs_get_user_war_rank(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_user_war_rank(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_data = cuint16()
		self.data = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_data.serialize(buff, buff_len)
		for i in range(self.len_of_data.value):
			buff, buff_len = self.data[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_data.deserialize(buff)
		self.data = []
		for i in range(self.len_of_data.value):
			self.data.append(war_rank_t())
			buff = self.data[i].deserialize(buff)
		return buff

	def add_data():
		if len(data) >= MAX_WAR_RANK.value:
			return None
		data.append(war_rank_t())
		return data[len(data) - 1]

class cs_get_invest_info(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_invest_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.invest_info = invest_info_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.invest_info.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.invest_info.deserialize(buff)
		return buff

class cs_draw_invest_refund(proto):
	def __init__(self):
		self.session = session_t()
		self.draw_day = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.draw_day.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.draw_day.deserialize(buff)
		return buff

class sc_draw_invest_refund(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.draw_day = cint32()
		self.invest_info = invest_info_t()
		self.user_res = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.draw_day.serialize(buff, buff_len)
		buff, buff_len = self.invest_info.serialize(buff, buff_len)
		buff, buff_len = self.user_res.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.draw_day.deserialize(buff)
		buff = self.invest_info.deserialize(buff)
		buff = self.user_res.deserialize(buff)
		return buff

class cs_invest(proto):
	def __init__(self):
		self.session = session_t()
		self.invest_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.invest_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.invest_entry.deserialize(buff)
		return buff

class sc_invest(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.invest_info = invest_info_t()
		self.user_res = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.invest_info.serialize(buff, buff_len)
		buff, buff_len = self.user_res.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.invest_info.deserialize(buff)
		buff = self.user_res.deserialize(buff)
		return buff

class cchat_chat(proto):
	def __init__(self):
		self.session = session_t()
		self.channel_id = cint64()
		self.chat_content = cstring()
		self.content_type = E_CHAT_CONTENT_TYPE()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		buff, buff_len = self.chat_content.serialize(buff, buff_len)
		buff, buff_len = self.content_type.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.channel_id.deserialize(buff)
		buff = self.chat_content.deserialize(buff)
		buff = self.content_type.deserialize(buff)
		return buff

class chatc_chat(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_chat_data_list = cuint16()
		self.chat_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_chat_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_chat_data_list.value):
			buff, buff_len = self.chat_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_chat_data_list.deserialize(buff)
		self.chat_data_list = []
		for i in range(self.len_of_chat_data_list.value):
			self.chat_data_list.append(chat_data_t())
			buff = self.chat_data_list[i].deserialize(buff)
		return buff

	def add_chat_data_list():
		if len(chat_data_list) >= MAX_CHAT_MSG_NUM.value:
			return None
		chat_data_list.append(chat_data_t())
		return chat_data_list[len(chat_data_list) - 1]

class cs_get_liveness_info(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_liveness_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.liveness_info = liveness_info_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.liveness_info.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.liveness_info.deserialize(buff)
		return buff

class cs_draw_liveness_reward(proto):
	def __init__(self):
		self.session = session_t()
		self.draw_point = cint32()
		self.item_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.draw_point.serialize(buff, buff_len)
		buff, buff_len = self.item_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.draw_point.deserialize(buff)
		buff = self.item_id.deserialize(buff)
		return buff

class sc_draw_liveness_reward(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.draw_point = cint32()
		self.liveness_info = liveness_info_t()
		self.rewards = rewards_t()
		self.user_res = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.draw_point.serialize(buff, buff_len)
		buff, buff_len = self.liveness_info.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.user_res.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.draw_point.deserialize(buff)
		buff = self.liveness_info.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.user_res.deserialize(buff)
		return buff

class schat_forward(proto):
	def __init__(self):
		self.user_id = cint64()
		self.server_serial_number = cint32()
		self.msg_content = cbigstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.server_serial_number.serialize(buff, buff_len)
		buff, buff_len = self.msg_content.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_id.deserialize(buff)
		buff = self.server_serial_number.deserialize(buff)
		buff = self.msg_content.deserialize(buff)
		return buff

class chats_forward(proto):
	def __init__(self):
		self.result = e_op_result()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.result.deserialize(buff)
		return buff

class cs_get_mail_head_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_mail_head_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_mail_head_list = cuint16()
		self.mail_head_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mail_head_list.serialize(buff, buff_len)
		for i in range(self.len_of_mail_head_list.value):
			buff, buff_len = self.mail_head_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_mail_head_list.deserialize(buff)
		self.mail_head_list = []
		for i in range(self.len_of_mail_head_list.value):
			self.mail_head_list.append(mail_head_t())
			buff = self.mail_head_list[i].deserialize(buff)
		return buff

	def add_mail_head_list():
		if len(mail_head_list) >= MAX_MAIL_COUNT.value:
			return None
		mail_head_list.append(mail_head_t())
		return mail_head_list[len(mail_head_list) - 1]

class cs_get_mail_body_list(proto):
	def __init__(self):
		self.session = session_t()
		self.len_of_mail_id_list = cuint16()
		self.mail_id_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mail_id_list.serialize(buff, buff_len)
		for i in range(self.len_of_mail_id_list.value):
			buff, buff_len = self.mail_id_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.len_of_mail_id_list.deserialize(buff)
		self.mail_id_list = []
		for i in range(self.len_of_mail_id_list.value):
			self.mail_id_list.append(cint64())
			buff = self.mail_id_list[i].deserialize(buff)
		return buff

	def add_mail_id_list():
		if len(mail_id_list) >= MAX_MAIL_COUNT.value:
			return None
		mail_id_list.append(ccint64())
		return mail_id_list[len(mail_id_list) - 1]

class sc_get_mail_body_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_mail_body_list = cuint16()
		self.mail_body_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mail_body_list.serialize(buff, buff_len)
		for i in range(self.len_of_mail_body_list.value):
			buff, buff_len = self.mail_body_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_mail_body_list.deserialize(buff)
		self.mail_body_list = []
		for i in range(self.len_of_mail_body_list.value):
			self.mail_body_list.append(mail_body_t())
			buff = self.mail_body_list[i].deserialize(buff)
		return buff

	def add_mail_body_list():
		if len(mail_body_list) >= MAX_MAIL_COUNT.value:
			return None
		mail_body_list.append(mail_body_t())
		return mail_body_list[len(mail_body_list) - 1]

class cs_mail_send(proto):
	def __init__(self):
		self.session = session_t()
		self.e_mail_type = E_MAIL_TYPE()
		self.recver_id = cint64()
		self.recver_nick_name = cstring()
		self.title = cstring()
		self.content = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.e_mail_type.serialize(buff, buff_len)
		buff, buff_len = self.recver_id.serialize(buff, buff_len)
		buff, buff_len = self.recver_nick_name.serialize(buff, buff_len)
		buff, buff_len = self.title.serialize(buff, buff_len)
		buff, buff_len = self.content.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.e_mail_type.deserialize(buff)
		buff = self.recver_id.deserialize(buff)
		buff = self.recver_nick_name.deserialize(buff)
		buff = self.title.deserialize(buff)
		buff = self.content.deserialize(buff)
		return buff

class sc_mail_send(proto):
	def __init__(self):
		self.common_result = common_result_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		return buff

class cs_mail_affix_pick(proto):
	def __init__(self):
		self.session = session_t()
		self.mail_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.mail_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.mail_id.deserialize(buff)
		return buff

class sc_mail_affix_pick(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.mail_body = mail_body_t()
		self.rewards = rewards_t()
		self.user_res = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.mail_body.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.user_res.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.mail_body.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.user_res.deserialize(buff)
		return buff

class schat_add_channel(proto):
	def __init__(self):
		self.channel_id = cint64()
		self.channel_type = E_CHAT_CHANNEL_TYPE()
		self.len_of_channel_list = cuint16()
		self.channel_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		buff, buff_len = self.channel_type.serialize(buff, buff_len)
		buff, buff_len = self.len_of_channel_list.serialize(buff, buff_len)
		for i in range(self.len_of_channel_list.value):
			buff, buff_len = self.channel_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.channel_id.deserialize(buff)
		buff = self.channel_type.deserialize(buff)
		buff = self.len_of_channel_list.deserialize(buff)
		self.channel_list = []
		for i in range(self.len_of_channel_list.value):
			self.channel_list.append(cint64())
			buff = self.channel_list[i].deserialize(buff)
		return buff

	def add_channel_list():
		if len(channel_list) >= MAX_CHAT_CHANNEL_MEMBER_NUM.value:
			return None
		channel_list.append(ccint64())
		return channel_list[len(channel_list) - 1]

class chats_add_channel(proto):
	def __init__(self):
		self.result = e_op_result()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.result.deserialize(buff)
		return buff

class schat_del_channel(proto):
	def __init__(self):
		self.channel_id = cint64()
		self.channel_type = E_CHAT_CHANNEL_TYPE()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		buff, buff_len = self.channel_type.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.channel_id.deserialize(buff)
		buff = self.channel_type.deserialize(buff)
		return buff

class chats_del_channel(proto):
	def __init__(self):
		self.result = e_op_result()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.result.deserialize(buff)
		return buff

class schat_join_channel(proto):
	def __init__(self):
		self.channel_id = cint64()
		self.channel_type = E_CHAT_CHANNEL_TYPE()
		self.len_of_channel_list = cuint16()
		self.channel_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		buff, buff_len = self.channel_type.serialize(buff, buff_len)
		buff, buff_len = self.len_of_channel_list.serialize(buff, buff_len)
		for i in range(self.len_of_channel_list.value):
			buff, buff_len = self.channel_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.channel_id.deserialize(buff)
		buff = self.channel_type.deserialize(buff)
		buff = self.len_of_channel_list.deserialize(buff)
		self.channel_list = []
		for i in range(self.len_of_channel_list.value):
			self.channel_list.append(cint64())
			buff = self.channel_list[i].deserialize(buff)
		return buff

	def add_channel_list():
		if len(channel_list) >= MAX_CHAT_CHANNEL_MEMBER_NUM.value:
			return None
		channel_list.append(ccint64())
		return channel_list[len(channel_list) - 1]

class chats_join_channel(proto):
	def __init__(self):
		self.result = e_op_result()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.result.deserialize(buff)
		return buff

class schat_quit_channel(proto):
	def __init__(self):
		self.user_id = cint64()
		self.channel_id = cint64()
		self.channel_type = E_CHAT_CHANNEL_TYPE()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		buff, buff_len = self.channel_type.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_id.deserialize(buff)
		buff = self.channel_id.deserialize(buff)
		buff = self.channel_type.deserialize(buff)
		return buff

class chats_quit_channel(proto):
	def __init__(self):
		self.result = e_op_result()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.result.deserialize(buff)
		return buff

class cs_req_user_detail(proto):
	def __init__(self):
		self.session = session_t()
		self.user_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		return buff

class sc_req_user_detail(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.detail = user_detail()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.detail.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.detail.deserialize(buff)
		return buff

class cs_req_guild_user_detail(proto):
	def __init__(self):
		self.session = session_t()
		self.guild_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		return buff

class sc_req_guild_user_detail(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.data = guild_t()
		self.len_of_city_list = cuint16()
		self.city_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_city_list.serialize(buff, buff_len)
		for i in range(self.len_of_city_list.value):
			buff, buff_len = self.city_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.data.deserialize(buff)
		buff = self.len_of_city_list.deserialize(buff)
		self.city_list = []
		for i in range(self.len_of_city_list.value):
			self.city_list.append(guild_city_t())
			buff = self.city_list[i].deserialize(buff)
		return buff

	def add_city_list():
		if len(city_list) >= MAX_GUILD_CITY_NUM.value:
			return None
		city_list.append(guild_city_t())
		return city_list[len(city_list) - 1]

class cs_guild_create_channel(proto):
	def __init__(self):
		self.session = session_t()
		self.channel_name = cstring()
		self.len_of_user_id_list = cuint16()
		self.user_id_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.channel_name.serialize(buff, buff_len)
		buff, buff_len = self.len_of_user_id_list.serialize(buff, buff_len)
		for i in range(self.len_of_user_id_list.value):
			buff, buff_len = self.user_id_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.channel_name.deserialize(buff)
		buff = self.len_of_user_id_list.deserialize(buff)
		self.user_id_list = []
		for i in range(self.len_of_user_id_list.value):
			self.user_id_list.append(cint64())
			buff = self.user_id_list[i].deserialize(buff)
		return buff

	def add_user_id_list():
		if len(user_id_list) >= MAX_CHAT_CHANNEL_MEMBER_NUM.value:
			return None
		user_id_list.append(ccint64())
		return user_id_list[len(user_id_list) - 1]

class sc_guild_create_channel(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.channel_data = chat_channel_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.channel_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.channel_data.deserialize(buff)
		return buff

class cs_guild_disolution_channel(proto):
	def __init__(self):
		self.session = session_t()
		self.channel_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.channel_id.deserialize(buff)
		return buff

class sc_guild_disolution_channel(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.channel_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.channel_id.deserialize(buff)
		return buff

class cs_guild_quit_channel(proto):
	def __init__(self):
		self.session = session_t()
		self.channel_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.channel_id.deserialize(buff)
		return buff

class sc_guild_quit_channel(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.channel_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.channel_id.deserialize(buff)
		return buff

class cs_guild_invite_join_channel(proto):
	def __init__(self):
		self.session = session_t()
		self.len_of_user_id_list = cuint16()
		self.user_id_list = []
		self.channel_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.len_of_user_id_list.serialize(buff, buff_len)
		for i in range(self.len_of_user_id_list.value):
			buff, buff_len = self.user_id_list[i].serialize(buff, buff_len)
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.len_of_user_id_list.deserialize(buff)
		self.user_id_list = []
		for i in range(self.len_of_user_id_list.value):
			self.user_id_list.append(cint64())
			buff = self.user_id_list[i].deserialize(buff)
		buff = self.channel_id.deserialize(buff)
		return buff

	def add_user_id_list():
		if len(user_id_list) >= MAX_CHAT_CHANNEL_MEMBER_NUM.value:
			return None
		user_id_list.append(ccint64())
		return user_id_list[len(user_id_list) - 1]

class sc_guild_invite_join_channel(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.channel_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.channel_id.deserialize(buff)
		return buff

class cs_req_guild_member(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_req_guild_member(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_guild_member_list = cuint16()
		self.guild_member_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_guild_member_list.serialize(buff, buff_len)
		for i in range(self.len_of_guild_member_list.value):
			buff, buff_len = self.guild_member_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_guild_member_list.deserialize(buff)
		self.guild_member_list = []
		for i in range(self.len_of_guild_member_list.value):
			self.guild_member_list.append(brief_guild_member())
			buff = self.guild_member_list[i].deserialize(buff)
		return buff

	def add_guild_member_list():
		if len(guild_member_list) >= MAX_GUILD_MEMBER.value:
			return None
		guild_member_list.append(brief_guild_member())
		return guild_member_list[len(guild_member_list) - 1]

class cs_guild_expel_channel(proto):
	def __init__(self):
		self.session = session_t()
		self.channel_id = cint64()
		self.len_of_user_id_list = cuint16()
		self.user_id_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_user_id_list.serialize(buff, buff_len)
		for i in range(self.len_of_user_id_list.value):
			buff, buff_len = self.user_id_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.channel_id.deserialize(buff)
		buff = self.len_of_user_id_list.deserialize(buff)
		self.user_id_list = []
		for i in range(self.len_of_user_id_list.value):
			self.user_id_list.append(cint64())
			buff = self.user_id_list[i].deserialize(buff)
		return buff

	def add_user_id_list():
		if len(user_id_list) >= MAX_CHAT_CHANNEL_MEMBER_NUM.value:
			return None
		user_id_list.append(ccint64())
		return user_id_list[len(user_id_list) - 1]

class sc_guild_expel_channel(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.channel_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.channel_id.deserialize(buff)
		return buff

class cs_guard_home(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_guard_home(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.data = user_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.data.deserialize(buff)
		return buff

class cs_guard_home_cancel(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_guard_home_cancel(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.data = user_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.data.deserialize(buff)
		return buff

class cs_world_chat(proto):
	def __init__(self):
		self.session = session_t()
		self.channel_id = cint64()
		self.content = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		buff, buff_len = self.content.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.channel_id.deserialize(buff)
		buff = self.content.deserialize(buff)
		return buff

class sc_world_chat(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.resources = user_resource_t()
		self.remain_world_chat_count = cint32()
		self.world_chat_cd_time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.remain_world_chat_count.serialize(buff, buff_len)
		buff, buff_len = self.world_chat_cd_time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.remain_world_chat_count.deserialize(buff)
		buff = self.world_chat_cd_time.deserialize(buff)
		return buff

class schat_world_chat(proto):
	def __init__(self):
		self.user_id = cint64()
		self.channel_id = cint64()
		self.content = cstring()
		self.content_type = E_CHAT_CONTENT_TYPE()
		self.channel_type = E_CHAT_CHANNEL_TYPE()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		buff, buff_len = self.content.serialize(buff, buff_len)
		buff, buff_len = self.content_type.serialize(buff, buff_len)
		buff, buff_len = self.channel_type.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_id.deserialize(buff)
		buff = self.channel_id.deserialize(buff)
		buff = self.content.deserialize(buff)
		buff = self.content_type.deserialize(buff)
		buff = self.channel_type.deserialize(buff)
		return buff

class chats_world_chat(proto):
	def __init__(self):
		self.result = e_op_result()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.result.deserialize(buff)
		return buff

class cchat_login(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class chatc_login(proto):
	def __init__(self):
		self.common_result = common_result_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		return buff

class cs_sync_user_event_flag(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_sync_user_event_flag(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_flag_list = cuint16()
		self.flag_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_flag_list.serialize(buff, buff_len)
		for i in range(self.len_of_flag_list.value):
			buff, buff_len = self.flag_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_flag_list.deserialize(buff)
		self.flag_list = []
		for i in range(self.len_of_flag_list.value):
			self.flag_list.append(cint32())
			buff = self.flag_list[i].deserialize(buff)
		return buff

	def add_flag_list():
		if len(flag_list) >= MAX_USER_FLAG_NUM.value:
			return None
		flag_list.append(ccint32())
		return flag_list[len(flag_list) - 1]

class cs_get_guild_member_brief(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_guild_member_brief(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.guild_member_data = guild_member_brief_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.guild_member_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.guild_member_data.deserialize(buff)
		return buff

class cs_hero_assign_junxian(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()
		self.junxian = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.junxian.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.junxian.deserialize(buff)
		return buff

class sc_hero_assign_junxian(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_data = hero_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		return buff

class cs_user_item(proto):
	def __init__(self):
		self.session = session_t()
		self.item_entry = cint32()
		self.use_num = cint32()
		self.slt_idx = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.use_num.serialize(buff, buff_len)
		buff, buff_len = self.slt_idx.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.use_num.deserialize(buff)
		buff = self.slt_idx.deserialize(buff)
		return buff

class sc_user_item(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.rewards = rewards_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []
		self.vip_lv = cint32()
		self.vip_point = cint32()
		self.vip_expire_time = cint32()
		self.resources = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.vip_lv.serialize(buff, buff_len)
		buff, buff_len = self.vip_point.serialize(buff, buff_len)
		buff, buff_len = self.vip_expire_time.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		buff = self.vip_lv.deserialize(buff)
		buff = self.vip_point.deserialize(buff)
		buff = self.vip_expire_time.deserialize(buff)
		buff = self.resources.deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_push_one_mail(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_push_one_mail(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.mail_head = mail_head_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.mail_head.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.mail_head.deserialize(buff)
		return buff

class cs_mail_read_set(proto):
	def __init__(self):
		self.session = session_t()
		self.len_of_mail_id_list = cuint16()
		self.mail_id_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mail_id_list.serialize(buff, buff_len)
		for i in range(self.len_of_mail_id_list.value):
			buff, buff_len = self.mail_id_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.len_of_mail_id_list.deserialize(buff)
		self.mail_id_list = []
		for i in range(self.len_of_mail_id_list.value):
			self.mail_id_list.append(cint64())
			buff = self.mail_id_list[i].deserialize(buff)
		return buff

	def add_mail_id_list():
		if len(mail_id_list) >= MAX_MAIL_COUNT.value:
			return None
		mail_id_list.append(ccint64())
		return mail_id_list[len(mail_id_list) - 1]

class sc_mail_read_set(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_mail_id_list = cuint16()
		self.mail_id_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mail_id_list.serialize(buff, buff_len)
		for i in range(self.len_of_mail_id_list.value):
			buff, buff_len = self.mail_id_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_mail_id_list.deserialize(buff)
		self.mail_id_list = []
		for i in range(self.len_of_mail_id_list.value):
			self.mail_id_list.append(cint64())
			buff = self.mail_id_list[i].deserialize(buff)
		return buff

	def add_mail_id_list():
		if len(mail_id_list) >= MAX_MAIL_COUNT.value:
			return None
		mail_id_list.append(ccint64())
		return mail_id_list[len(mail_id_list) - 1]

class cs_get_guild_battle_record_list(proto):
	def __init__(self):
		self.session = session_t()
		self.page = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.page.deserialize(buff)
		return buff

class sc_get_guild_battle_record_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.amount = cint32()
		self.page = cint32()
		self.len_of_brief_record = cuint16()
		self.brief_record = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.amount.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		buff, buff_len = self.len_of_brief_record.serialize(buff, buff_len)
		for i in range(self.len_of_brief_record.value):
			buff, buff_len = self.brief_record[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.amount.deserialize(buff)
		buff = self.page.deserialize(buff)
		buff = self.len_of_brief_record.deserialize(buff)
		self.brief_record = []
		for i in range(self.len_of_brief_record.value):
			self.brief_record.append(brief_battle_record())
			buff = self.brief_record[i].deserialize(buff)
		return buff

	def add_brief_record():
		if len(brief_record) >= MAX_BATTLE_RECORD_NUM.value:
			return None
		brief_record.append(brief_battle_record())
		return brief_record[len(brief_record) - 1]

class cs_get_no_read_mail_num(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_no_read_mail_num(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.no_read_mail_num = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.no_read_mail_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.no_read_mail_num.deserialize(buff)
		return buff

class schat_sys_info(proto):
	def __init__(self):
		self.user_id = cint64()
		self.channel_id = cint64()
		self.content = cstring()
		self.content_type = E_CHAT_CONTENT_TYPE()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		buff, buff_len = self.content.serialize(buff, buff_len)
		buff, buff_len = self.content_type.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_id.deserialize(buff)
		buff = self.channel_id.deserialize(buff)
		buff = self.content.deserialize(buff)
		buff = self.content_type.deserialize(buff)
		return buff

class chats_sys_info(proto):
	def __init__(self):
		self.result = e_op_result()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.result.deserialize(buff)
		return buff

class cs_sell_item(proto):
	def __init__(self):
		self.session = session_t()
		self.item_entry = cint32()
		self.sell_num = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.sell_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.sell_num.deserialize(buff)
		return buff

class sc_sell_item(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []
		self.resources = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		buff = self.resources.deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_get_fanjiqing(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_fanjiqing(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.resource_icr = user_resource_increase_t()
		self.resource_dec = user_resource_increase_t()
		self.resource_out_icr = user_resource_increase_t()
		self.guild_lv = cint32()
		self.len_of_city_list = cuint16()
		self.city_list = []
		self.len_of_effect_list = cuint16()
		self.effect_list = []
		self.resource_miracle = user_resource_increase_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.resource_icr.serialize(buff, buff_len)
		buff, buff_len = self.resource_dec.serialize(buff, buff_len)
		buff, buff_len = self.resource_out_icr.serialize(buff, buff_len)
		buff, buff_len = self.guild_lv.serialize(buff, buff_len)
		buff, buff_len = self.len_of_city_list.serialize(buff, buff_len)
		for i in range(self.len_of_city_list.value):
			buff, buff_len = self.city_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_effect_list.serialize(buff, buff_len)
		for i in range(self.len_of_effect_list.value):
			buff, buff_len = self.effect_list[i].serialize(buff, buff_len)
		buff, buff_len = self.resource_miracle.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.resource_icr.deserialize(buff)
		buff = self.resource_dec.deserialize(buff)
		buff = self.resource_out_icr.deserialize(buff)
		buff = self.guild_lv.deserialize(buff)
		buff = self.len_of_city_list.deserialize(buff)
		self.city_list = []
		for i in range(self.len_of_city_list.value):
			self.city_list.append(guild_city_t())
			buff = self.city_list[i].deserialize(buff)
		buff = self.len_of_effect_list.deserialize(buff)
		self.effect_list = []
		for i in range(self.len_of_effect_list.value):
			self.effect_list.append(effect_t())
			buff = self.effect_list[i].deserialize(buff)
		buff = self.resource_miracle.deserialize(buff)
		return buff

	def add_city_list():
		if len(city_list) >= MAX_GUILD_CITY_NUM.value:
			return None
		city_list.append(guild_city_t())
		return city_list[len(city_list) - 1]

	def add_effect_list():
		if len(effect_list) >= e_effect_type_global_max.value:
			return None
		effect_list.append(effect_t())
		return effect_list[len(effect_list) - 1]

class cs_get_my_blocks(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_my_blocks(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_block_data_list = cuint16()
		self.block_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_block_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_block_data_list.value):
			buff, buff_len = self.block_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_block_data_list.deserialize(buff)
		self.block_data_list = []
		for i in range(self.len_of_block_data_list.value):
			self.block_data_list.append(block_brief_data_t())
			buff = self.block_data_list[i].deserialize(buff)
		return buff

	def add_block_data_list():
		if len(block_data_list) >= MAX_GET_LAND_NUM.value:
			return None
		block_data_list.append(block_brief_data_t())
		return block_data_list[len(block_data_list) - 1]

class cs_change_defend_hero(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()
		self.defend_hero_entry = cint32()
		self.change_pos = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.defend_hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.change_pos.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.defend_hero_entry.deserialize(buff)
		buff = self.change_pos.deserialize(buff)
		return buff

class sc_change_defend_hero(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.castle_id = cint64()
		self.defend_hero_entry = cint32()
		self.change_pos = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.defend_hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.change_pos.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.defend_hero_entry.deserialize(buff)
		buff = self.change_pos.deserialize(buff)
		return buff

class cs_get_building_lv(proto):
	def __init__(self):
		self.session = session_t()
		self.entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.entry.deserialize(buff)
		return buff

class sc_get_building_lv(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.entry = cint32()
		self.len_of_building_data_list = cuint16()
		self.building_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_building_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_building_data_list.value):
			buff, buff_len = self.building_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.entry.deserialize(buff)
		buff = self.len_of_building_data_list.deserialize(buff)
		self.building_data_list = []
		for i in range(self.len_of_building_data_list.value):
			self.building_data_list.append(building_date_t())
			buff = self.building_data_list[i].deserialize(buff)
		return buff

	def add_building_data_list():
		if len(building_data_list) >= MAX_BUILDING_COUNT.value:
			return None
		building_data_list.append(building_date_t())
		return building_data_list[len(building_data_list) - 1]

class cs_accelerate_block_building_lvup(proto):
	def __init__(self):
		self.session = session_t()
		self.block_id = cint32()
		self.item_entry = cint32()
		self.item_num = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.item_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.item_num.deserialize(buff)
		return buff

class sc_accelerate_block_building_lvup(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.block_id = cint32()
		self.item_entry = cint32()
		self.item_num = cint32()
		self.event_data = game_event_data_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.item_num.serialize(buff, buff_len)
		buff, buff_len = self.event_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.item_num.deserialize(buff)
		buff = self.event_data.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_get_nobility_entry(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_nobility_entry(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.nobility_entry = cint32()
		self.kill_point = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.nobility_entry.serialize(buff, buff_len)
		buff, buff_len = self.kill_point.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.nobility_entry.deserialize(buff)
		buff = self.kill_point.deserialize(buff)
		return buff

class cs_silver_coin_lottery_draw(proto):
	def __init__(self):
		self.session = session_t()
		self.draw_type = cint32()
		self.draw_count = cint32()
		self.lottery_ticket_item_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.draw_type.serialize(buff, buff_len)
		buff, buff_len = self.draw_count.serialize(buff, buff_len)
		buff, buff_len = self.lottery_ticket_item_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.draw_type.deserialize(buff)
		buff = self.draw_count.deserialize(buff)
		buff = self.lottery_ticket_item_id.deserialize(buff)
		return buff

class sc_silver_coin_lottery_draw(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.draw_type = cint32()
		self.resources = user_resource_t()
		self.rewards = rewards_t()
		self.free_gold_lottery_surplus_time = cint32()
		self.surplus_lottery_hit_count = cint32()
		self.len_of_lottery_reward_list = cuint16()
		self.lottery_reward_list = []
		self.gold_5_draw = cint32()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []
		self.timed_super_id = cint32()
		self.item_data = item_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.draw_type.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.free_gold_lottery_surplus_time.serialize(buff, buff_len)
		buff, buff_len = self.surplus_lottery_hit_count.serialize(buff, buff_len)
		buff, buff_len = self.len_of_lottery_reward_list.serialize(buff, buff_len)
		for i in range(self.len_of_lottery_reward_list.value):
			buff, buff_len = self.lottery_reward_list[i].serialize(buff, buff_len)
		buff, buff_len = self.gold_5_draw.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.timed_super_id.serialize(buff, buff_len)
		buff, buff_len = self.item_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.draw_type.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.free_gold_lottery_surplus_time.deserialize(buff)
		buff = self.surplus_lottery_hit_count.deserialize(buff)
		buff = self.len_of_lottery_reward_list.deserialize(buff)
		self.lottery_reward_list = []
		for i in range(self.len_of_lottery_reward_list.value):
			self.lottery_reward_list.append(reward_info_t())
			buff = self.lottery_reward_list[i].deserialize(buff)
		buff = self.gold_5_draw.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		buff = self.timed_super_id.deserialize(buff)
		buff = self.item_data.deserialize(buff)
		return buff

	def add_lottery_reward_list():
		if len(lottery_reward_list) >= MAX_LOTTERY_REWARD_NUM.value:
			return None
		lottery_reward_list.append(reward_info_t())
		return lottery_reward_list[len(lottery_reward_list) - 1]

	def add_item_data_list():
		if len(item_data_list) >= MAX_PRESENT_ITEM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_broadcast_msg(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_broadcast_msg(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.e_broadcast_type = E_BROADCAST_TYPE()
		self.str_0 = cstring()
		self.param_0 = cint32()
		self.param_1 = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.e_broadcast_type.serialize(buff, buff_len)
		buff, buff_len = self.str_0.serialize(buff, buff_len)
		buff, buff_len = self.param_0.serialize(buff, buff_len)
		buff, buff_len = self.param_1.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.e_broadcast_type.deserialize(buff)
		buff = self.str_0.deserialize(buff)
		buff = self.param_0.deserialize(buff)
		buff = self.param_1.deserialize(buff)
		return buff

class cs_get_newbie_step(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_newbie_step(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.newbie_step = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.newbie_step.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.newbie_step.deserialize(buff)
		return buff

class cs_set_newbie_step(proto):
	def __init__(self):
		self.session = session_t()
		self.newbie_step = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.newbie_step.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.newbie_step.deserialize(buff)
		return buff

class sc_set_newbie_step(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.newbie_step = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.newbie_step.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.newbie_step.deserialize(buff)
		return buff

class cs_get_world_cities(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_world_cities(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_block_data_list = cuint16()
		self.block_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_block_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_block_data_list.value):
			buff, buff_len = self.block_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_block_data_list.deserialize(buff)
		self.block_data_list = []
		for i in range(self.len_of_block_data_list.value):
			self.block_data_list.append(block_brief_data_t())
			buff = self.block_data_list[i].deserialize(buff)
		return buff

	def add_block_data_list():
		if len(block_data_list) >= MAX_GET_LAND_NUM.value:
			return None
		block_data_list.append(block_brief_data_t())
		return block_data_list[len(block_data_list) - 1]

class cs_get_state_cities(proto):
	def __init__(self):
		self.session = session_t()
		self.state_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.state_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.state_entry.deserialize(buff)
		return buff

class sc_get_state_cities(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.state_entry = cint32()
		self.len_of_block_data_list = cuint16()
		self.block_data_list = []
		self.len_of_points = cuint16()
		self.points = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.state_entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_block_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_block_data_list.value):
			buff, buff_len = self.block_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_points.serialize(buff, buff_len)
		for i in range(self.len_of_points.value):
			buff, buff_len = self.points[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.state_entry.deserialize(buff)
		buff = self.len_of_block_data_list.deserialize(buff)
		self.block_data_list = []
		for i in range(self.len_of_block_data_list.value):
			self.block_data_list.append(block_brief_data_t())
			buff = self.block_data_list[i].deserialize(buff)
		buff = self.len_of_points.deserialize(buff)
		self.points = []
		for i in range(self.len_of_points.value):
			self.points.append(ally_castle())
			buff = self.points[i].deserialize(buff)
		return buff

	def add_block_data_list():
		if len(block_data_list) >= MAX_MAP_CITY_NUM.value:
			return None
		block_data_list.append(block_brief_data_t())
		return block_data_list[len(block_data_list) - 1]

	def add_points():
		if len(points) >= MAX_GUILD_MEMBER.value:
			return None
		points.append(ally_castle())
		return points[len(points) - 1]

class cs_get_season_data(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_season_data(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_season_data = season_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_season_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_season_data.deserialize(buff)
		return buff

class cs_buy_season_reward(proto):
	def __init__(self):
		self.session = session_t()
		self.item_entry = cint32()
		self.price = cint32()
		self.currency_type = cint32()
		self.buy_num = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.price.serialize(buff, buff_len)
		buff, buff_len = self.currency_type.serialize(buff, buff_len)
		buff, buff_len = self.buy_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.price.deserialize(buff)
		buff = self.currency_type.deserialize(buff)
		buff = self.buy_num.deserialize(buff)
		return buff

class sc_buy_season_reward(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_season_data = season_t()
		self.resources = user_resource_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_season_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_season_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_SHOP_BUY_ITEM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_read_battle_report(proto):
	def __init__(self):
		self.session = session_t()
		self.battle_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.battle_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.battle_id.deserialize(buff)
		return buff

class sc_read_battle_report(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.battle_id = cint64()
		self.amount = cint32()
		self.page = cint32()
		self.len_of_brief_record = cuint16()
		self.brief_record = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.battle_id.serialize(buff, buff_len)
		buff, buff_len = self.amount.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		buff, buff_len = self.len_of_brief_record.serialize(buff, buff_len)
		for i in range(self.len_of_brief_record.value):
			buff, buff_len = self.brief_record[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.battle_id.deserialize(buff)
		buff = self.amount.deserialize(buff)
		buff = self.page.deserialize(buff)
		buff = self.len_of_brief_record.deserialize(buff)
		self.brief_record = []
		for i in range(self.len_of_brief_record.value):
			self.brief_record.append(brief_battle_record())
			buff = self.brief_record[i].deserialize(buff)
		return buff

	def add_brief_record():
		if len(brief_record) >= MAX_BATTLE_RECORD_NUM.value:
			return None
		brief_record.append(brief_battle_record())
		return brief_record[len(brief_record) - 1]

class cs_get_world_trend_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_world_trend_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.current_wt_entry = cint32()
		self.len_of_data = cuint16()
		self.data = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.current_wt_entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_data.serialize(buff, buff_len)
		for i in range(self.len_of_data.value):
			buff, buff_len = self.data[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.current_wt_entry.deserialize(buff)
		buff = self.len_of_data.deserialize(buff)
		self.data = []
		for i in range(self.len_of_data.value):
			self.data.append(world_trend_t())
			buff = self.data[i].deserialize(buff)
		return buff

	def add_data():
		if len(data) >= MAX_WORLD_TREND_NUM.value:
			return None
		data.append(world_trend_t())
		return data[len(data) - 1]

class cs_get_world_trend_rewards(proto):
	def __init__(self):
		self.session = session_t()
		self.entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.entry.deserialize(buff)
		return buff

class sc_get_world_trend_rewards(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.rewards = rewards_t()
		self.entry = cint32()
		self.change_data = world_trend_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.change_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.entry.deserialize(buff)
		buff = self.change_data.deserialize(buff)
		return buff

class cs_get_state_achi_list(proto):
	def __init__(self):
		self.session = session_t()
		self.state = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.state.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.state.deserialize(buff)
		return buff

class sc_get_state_achi_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_data = cuint16()
		self.data = []
		self.state = cint32()
		self.city_info = cbigstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_data.serialize(buff, buff_len)
		for i in range(self.len_of_data.value):
			buff, buff_len = self.data[i].serialize(buff, buff_len)
		buff, buff_len = self.state.serialize(buff, buff_len)
		buff, buff_len = self.city_info.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_data.deserialize(buff)
		self.data = []
		for i in range(self.len_of_data.value):
			self.data.append(state_achi_t())
			buff = self.data[i].deserialize(buff)
		buff = self.state.deserialize(buff)
		buff = self.city_info.deserialize(buff)
		return buff

	def add_data():
		if len(data) >= MAX_STATE_ACHI_NUM.value:
			return None
		data.append(state_achi_t())
		return data[len(data) - 1]

class cs_get_state_achi_rewards(proto):
	def __init__(self):
		self.session = session_t()
		self.entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.entry.deserialize(buff)
		return buff

class sc_get_state_achi_rewards(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.rewards = rewards_t()
		self.entry = cint32()
		self.change_data = state_achi_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.change_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.entry.deserialize(buff)
		buff = self.change_data.deserialize(buff)
		return buff

class cs_onebtn_conscript_soldier(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()
		self.len_of_soldier_count = cuint16()
		self.soldier_count = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.len_of_soldier_count.serialize(buff, buff_len)
		for i in range(self.len_of_soldier_count.value):
			buff, buff_len = self.soldier_count[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.len_of_soldier_count.deserialize(buff)
		self.soldier_count = []
		for i in range(self.len_of_soldier_count.value):
			self.soldier_count.append(cint32())
			buff = self.soldier_count[i].deserialize(buff)
		return buff

	def add_soldier_count():
		if len(soldier_count) >= MAX_CORPS_TROOPS_NUM.value:
			return None
		soldier_count.append(ccint32())
		return soldier_count[len(soldier_count) - 1]

class sc_onebtn_conscript_soldier(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.len_of_troop_data = cuint16()
		self.troop_data = []
		self.resources = user_resource_t()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.len_of_troop_data.serialize(buff, buff_len)
		for i in range(self.len_of_troop_data.value):
			buff, buff_len = self.troop_data[i].serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.len_of_troop_data.deserialize(buff)
		self.troop_data = []
		for i in range(self.len_of_troop_data.value):
			self.troop_data.append(troops_data_t())
			buff = self.troop_data[i].deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		return buff

	def add_troop_data():
		if len(troop_data) >= MAX_CORPS_TROOPS_NUM.value:
			return None
		troop_data.append(troops_data_t())
		return troop_data[len(troop_data) - 1]

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

class cs_query_pay_result(proto):
	def __init__(self):
		self.session = session_t()
		self.order_id = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.order_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.order_id.deserialize(buff)
		return buff

class sc_query_pay_result(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.order_id = cstring()
		self.gold_coin = cint32()
		self.charge_product_id_list = cstring()
		self.vip_lv = cint32()
		self.vip_point = cint32()
		self.activity_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.order_id.serialize(buff, buff_len)
		buff, buff_len = self.gold_coin.serialize(buff, buff_len)
		buff, buff_len = self.charge_product_id_list.serialize(buff, buff_len)
		buff, buff_len = self.vip_lv.serialize(buff, buff_len)
		buff, buff_len = self.vip_point.serialize(buff, buff_len)
		buff, buff_len = self.activity_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.order_id.deserialize(buff)
		buff = self.gold_coin.deserialize(buff)
		buff = self.charge_product_id_list.deserialize(buff)
		buff = self.vip_lv.deserialize(buff)
		buff = self.vip_point.deserialize(buff)
		buff = self.activity_id.deserialize(buff)
		return buff

class cs_hero_star_lvup(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()
		self.to_star_lv = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.to_star_lv.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.to_star_lv.deserialize(buff)
		return buff

class sc_hero_star_lvup(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_data = hero_data_t()
		self.resources = user_resource_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_get_vip_reward_status(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_vip_reward_status(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_status_list = cuint16()
		self.status_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_status_list.serialize(buff, buff_len)
		for i in range(self.len_of_status_list.value):
			buff, buff_len = self.status_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_status_list.deserialize(buff)
		self.status_list = []
		for i in range(self.len_of_status_list.value):
			self.status_list.append(vip_reward_status_t())
			buff = self.status_list[i].deserialize(buff)
		return buff

	def add_status_list():
		if len(status_list) >= MAX_VIP_LV.value:
			return None
		status_list.append(vip_reward_status_t())
		return status_list[len(status_list) - 1]

class cs_get_vip_reward(proto):
	def __init__(self):
		self.session = session_t()
		self.vip_lv = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.vip_lv.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.vip_lv.deserialize(buff)
		return buff

class sc_get_vip_reward(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.change_status = vip_reward_status_t()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.change_status.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.change_status.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

class cs_miracle_battle(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()
		self.e_event_type = E_EVENT_TYPE()
		self.block_id = cint32()
		self.use_token = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.e_event_type.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.use_token.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.e_event_type.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.use_token.deserialize(buff)
		return buff

class sc_miracle_battle(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.e_event_type = E_EVENT_TYPE()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []
		self.len_of_corps_data_list = cuint16()
		self.corps_data_list = []
		self.use_token = cbool()
		self.token = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.e_event_type.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_corps_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_corps_data_list.value):
			buff, buff_len = self.corps_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.use_token.serialize(buff, buff_len)
		buff, buff_len = self.token.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.e_event_type.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		buff = self.len_of_corps_data_list.deserialize(buff)
		self.corps_data_list = []
		for i in range(self.len_of_corps_data_list.value):
			self.corps_data_list.append(corps_data_t())
			buff = self.corps_data_list[i].deserialize(buff)
		buff = self.use_token.deserialize(buff)
		buff = self.token.deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

	def add_corps_data_list():
		if len(corps_data_list) >= MAX_CORPS_COUNT.value:
			return None
		corps_data_list.append(corps_data_t())
		return corps_data_list[len(corps_data_list) - 1]

class cs_hero_quality_lvup(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()
		self.to_quality = E_HERO_QUALITY()
		self.to_quality_lv = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.to_quality.serialize(buff, buff_len)
		buff, buff_len = self.to_quality_lv.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.to_quality.deserialize(buff)
		buff = self.to_quality_lv.deserialize(buff)
		return buff

class sc_hero_quality_lvup(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_data = hero_data_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []
		self.resources = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		buff = self.resources.deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_hangup_data_req(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_hangup_data_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_data = cuint16()
		self.data = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_data.serialize(buff, buff_len)
		for i in range(self.len_of_data.value):
			buff, buff_len = self.data[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_data.deserialize(buff)
		self.data = []
		for i in range(self.len_of_data.value):
			self.data.append(hangup_user_data_t())
			buff = self.data[i].deserialize(buff)
		return buff

	def add_data():
		if len(data) >= MAX_TOWER_LEVEL.value:
			return None
		data.append(hangup_user_data_t())
		return data[len(data) - 1]

class cs_hangup_reward(proto):
	def __init__(self):
		self.session = session_t()
		self.entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.entry.deserialize(buff)
		return buff

class sc_hangup_reward(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.data = hangup_user_data_t()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.data.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

class cs_hangup_send(proto):
	def __init__(self):
		self.session = session_t()
		self.entry = cint32()
		self.len_of_hero_entry = cuint16()
		self.hero_entry = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_hero_entry.serialize(buff, buff_len)
		for i in range(self.len_of_hero_entry.value):
			buff, buff_len = self.hero_entry[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.entry.deserialize(buff)
		buff = self.len_of_hero_entry.deserialize(buff)
		self.hero_entry = []
		for i in range(self.len_of_hero_entry.value):
			self.hero_entry.append(cint64())
			buff = self.hero_entry[i].deserialize(buff)
		return buff

	def add_hero_entry():
		if len(hero_entry) >= MAX_HANGUP_SLOT.value:
			return None
		hero_entry.append(ccint64())
		return hero_entry[len(hero_entry) - 1]

class sc_hangup_send(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.data = hangup_user_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.data.deserialize(buff)
		return buff

class cs_wandering(proto):
	def __init__(self):
		self.session = session_t()
		self.region = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.region.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.region.deserialize(buff)
		return buff

class sc_wandering(proto):
	def __init__(self):
		self.common_result = common_result_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		return buff

class cs_hero_change_equip_one_key(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()
		self.len_of_equip_entry_list = cuint16()
		self.equip_entry_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_equip_entry_list.serialize(buff, buff_len)
		for i in range(self.len_of_equip_entry_list.value):
			buff, buff_len = self.equip_entry_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.len_of_equip_entry_list.deserialize(buff)
		self.equip_entry_list = []
		for i in range(self.len_of_equip_entry_list.value):
			self.equip_entry_list.append(cint32())
			buff = self.equip_entry_list[i].deserialize(buff)
		return buff

	def add_equip_entry_list():
		if len(equip_entry_list) >= e_equip_slot_max.value:
			return None
		equip_entry_list.append(ccint32())
		return equip_entry_list[len(equip_entry_list) - 1]

class sc_hero_change_equip_one_key(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_data = hero_data_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_arena_data_req(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_arena_data_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_data = arena_user_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		return buff

class cs_arena_set_formation(proto):
	def __init__(self):
		self.session = session_t()
		self.index = cint32()
		self.formation = arena_formation()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.index.serialize(buff, buff_len)
		buff, buff_len = self.formation.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.index.deserialize(buff)
		buff = self.formation.deserialize(buff)
		return buff

class sc_arena_set_formation(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_data = arena_user_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		return buff

class cs_arena_rank_req(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_arena_rank_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_user_data = cuint16()
		self.user_data = []
		self.me = arena_user_brief_t()
		self.rank = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_user_data.serialize(buff, buff_len)
		for i in range(self.len_of_user_data.value):
			buff, buff_len = self.user_data[i].serialize(buff, buff_len)
		buff, buff_len = self.me.serialize(buff, buff_len)
		buff, buff_len = self.rank.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_user_data.deserialize(buff)
		self.user_data = []
		for i in range(self.len_of_user_data.value):
			self.user_data.append(arena_user_brief_t())
			buff = self.user_data[i].deserialize(buff)
		buff = self.me.deserialize(buff)
		buff = self.rank.deserialize(buff)
		return buff

	def add_user_data():
		if len(user_data) >= MAX_ARENA_RANK_NUM.value:
			return None
		user_data.append(arena_user_brief_t())
		return user_data[len(user_data) - 1]

class cs_arena_fresh(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_arena_fresh(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_data = arena_user_data_t()
		self.gold = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		buff, buff_len = self.gold.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		buff = self.gold.deserialize(buff)
		return buff

class cs_arena_fight(proto):
	def __init__(self):
		self.session = session_t()
		self.enemy_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.enemy_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.enemy_id.deserialize(buff)
		return buff

class sc_arena_fight(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_data = arena_user_data_t()
		self.reward = rewards_t()
		self.len_of_records = cuint16()
		self.records = []
		self.coin = cint32()
		self.honor = cint32()
		self.score = cint32()
		self.result = E_BATTLE_RESULT_TYPE()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		buff, buff_len = self.reward.serialize(buff, buff_len)
		buff, buff_len = self.len_of_records.serialize(buff, buff_len)
		for i in range(self.len_of_records.value):
			buff, buff_len = self.records[i].serialize(buff, buff_len)
		buff, buff_len = self.coin.serialize(buff, buff_len)
		buff, buff_len = self.honor.serialize(buff, buff_len)
		buff, buff_len = self.score.serialize(buff, buff_len)
		buff, buff_len = self.result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		buff = self.reward.deserialize(buff)
		buff = self.len_of_records.deserialize(buff)
		self.records = []
		for i in range(self.len_of_records.value):
			self.records.append(brief_battle_record())
			buff = self.records[i].deserialize(buff)
		buff = self.coin.deserialize(buff)
		buff = self.honor.deserialize(buff)
		buff = self.score.deserialize(buff)
		buff = self.result.deserialize(buff)
		return buff

	def add_records():
		if len(records) >= MAX_ARENA_CORPS_NUM.value:
			return None
		records.append(brief_battle_record())
		return records[len(records) - 1]

class cs_arena_buy_times(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_arena_buy_times(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_data = arena_user_data_t()
		self.gold = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		buff, buff_len = self.gold.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		buff = self.gold.deserialize(buff)
		return buff

class cs_arena_pick_day_reward(proto):
	def __init__(self):
		self.session = session_t()
		self.entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.entry.deserialize(buff)
		return buff

class sc_arena_pick_day_reward(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.entry = cint32()
		self.user_data = arena_user_data_t()
		self.reward = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		buff, buff_len = self.reward.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.entry.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		buff = self.reward.deserialize(buff)
		return buff

class cs_arena_pick_season_reward(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_arena_pick_season_reward(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_data = arena_user_data_t()
		self.reward = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		buff, buff_len = self.reward.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		buff = self.reward.deserialize(buff)
		return buff

class cs_arena_battle_record_list(proto):
	def __init__(self):
		self.session = session_t()
		self.page = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.page.deserialize(buff)
		return buff

class sc_arena_battle_record_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.amount = cint32()
		self.page = cint32()
		self.len_of_brief_record = cuint16()
		self.brief_record = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.amount.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		buff, buff_len = self.len_of_brief_record.serialize(buff, buff_len)
		for i in range(self.len_of_brief_record.value):
			buff, buff_len = self.brief_record[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.amount.deserialize(buff)
		buff = self.page.deserialize(buff)
		buff = self.len_of_brief_record.deserialize(buff)
		self.brief_record = []
		for i in range(self.len_of_brief_record.value):
			self.brief_record.append(brief_battle_record())
			buff = self.brief_record[i].deserialize(buff)
		return buff

	def add_brief_record():
		if len(brief_record) >= MAX_ARENA_RECORD_NUM.value:
			return None
		brief_record.append(brief_battle_record())
		return brief_record[len(brief_record) - 1]

class cs_get_tower_info(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_tower_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.infos = tower_info()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.infos.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.infos.deserialize(buff)
		return buff

class cs_get_tower_floor_info(proto):
	def __init__(self):
		self.session = session_t()
		self.floor = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.floor.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.floor.deserialize(buff)
		return buff

class sc_get_tower_floor_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.floor = cint32()
		self.len_of_formation = cuint16()
		self.formation = []
		self.len_of_hero = cuint16()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.floor.serialize(buff, buff_len)
		buff, buff_len = self.len_of_formation.serialize(buff, buff_len)
		for i in range(self.len_of_formation.value):
			buff, buff_len = self.formation[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_hero.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.floor.deserialize(buff)
		buff = self.len_of_formation.deserialize(buff)
		self.formation = []
		for i in range(self.len_of_formation.value):
			self.formation.append(arena_formation())
			buff = self.formation[i].deserialize(buff)
		buff = self.len_of_hero.deserialize(buff)
		return buff

	def add_formation():
		if len(formation) >= MAX_TOWER_CORPS_NUM.value:
			return None
		formation.append(arena_formation())
		return formation[len(formation) - 1]

class cs_tower_floor_trial(proto):
	def __init__(self):
		self.session = session_t()
		self.floor = cint32()
		self.len_of_formation = cuint16()
		self.formation = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.floor.serialize(buff, buff_len)
		buff, buff_len = self.len_of_formation.serialize(buff, buff_len)
		for i in range(self.len_of_formation.value):
			buff, buff_len = self.formation[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.floor.deserialize(buff)
		buff = self.len_of_formation.deserialize(buff)
		self.formation = []
		for i in range(self.len_of_formation.value):
			self.formation.append(arena_formation())
			buff = self.formation[i].deserialize(buff)
		return buff

	def add_formation():
		if len(formation) >= MAX_TOWER_CORPS_NUM.value:
			return None
		formation.append(arena_formation())
		return formation[len(formation) - 1]

class sc_tower_floor_trial(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.infos = tower_info()
		self.rewards = rewards_t()
		self.fight_result = E_CHALLENGE_RESULT()
		self.len_of_records = cuint16()
		self.records = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.infos.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.fight_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_records.serialize(buff, buff_len)
		for i in range(self.len_of_records.value):
			buff, buff_len = self.records[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.infos.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.fight_result.deserialize(buff)
		buff = self.len_of_records.deserialize(buff)
		self.records = []
		for i in range(self.len_of_records.value):
			self.records.append(brief_battle_record())
			buff = self.records[i].deserialize(buff)
		return buff

	def add_records():
		if len(records) >= MAX_TOWER_CORPS_NUM.value:
			return None
		records.append(brief_battle_record())
		return records[len(records) - 1]

class cs_user_shop_info(proto):
	def __init__(self):
		self.session = session_t()
		self.type = E_SHOP_TYPE()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.type.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.type.deserialize(buff)
		return buff

class sc_user_shop_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.type = E_SHOP_TYPE()
		self.len_of_item_list = cuint16()
		self.item_list = []
		self.refresh_count = cint32()
		self.guild_force = cint32()
		self.buy_limit = cint32()
		self.currency_info = currency_info_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.type.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_list.value):
			buff, buff_len = self.item_list[i].serialize(buff, buff_len)
		buff, buff_len = self.refresh_count.serialize(buff, buff_len)
		buff, buff_len = self.guild_force.serialize(buff, buff_len)
		buff, buff_len = self.buy_limit.serialize(buff, buff_len)
		buff, buff_len = self.currency_info.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.type.deserialize(buff)
		buff = self.len_of_item_list.deserialize(buff)
		self.item_list = []
		for i in range(self.len_of_item_list.value):
			self.item_list.append(shop_item_data_t())
			buff = self.item_list[i].deserialize(buff)
		buff = self.refresh_count.deserialize(buff)
		buff = self.guild_force.deserialize(buff)
		buff = self.buy_limit.deserialize(buff)
		buff = self.currency_info.deserialize(buff)
		return buff

	def add_item_list():
		if len(item_list) >= MAX_SHOP_KINDS.value:
			return None
		item_list.append(shop_item_data_t())
		return item_list[len(item_list) - 1]

class cs_user_shop_buy(proto):
	def __init__(self):
		self.session = session_t()
		self.type = E_SHOP_TYPE()
		self.buy_info = buy_shop_item_info_t()
		self.buy_times = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.type.serialize(buff, buff_len)
		buff, buff_len = self.buy_info.serialize(buff, buff_len)
		buff, buff_len = self.buy_times.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.type.deserialize(buff)
		buff = self.buy_info.deserialize(buff)
		buff = self.buy_times.deserialize(buff)
		return buff

class sc_user_shop_buy(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.type = E_SHOP_TYPE()
		self.buy_result = shop_buy_result_t()
		self.buy_times = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.type.serialize(buff, buff_len)
		buff, buff_len = self.buy_result.serialize(buff, buff_len)
		buff, buff_len = self.buy_times.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.type.deserialize(buff)
		buff = self.buy_result.deserialize(buff)
		buff = self.buy_times.deserialize(buff)
		return buff

class cs_user_shop_refresh(proto):
	def __init__(self):
		self.session = session_t()
		self.type = E_SHOP_TYPE()
		self.use_ticket = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.type.serialize(buff, buff_len)
		buff, buff_len = self.use_ticket.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.type.deserialize(buff)
		buff = self.use_ticket.deserialize(buff)
		return buff

class sc_user_shop_refresh(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.type = E_SHOP_TYPE()
		self.refresh_count = cint32()
		self.currency_info = currency_info_t()
		self.len_of_item_list = cuint16()
		self.item_list = []
		self.ticket = item_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.type.serialize(buff, buff_len)
		buff, buff_len = self.refresh_count.serialize(buff, buff_len)
		buff, buff_len = self.currency_info.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_list.value):
			buff, buff_len = self.item_list[i].serialize(buff, buff_len)
		buff, buff_len = self.ticket.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.type.deserialize(buff)
		buff = self.refresh_count.deserialize(buff)
		buff = self.currency_info.deserialize(buff)
		buff = self.len_of_item_list.deserialize(buff)
		self.item_list = []
		for i in range(self.len_of_item_list.value):
			self.item_list.append(shop_item_data_t())
			buff = self.item_list[i].deserialize(buff)
		buff = self.ticket.deserialize(buff)
		return buff

	def add_item_list():
		if len(item_list) >= MAX_SHOP_KINDS.value:
			return None
		item_list.append(shop_item_data_t())
		return item_list[len(item_list) - 1]

class cs_use_exp_item(proto):
	def __init__(self):
		self.session = session_t()
		self.lv_up_type = cint32()
		self.max_lv_corps_key = corps_key_t()
		self.max_lv_hero_entry = cint32()
		self.lv_up_corps_key = corps_key_t()
		self.lv_up_hero_entry = cint32()
		self.len_of_exp_item_list = cuint16()
		self.exp_item_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.lv_up_type.serialize(buff, buff_len)
		buff, buff_len = self.max_lv_corps_key.serialize(buff, buff_len)
		buff, buff_len = self.max_lv_hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.lv_up_corps_key.serialize(buff, buff_len)
		buff, buff_len = self.lv_up_hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_exp_item_list.serialize(buff, buff_len)
		for i in range(self.len_of_exp_item_list.value):
			buff, buff_len = self.exp_item_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.lv_up_type.deserialize(buff)
		buff = self.max_lv_corps_key.deserialize(buff)
		buff = self.max_lv_hero_entry.deserialize(buff)
		buff = self.lv_up_corps_key.deserialize(buff)
		buff = self.lv_up_hero_entry.deserialize(buff)
		buff = self.len_of_exp_item_list.deserialize(buff)
		self.exp_item_list = []
		for i in range(self.len_of_exp_item_list.value):
			self.exp_item_list.append(exp_item_t())
			buff = self.exp_item_list[i].deserialize(buff)
		return buff

	def add_exp_item_list():
		if len(exp_item_list) >= MAX_USE_EXP_ITEM_TYPE_NUM.value:
			return None
		exp_item_list.append(exp_item_t())
		return exp_item_list[len(exp_item_list) - 1]

class sc_use_exp_item(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []
		self.lv_up_type = cint32()
		self.corps_data = corps_data_t()
		self.hero_data = hero_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.lv_up_type.serialize(buff, buff_len)
		buff, buff_len = self.corps_data.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		buff = self.lv_up_type.deserialize(buff)
		buff = self.corps_data.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_tower_floor_report(proto):
	def __init__(self):
		self.session = session_t()
		self.floor = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.floor.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.floor.deserialize(buff)
		return buff

class sc_tower_floor_report(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.floor = cint32()
		self.len_of_reports = cuint16()
		self.reports = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.floor.serialize(buff, buff_len)
		buff, buff_len = self.len_of_reports.serialize(buff, buff_len)
		for i in range(self.len_of_reports.value):
			buff, buff_len = self.reports[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.floor.deserialize(buff)
		buff = self.len_of_reports.deserialize(buff)
		self.reports = []
		for i in range(self.len_of_reports.value):
			self.reports.append(tower_report())
			buff = self.reports[i].deserialize(buff)
		return buff

	def add_reports():
		if len(reports) >= TOWER_REPORT_NUMS.value:
			return None
		reports.append(tower_report())
		return reports[len(reports) - 1]

class cs_get_state_status(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_state_status(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_state_status_list = cuint16()
		self.state_status_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_state_status_list.serialize(buff, buff_len)
		for i in range(self.len_of_state_status_list.value):
			buff, buff_len = self.state_status_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_state_status_list.deserialize(buff)
		self.state_status_list = []
		for i in range(self.len_of_state_status_list.value):
			self.state_status_list.append(state_status_t())
			buff = self.state_status_list[i].deserialize(buff)
		return buff

	def add_state_status_list():
		if len(state_status_list) >= MAX_STATE_NUM.value:
			return None
		state_status_list.append(state_status_t())
		return state_status_list[len(state_status_list) - 1]

class cs_get_newbie_zhaoyu(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_newbie_zhaoyu(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.newbie_for_zhaoyu = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.newbie_for_zhaoyu.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.newbie_for_zhaoyu.deserialize(buff)
		return buff

class cs_set_newbie_zhaoyu(proto):
	def __init__(self):
		self.session = session_t()
		self.newbie_for_zhaoyu = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.newbie_for_zhaoyu.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.newbie_for_zhaoyu.deserialize(buff)
		return buff

class sc_set_newbie_zhaoyu(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.newbie_for_zhaoyu = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.newbie_for_zhaoyu.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.newbie_for_zhaoyu.deserialize(buff)
		return buff

class cs_pick_gift(proto):
	def __init__(self):
		self.session = session_t()
		self.gift_code = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.gift_code.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.gift_code.deserialize(buff)
		return buff

class sc_pick_gift(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.gift_code = cstring()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.gift_code.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.gift_code.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

class cs_share_report(proto):
	def __init__(self):
		self.session = session_t()
		self.type = SHARE_RECORD_TYPE()
		self.battle_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.type.serialize(buff, buff_len)
		buff, buff_len = self.battle_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.type.deserialize(buff)
		buff = self.battle_id.deserialize(buff)
		return buff

class sc_share_report(proto):
	def __init__(self):
		self.common_result = common_result_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		return buff

class cs_get_arena_record(proto):
	def __init__(self):
		self.session = session_t()
		self.battle_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.battle_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.battle_id.deserialize(buff)
		return buff

class sc_get_arena_record(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.battle_id = cint64()
		self.record = battle_record()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.battle_id.serialize(buff, buff_len)
		buff, buff_len = self.record.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.battle_id.deserialize(buff)
		buff = self.record.deserialize(buff)
		return buff

class cs_match_data_req(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_match_data_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_data = match_user_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		return buff

class cs_match_set_formation(proto):
	def __init__(self):
		self.session = session_t()
		self.index = cint32()
		self.formationtype = E_MATCH_FORMATION()
		self.formation = match_formation()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.index.serialize(buff, buff_len)
		buff, buff_len = self.formationtype.serialize(buff, buff_len)
		buff, buff_len = self.formation.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.index.deserialize(buff)
		buff = self.formationtype.deserialize(buff)
		buff = self.formation.deserialize(buff)
		return buff

class sc_match_set_formation(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_data = match_user_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		return buff

class cs_match_rank_req(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_match_rank_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_user_data = cuint16()
		self.user_data = []
		self.me = match_user_brief_t()
		self.rank = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_user_data.serialize(buff, buff_len)
		for i in range(self.len_of_user_data.value):
			buff, buff_len = self.user_data[i].serialize(buff, buff_len)
		buff, buff_len = self.me.serialize(buff, buff_len)
		buff, buff_len = self.rank.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_user_data.deserialize(buff)
		self.user_data = []
		for i in range(self.len_of_user_data.value):
			self.user_data.append(match_user_brief_t())
			buff = self.user_data[i].deserialize(buff)
		buff = self.me.deserialize(buff)
		buff = self.rank.deserialize(buff)
		return buff

	def add_user_data():
		if len(user_data) >= MAX_ARENA_RANK_NUM.value:
			return None
		user_data.append(match_user_brief_t())
		return user_data[len(user_data) - 1]

class cs_match_fight(proto):
	def __init__(self):
		self.session = session_t()
		self.enemy_id = cint64()
		self.rank = cint32()
		self.corps_key = corps_key_t()
		self.formation_enemy = match_formation()
		self.formation_self = match_formation()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.enemy_id.serialize(buff, buff_len)
		buff, buff_len = self.rank.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.formation_enemy.serialize(buff, buff_len)
		buff, buff_len = self.formation_self.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.enemy_id.deserialize(buff)
		buff = self.rank.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.formation_enemy.deserialize(buff)
		buff = self.formation_self.deserialize(buff)
		return buff

class sc_match_fight(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_data = match_user_data_t()
		self.rank_up = cint32()
		self.reward = rewards_t()
		self.len_of_records = cuint16()
		self.records = []
		self.coin = cint32()
		self.result = E_BATTLE_RESULT_TYPE()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		buff, buff_len = self.rank_up.serialize(buff, buff_len)
		buff, buff_len = self.reward.serialize(buff, buff_len)
		buff, buff_len = self.len_of_records.serialize(buff, buff_len)
		for i in range(self.len_of_records.value):
			buff, buff_len = self.records[i].serialize(buff, buff_len)
		buff, buff_len = self.coin.serialize(buff, buff_len)
		buff, buff_len = self.result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		buff = self.rank_up.deserialize(buff)
		buff = self.reward.deserialize(buff)
		buff = self.len_of_records.deserialize(buff)
		self.records = []
		for i in range(self.len_of_records.value):
			self.records.append(brief_battle_record())
			buff = self.records[i].deserialize(buff)
		buff = self.coin.deserialize(buff)
		buff = self.result.deserialize(buff)
		return buff

	def add_records():
		if len(records) >= MAX_ARENA_CORPS_NUM.value:
			return None
		records.append(brief_battle_record())
		return records[len(records) - 1]

class cs_get_match_record(proto):
	def __init__(self):
		self.session = session_t()
		self.battle_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.battle_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.battle_id.deserialize(buff)
		return buff

class sc_get_match_record(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.battle_id = cint64()
		self.record = battle_record()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.battle_id.serialize(buff, buff_len)
		buff, buff_len = self.record.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.battle_id.deserialize(buff)
		buff = self.record.deserialize(buff)
		return buff

class cs_match_battle_record_list(proto):
	def __init__(self):
		self.session = session_t()
		self.page = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.page.deserialize(buff)
		return buff

class sc_match_battle_record_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.amount = cint32()
		self.page = cint32()
		self.len_of_brief_record = cuint16()
		self.brief_record = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.amount.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		buff, buff_len = self.len_of_brief_record.serialize(buff, buff_len)
		for i in range(self.len_of_brief_record.value):
			buff, buff_len = self.brief_record[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.amount.deserialize(buff)
		buff = self.page.deserialize(buff)
		buff = self.len_of_brief_record.deserialize(buff)
		self.brief_record = []
		for i in range(self.len_of_brief_record.value):
			self.brief_record.append(brief_battle_record())
			buff = self.brief_record[i].deserialize(buff)
		return buff

	def add_brief_record():
		if len(brief_record) >= MAX_ARENA_RECORD_NUM.value:
			return None
		brief_record.append(brief_battle_record())
		return brief_record[len(brief_record) - 1]

class cs_match_refresh_enemy_req(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_match_refresh_enemy_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_data = match_user_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		return buff

class cs_match_buy_times(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_match_buy_times(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_data = match_user_data_t()
		self.gold = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		buff, buff_len = self.gold.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		buff = self.gold.deserialize(buff)
		return buff

class cs_battle_for_cp(proto):
	def __init__(self):
		self.session = session_t()
		self.l_laofan_hero_0 = laofan_hero_data_t()
		self.l_laofan_hero_1 = laofan_hero_data_t()
		self.l_laofan_hero_2 = laofan_hero_data_t()
		self.l_laofan_troops_0 = laofan_troops_data_t()
		self.l_laofan_troops_1 = laofan_troops_data_t()
		self.l_laofan_troops_2 = laofan_troops_data_t()
		self.l_laofan_troops_3 = laofan_troops_data_t()
		self.l_laofan_troops_4 = laofan_troops_data_t()
		self.r_laofan_hero_0 = laofan_hero_data_t()
		self.r_laofan_hero_1 = laofan_hero_data_t()
		self.r_laofan_hero_2 = laofan_hero_data_t()
		self.r_laofan_troops_0 = laofan_troops_data_t()
		self.r_laofan_troops_1 = laofan_troops_data_t()
		self.r_laofan_troops_2 = laofan_troops_data_t()
		self.r_laofan_troops_3 = laofan_troops_data_t()
		self.r_laofan_troops_4 = laofan_troops_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.l_laofan_hero_0.serialize(buff, buff_len)
		buff, buff_len = self.l_laofan_hero_1.serialize(buff, buff_len)
		buff, buff_len = self.l_laofan_hero_2.serialize(buff, buff_len)
		buff, buff_len = self.l_laofan_troops_0.serialize(buff, buff_len)
		buff, buff_len = self.l_laofan_troops_1.serialize(buff, buff_len)
		buff, buff_len = self.l_laofan_troops_2.serialize(buff, buff_len)
		buff, buff_len = self.l_laofan_troops_3.serialize(buff, buff_len)
		buff, buff_len = self.l_laofan_troops_4.serialize(buff, buff_len)
		buff, buff_len = self.r_laofan_hero_0.serialize(buff, buff_len)
		buff, buff_len = self.r_laofan_hero_1.serialize(buff, buff_len)
		buff, buff_len = self.r_laofan_hero_2.serialize(buff, buff_len)
		buff, buff_len = self.r_laofan_troops_0.serialize(buff, buff_len)
		buff, buff_len = self.r_laofan_troops_1.serialize(buff, buff_len)
		buff, buff_len = self.r_laofan_troops_2.serialize(buff, buff_len)
		buff, buff_len = self.r_laofan_troops_3.serialize(buff, buff_len)
		buff, buff_len = self.r_laofan_troops_4.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.l_laofan_hero_0.deserialize(buff)
		buff = self.l_laofan_hero_1.deserialize(buff)
		buff = self.l_laofan_hero_2.deserialize(buff)
		buff = self.l_laofan_troops_0.deserialize(buff)
		buff = self.l_laofan_troops_1.deserialize(buff)
		buff = self.l_laofan_troops_2.deserialize(buff)
		buff = self.l_laofan_troops_3.deserialize(buff)
		buff = self.l_laofan_troops_4.deserialize(buff)
		buff = self.r_laofan_hero_0.deserialize(buff)
		buff = self.r_laofan_hero_1.deserialize(buff)
		buff = self.r_laofan_hero_2.deserialize(buff)
		buff = self.r_laofan_troops_0.deserialize(buff)
		buff = self.r_laofan_troops_1.deserialize(buff)
		buff = self.r_laofan_troops_2.deserialize(buff)
		buff = self.r_laofan_troops_3.deserialize(buff)
		buff = self.r_laofan_troops_4.deserialize(buff)
		return buff

class sc_battle_for_cp(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.record = battle_record()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.record.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.record.deserialize(buff)
		return buff

class cs_get_tower_floor_reward(proto):
	def __init__(self):
		self.session = session_t()
		self.floor = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.floor.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.floor.deserialize(buff)
		return buff

class sc_get_tower_floor_reward(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.infos = tower_info()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.infos.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.infos.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

class cs_get_storage_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_storage_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_storage_list = cuint16()
		self.storage_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_storage_list.serialize(buff, buff_len)
		for i in range(self.len_of_storage_list.value):
			buff, buff_len = self.storage_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_storage_list.deserialize(buff)
		self.storage_list = []
		for i in range(self.len_of_storage_list.value):
			self.storage_list.append(storage_data_t())
			buff = self.storage_list[i].deserialize(buff)
		return buff

	def add_storage_list():
		if len(storage_list) >= MAX_STORAGE_NUM.value:
			return None
		storage_list.append(storage_data_t())
		return storage_list[len(storage_list) - 1]

class cs_tower_hangup_send(proto):
	def __init__(self):
		self.session = session_t()
		self.mode = cint32()
		self.floor = cint32()
		self.len_of_hero_entry = cuint16()
		self.hero_entry = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.mode.serialize(buff, buff_len)
		buff, buff_len = self.floor.serialize(buff, buff_len)
		buff, buff_len = self.len_of_hero_entry.serialize(buff, buff_len)
		for i in range(self.len_of_hero_entry.value):
			buff, buff_len = self.hero_entry[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.mode.deserialize(buff)
		buff = self.floor.deserialize(buff)
		buff = self.len_of_hero_entry.deserialize(buff)
		self.hero_entry = []
		for i in range(self.len_of_hero_entry.value):
			self.hero_entry.append(cint32())
			buff = self.hero_entry[i].deserialize(buff)
		return buff

	def add_hero_entry():
		if len(hero_entry) >= MAX_HANGUP_SLOT.value:
			return None
		hero_entry.append(ccint32())
		return hero_entry[len(hero_entry) - 1]

class sc_tower_hangup_send(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.infos = tower_info()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.infos.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.infos.deserialize(buff)
		return buff

class cs_tower_hangup_reward(proto):
	def __init__(self):
		self.session = session_t()
		self.mode = cint32()
		self.floor = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.mode.serialize(buff, buff_len)
		buff, buff_len = self.floor.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.mode.deserialize(buff)
		buff = self.floor.deserialize(buff)
		return buff

class sc_tower_hangup_reward(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.infos = tower_info()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.infos.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.infos.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

class cs_tower_hangup_stop(proto):
	def __init__(self):
		self.session = session_t()
		self.mode = cint32()
		self.floor = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.mode.serialize(buff, buff_len)
		buff, buff_len = self.floor.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.mode.deserialize(buff)
		buff = self.floor.deserialize(buff)
		return buff

class sc_tower_hangup_stop(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.infos = tower_info()
		self.rewards = rewards_t()
		self.len_of_hero_entry = cuint16()
		self.hero_entry = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.infos.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.len_of_hero_entry.serialize(buff, buff_len)
		for i in range(self.len_of_hero_entry.value):
			buff, buff_len = self.hero_entry[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.infos.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.len_of_hero_entry.deserialize(buff)
		self.hero_entry = []
		for i in range(self.len_of_hero_entry.value):
			self.hero_entry.append(cint32())
			buff = self.hero_entry[i].deserialize(buff)
		return buff

	def add_hero_entry():
		if len(hero_entry) >= MAX_HANGUP_SLOT.value:
			return None
		hero_entry.append(ccint32())
		return hero_entry[len(hero_entry) - 1]

class cs_equip_make(proto):
	def __init__(self):
		self.session = session_t()
		self.consume_item_0 = equip_make_consume_item_t()
		self.consume_item_1 = equip_make_consume_item_t()
		self.consume_item_2 = equip_make_consume_item_t()
		self.consume_item_3 = equip_make_consume_item_t()
		self.consume_item_4 = equip_make_consume_item_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.consume_item_0.serialize(buff, buff_len)
		buff, buff_len = self.consume_item_1.serialize(buff, buff_len)
		buff, buff_len = self.consume_item_2.serialize(buff, buff_len)
		buff, buff_len = self.consume_item_3.serialize(buff, buff_len)
		buff, buff_len = self.consume_item_4.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.consume_item_0.deserialize(buff)
		buff = self.consume_item_1.deserialize(buff)
		buff = self.consume_item_2.deserialize(buff)
		buff = self.consume_item_3.deserialize(buff)
		buff = self.consume_item_4.deserialize(buff)
		return buff

class sc_equip_make(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.make_success = cbool()
		self.resources = user_resource_t()
		self.rewards = rewards_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.make_success.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.make_success.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_get_tower_record(proto):
	def __init__(self):
		self.session = session_t()
		self.battle_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.battle_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.battle_id.deserialize(buff)
		return buff

class sc_get_tower_record(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.battle_id = cint64()
		self.record = battle_record()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.battle_id.serialize(buff, buff_len)
		buff, buff_len = self.record.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.battle_id.deserialize(buff)
		buff = self.record.deserialize(buff)
		return buff

class cs_get_tower_rank(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_tower_rank(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_infos = cuint16()
		self.infos = []
		self.me = tower_rank()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_infos.serialize(buff, buff_len)
		for i in range(self.len_of_infos.value):
			buff, buff_len = self.infos[i].serialize(buff, buff_len)
		buff, buff_len = self.me.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_infos.deserialize(buff)
		self.infos = []
		for i in range(self.len_of_infos.value):
			self.infos.append(tower_rank())
			buff = self.infos[i].deserialize(buff)
		buff = self.me.deserialize(buff)
		return buff

	def add_infos():
		if len(infos) >= MAX_TOWER_RANK_NUM.value:
			return None
		infos.append(tower_rank())
		return infos[len(infos) - 1]

class cs_tower_battle_record_list(proto):
	def __init__(self):
		self.session = session_t()
		self.page = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.page.deserialize(buff)
		return buff

class sc_tower_battle_record_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.amount = cint32()
		self.page = cint32()
		self.len_of_brief_record = cuint16()
		self.brief_record = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.amount.serialize(buff, buff_len)
		buff, buff_len = self.page.serialize(buff, buff_len)
		buff, buff_len = self.len_of_brief_record.serialize(buff, buff_len)
		for i in range(self.len_of_brief_record.value):
			buff, buff_len = self.brief_record[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.amount.deserialize(buff)
		buff = self.page.deserialize(buff)
		buff = self.len_of_brief_record.deserialize(buff)
		self.brief_record = []
		for i in range(self.len_of_brief_record.value):
			self.brief_record.append(brief_battle_record())
			buff = self.brief_record[i].deserialize(buff)
		return buff

	def add_brief_record():
		if len(brief_record) >= MAX_ARENA_RECORD_NUM.value:
			return None
		brief_record.append(brief_battle_record())
		return brief_record[len(brief_record) - 1]

class cs_get_guild_command(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_guild_command(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.data = guild_command_data()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.data.deserialize(buff)
		return buff

class cs_buy_guild_command(proto):
	def __init__(self):
		self.session = session_t()
		self.entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.entry.deserialize(buff)
		return buff

class sc_buy_guild_command(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.data = guild_command_data()
		self.gold_coin = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		buff, buff_len = self.gold_coin.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.data.deserialize(buff)
		buff = self.gold_coin.deserialize(buff)
		return buff

class cs_add_guild_command(proto):
	def __init__(self):
		self.session = session_t()
		self.entry = cint32()
		self.index = cint32()
		self.block_id = cint32()
		self.start_time = cint32()
		self.mark = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.index.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.start_time.serialize(buff, buff_len)
		buff, buff_len = self.mark.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.entry.deserialize(buff)
		buff = self.index.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.start_time.deserialize(buff)
		buff = self.mark.deserialize(buff)
		return buff

class sc_add_guild_command(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.data = guild_command_data()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.data.deserialize(buff)
		return buff

class cs_del_guild_command(proto):
	def __init__(self):
		self.session = session_t()
		self.entry = cint32()
		self.index = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.index.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.entry.deserialize(buff)
		buff = self.index.deserialize(buff)
		return buff

class sc_del_guild_command(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.data = guild_command_data()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.data.deserialize(buff)
		return buff

class cs_get_plot_quest_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_plot_quest_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_mission_list = cuint16()
		self.mission_list = []
		self.new_quest = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mission_list.serialize(buff, buff_len)
		for i in range(self.len_of_mission_list.value):
			buff, buff_len = self.mission_list[i].serialize(buff, buff_len)
		buff, buff_len = self.new_quest.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_mission_list.deserialize(buff)
		self.mission_list = []
		for i in range(self.len_of_mission_list.value):
			self.mission_list.append(mission_t())
			buff = self.mission_list[i].deserialize(buff)
		buff = self.new_quest.deserialize(buff)
		return buff

	def add_mission_list():
		if len(mission_list) >= MAX_MISSION_NUM.value:
			return None
		mission_list.append(mission_t())
		return mission_list[len(mission_list) - 1]

class cs_get_plot_quest_rewards(proto):
	def __init__(self):
		self.session = session_t()
		self.entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.entry.deserialize(buff)
		return buff

class sc_get_plot_quest_rewards(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.rewards = rewards_t()
		self.entry = cint32()
		self.len_of_change_mission_list = cuint16()
		self.change_mission_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_change_mission_list.serialize(buff, buff_len)
		for i in range(self.len_of_change_mission_list.value):
			buff, buff_len = self.change_mission_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.entry.deserialize(buff)
		buff = self.len_of_change_mission_list.deserialize(buff)
		self.change_mission_list = []
		for i in range(self.len_of_change_mission_list.value):
			self.change_mission_list.append(mission_t())
			buff = self.change_mission_list[i].deserialize(buff)
		return buff

	def add_change_mission_list():
		if len(change_mission_list) >= MAX_MISSION_NUM.value:
			return None
		change_mission_list.append(mission_t())
		return change_mission_list[len(change_mission_list) - 1]

class cs_get_advise(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_advise(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.advise_entry = cint32()
		self.plot_quest_entry = cint32()
		self.plot_quest_data = mission_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.advise_entry.serialize(buff, buff_len)
		buff, buff_len = self.plot_quest_entry.serialize(buff, buff_len)
		buff, buff_len = self.plot_quest_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.advise_entry.deserialize(buff)
		buff = self.plot_quest_entry.deserialize(buff)
		buff = self.plot_quest_data.deserialize(buff)
		return buff

class cs_get_guild_quest_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_guild_quest_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_mission_list = cuint16()
		self.mission_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mission_list.serialize(buff, buff_len)
		for i in range(self.len_of_mission_list.value):
			buff, buff_len = self.mission_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_mission_list.deserialize(buff)
		self.mission_list = []
		for i in range(self.len_of_mission_list.value):
			self.mission_list.append(mission_t())
			buff = self.mission_list[i].deserialize(buff)
		return buff

	def add_mission_list():
		if len(mission_list) >= MAX_MISSION_NUM.value:
			return None
		mission_list.append(mission_t())
		return mission_list[len(mission_list) - 1]

class cs_get_guild_quest_rewards(proto):
	def __init__(self):
		self.session = session_t()
		self.entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.entry.deserialize(buff)
		return buff

class sc_get_guild_quest_rewards(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.rewards = rewards_t()
		self.entry = cint32()
		self.len_of_mission_list = cuint16()
		self.mission_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mission_list.serialize(buff, buff_len)
		for i in range(self.len_of_mission_list.value):
			buff, buff_len = self.mission_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.entry.deserialize(buff)
		buff = self.len_of_mission_list.deserialize(buff)
		self.mission_list = []
		for i in range(self.len_of_mission_list.value):
			self.mission_list.append(mission_t())
			buff = self.mission_list[i].deserialize(buff)
		return buff

	def add_mission_list():
		if len(mission_list) >= MAX_MISSION_NUM.value:
			return None
		mission_list.append(mission_t())
		return mission_list[len(mission_list) - 1]

class cs_hero_skill_lvup(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()
		self.skill_index = cint32()
		self.to_lv = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.skill_index.serialize(buff, buff_len)
		buff, buff_len = self.to_lv.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.skill_index.deserialize(buff)
		buff = self.to_lv.deserialize(buff)
		return buff

class sc_hero_skill_lvup(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_entry = cint32()
		self.hero_data = hero_data_t()
		self.resources = user_resource_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_cal_hero_power(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()
		self.quality = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.quality.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.quality.deserialize(buff)
		return buff

class sc_cal_hero_power(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_entry = cint32()
		self.quality = cint32()
		self.power = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.quality.serialize(buff, buff_len)
		buff, buff_len = self.power.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.quality.deserialize(buff)
		buff = self.power.deserialize(buff)
		return buff

class cs_tower_hangup_data(proto):
	def __init__(self):
		self.session = session_t()
		self.floor = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.floor.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.floor.deserialize(buff)
		return buff

class sc_tower_hangup_data(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hangup_data = hangup_user_info()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hangup_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hangup_data.deserialize(buff)
		return buff

class cs_get_formation_power(proto):
	def __init__(self):
		self.session = session_t()
		self.param = cint32()
		self.formation = arena_formation()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.param.serialize(buff, buff_len)
		buff, buff_len = self.formation.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.param.deserialize(buff)
		buff = self.formation.deserialize(buff)
		return buff

class sc_get_formation_power(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.param = cint32()
		self.power = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.param.serialize(buff, buff_len)
		buff, buff_len = self.power.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.param.deserialize(buff)
		buff = self.power.deserialize(buff)
		return buff

class cs_get_fund_data(proto):
	def __init__(self):
		self.session = session_t()
		self.activityid = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.activityid.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.activityid.deserialize(buff)
		return buff

class sc_get_fund_data(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.num = cint32()
		self.recharge = cbool()
		self.len_of_reward_items = cuint16()
		self.reward_items = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.num.serialize(buff, buff_len)
		buff, buff_len = self.recharge.serialize(buff, buff_len)
		buff, buff_len = self.len_of_reward_items.serialize(buff, buff_len)
		for i in range(self.len_of_reward_items.value):
			buff, buff_len = self.reward_items[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.num.deserialize(buff)
		buff = self.recharge.deserialize(buff)
		buff = self.len_of_reward_items.deserialize(buff)
		self.reward_items = []
		for i in range(self.len_of_reward_items.value):
			self.reward_items.append(cint32())
			buff = self.reward_items[i].deserialize(buff)
		return buff

	def add_reward_items():
		if len(reward_items) >= MAX_FUND_REWARD_ITEM.value:
			return None
		reward_items.append(ccint32())
		return reward_items[len(reward_items) - 1]

class cs_get_month_card_data(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_month_card_data(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_month_card_data = cuint16()
		self.month_card_data = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_month_card_data.serialize(buff, buff_len)
		for i in range(self.len_of_month_card_data.value):
			buff, buff_len = self.month_card_data[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_month_card_data.deserialize(buff)
		self.month_card_data = []
		for i in range(self.len_of_month_card_data.value):
			self.month_card_data.append(user_month_card_t())
			buff = self.month_card_data[i].deserialize(buff)
		return buff

	def add_month_card_data():
		if len(month_card_data) >= MAX_USER_MONTH_CARD.value:
			return None
		month_card_data.append(user_month_card_t())
		return month_card_data[len(month_card_data) - 1]

class cs_pick_month_card_data(proto):
	def __init__(self):
		self.session = session_t()
		self.entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.entry.deserialize(buff)
		return buff

class sc_pick_month_card_data(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.entry = cint32()
		self.len_of_month_card_data = cuint16()
		self.month_card_data = []
		self.rewards = rewards_t()
		self.golds = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_month_card_data.serialize(buff, buff_len)
		for i in range(self.len_of_month_card_data.value):
			buff, buff_len = self.month_card_data[i].serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.golds.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.entry.deserialize(buff)
		buff = self.len_of_month_card_data.deserialize(buff)
		self.month_card_data = []
		for i in range(self.len_of_month_card_data.value):
			self.month_card_data.append(user_month_card_t())
			buff = self.month_card_data[i].deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.golds.deserialize(buff)
		return buff

	def add_month_card_data():
		if len(month_card_data) >= MAX_USER_MONTH_CARD.value:
			return None
		month_card_data.append(user_month_card_t())
		return month_card_data[len(month_card_data) - 1]

class cs_soldier_transform(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()
		self.troop_index = cint32()
		self.soldier_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.troop_index.serialize(buff, buff_len)
		buff, buff_len = self.soldier_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.troop_index.deserialize(buff)
		buff = self.soldier_entry.deserialize(buff)
		return buff

class sc_soldier_transform(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.troop_index = cint32()
		self.troop_data = troops_data_t()
		self.hero_data = hero_data_t()
		self.resources = user_resource_t()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.troop_index.serialize(buff, buff_len)
		buff, buff_len = self.troop_data.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.troop_index.deserialize(buff)
		buff = self.troop_data.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

class cs_modify_name(proto):
	def __init__(self):
		self.session = session_t()
		self.nick_name = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		return buff

class sc_modify_name(proto):
	def __init__(self):
		self.common_result = common_result_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		return buff

class cs_hero_combine(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()
		self.star_lv = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.star_lv.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.star_lv.deserialize(buff)
		return buff

class sc_hero_combine(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []
		self.len_of_reward_hero_list = cuint16()
		self.reward_hero_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_reward_hero_list.serialize(buff, buff_len)
		for i in range(self.len_of_reward_hero_list.value):
			buff, buff_len = self.reward_hero_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		buff = self.len_of_reward_hero_list.deserialize(buff)
		self.reward_hero_list = []
		for i in range(self.len_of_reward_hero_list.value):
			self.reward_hero_list.append(rewards_hero_t())
			buff = self.reward_hero_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

	def add_reward_hero_list():
		if len(reward_hero_list) >= MAX_HERO_COMBINE_NUM.value:
			return None
		reward_hero_list.append(rewards_hero_t())
		return reward_hero_list[len(reward_hero_list) - 1]

class cs_block_spy(proto):
	def __init__(self):
		self.session = session_t()
		self.block_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		return buff

class sc_block_spy(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.block_id = cint32()
		self.len_of_battle_id = cuint16()
		self.battle_id = []
		self.resource_info = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_battle_id.serialize(buff, buff_len)
		for i in range(self.len_of_battle_id.value):
			buff, buff_len = self.battle_id[i].serialize(buff, buff_len)
		buff, buff_len = self.resource_info.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.len_of_battle_id.deserialize(buff)
		self.battle_id = []
		for i in range(self.len_of_battle_id.value):
			self.battle_id.append(cint64())
			buff = self.battle_id[i].deserialize(buff)
		buff = self.resource_info.deserialize(buff)
		return buff

	def add_battle_id():
		if len(battle_id) >= MAX_BATTLE_RECORD_NUM.value:
			return None
		battle_id.append(ccint64())
		return battle_id[len(battle_id) - 1]

class cs_buy_token(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_buy_token(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.token = cint32()
		self.token_buy_times = cint32()
		self.gold = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.token.serialize(buff, buff_len)
		buff, buff_len = self.token_buy_times.serialize(buff, buff_len)
		buff, buff_len = self.gold.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.token.deserialize(buff)
		buff = self.token_buy_times.deserialize(buff)
		buff = self.gold.deserialize(buff)
		return buff

class cs_shop_refresh_buy_times(proto):
	def __init__(self):
		self.session = session_t()
		self.type = E_SHOP_TYPE()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.type.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.type.deserialize(buff)
		return buff

class sc_shop_refresh_buy_times(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.type = E_SHOP_TYPE()
		self.buy_limit = cint32()
		self.currency_info = currency_info_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.type.serialize(buff, buff_len)
		buff, buff_len = self.buy_limit.serialize(buff, buff_len)
		buff, buff_len = self.currency_info.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.type.deserialize(buff)
		buff = self.buy_limit.deserialize(buff)
		buff = self.currency_info.deserialize(buff)
		return buff

class cs_guild_user_mark(proto):
	def __init__(self):
		self.session = session_t()
		self.block_id = cint32()
		self.name = cstring()
		self.notice = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		buff, buff_len = self.notice.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.name.deserialize(buff)
		buff = self.notice.deserialize(buff)
		return buff

class sc_guild_user_mark(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.block_id = cint32()
		self.gold = cint32()
		self.len_of_mark_list = cuint16()
		self.mark_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.gold.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mark_list.serialize(buff, buff_len)
		for i in range(self.len_of_mark_list.value):
			buff, buff_len = self.mark_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.gold.deserialize(buff)
		buff = self.len_of_mark_list.deserialize(buff)
		self.mark_list = []
		for i in range(self.len_of_mark_list.value):
			self.mark_list.append(guild_mark_t())
			buff = self.mark_list[i].deserialize(buff)
		return buff

	def add_mark_list():
		if len(mark_list) >= MAX_GUILD_MARK.value:
			return None
		mark_list.append(guild_mark_t())
		return mark_list[len(mark_list) - 1]

class cs_guild_condition(proto):
	def __init__(self):
		self.session = session_t()
		self.force_limit = cint32()
		self.is_limit = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.force_limit.serialize(buff, buff_len)
		buff, buff_len = self.is_limit.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.force_limit.deserialize(buff)
		buff = self.is_limit.deserialize(buff)
		return buff

class sc_guild_condition(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.guild_data = guild_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.guild_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.guild_data.deserialize(buff)
		return buff

class cs_wash_skill(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()
		self.skill_index = cint32()
		self.wash_quality = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.skill_index.serialize(buff, buff_len)
		buff, buff_len = self.wash_quality.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.skill_index.deserialize(buff)
		buff = self.wash_quality.deserialize(buff)
		return buff

class sc_wash_skill(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.skill_index = cint32()
		self.hero_data = hero_data_t()
		self.resources = user_resource_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []
		self.result = e_op_result()
		self.wash_count = cint32()
		self.total_consume_gold = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.skill_index.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.result.serialize(buff, buff_len)
		buff, buff_len = self.wash_count.serialize(buff, buff_len)
		buff, buff_len = self.total_consume_gold.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.skill_index.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		buff = self.result.deserialize(buff)
		buff = self.wash_count.deserialize(buff)
		buff = self.total_consume_gold.deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_wash_skill_affirm(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()
		self.skill_index = cint32()
		self.affirm = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.skill_index.serialize(buff, buff_len)
		buff, buff_len = self.affirm.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.skill_index.deserialize(buff)
		buff = self.affirm.deserialize(buff)
		return buff

class sc_wash_skill_affirm(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.affirm = cbool()
		self.skill_index = cint32()
		self.hero_data = hero_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.affirm.serialize(buff, buff_len)
		buff, buff_len = self.skill_index.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.affirm.deserialize(buff)
		buff = self.skill_index.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		return buff

class cs_get_user_mark(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_user_mark(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_data_list = cuint16()
		self.data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_data_list.value):
			buff, buff_len = self.data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_data_list.deserialize(buff)
		self.data_list = []
		for i in range(self.len_of_data_list.value):
			self.data_list.append(user_mark_t())
			buff = self.data_list[i].deserialize(buff)
		return buff

	def add_data_list():
		if len(data_list) >= MAX_USER_MARK.value:
			return None
		data_list.append(user_mark_t())
		return data_list[len(data_list) - 1]

class cs_set_user_mark(proto):
	def __init__(self):
		self.session = session_t()
		self.block_id = cint32()
		self.name = cstring()
		self.notice = cstring()
		self.is_add = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		buff, buff_len = self.notice.serialize(buff, buff_len)
		buff, buff_len = self.is_add.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.name.deserialize(buff)
		buff = self.notice.deserialize(buff)
		buff = self.is_add.deserialize(buff)
		return buff

class sc_set_user_mark(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.is_add = cbool()
		self.block_id = cint32()
		self.len_of_data_list = cuint16()
		self.data_list = []
		self.gold = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.is_add.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_data_list.value):
			buff, buff_len = self.data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.gold.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.is_add.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.len_of_data_list.deserialize(buff)
		self.data_list = []
		for i in range(self.len_of_data_list.value):
			self.data_list.append(user_mark_t())
			buff = self.data_list[i].deserialize(buff)
		buff = self.gold.deserialize(buff)
		return buff

	def add_data_list():
		if len(data_list) >= MAX_USER_MARK.value:
			return None
		data_list.append(user_mark_t())
		return data_list[len(data_list) - 1]

class cs_get_block_mark(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_block_mark(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_data_list = cuint16()
		self.data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_data_list.value):
			buff, buff_len = self.data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_data_list.deserialize(buff)
		self.data_list = []
		for i in range(self.len_of_data_list.value):
			self.data_list.append(block_mark_t())
			buff = self.data_list[i].deserialize(buff)
		return buff

	def add_data_list():
		if len(data_list) >= MAX_BLOCK_MARK.value:
			return None
		data_list.append(block_mark_t())
		return data_list[len(data_list) - 1]

class cs_add_block_mark(proto):
	def __init__(self):
		self.session = session_t()
		self.block_id = cint32()
		self.name = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.name.deserialize(buff)
		return buff

class sc_add_block_mark(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.block_id = cint32()
		self.len_of_data_list = cuint16()
		self.data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_data_list.value):
			buff, buff_len = self.data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.len_of_data_list.deserialize(buff)
		self.data_list = []
		for i in range(self.len_of_data_list.value):
			self.data_list.append(block_mark_t())
			buff = self.data_list[i].deserialize(buff)
		return buff

	def add_data_list():
		if len(data_list) >= MAX_BLOCK_MARK.value:
			return None
		data_list.append(block_mark_t())
		return data_list[len(data_list) - 1]

class cs_del_block_mark(proto):
	def __init__(self):
		self.session = session_t()
		self.block_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		return buff

class sc_del_block_mark(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.block_id = cint32()
		self.len_of_data_list = cuint16()
		self.data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_data_list.value):
			buff, buff_len = self.data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.len_of_data_list.deserialize(buff)
		self.data_list = []
		for i in range(self.len_of_data_list.value):
			self.data_list.append(block_mark_t())
			buff = self.data_list[i].deserialize(buff)
		return buff

	def add_data_list():
		if len(data_list) >= MAX_BLOCK_MARK.value:
			return None
		data_list.append(block_mark_t())
		return data_list[len(data_list) - 1]

class cs_get_chapter_rewards(proto):
	def __init__(self):
		self.session = session_t()
		self.chapter = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.chapter.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.chapter.deserialize(buff)
		return buff

class sc_get_chapter_rewards(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.tasks = fame_task_t()
		self.rewards = rewards_t()
		self.timed_super_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.tasks.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.timed_super_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.tasks.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.timed_super_id.deserialize(buff)
		return buff

class cs_get_fame_rewards(proto):
	def __init__(self):
		self.session = session_t()
		self.stage = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.stage.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.stage.deserialize(buff)
		return buff

class sc_get_fame_rewards(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.fame = cint32()
		self.len_of_fame_rewards = cuint16()
		self.fame_rewards = []
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.fame.serialize(buff, buff_len)
		buff, buff_len = self.len_of_fame_rewards.serialize(buff, buff_len)
		for i in range(self.len_of_fame_rewards.value):
			buff, buff_len = self.fame_rewards[i].serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.fame.deserialize(buff)
		buff = self.len_of_fame_rewards.deserialize(buff)
		self.fame_rewards = []
		for i in range(self.len_of_fame_rewards.value):
			self.fame_rewards.append(E_MISSION_STATUS())
			buff = self.fame_rewards[i].deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

	def add_fame_rewards():
		if len(fame_rewards) >= MAX_FAME_REAWRD_NUM.value:
			return None
		fame_rewards.append(E_MISSION_STATUS())
		return fame_rewards[len(fame_rewards) - 1]

class cs_get_npc_info(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_npc_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_npc_info_list = cuint16()
		self.npc_info_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_npc_info_list.serialize(buff, buff_len)
		for i in range(self.len_of_npc_info_list.value):
			buff, buff_len = self.npc_info_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_npc_info_list.deserialize(buff)
		self.npc_info_list = []
		for i in range(self.len_of_npc_info_list.value):
			self.npc_info_list.append(npc_info_t())
			buff = self.npc_info_list[i].deserialize(buff)
		return buff

	def add_npc_info_list():
		if len(npc_info_list) >= MAX_NPC_DLG_GROUP_NUM.value:
			return None
		npc_info_list.append(npc_info_t())
		return npc_info_list[len(npc_info_list) - 1]

class cs_get_npc_group_info(proto):
	def __init__(self):
		self.session = session_t()
		self.group_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.group_id.deserialize(buff)
		return buff

class sc_get_npc_group_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.npc_info = npc_info_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.npc_info.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.npc_info.deserialize(buff)
		return buff

class cs_open_npc_dialogue(proto):
	def __init__(self):
		self.session = session_t()
		self.group_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.group_id.deserialize(buff)
		return buff

class sc_open_npc_dialogue(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.npc_info = npc_info_t()
		self.len_of_rewards = cuint16()
		self.rewards = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.npc_info.serialize(buff, buff_len)
		buff, buff_len = self.len_of_rewards.serialize(buff, buff_len)
		for i in range(self.len_of_rewards.value):
			buff, buff_len = self.rewards[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.npc_info.deserialize(buff)
		buff = self.len_of_rewards.deserialize(buff)
		self.rewards = []
		for i in range(self.len_of_rewards.value):
			self.rewards.append(rewards_t())
			buff = self.rewards[i].deserialize(buff)
		return buff

	def add_rewards():
		if len(rewards) >= MAX_OPEN_NPC_DLG_REWARD_NUM.value:
			return None
		rewards.append(rewards_t())
		return rewards[len(rewards) - 1]

class cs_get_npc_rewards(proto):
	def __init__(self):
		self.session = session_t()
		self.ntype = cint32()
		self.group_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.ntype.serialize(buff, buff_len)
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.ntype.deserialize(buff)
		buff = self.group_id.deserialize(buff)
		return buff

class sc_get_npc_rewards(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.ntype = cint32()
		self.npc_info = npc_info_t()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.ntype.serialize(buff, buff_len)
		buff, buff_len = self.npc_info.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.ntype.deserialize(buff)
		buff = self.npc_info.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

class cs_npc_exchange(proto):
	def __init__(self):
		self.session = session_t()
		self.group_id = cint32()
		self.from_count = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		buff, buff_len = self.from_count.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.group_id.deserialize(buff)
		buff = self.from_count.deserialize(buff)
		return buff

class sc_npc_exchange(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.resources = user_resource_t()
		self.npc_info = npc_info_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.npc_info.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.npc_info.deserialize(buff)
		return buff

class cs_get_museum_collection_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_museum_collection_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_museum_collection_list = cuint16()
		self.museum_collection_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_museum_collection_list.serialize(buff, buff_len)
		for i in range(self.len_of_museum_collection_list.value):
			buff, buff_len = self.museum_collection_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_museum_collection_list.deserialize(buff)
		self.museum_collection_list = []
		for i in range(self.len_of_museum_collection_list.value):
			self.museum_collection_list.append(museum_collection_t())
			buff = self.museum_collection_list[i].deserialize(buff)
		return buff

	def add_museum_collection_list():
		if len(museum_collection_list) >= MAX_GET_MUSEUM_COLLECTION_NUM.value:
			return None
		museum_collection_list.append(museum_collection_t())
		return museum_collection_list[len(museum_collection_list) - 1]

class cs_museum_collection_reward_draw(proto):
	def __init__(self):
		self.session = session_t()
		self.museum_collection_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.museum_collection_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.museum_collection_entry.deserialize(buff)
		return buff

class sc_museum_collection_reward_draw(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.museum_collection = museum_collection_t()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.museum_collection.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.museum_collection.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

class cs_get_museum_group_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_museum_group_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_museum_group_list = cuint16()
		self.museum_group_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_museum_group_list.serialize(buff, buff_len)
		for i in range(self.len_of_museum_group_list.value):
			buff, buff_len = self.museum_group_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_museum_group_list.deserialize(buff)
		self.museum_group_list = []
		for i in range(self.len_of_museum_group_list.value):
			self.museum_group_list.append(museum_group_t())
			buff = self.museum_group_list[i].deserialize(buff)
		return buff

	def add_museum_group_list():
		if len(museum_group_list) >= MAX_GET_MUSEUM_GROUP_NUM.value:
			return None
		museum_group_list.append(museum_group_t())
		return museum_group_list[len(museum_group_list) - 1]

class cs_museum_group_active(proto):
	def __init__(self):
		self.session = session_t()
		self.museum_group_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.museum_group_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.museum_group_entry.deserialize(buff)
		return buff

class sc_museum_group_active(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.museum_group = museum_group_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.museum_group.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.museum_group.deserialize(buff)
		return buff

class cs_guild_assist(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()
		self.build_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.build_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.build_id.deserialize(buff)
		return buff

class sc_guild_assist(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.game_event_data = game_event_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.game_event_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.game_event_data.deserialize(buff)
		return buff

class cs_get_guild_assist(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_guild_assist(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.assist_other_times = cint32()
		self.len_of_assist_list = cuint16()
		self.assist_list = []
		self.has_assist = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.assist_other_times.serialize(buff, buff_len)
		buff, buff_len = self.len_of_assist_list.serialize(buff, buff_len)
		for i in range(self.len_of_assist_list.value):
			buff, buff_len = self.assist_list[i].serialize(buff, buff_len)
		buff, buff_len = self.has_assist.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.assist_other_times.deserialize(buff)
		buff = self.len_of_assist_list.deserialize(buff)
		self.assist_list = []
		for i in range(self.len_of_assist_list.value):
			self.assist_list.append(guild_assist_event_t())
			buff = self.assist_list[i].deserialize(buff)
		buff = self.has_assist.deserialize(buff)
		return buff

	def add_assist_list():
		if len(assist_list) >= MAX_ASSIST_NUM.value:
			return None
		assist_list.append(guild_assist_event_t())
		return assist_list[len(assist_list) - 1]

class cs_guild_assist_other(proto):
	def __init__(self):
		self.session = session_t()
		self.event_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		return buff

class sc_guild_assist_other(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.event_id = cint64()
		self.assist_other_times = cint32()
		self.assist_times = cint32()
		self.len_of_assist_list = cuint16()
		self.assist_list = []
		self.has_assist = cbool()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.assist_other_times.serialize(buff, buff_len)
		buff, buff_len = self.assist_times.serialize(buff, buff_len)
		buff, buff_len = self.len_of_assist_list.serialize(buff, buff_len)
		for i in range(self.len_of_assist_list.value):
			buff, buff_len = self.assist_list[i].serialize(buff, buff_len)
		buff, buff_len = self.has_assist.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.assist_other_times.deserialize(buff)
		buff = self.assist_times.deserialize(buff)
		buff = self.len_of_assist_list.deserialize(buff)
		self.assist_list = []
		for i in range(self.len_of_assist_list.value):
			self.assist_list.append(guild_assist_event_t())
			buff = self.assist_list[i].deserialize(buff)
		buff = self.has_assist.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

	def add_assist_list():
		if len(assist_list) >= MAX_ASSIST_NUM.value:
			return None
		assist_list.append(guild_assist_event_t())
		return assist_list[len(assist_list) - 1]

class cs_sync_user_event_flag_with_param(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_sync_user_event_flag_with_param(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_flag_list = cuint16()
		self.flag_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_flag_list.serialize(buff, buff_len)
		for i in range(self.len_of_flag_list.value):
			buff, buff_len = self.flag_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_flag_list.deserialize(buff)
		self.flag_list = []
		for i in range(self.len_of_flag_list.value):
			self.flag_list.append(user_event_flag_with_param())
			buff = self.flag_list[i].deserialize(buff)
		return buff

	def add_flag_list():
		if len(flag_list) >= MAX_USER_FLAG_NUM.value:
			return None
		flag_list.append(user_event_flag_with_param())
		return flag_list[len(flag_list) - 1]

class cs_get_game_event(proto):
	def __init__(self):
		self.session = session_t()
		self.event_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		return buff

class sc_get_game_event(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.game_event_data = game_event_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.game_event_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.game_event_data.deserialize(buff)
		return buff

class cs_discovery_get(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_discovery_get(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.data = user_discovery_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.data.deserialize(buff)
		return buff

class cs_discovery_find(proto):
	def __init__(self):
		self.session = session_t()
		self.region = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.region.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.region.deserialize(buff)
		return buff

class sc_discovery_find(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.region = cint32()
		self.data = user_discovery_t()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.region.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.region.deserialize(buff)
		buff = self.data.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_DISCOVERY_EVENT.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

class cs_discovery_catch(proto):
	def __init__(self):
		self.session = session_t()
		self.event_id = cint64()
		self.hero_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		return buff

class sc_discovery_catch(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.event_id = cint64()
		self.hero_entry = cint32()
		self.data = user_discovery_t()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []
		self.hero = hero_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.hero.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.data.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		buff = self.hero.deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_DISCOVERY_EVENT.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

class cs_discovery_trigger(proto):
	def __init__(self):
		self.session = session_t()
		self.event_id = cint64()
		self.hero_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		return buff

class sc_discovery_trigger(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_entry = cint32()
		self.data = user_discovery_t()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []
		self.hero = hero_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.hero.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.data.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		buff = self.hero.deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_DISCOVERY_EVENT.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

class cs_discovery_quit(proto):
	def __init__(self):
		self.session = session_t()
		self.event_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		return buff

class sc_discovery_quit(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.event_id = cint64()
		self.data = user_discovery_t()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []
		self.hero = hero_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.hero.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.data.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		buff = self.hero.deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_DISCOVERY_EVENT.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

class cs_get_guild_assist_resource_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_guild_assist_resource_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_assist_res_list = cuint16()
		self.assist_res_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_assist_res_list.serialize(buff, buff_len)
		for i in range(self.len_of_assist_res_list.value):
			buff, buff_len = self.assist_res_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_assist_res_list.deserialize(buff)
		self.assist_res_list = []
		for i in range(self.len_of_assist_res_list.value):
			self.assist_res_list.append(user_seized_resource())
			buff = self.assist_res_list[i].deserialize(buff)
		return buff

	def add_assist_res_list():
		if len(assist_res_list) >= MAX_GUILD_ASSIST_RESOURCE_PER_PAGE.value:
			return None
		assist_res_list.append(user_seized_resource())
		return assist_res_list[len(assist_res_list) - 1]

class cs_guild_assist_res_other(proto):
	def __init__(self):
		self.session = session_t()
		self.event_id = cint64()
		self.resource_info = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.resource_info.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.resource_info.deserialize(buff)
		return buff

class sc_guild_assist_res_other(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.game_event_data = game_event_data_t()
		self.len_of_assist_res_list = cuint16()
		self.assist_res_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.game_event_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_assist_res_list.serialize(buff, buff_len)
		for i in range(self.len_of_assist_res_list.value):
			buff, buff_len = self.assist_res_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.game_event_data.deserialize(buff)
		buff = self.len_of_assist_res_list.deserialize(buff)
		self.assist_res_list = []
		for i in range(self.len_of_assist_res_list.value):
			self.assist_res_list.append(user_seized_resource())
			buff = self.assist_res_list[i].deserialize(buff)
		return buff

	def add_assist_res_list():
		if len(assist_res_list) >= MAX_GUILD_ASSIST_RESOURCE_PER_PAGE.value:
			return None
		assist_res_list.append(user_seized_resource())
		return assist_res_list[len(assist_res_list) - 1]

class cs_get_adventure_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_adventure_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_events = cuint16()
		self.events = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_events.serialize(buff, buff_len)
		for i in range(self.len_of_events.value):
			buff, buff_len = self.events[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_events.deserialize(buff)
		self.events = []
		for i in range(self.len_of_events.value):
			self.events.append(adventure_event())
			buff = self.events[i].deserialize(buff)
		return buff

	def add_events():
		if len(events) >= MAX_ADVENTURE_EVENT_NUM.value:
			return None
		events.append(adventure_event())
		return events[len(events) - 1]

class cs_get_adventure_event(proto):
	def __init__(self):
		self.session = session_t()
		self.event_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		return buff

class sc_get_adventure_event(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.event_id = cint64()
		self.adventure_group_id = cint32()
		self.adventure_event_id = cint32()
		self.total_times = cint32()
		self.buy_times = cint32()
		self.cur_times = cint32()
		self.dest_block_id = cint32()
		self.refer = cint32()
		self.museum_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.adventure_group_id.serialize(buff, buff_len)
		buff, buff_len = self.adventure_event_id.serialize(buff, buff_len)
		buff, buff_len = self.total_times.serialize(buff, buff_len)
		buff, buff_len = self.buy_times.serialize(buff, buff_len)
		buff, buff_len = self.cur_times.serialize(buff, buff_len)
		buff, buff_len = self.dest_block_id.serialize(buff, buff_len)
		buff, buff_len = self.refer.serialize(buff, buff_len)
		buff, buff_len = self.museum_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.adventure_group_id.deserialize(buff)
		buff = self.adventure_event_id.deserialize(buff)
		buff = self.total_times.deserialize(buff)
		buff = self.buy_times.deserialize(buff)
		buff = self.cur_times.deserialize(buff)
		buff = self.dest_block_id.deserialize(buff)
		buff = self.refer.deserialize(buff)
		buff = self.museum_id.deserialize(buff)
		return buff

class cs_adventure_step(proto):
	def __init__(self):
		self.session = session_t()
		self.event_id = cint64()
		self.refer = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.refer.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.refer.deserialize(buff)
		return buff

class sc_adventure_step(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.event_id = cint64()
		self.refer = cint32()
		self.cur_times = cint32()
		self.over = cbool()
		self.success = cbool()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.refer.serialize(buff, buff_len)
		buff, buff_len = self.cur_times.serialize(buff, buff_len)
		buff, buff_len = self.over.serialize(buff, buff_len)
		buff, buff_len = self.success.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.refer.deserialize(buff)
		buff = self.cur_times.deserialize(buff)
		buff = self.over.deserialize(buff)
		buff = self.success.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

class cs_adventure_buy_times(proto):
	def __init__(self):
		self.session = session_t()
		self.event_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		return buff

class sc_adventure_buy_times(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.event_id = cint64()
		self.buy_times = cint32()
		self.total_times = cint32()
		self.resources = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.buy_times.serialize(buff, buff_len)
		buff, buff_len = self.total_times.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.buy_times.deserialize(buff)
		buff = self.total_times.deserialize(buff)
		buff = self.resources.deserialize(buff)
		return buff

class cs_query_reserver_soldier(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		return buff

class sc_query_reserver_soldier(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_reserver_soldier_list = cuint16()
		self.reserver_soldier_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_reserver_soldier_list.serialize(buff, buff_len)
		for i in range(self.len_of_reserver_soldier_list.value):
			buff, buff_len = self.reserver_soldier_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_reserver_soldier_list.deserialize(buff)
		self.reserver_soldier_list = []
		for i in range(self.len_of_reserver_soldier_list.value):
			self.reserver_soldier_list.append(reserver_soldier_t())
			buff = self.reserver_soldier_list[i].deserialize(buff)
		return buff

	def add_reserver_soldier_list():
		if len(reserver_soldier_list) >= MAX_CASTLE_NUM.value:
			return None
		reserver_soldier_list.append(reserver_soldier_t())
		return reserver_soldier_list[len(reserver_soldier_list) - 1]

class cs_use_reserver_soldier(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()
		self.len_of_soldier_count = cuint16()
		self.soldier_count = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.len_of_soldier_count.serialize(buff, buff_len)
		for i in range(self.len_of_soldier_count.value):
			buff, buff_len = self.soldier_count[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.len_of_soldier_count.deserialize(buff)
		self.soldier_count = []
		for i in range(self.len_of_soldier_count.value):
			self.soldier_count.append(cint32())
			buff = self.soldier_count[i].deserialize(buff)
		return buff

	def add_soldier_count():
		if len(soldier_count) >= MAX_CORPS_TROOPS_NUM.value:
			return None
		soldier_count.append(ccint32())
		return soldier_count[len(soldier_count) - 1]

class sc_use_reserver_soldier(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.len_of_troop_data = cuint16()
		self.troop_data = []
		self.resources = user_resource_t()
		self.reserver_soldier = reserver_soldier_t()
		self.event_data = game_event_data_t()
		self.len_of_soldier_count = cuint16()
		self.soldier_count = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.len_of_troop_data.serialize(buff, buff_len)
		for i in range(self.len_of_troop_data.value):
			buff, buff_len = self.troop_data[i].serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.reserver_soldier.serialize(buff, buff_len)
		buff, buff_len = self.event_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_soldier_count.serialize(buff, buff_len)
		for i in range(self.len_of_soldier_count.value):
			buff, buff_len = self.soldier_count[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.len_of_troop_data.deserialize(buff)
		self.troop_data = []
		for i in range(self.len_of_troop_data.value):
			self.troop_data.append(troops_data_t())
			buff = self.troop_data[i].deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.reserver_soldier.deserialize(buff)
		buff = self.event_data.deserialize(buff)
		buff = self.len_of_soldier_count.deserialize(buff)
		self.soldier_count = []
		for i in range(self.len_of_soldier_count.value):
			self.soldier_count.append(cint32())
			buff = self.soldier_count[i].deserialize(buff)
		return buff

	def add_troop_data():
		if len(troop_data) >= MAX_CORPS_TROOPS_NUM.value:
			return None
		troop_data.append(troops_data_t())
		return troop_data[len(troop_data) - 1]

	def add_soldier_count():
		if len(soldier_count) >= MAX_CORPS_TROOPS_NUM.value:
			return None
		soldier_count.append(ccint32())
		return soldier_count[len(soldier_count) - 1]

class cs_adventure_exit(proto):
	def __init__(self):
		self.session = session_t()
		self.event_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		return buff

class sc_adventure_exit(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_events = cuint16()
		self.events = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_events.serialize(buff, buff_len)
		for i in range(self.len_of_events.value):
			buff, buff_len = self.events[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_events.deserialize(buff)
		self.events = []
		for i in range(self.len_of_events.value):
			self.events.append(adventure_event())
			buff = self.events[i].deserialize(buff)
		return buff

	def add_events():
		if len(events) >= MAX_ADVENTURE_EVENT_NUM.value:
			return None
		events.append(adventure_event())
		return events[len(events) - 1]

class cs_get_raffle_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_raffle_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_raffle_list = cuint16()
		self.raffle_list = []
		self.len_of_finish_list = cuint16()
		self.finish_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_raffle_list.serialize(buff, buff_len)
		for i in range(self.len_of_raffle_list.value):
			buff, buff_len = self.raffle_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_finish_list.serialize(buff, buff_len)
		for i in range(self.len_of_finish_list.value):
			buff, buff_len = self.finish_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_raffle_list.deserialize(buff)
		self.raffle_list = []
		for i in range(self.len_of_raffle_list.value):
			self.raffle_list.append(raffle_data())
			buff = self.raffle_list[i].deserialize(buff)
		buff = self.len_of_finish_list.deserialize(buff)
		self.finish_list = []
		for i in range(self.len_of_finish_list.value):
			self.finish_list.append(cint32())
			buff = self.finish_list[i].deserialize(buff)
		return buff

	def add_raffle_list():
		if len(raffle_list) >= MAX_RAFFLE_EVENT_NUM.value:
			return None
		raffle_list.append(raffle_data())
		return raffle_list[len(raffle_list) - 1]

	def add_finish_list():
		if len(finish_list) >= MAX_RAFFLE_EVENT_NUM.value:
			return None
		finish_list.append(ccint32())
		return finish_list[len(finish_list) - 1]

class cs_raffle_draw(proto):
	def __init__(self):
		self.session = session_t()
		self.raffle_id = cint32()
		self.draw_count = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.raffle_id.serialize(buff, buff_len)
		buff, buff_len = self.draw_count.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.raffle_id.deserialize(buff)
		buff = self.draw_count.deserialize(buff)
		return buff

class sc_raffle_draw(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.raffle_id = cint32()
		self.data = raffle_data()
		self.resources = user_resource_t()
		self.rewards = rewards_t()
		self.len_of_lottery_reward_list = cuint16()
		self.lottery_reward_list = []
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []
		self.timed_super_id = cint32()
		self.item_data = item_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.raffle_id.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.len_of_lottery_reward_list.serialize(buff, buff_len)
		for i in range(self.len_of_lottery_reward_list.value):
			buff, buff_len = self.lottery_reward_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.timed_super_id.serialize(buff, buff_len)
		buff, buff_len = self.item_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.raffle_id.deserialize(buff)
		buff = self.data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.len_of_lottery_reward_list.deserialize(buff)
		self.lottery_reward_list = []
		for i in range(self.len_of_lottery_reward_list.value):
			self.lottery_reward_list.append(reward_info_t())
			buff = self.lottery_reward_list[i].deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		buff = self.timed_super_id.deserialize(buff)
		buff = self.item_data.deserialize(buff)
		return buff

	def add_lottery_reward_list():
		if len(lottery_reward_list) >= MAX_RAFFLE_REWARD_NUM.value:
			return None
		lottery_reward_list.append(reward_info_t())
		return lottery_reward_list[len(lottery_reward_list) - 1]

	def add_item_data_list():
		if len(item_data_list) >= MAX_PRESENT_ITEM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_hero_chip_replace(proto):
	def __init__(self):
		self.session = session_t()
		self.item_entry = cint32()
		self.get_item_data = item_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.get_item_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.get_item_data.deserialize(buff)
		return buff

class sc_hero_chip_replace(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_HERO_CHIP_OPER_ITEM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_get_raffle_data(proto):
	def __init__(self):
		self.session = session_t()
		self.raffle_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.raffle_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.raffle_id.deserialize(buff)
		return buff

class sc_get_raffle_data(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.raffle = raffle_data()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.raffle.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.raffle.deserialize(buff)
		return buff

class cs_del_mail_list(proto):
	def __init__(self):
		self.session = session_t()
		self.len_of_mail_id_list = cuint16()
		self.mail_id_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mail_id_list.serialize(buff, buff_len)
		for i in range(self.len_of_mail_id_list.value):
			buff, buff_len = self.mail_id_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.len_of_mail_id_list.deserialize(buff)
		self.mail_id_list = []
		for i in range(self.len_of_mail_id_list.value):
			self.mail_id_list.append(cint64())
			buff = self.mail_id_list[i].deserialize(buff)
		return buff

	def add_mail_id_list():
		if len(mail_id_list) >= MAX_MAIL_COUNT.value:
			return None
		mail_id_list.append(ccint64())
		return mail_id_list[len(mail_id_list) - 1]

class sc_del_mail_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_mail_id_list = cuint16()
		self.mail_id_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mail_id_list.serialize(buff, buff_len)
		for i in range(self.len_of_mail_id_list.value):
			buff, buff_len = self.mail_id_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_mail_id_list.deserialize(buff)
		self.mail_id_list = []
		for i in range(self.len_of_mail_id_list.value):
			self.mail_id_list.append(cint64())
			buff = self.mail_id_list[i].deserialize(buff)
		return buff

	def add_mail_id_list():
		if len(mail_id_list) >= MAX_MAIL_COUNT.value:
			return None
		mail_id_list.append(ccint64())
		return mail_id_list[len(mail_id_list) - 1]

class cs_one_key_mail_affix_pick(proto):
	def __init__(self):
		self.session = session_t()
		self.len_of_mail_id_list = cuint16()
		self.mail_id_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mail_id_list.serialize(buff, buff_len)
		for i in range(self.len_of_mail_id_list.value):
			buff, buff_len = self.mail_id_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.len_of_mail_id_list.deserialize(buff)
		self.mail_id_list = []
		for i in range(self.len_of_mail_id_list.value):
			self.mail_id_list.append(cint64())
			buff = self.mail_id_list[i].deserialize(buff)
		return buff

	def add_mail_id_list():
		if len(mail_id_list) >= MAX_MAIL_COUNT.value:
			return None
		mail_id_list.append(ccint64())
		return mail_id_list[len(mail_id_list) - 1]

class sc_one_key_mail_affix_pick(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_mail_id_list = cuint16()
		self.mail_id_list = []
		self.rewards = rewards_t()
		self.user_res = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mail_id_list.serialize(buff, buff_len)
		for i in range(self.len_of_mail_id_list.value):
			buff, buff_len = self.mail_id_list[i].serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.user_res.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_mail_id_list.deserialize(buff)
		self.mail_id_list = []
		for i in range(self.len_of_mail_id_list.value):
			self.mail_id_list.append(cint64())
			buff = self.mail_id_list[i].deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.user_res.deserialize(buff)
		return buff

	def add_mail_id_list():
		if len(mail_id_list) >= MAX_MAIL_COUNT.value:
			return None
		mail_id_list.append(ccint64())
		return mail_id_list[len(mail_id_list) - 1]

class cs_corps_recover_phy(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		return buff

class sc_corps_recover_phy(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.corps_data = corps_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.corps_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.corps_data.deserialize(buff)
		return buff

class cs_accelerate_game_event(proto):
	def __init__(self):
		self.session = session_t()
		self.event_id = cint64()
		self.item_entry = cint32()
		self.item_num = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.item_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.item_num.deserialize(buff)
		return buff

class sc_accelerate_game_event(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.event_id = cint64()
		self.item_entry = cint32()
		self.item_num = cint32()
		self.resources = user_resource_t()
		self.event_data = game_event_data_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.item_num.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.event_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.item_num.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.event_data.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_discovery_buy_times(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_discovery_buy_times(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_discovery_info = user_discovery_t()
		self.resources = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_discovery_info.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_discovery_info.deserialize(buff)
		buff = self.resources.deserialize(buff)
		return buff

class cs_get_mission_by_entry(proto):
	def __init__(self):
		self.session = session_t()
		self.entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.entry.deserialize(buff)
		return buff

class sc_get_mission_by_entry(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.mission_data = mission_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.mission_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.mission_data.deserialize(buff)
		return buff

class cs_hero_reset(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		return buff

class sc_hero_reset(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.hero_data = hero_data_t()
		self.resources = user_resource_t()
		self.len_of_item_data_list = cuint16()
		self.item_data_list = []
		self.surplus_reset_time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.hero_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_data_list.value):
			buff, buff_len = self.item_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.surplus_reset_time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.hero_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.len_of_item_data_list.deserialize(buff)
		self.item_data_list = []
		for i in range(self.len_of_item_data_list.value):
			self.item_data_list.append(item_data_t())
			buff = self.item_data_list[i].deserialize(buff)
		buff = self.surplus_reset_time.deserialize(buff)
		return buff

	def add_item_data_list():
		if len(item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_data_list.append(item_data_t())
		return item_data_list[len(item_data_list) - 1]

class cs_hero_reset_info(proto):
	def __init__(self):
		self.session = session_t()
		self.hero_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		return buff

class sc_hero_reset_info(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.surplus_reset_time = cint32()
		self.hero_entry = cint32()
		self.hero_reset_reback = hero_reset_reback_t()
		self.corps_key = corps_key_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.surplus_reset_time.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.hero_reset_reback.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.surplus_reset_time.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.hero_reset_reback.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		return buff

class cs_get_block_array_by_index(proto):
	def __init__(self):
		self.session = session_t()
		self.index = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.index.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.index.deserialize(buff)
		return buff

class sc_get_block_array_by_index(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_block_array = cuint16()
		self.block_array = []
		self.index = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_block_array.serialize(buff, buff_len)
		for i in range(self.len_of_block_array.value):
			buff, buff_len = self.block_array[i].serialize(buff, buff_len)
		buff, buff_len = self.index.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_block_array.deserialize(buff)
		self.block_array = []
		for i in range(self.len_of_block_array.value):
			self.block_array.append(cint32())
			buff = self.block_array[i].deserialize(buff)
		buff = self.index.deserialize(buff)
		return buff

	def add_block_array():
		if len(block_array) >= MAX_MIN_MAP_NUM.value:
			return None
		block_array.append(ccint32())
		return block_array[len(block_array) - 1]

class cs_buy_reserver_soldier(proto):
	def __init__(self):
		self.session = session_t()
		self.castle_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		return buff

class sc_buy_reserver_soldier(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.reserver_soldier = reserver_soldier_t()
		self.resources = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.reserver_soldier.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.reserver_soldier.deserialize(buff)
		buff = self.resources.deserialize(buff)
		return buff

class cs_corps_crusade(proto):
	def __init__(self):
		self.session = session_t()
		self.corps_key = corps_key_t()
		self.block_id = cint32()
		self.use_token = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.use_token.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.use_token.deserialize(buff)
		return buff

class sc_corps_crusade(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corps_key = corps_key_t()
		self.len_of_game_event_data_list = cuint16()
		self.game_event_data_list = []
		self.len_of_corps_data_list = cuint16()
		self.corps_data_list = []
		self.use_token = cbool()
		self.token = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.len_of_game_event_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_game_event_data_list.value):
			buff, buff_len = self.game_event_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_corps_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_corps_data_list.value):
			buff, buff_len = self.corps_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.use_token.serialize(buff, buff_len)
		buff, buff_len = self.token.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.len_of_game_event_data_list.deserialize(buff)
		self.game_event_data_list = []
		for i in range(self.len_of_game_event_data_list.value):
			self.game_event_data_list.append(game_event_data_t())
			buff = self.game_event_data_list[i].deserialize(buff)
		buff = self.len_of_corps_data_list.deserialize(buff)
		self.corps_data_list = []
		for i in range(self.len_of_corps_data_list.value):
			self.corps_data_list.append(corps_data_t())
			buff = self.corps_data_list[i].deserialize(buff)
		buff = self.use_token.deserialize(buff)
		buff = self.token.deserialize(buff)
		return buff

	def add_game_event_data_list():
		if len(game_event_data_list) >= MAX_GAME_EVENT_NUM.value:
			return None
		game_event_data_list.append(game_event_data_t())
		return game_event_data_list[len(game_event_data_list) - 1]

	def add_corps_data_list():
		if len(corps_data_list) >= MAX_CORPS_COUNT.value:
			return None
		corps_data_list.append(corps_data_t())
		return corps_data_list[len(corps_data_list) - 1]

class cs_get_wtquest_list(proto):
	def __init__(self):
		self.session = session_t()
		self.wt_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.wt_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.wt_entry.deserialize(buff)
		return buff

class sc_get_wtquest_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.wt_entry = cint32()
		self.len_of_quest_list = cuint16()
		self.quest_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.wt_entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_quest_list.serialize(buff, buff_len)
		for i in range(self.len_of_quest_list.value):
			buff, buff_len = self.quest_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.wt_entry.deserialize(buff)
		buff = self.len_of_quest_list.deserialize(buff)
		self.quest_list = []
		for i in range(self.len_of_quest_list.value):
			self.quest_list.append(wt_quest_t())
			buff = self.quest_list[i].deserialize(buff)
		return buff

	def add_quest_list():
		if len(quest_list) >= MAX_WT_GROUP_QUEST_NUM.value:
			return None
		quest_list.append(wt_quest_t())
		return quest_list[len(quest_list) - 1]

class cs_get_wtquest_rewards(proto):
	def __init__(self):
		self.session = session_t()
		self.wt_entry = cint32()
		self.wtquest_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.wt_entry.serialize(buff, buff_len)
		buff, buff_len = self.wtquest_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.wt_entry.deserialize(buff)
		buff = self.wtquest_entry.deserialize(buff)
		return buff

class sc_get_wtquest_rewards(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.wt_entry = cint32()
		self.quest_data = wt_quest_t()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.wt_entry.serialize(buff, buff_len)
		buff, buff_len = self.quest_data.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.wt_entry.deserialize(buff)
		buff = self.quest_data.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

class cs_get_wt_guild_rank(proto):
	def __init__(self):
		self.session = session_t()
		self.wt_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.wt_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.wt_entry.deserialize(buff)
		return buff

class sc_get_wt_guild_rank(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.wt_entry = cint32()
		self.len_of_rank = cuint16()
		self.rank = []
		self.guild_rank = wt_guild_rank_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.wt_entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_rank.serialize(buff, buff_len)
		for i in range(self.len_of_rank.value):
			buff, buff_len = self.rank[i].serialize(buff, buff_len)
		buff, buff_len = self.guild_rank.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.wt_entry.deserialize(buff)
		buff = self.len_of_rank.deserialize(buff)
		self.rank = []
		for i in range(self.len_of_rank.value):
			self.rank.append(wt_guild_rank_t())
			buff = self.rank[i].deserialize(buff)
		buff = self.guild_rank.deserialize(buff)
		return buff

	def add_rank():
		if len(rank) >= MAX_WT_RANK_NUM.value:
			return None
		rank.append(wt_guild_rank_t())
		return rank[len(rank) - 1]

class cs_get_wt_user_rank(proto):
	def __init__(self):
		self.session = session_t()
		self.wt_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.wt_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.wt_entry.deserialize(buff)
		return buff

class sc_get_wt_user_rank(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.wt_entry = cint32()
		self.len_of_rank = cuint16()
		self.rank = []
		self.user_rank = wt_user_rank_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.wt_entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_rank.serialize(buff, buff_len)
		for i in range(self.len_of_rank.value):
			buff, buff_len = self.rank[i].serialize(buff, buff_len)
		buff, buff_len = self.user_rank.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.wt_entry.deserialize(buff)
		buff = self.len_of_rank.deserialize(buff)
		self.rank = []
		for i in range(self.len_of_rank.value):
			self.rank.append(wt_user_rank_t())
			buff = self.rank[i].deserialize(buff)
		buff = self.user_rank.deserialize(buff)
		return buff

	def add_rank():
		if len(rank) >= MAX_WT_RANK_NUM.value:
			return None
		rank.append(wt_user_rank_t())
		return rank[len(rank) - 1]

class cs_hero_buy_spirit(proto):
	def __init__(self):
		self.session = session_t()
		self.len_of_hero_entry = cuint16()
		self.hero_entry = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.len_of_hero_entry.serialize(buff, buff_len)
		for i in range(self.len_of_hero_entry.value):
			buff, buff_len = self.hero_entry[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.len_of_hero_entry.deserialize(buff)
		self.hero_entry = []
		for i in range(self.len_of_hero_entry.value):
			self.hero_entry.append(cint32())
			buff = self.hero_entry[i].deserialize(buff)
		return buff

	def add_hero_entry():
		if len(hero_entry) >= MAX_CORPS_TROOPS_NUM.value:
			return None
		hero_entry.append(ccint32())
		return hero_entry[len(hero_entry) - 1]

class sc_hero_buy_spirit(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_heros = cuint16()
		self.heros = []
		self.gold = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_heros.serialize(buff, buff_len)
		for i in range(self.len_of_heros.value):
			buff, buff_len = self.heros[i].serialize(buff, buff_len)
		buff, buff_len = self.gold.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_heros.deserialize(buff)
		self.heros = []
		for i in range(self.len_of_heros.value):
			self.heros.append(hero_data_t())
			buff = self.heros[i].deserialize(buff)
		buff = self.gold.deserialize(buff)
		return buff

	def add_heros():
		if len(heros) >= MAX_CORPS_TROOPS_NUM.value:
			return None
		heros.append(hero_data_t())
		return heros[len(heros) - 1]

class cs_query_rebel(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_query_rebel(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.rebel_data = user_rebel_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.rebel_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.rebel_data.deserialize(buff)
		return buff

class cs_rebel_search(proto):
	def __init__(self):
		self.session = session_t()
		self.id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.id.deserialize(buff)
		return buff

class sc_rebel_search(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.rebel_data = user_rebel_data_t()
		self.new_event = game_event_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.rebel_data.serialize(buff, buff_len)
		buff, buff_len = self.new_event.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.rebel_data.deserialize(buff)
		buff = self.new_event.deserialize(buff)
		return buff

class cs_rebel_buy_times(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_rebel_buy_times(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.rebel_data = user_rebel_data_t()
		self.resources = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.rebel_data.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.rebel_data.deserialize(buff)
		buff = self.resources.deserialize(buff)
		return buff

class cs_killpoint_reward(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_killpoint_reward(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_kp_data = user_kill_point_t()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_kp_data.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_kp_data.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

class cs_killpoint_lvup(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_killpoint_lvup(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.user_kp_data = user_kill_point_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.user_kp_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.user_kp_data.deserialize(buff)
		return buff

class cs_get_guild_crusade_city_rank(proto):
	def __init__(self):
		self.session = session_t()
		self.block_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		return buff

class sc_get_guild_crusade_city_rank(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.block_id = cint32()
		self.len_of_data = cuint16()
		self.data = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_data.serialize(buff, buff_len)
		for i in range(self.len_of_data.value):
			buff, buff_len = self.data[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.len_of_data.deserialize(buff)
		self.data = []
		for i in range(self.len_of_data.value):
			self.data.append(guild_crusade_t())
			buff = self.data[i].deserialize(buff)
		return buff

	def add_data():
		if len(data) >= MAX_CRUSADE_GUILD_RANK.value:
			return None
		data.append(guild_crusade_t())
		return data[len(data) - 1]

class cs_corps_exchange_hero_incorp(proto):
	def __init__(self):
		self.session = session_t()
		self.corp1_key = corps_key_t()
		self.corp2_key = corps_key_t()
		self.hero1_idx = cint32()
		self.hero2_idx = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.corp1_key.serialize(buff, buff_len)
		buff, buff_len = self.corp2_key.serialize(buff, buff_len)
		buff, buff_len = self.hero1_idx.serialize(buff, buff_len)
		buff, buff_len = self.hero2_idx.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.corp1_key.deserialize(buff)
		buff = self.corp2_key.deserialize(buff)
		buff = self.hero1_idx.deserialize(buff)
		buff = self.hero2_idx.deserialize(buff)
		return buff

class sc_corps_exchange_hero_incorp(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.corp1_data = corps_data_t()
		self.corp2_data = corps_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.corp1_data.serialize(buff, buff_len)
		buff, buff_len = self.corp2_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.corp1_data.deserialize(buff)
		buff = self.corp2_data.deserialize(buff)
		return buff

class cs_get_guild_gift_list(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_guild_gift_list(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_data = cuint16()
		self.data = []
		self.energy = cint32()
		self.gift_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_data.serialize(buff, buff_len)
		for i in range(self.len_of_data.value):
			buff, buff_len = self.data[i].serialize(buff, buff_len)
		buff, buff_len = self.energy.serialize(buff, buff_len)
		buff, buff_len = self.gift_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_data.deserialize(buff)
		self.data = []
		for i in range(self.len_of_data.value):
			self.data.append(guild_gift_item())
			buff = self.data[i].deserialize(buff)
		buff = self.energy.deserialize(buff)
		buff = self.gift_id.deserialize(buff)
		return buff

	def add_data():
		if len(data) >= MAX_GUILD_GIFT_LIST_NUM.value:
			return None
		data.append(guild_gift_item())
		return data[len(data) - 1]

class cs_reward_guild_gift(proto):
	def __init__(self):
		self.session = session_t()
		self.item_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.item_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.item_id.deserialize(buff)
		return buff

class sc_reward_guild_gift(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.energy = cint32()
		self.item_id = cint64()
		self.resources = user_resource_t()
		self.rewards = rewards_t()
		self.gift_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.energy.serialize(buff, buff_len)
		buff, buff_len = self.item_id.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		buff, buff_len = self.gift_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.energy.deserialize(buff)
		buff = self.item_id.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		buff = self.gift_id.deserialize(buff)
		return buff

class cs_season_chat(proto):
	def __init__(self):
		self.session = session_t()
		self.channel_id = cint64()
		self.content = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		buff, buff_len = self.content.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.channel_id.deserialize(buff)
		buff = self.content.deserialize(buff)
		return buff

class sc_season_chat(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.resources = user_resource_t()
		self.remain_season_chat_count = cint32()
		self.season_chat_cd_time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.remain_season_chat_count.serialize(buff, buff_len)
		buff, buff_len = self.season_chat_cd_time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.resources.deserialize(buff)
		buff = self.remain_season_chat_count.deserialize(buff)
		buff = self.season_chat_cd_time.deserialize(buff)
		return buff

class cs_openid_req(proto):
	def __init__(self):
		self.session = session_t()
		self.access_token = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.access_token.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.access_token.deserialize(buff)
		return buff

class sc_openid_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.sdk_open_id = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.sdk_open_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.sdk_open_id.deserialize(buff)
		return buff

class schat_herat_beat(proto):
	def __init__(self):
		pass
	def serialize(self, buff, buff_len):
		return buff, buff_len

	def deserialize(self, buff):
		return buff

class chats_herat_beat(proto):
	def __init__(self):
		pass
	def serialize(self, buff, buff_len):
		return buff, buff_len

	def deserialize(self, buff):
		return buff

class cs_query_balance(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_query_balance(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.cur_balance = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.cur_balance.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.cur_balance.deserialize(buff)
		return buff

class cs_get_map_color(proto):
	def __init__(self):
		self.session = session_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		return buff

class sc_get_map_color(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.len_of_map_color_list = cuint16()
		self.map_color_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.len_of_map_color_list.serialize(buff, buff_len)
		for i in range(self.len_of_map_color_list.value):
			buff, buff_len = self.map_color_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.len_of_map_color_list.deserialize(buff)
		self.map_color_list = []
		for i in range(self.len_of_map_color_list.value):
			self.map_color_list.append(map_color())
			buff = self.map_color_list[i].deserialize(buff)
		return buff

	def add_map_color_list():
		if len(map_color_list) >= MAX_COUNTY_NUM.value:
			return None
		map_color_list.append(map_color())
		return map_color_list[len(map_color_list) - 1]

class cs_lucky_treasuer_req(proto):
	def __init__(self):
		self.session = session_t()
		self.draw_count = cint32()
		self.activity_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.draw_count.serialize(buff, buff_len)
		buff, buff_len = self.activity_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.draw_count.deserialize(buff)
		buff = self.activity_id.deserialize(buff)
		return buff

class sc_lucky_treasuer_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.totalcount = cint32()
		self.luckynum = cint32()
		self.box_state = cint32()
		self.draw_count = cint32()
		self.len_of_draw_items = cuint16()
		self.draw_items = []
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.totalcount.serialize(buff, buff_len)
		buff, buff_len = self.luckynum.serialize(buff, buff_len)
		buff, buff_len = self.box_state.serialize(buff, buff_len)
		buff, buff_len = self.draw_count.serialize(buff, buff_len)
		buff, buff_len = self.len_of_draw_items.serialize(buff, buff_len)
		for i in range(self.len_of_draw_items.value):
			buff, buff_len = self.draw_items[i].serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.totalcount.deserialize(buff)
		buff = self.luckynum.deserialize(buff)
		buff = self.box_state.deserialize(buff)
		buff = self.draw_count.deserialize(buff)
		buff = self.len_of_draw_items.deserialize(buff)
		self.draw_items = []
		for i in range(self.len_of_draw_items.value):
			self.draw_items.append(cint32())
			buff = self.draw_items[i].deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

	def add_draw_items():
		if len(draw_items) >= MAX_LUCKY_TREASURE.value:
			return None
		draw_items.append(ccint32())
		return draw_items[len(draw_items) - 1]

class cs_lucky_getbox_req(proto):
	def __init__(self):
		self.session = session_t()
		self.box_idx = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.box_idx.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.box_idx.deserialize(buff)
		return buff

class sc_lucky_getbox_req(proto):
	def __init__(self):
		self.common_result = common_result_t()
		self.box_idx = cint32()
		self.box_state = cint32()
		self.rewards = rewards_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.common_result.serialize(buff, buff_len)
		buff, buff_len = self.box_idx.serialize(buff, buff_len)
		buff, buff_len = self.box_state.serialize(buff, buff_len)
		buff, buff_len = self.rewards.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.common_result.deserialize(buff)
		buff = self.box_idx.deserialize(buff)
		buff = self.box_state.deserialize(buff)
		buff = self.rewards.deserialize(buff)
		return buff

