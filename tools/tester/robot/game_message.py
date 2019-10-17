import sys
sys.path.append("..\gen_protocol")
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
        
    
    # CS_REGISTER
    @CallbackBase.callback(OP_CODE.CS_REGISTER)
    def send_register_decorate(self, code):
        packet = cs_register()
        self.make_register_packet(packet)
        self.mes_que[code] = packet
    # makeup register packet
    def make_register_packet(self, packet):
        return None
    # send register
    def send_register(self):
        self.dispatch(OP_CODE.CS_REGISTER)(OP_CODE.CS_REGISTER)
    
    # handle SC_REGISTER
    @CallbackBase.callback(OP_CODE.SC_REGISTER)
    def handle_register_decorate(self, recv_buff):
        packet = sc_register()
        packet.deserialize(recv_buff)
        return self.handle_register(packet)    
    def handle_register(self, packet):
        return None

    
    # CS_LOGIN
    @CallbackBase.callback(OP_CODE.CS_LOGIN)
    def send_login_decorate(self, code):
        packet = cs_login()
        self.make_login_packet(packet)
        self.mes_que[code] = packet
    # makeup login packet
    def make_login_packet(self, packet):
        return None
    # send login
    def send_login(self):
        self.dispatch(OP_CODE.CS_LOGIN)(OP_CODE.CS_LOGIN)
    
    # handle SC_LOGIN
    @CallbackBase.callback(OP_CODE.SC_LOGIN)
    def handle_login_decorate(self, recv_buff):
        packet = sc_login()
        packet.deserialize(recv_buff)
        return self.handle_login(packet)    
    def handle_login(self, packet):
        return None

    
    # CS_GET_USER_INFO
    @CallbackBase.callback(OP_CODE.CS_GET_USER_INFO)
    def send_get_user_info_decorate(self, code):
        packet = cs_get_user_info()
        self.make_get_user_info_packet(packet)
        self.mes_que[code] = packet
    # makeup get_user_info packet
    def make_get_user_info_packet(self, packet):
        return None
    # send get_user_info
    def send_get_user_info(self):
        self.dispatch(OP_CODE.CS_GET_USER_INFO)(OP_CODE.CS_GET_USER_INFO)
    
    # handle SC_GET_USER_INFO
    @CallbackBase.callback(OP_CODE.SC_GET_USER_INFO)
    def handle_get_user_info_decorate(self, recv_buff):
        packet = sc_get_user_info()
        packet.deserialize(recv_buff)
        return self.handle_get_user_info(packet)    
    def handle_get_user_info(self, packet):
        return None

    
    # CS_GET_CASTLE_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_CASTLE_LIST)
    def send_get_castle_list_decorate(self, code):
        packet = cs_get_castle_list()
        self.make_get_castle_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_castle_list packet
    def make_get_castle_list_packet(self, packet):
        return None
    # send get_castle_list
    def send_get_castle_list(self):
        self.dispatch(OP_CODE.CS_GET_CASTLE_LIST)(OP_CODE.CS_GET_CASTLE_LIST)
    
    # handle SC_GET_CASTLE_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_CASTLE_LIST)
    def handle_get_castle_list_decorate(self, recv_buff):
        packet = sc_get_castle_list()
        packet.deserialize(recv_buff)
        return self.handle_get_castle_list(packet)    
    def handle_get_castle_list(self, packet):
        return None

    
    # CS_GET_BUILDING_DATA
    @CallbackBase.callback(OP_CODE.CS_GET_BUILDING_DATA)
    def send_get_building_data_decorate(self, code):
        packet = cs_get_building_data()
        self.make_get_building_data_packet(packet)
        self.mes_que[code] = packet
    # makeup get_building_data packet
    def make_get_building_data_packet(self, packet):
        return None
    # send get_building_data
    def send_get_building_data(self):
        self.dispatch(OP_CODE.CS_GET_BUILDING_DATA)(OP_CODE.CS_GET_BUILDING_DATA)
    
    # handle SC_GET_BUILDING_DATA
    @CallbackBase.callback(OP_CODE.SC_GET_BUILDING_DATA)
    def handle_get_building_data_decorate(self, recv_buff):
        packet = sc_get_building_data()
        packet.deserialize(recv_buff)
        return self.handle_get_building_data(packet)    
    def handle_get_building_data(self, packet):
        return None

    
    # CS_BUILDING_LVUP
    @CallbackBase.callback(OP_CODE.CS_BUILDING_LVUP)
    def send_building_lvup_decorate(self, code):
        packet = cs_building_lvup()
        self.make_building_lvup_packet(packet)
        self.mes_que[code] = packet
    # makeup building_lvup packet
    def make_building_lvup_packet(self, packet):
        return None
    # send building_lvup
    def send_building_lvup(self):
        self.dispatch(OP_CODE.CS_BUILDING_LVUP)(OP_CODE.CS_BUILDING_LVUP)
    
    # handle SC_BUILDING_LVUP
    @CallbackBase.callback(OP_CODE.SC_BUILDING_LVUP)
    def handle_building_lvup_decorate(self, recv_buff):
        packet = sc_building_lvup()
        packet.deserialize(recv_buff)
        return self.handle_building_lvup(packet)    
    def handle_building_lvup(self, packet):
        return None

    
    # CS_ACCELERATE_BUILDING_LVUP
    @CallbackBase.callback(OP_CODE.CS_ACCELERATE_BUILDING_LVUP)
    def send_accelerate_building_lvup_decorate(self, code):
        packet = cs_accelerate_building_lvup()
        self.make_accelerate_building_lvup_packet(packet)
        self.mes_que[code] = packet
    # makeup accelerate_building_lvup packet
    def make_accelerate_building_lvup_packet(self, packet):
        return None
    # send accelerate_building_lvup
    def send_accelerate_building_lvup(self):
        self.dispatch(OP_CODE.CS_ACCELERATE_BUILDING_LVUP)(OP_CODE.CS_ACCELERATE_BUILDING_LVUP)
    
    # handle SC_ACCELERATE_BUILDING_LVUP
    @CallbackBase.callback(OP_CODE.SC_ACCELERATE_BUILDING_LVUP)
    def handle_accelerate_building_lvup_decorate(self, recv_buff):
        packet = sc_accelerate_building_lvup()
        packet.deserialize(recv_buff)
        return self.handle_accelerate_building_lvup(packet)    
    def handle_accelerate_building_lvup(self, packet):
        return None

    
    # CS_GET_HERO_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_HERO_LIST)
    def send_get_hero_list_decorate(self, code):
        packet = cs_get_hero_list()
        self.make_get_hero_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_hero_list packet
    def make_get_hero_list_packet(self, packet):
        return None
    # send get_hero_list
    def send_get_hero_list(self):
        self.dispatch(OP_CODE.CS_GET_HERO_LIST)(OP_CODE.CS_GET_HERO_LIST)
    
    # handle SC_GET_HERO_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_HERO_LIST)
    def handle_get_hero_list_decorate(self, recv_buff):
        packet = sc_get_hero_list()
        packet.deserialize(recv_buff)
        return self.handle_get_hero_list(packet)    
    def handle_get_hero_list(self, packet):
        return None

    
    # CS_GET_SINGLE_HERO_DATA
    @CallbackBase.callback(OP_CODE.CS_GET_SINGLE_HERO_DATA)
    def send_get_single_hero_data_decorate(self, code):
        packet = cs_get_single_hero_data()
        self.make_get_single_hero_data_packet(packet)
        self.mes_que[code] = packet
    # makeup get_single_hero_data packet
    def make_get_single_hero_data_packet(self, packet):
        return None
    # send get_single_hero_data
    def send_get_single_hero_data(self):
        self.dispatch(OP_CODE.CS_GET_SINGLE_HERO_DATA)(OP_CODE.CS_GET_SINGLE_HERO_DATA)
    
    # handle SC_GET_SINGLE_HERO_DATA
    @CallbackBase.callback(OP_CODE.SC_GET_SINGLE_HERO_DATA)
    def handle_get_single_hero_data_decorate(self, recv_buff):
        packet = sc_get_single_hero_data()
        packet.deserialize(recv_buff)
        return self.handle_get_single_hero_data(packet)    
    def handle_get_single_hero_data(self, packet):
        return None

    
    # CS_ACCELERATE_HERO_TRAIN
    @CallbackBase.callback(OP_CODE.CS_ACCELERATE_HERO_TRAIN)
    def send_accelerate_hero_train_decorate(self, code):
        packet = cs_accelerate_hero_train()
        self.make_accelerate_hero_train_packet(packet)
        self.mes_que[code] = packet
    # makeup accelerate_hero_train packet
    def make_accelerate_hero_train_packet(self, packet):
        return None
    # send accelerate_hero_train
    def send_accelerate_hero_train(self):
        self.dispatch(OP_CODE.CS_ACCELERATE_HERO_TRAIN)(OP_CODE.CS_ACCELERATE_HERO_TRAIN)
    
    # handle SC_ACCELERATE_HERO_TRAIN
    @CallbackBase.callback(OP_CODE.SC_ACCELERATE_HERO_TRAIN)
    def handle_accelerate_hero_train_decorate(self, recv_buff):
        packet = sc_accelerate_hero_train()
        packet.deserialize(recv_buff)
        return self.handle_accelerate_hero_train(packet)    
    def handle_accelerate_hero_train(self, packet):
        return None

    
    # CS_HERO_TRAIN
    @CallbackBase.callback(OP_CODE.CS_HERO_TRAIN)
    def send_hero_train_decorate(self, code):
        packet = cs_hero_train()
        self.make_hero_train_packet(packet)
        self.mes_que[code] = packet
    # makeup hero_train packet
    def make_hero_train_packet(self, packet):
        return None
    # send hero_train
    def send_hero_train(self):
        self.dispatch(OP_CODE.CS_HERO_TRAIN)(OP_CODE.CS_HERO_TRAIN)
    
    # handle SC_HERO_TRAIN
    @CallbackBase.callback(OP_CODE.SC_HERO_TRAIN)
    def handle_hero_train_decorate(self, recv_buff):
        packet = sc_hero_train()
        packet.deserialize(recv_buff)
        return self.handle_hero_train(packet)    
    def handle_hero_train(self, packet):
        return None

    
    # CS_CANCEL_HERO_TRAIN
    @CallbackBase.callback(OP_CODE.CS_CANCEL_HERO_TRAIN)
    def send_cancel_hero_train_decorate(self, code):
        packet = cs_cancel_hero_train()
        self.make_cancel_hero_train_packet(packet)
        self.mes_que[code] = packet
    # makeup cancel_hero_train packet
    def make_cancel_hero_train_packet(self, packet):
        return None
    # send cancel_hero_train
    def send_cancel_hero_train(self):
        self.dispatch(OP_CODE.CS_CANCEL_HERO_TRAIN)(OP_CODE.CS_CANCEL_HERO_TRAIN)
    
    # handle SC_CANCEL_HERO_TRAIN
    @CallbackBase.callback(OP_CODE.SC_CANCEL_HERO_TRAIN)
    def handle_cancel_hero_train_decorate(self, recv_buff):
        packet = sc_cancel_hero_train()
        packet.deserialize(recv_buff)
        return self.handle_cancel_hero_train(packet)    
    def handle_cancel_hero_train(self, packet):
        return None

    
    # CS_GET_CORPS_INFO
    @CallbackBase.callback(OP_CODE.CS_GET_CORPS_INFO)
    def send_get_corps_info_decorate(self, code):
        packet = cs_get_corps_info()
        self.make_get_corps_info_packet(packet)
        self.mes_que[code] = packet
    # makeup get_corps_info packet
    def make_get_corps_info_packet(self, packet):
        return None
    # send get_corps_info
    def send_get_corps_info(self):
        self.dispatch(OP_CODE.CS_GET_CORPS_INFO)(OP_CODE.CS_GET_CORPS_INFO)
    
    # handle SC_GET_CORPS_INFO
    @CallbackBase.callback(OP_CODE.SC_GET_CORPS_INFO)
    def handle_get_corps_info_decorate(self, recv_buff):
        packet = sc_get_corps_info()
        packet.deserialize(recv_buff)
        return self.handle_get_corps_info(packet)    
    def handle_get_corps_info(self, packet):
        return None

    
    # CS_GET_GAME_EVENT_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_GAME_EVENT_LIST)
    def send_get_game_event_list_decorate(self, code):
        packet = cs_get_game_event_list()
        self.make_get_game_event_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_game_event_list packet
    def make_get_game_event_list_packet(self, packet):
        return None
    # send get_game_event_list
    def send_get_game_event_list(self):
        self.dispatch(OP_CODE.CS_GET_GAME_EVENT_LIST)(OP_CODE.CS_GET_GAME_EVENT_LIST)
    
    # handle SC_GET_GAME_EVENT_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_GAME_EVENT_LIST)
    def handle_get_game_event_list_decorate(self, recv_buff):
        packet = sc_get_game_event_list()
        packet.deserialize(recv_buff)
        return self.handle_get_game_event_list(packet)    
    def handle_get_game_event_list(self, packet):
        return None

    
    # CS_QUERY_GAME_EVENT_RESULT
    @CallbackBase.callback(OP_CODE.CS_QUERY_GAME_EVENT_RESULT)
    def send_query_game_event_result_decorate(self, code):
        packet = cs_query_game_event_result()
        self.make_query_game_event_result_packet(packet)
        self.mes_que[code] = packet
    # makeup query_game_event_result packet
    def make_query_game_event_result_packet(self, packet):
        return None
    # send query_game_event_result
    def send_query_game_event_result(self):
        self.dispatch(OP_CODE.CS_QUERY_GAME_EVENT_RESULT)(OP_CODE.CS_QUERY_GAME_EVENT_RESULT)
    
    # handle SC_QUERY_GAME_EVENT_RESULT
    @CallbackBase.callback(OP_CODE.SC_QUERY_GAME_EVENT_RESULT)
    def handle_query_game_event_result_decorate(self, recv_buff):
        packet = sc_query_game_event_result()
        packet.deserialize(recv_buff)
        return self.handle_query_game_event_result(packet)    
    def handle_query_game_event_result(self, packet):
        return None

    
    # CS_GET_BATTLE_RESULT
    @CallbackBase.callback(OP_CODE.CS_GET_BATTLE_RESULT)
    def send_get_battle_result_decorate(self, code):
        packet = cs_get_battle_result()
        self.make_get_battle_result_packet(packet)
        self.mes_que[code] = packet
    # makeup get_battle_result packet
    def make_get_battle_result_packet(self, packet):
        return None
    # send get_battle_result
    def send_get_battle_result(self):
        self.dispatch(OP_CODE.CS_GET_BATTLE_RESULT)(OP_CODE.CS_GET_BATTLE_RESULT)
    
    # handle SC_GET_BATTLE_RESULT
    @CallbackBase.callback(OP_CODE.SC_GET_BATTLE_RESULT)
    def handle_get_battle_result_decorate(self, recv_buff):
        packet = sc_get_battle_result()
        packet.deserialize(recv_buff)
        return self.handle_get_battle_result(packet)    
    def handle_get_battle_result(self, packet):
        return None

    
    # CS_GM_COMMAND
    @CallbackBase.callback(OP_CODE.CS_GM_COMMAND)
    def send_gm_command_decorate(self, code):
        packet = cs_gm_command()
        self.make_gm_command_packet(packet)
        self.mes_que[code] = packet
    # makeup gm_command packet
    def make_gm_command_packet(self, packet):
        return None
    # send gm_command
    def send_gm_command(self):
        self.dispatch(OP_CODE.CS_GM_COMMAND)(OP_CODE.CS_GM_COMMAND)
    
    # handle SC_GM_COMMAND
    @CallbackBase.callback(OP_CODE.SC_GM_COMMAND)
    def handle_gm_command_decorate(self, recv_buff):
        packet = sc_gm_command()
        packet.deserialize(recv_buff)
        return self.handle_gm_command(packet)    
    def handle_gm_command(self, packet):
        return None

    
    # CS_CORPS_MOVE
    @CallbackBase.callback(OP_CODE.CS_CORPS_MOVE)
    def send_corps_move_decorate(self, code):
        packet = cs_corps_move()
        self.make_corps_move_packet(packet)
        self.mes_que[code] = packet
    # makeup corps_move packet
    def make_corps_move_packet(self, packet):
        return None
    # send corps_move
    def send_corps_move(self):
        self.dispatch(OP_CODE.CS_CORPS_MOVE)(OP_CODE.CS_CORPS_MOVE)
    
    # handle SC_CORPS_MOVE
    @CallbackBase.callback(OP_CODE.SC_CORPS_MOVE)
    def handle_corps_move_decorate(self, recv_buff):
        packet = sc_corps_move()
        packet.deserialize(recv_buff)
        return self.handle_corps_move(packet)    
    def handle_corps_move(self, packet):
        return None

    
    # CS_GAME_EVENT_DISCARD
    @CallbackBase.callback(OP_CODE.CS_GAME_EVENT_DISCARD)
    def send_game_event_discard_decorate(self, code):
        packet = cs_game_event_discard()
        self.make_game_event_discard_packet(packet)
        self.mes_que[code] = packet
    # makeup game_event_discard packet
    def make_game_event_discard_packet(self, packet):
        return None
    # send game_event_discard
    def send_game_event_discard(self):
        self.dispatch(OP_CODE.CS_GAME_EVENT_DISCARD)(OP_CODE.CS_GAME_EVENT_DISCARD)
    
    # handle SC_GAME_EVENT_DISCARD
    @CallbackBase.callback(OP_CODE.SC_GAME_EVENT_DISCARD)
    def handle_game_event_discard_decorate(self, recv_buff):
        packet = sc_game_event_discard()
        packet.deserialize(recv_buff)
        return self.handle_game_event_discard(packet)    
    def handle_game_event_discard(self, packet):
        return None

    
    # CS_BLOCK_DISCARD
    @CallbackBase.callback(OP_CODE.CS_BLOCK_DISCARD)
    def send_block_discard_decorate(self, code):
        packet = cs_block_discard()
        self.make_block_discard_packet(packet)
        self.mes_que[code] = packet
    # makeup block_discard packet
    def make_block_discard_packet(self, packet):
        return None
    # send block_discard
    def send_block_discard(self):
        self.dispatch(OP_CODE.CS_BLOCK_DISCARD)(OP_CODE.CS_BLOCK_DISCARD)
    
    # handle SC_BLOCK_DISCARD
    @CallbackBase.callback(OP_CODE.SC_BLOCK_DISCARD)
    def handle_block_discard_decorate(self, recv_buff):
        packet = sc_block_discard()
        packet.deserialize(recv_buff)
        return self.handle_block_discard(packet)    
    def handle_block_discard(self, packet):
        return None

    
    # CS_GET_CHUNK_EVENTS
    @CallbackBase.callback(OP_CODE.CS_GET_CHUNK_EVENTS)
    def send_get_chunk_events_decorate(self, code):
        packet = cs_get_chunk_events()
        self.make_get_chunk_events_packet(packet)
        self.mes_que[code] = packet
    # makeup get_chunk_events packet
    def make_get_chunk_events_packet(self, packet):
        return None
    # send get_chunk_events
    def send_get_chunk_events(self):
        self.dispatch(OP_CODE.CS_GET_CHUNK_EVENTS)(OP_CODE.CS_GET_CHUNK_EVENTS)
    
    # handle SC_GET_CHUNK_EVENTS
    @CallbackBase.callback(OP_CODE.SC_GET_CHUNK_EVENTS)
    def handle_get_chunk_events_decorate(self, recv_buff):
        packet = sc_get_chunk_events()
        packet.deserialize(recv_buff)
        return self.handle_get_chunk_events(packet)    
    def handle_get_chunk_events(self, packet):
        return None

    
    # CS_CONSCRIPT_SOLDIER
    @CallbackBase.callback(OP_CODE.CS_CONSCRIPT_SOLDIER)
    def send_conscript_soldier_decorate(self, code):
        packet = cs_conscript_soldier()
        self.make_conscript_soldier_packet(packet)
        self.mes_que[code] = packet
    # makeup conscript_soldier packet
    def make_conscript_soldier_packet(self, packet):
        return None
    # send conscript_soldier
    def send_conscript_soldier(self):
        self.dispatch(OP_CODE.CS_CONSCRIPT_SOLDIER)(OP_CODE.CS_CONSCRIPT_SOLDIER)
    
    # handle SC_CONSCRIPT_SOLDIER
    @CallbackBase.callback(OP_CODE.SC_CONSCRIPT_SOLDIER)
    def handle_conscript_soldier_decorate(self, recv_buff):
        packet = sc_conscript_soldier()
        packet.deserialize(recv_buff)
        return self.handle_conscript_soldier(packet)    
    def handle_conscript_soldier(self, packet):
        return None

    
    # CS_CANCEL_CONSCRIPT_SOLDIER
    @CallbackBase.callback(OP_CODE.CS_CANCEL_CONSCRIPT_SOLDIER)
    def send_cancel_conscript_soldier_decorate(self, code):
        packet = cs_cancel_conscript_soldier()
        self.make_cancel_conscript_soldier_packet(packet)
        self.mes_que[code] = packet
    # makeup cancel_conscript_soldier packet
    def make_cancel_conscript_soldier_packet(self, packet):
        return None
    # send cancel_conscript_soldier
    def send_cancel_conscript_soldier(self):
        self.dispatch(OP_CODE.CS_CANCEL_CONSCRIPT_SOLDIER)(OP_CODE.CS_CANCEL_CONSCRIPT_SOLDIER)
    
    # handle SC_CANCEL_CONSCRIPT_SOLDIER
    @CallbackBase.callback(OP_CODE.SC_CANCEL_CONSCRIPT_SOLDIER)
    def handle_cancel_conscript_soldier_decorate(self, recv_buff):
        packet = sc_cancel_conscript_soldier()
        packet.deserialize(recv_buff)
        return self.handle_cancel_conscript_soldier(packet)    
    def handle_cancel_conscript_soldier(self, packet):
        return None

    
    # CS_SYNC_TROOP_DATA
    @CallbackBase.callback(OP_CODE.CS_SYNC_TROOP_DATA)
    def send_sync_troop_data_decorate(self, code):
        packet = cs_sync_troop_data()
        self.make_sync_troop_data_packet(packet)
        self.mes_que[code] = packet
    # makeup sync_troop_data packet
    def make_sync_troop_data_packet(self, packet):
        return None
    # send sync_troop_data
    def send_sync_troop_data(self):
        self.dispatch(OP_CODE.CS_SYNC_TROOP_DATA)(OP_CODE.CS_SYNC_TROOP_DATA)
    
    # handle SC_SYNC_TROOP_DATA
    @CallbackBase.callback(OP_CODE.SC_SYNC_TROOP_DATA)
    def handle_sync_troop_data_decorate(self, recv_buff):
        packet = sc_sync_troop_data()
        packet.deserialize(recv_buff)
        return self.handle_sync_troop_data(packet)    
    def handle_sync_troop_data(self, packet):
        return None

    
    # CS_DISMISS_SOLDIER
    @CallbackBase.callback(OP_CODE.CS_DISMISS_SOLDIER)
    def send_dismiss_soldier_decorate(self, code):
        packet = cs_dismiss_soldier()
        self.make_dismiss_soldier_packet(packet)
        self.mes_que[code] = packet
    # makeup dismiss_soldier packet
    def make_dismiss_soldier_packet(self, packet):
        return None
    # send dismiss_soldier
    def send_dismiss_soldier(self):
        self.dispatch(OP_CODE.CS_DISMISS_SOLDIER)(OP_CODE.CS_DISMISS_SOLDIER)
    
    # handle SC_DISMISS_SOLDIER
    @CallbackBase.callback(OP_CODE.SC_DISMISS_SOLDIER)
    def handle_dismiss_soldier_decorate(self, recv_buff):
        packet = sc_dismiss_soldier()
        packet.deserialize(recv_buff)
        return self.handle_dismiss_soldier(packet)    
    def handle_dismiss_soldier(self, packet):
        return None

    
    # CS_CORP_CHANGE_BATTLE_POS
    @CallbackBase.callback(OP_CODE.CS_CORP_CHANGE_BATTLE_POS)
    def send_corp_change_battle_pos_decorate(self, code):
        packet = cs_corp_change_battle_pos()
        self.make_corp_change_battle_pos_packet(packet)
        self.mes_que[code] = packet
    # makeup corp_change_battle_pos packet
    def make_corp_change_battle_pos_packet(self, packet):
        return None
    # send corp_change_battle_pos
    def send_corp_change_battle_pos(self):
        self.dispatch(OP_CODE.CS_CORP_CHANGE_BATTLE_POS)(OP_CODE.CS_CORP_CHANGE_BATTLE_POS)
    
    # handle SC_CORP_CHANGE_BATTLE_POS
    @CallbackBase.callback(OP_CODE.SC_CORP_CHANGE_BATTLE_POS)
    def handle_corp_change_battle_pos_decorate(self, recv_buff):
        packet = sc_corp_change_battle_pos()
        packet.deserialize(recv_buff)
        return self.handle_corp_change_battle_pos(packet)    
    def handle_corp_change_battle_pos(self, packet):
        return None

    
    # CS_HERO_ASSIGN_POINT
    @CallbackBase.callback(OP_CODE.CS_HERO_ASSIGN_POINT)
    def send_hero_assign_point_decorate(self, code):
        packet = cs_hero_assign_point()
        self.make_hero_assign_point_packet(packet)
        self.mes_que[code] = packet
    # makeup hero_assign_point packet
    def make_hero_assign_point_packet(self, packet):
        return None
    # send hero_assign_point
    def send_hero_assign_point(self):
        self.dispatch(OP_CODE.CS_HERO_ASSIGN_POINT)(OP_CODE.CS_HERO_ASSIGN_POINT)
    
    # handle SC_HERO_ASSIGN_POINT
    @CallbackBase.callback(OP_CODE.SC_HERO_ASSIGN_POINT)
    def handle_hero_assign_point_decorate(self, recv_buff):
        packet = sc_hero_assign_point()
        packet.deserialize(recv_buff)
        return self.handle_hero_assign_point(packet)    
    def handle_hero_assign_point(self, packet):
        return None

    
    # CS_RESET_HERO_POINT
    @CallbackBase.callback(OP_CODE.CS_RESET_HERO_POINT)
    def send_reset_hero_point_decorate(self, code):
        packet = cs_reset_hero_point()
        self.make_reset_hero_point_packet(packet)
        self.mes_que[code] = packet
    # makeup reset_hero_point packet
    def make_reset_hero_point_packet(self, packet):
        return None
    # send reset_hero_point
    def send_reset_hero_point(self):
        self.dispatch(OP_CODE.CS_RESET_HERO_POINT)(OP_CODE.CS_RESET_HERO_POINT)
    
    # handle SC_RESET_HERO_POINT
    @CallbackBase.callback(OP_CODE.SC_RESET_HERO_POINT)
    def handle_reset_hero_point_decorate(self, recv_buff):
        packet = sc_reset_hero_point()
        packet.deserialize(recv_buff)
        return self.handle_reset_hero_point(packet)    
    def handle_reset_hero_point(self, packet):
        return None

    
    # CS_CORPS_CHANGE_HERO
    @CallbackBase.callback(OP_CODE.CS_CORPS_CHANGE_HERO)
    def send_corps_change_hero_decorate(self, code):
        packet = cs_corps_change_hero()
        self.make_corps_change_hero_packet(packet)
        self.mes_que[code] = packet
    # makeup corps_change_hero packet
    def make_corps_change_hero_packet(self, packet):
        return None
    # send corps_change_hero
    def send_corps_change_hero(self):
        self.dispatch(OP_CODE.CS_CORPS_CHANGE_HERO)(OP_CODE.CS_CORPS_CHANGE_HERO)
    
    # handle SC_CORPS_CHANGE_HERO
    @CallbackBase.callback(OP_CODE.SC_CORPS_CHANGE_HERO)
    def handle_corps_change_hero_decorate(self, recv_buff):
        packet = sc_corps_change_hero()
        packet.deserialize(recv_buff)
        return self.handle_corps_change_hero(packet)    
    def handle_corps_change_hero(self, packet):
        return None

    
    # CS_GET_ITEM_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_ITEM_LIST)
    def send_get_item_list_decorate(self, code):
        packet = cs_get_item_list()
        self.make_get_item_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_item_list packet
    def make_get_item_list_packet(self, packet):
        return None
    # send get_item_list
    def send_get_item_list(self):
        self.dispatch(OP_CODE.CS_GET_ITEM_LIST)(OP_CODE.CS_GET_ITEM_LIST)
    
    # handle SC_GET_ITEM_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_ITEM_LIST)
    def handle_get_item_list_decorate(self, recv_buff):
        packet = sc_get_item_list()
        packet.deserialize(recv_buff)
        return self.handle_get_item_list(packet)    
    def handle_get_item_list(self, packet):
        return None

    
    # CS_RECRUIT_HERO
    @CallbackBase.callback(OP_CODE.CS_RECRUIT_HERO)
    def send_recruit_hero_decorate(self, code):
        packet = cs_recruit_hero()
        self.make_recruit_hero_packet(packet)
        self.mes_que[code] = packet
    # makeup recruit_hero packet
    def make_recruit_hero_packet(self, packet):
        return None
    # send recruit_hero
    def send_recruit_hero(self):
        self.dispatch(OP_CODE.CS_RECRUIT_HERO)(OP_CODE.CS_RECRUIT_HERO)
    
    # handle SC_RECRUIT_HERO
    @CallbackBase.callback(OP_CODE.SC_RECRUIT_HERO)
    def handle_recruit_hero_decorate(self, recv_buff):
        packet = sc_recruit_hero()
        packet.deserialize(recv_buff)
        return self.handle_recruit_hero(packet)    
    def handle_recruit_hero(self, packet):
        return None

    
    # CS_LAND_BUILD
    @CallbackBase.callback(OP_CODE.CS_LAND_BUILD)
    def send_land_build_decorate(self, code):
        packet = cs_land_build()
        self.make_land_build_packet(packet)
        self.mes_que[code] = packet
    # makeup land_build packet
    def make_land_build_packet(self, packet):
        return None
    # send land_build
    def send_land_build(self):
        self.dispatch(OP_CODE.CS_LAND_BUILD)(OP_CODE.CS_LAND_BUILD)
    
    # handle SC_LAND_BUILD
    @CallbackBase.callback(OP_CODE.SC_LAND_BUILD)
    def handle_land_build_decorate(self, recv_buff):
        packet = sc_land_build()
        packet.deserialize(recv_buff)
        return self.handle_land_build(packet)    
    def handle_land_build(self, packet):
        return None

    
    # CS_BLOCK_BUILDING_DISCARD
    @CallbackBase.callback(OP_CODE.CS_BLOCK_BUILDING_DISCARD)
    def send_block_building_discard_decorate(self, code):
        packet = cs_block_building_discard()
        self.make_block_building_discard_packet(packet)
        self.mes_que[code] = packet
    # makeup block_building_discard packet
    def make_block_building_discard_packet(self, packet):
        return None
    # send block_building_discard
    def send_block_building_discard(self):
        self.dispatch(OP_CODE.CS_BLOCK_BUILDING_DISCARD)(OP_CODE.CS_BLOCK_BUILDING_DISCARD)
    
    # handle SC_BLOCK_BUILDING_DISCARD
    @CallbackBase.callback(OP_CODE.SC_BLOCK_BUILDING_DISCARD)
    def handle_block_building_discard_decorate(self, recv_buff):
        packet = sc_block_building_discard()
        packet.deserialize(recv_buff)
        return self.handle_block_building_discard(packet)    
    def handle_block_building_discard(self, packet):
        return None

    
    # CS_CASTLE_MOVE
    @CallbackBase.callback(OP_CODE.CS_CASTLE_MOVE)
    def send_castle_move_decorate(self, code):
        packet = cs_castle_move()
        self.make_castle_move_packet(packet)
        self.mes_que[code] = packet
    # makeup castle_move packet
    def make_castle_move_packet(self, packet):
        return None
    # send castle_move
    def send_castle_move(self):
        self.dispatch(OP_CODE.CS_CASTLE_MOVE)(OP_CODE.CS_CASTLE_MOVE)
    
    # handle SC_CASTLE_MOVE
    @CallbackBase.callback(OP_CODE.SC_CASTLE_MOVE)
    def handle_castle_move_decorate(self, recv_buff):
        packet = sc_castle_move()
        packet.deserialize(recv_buff)
        return self.handle_castle_move(packet)    
    def handle_castle_move(self, packet):
        return None

    
    # CS_HERO_CHANGE_EQUIP
    @CallbackBase.callback(OP_CODE.CS_HERO_CHANGE_EQUIP)
    def send_hero_change_equip_decorate(self, code):
        packet = cs_hero_change_equip()
        self.make_hero_change_equip_packet(packet)
        self.mes_que[code] = packet
    # makeup hero_change_equip packet
    def make_hero_change_equip_packet(self, packet):
        return None
    # send hero_change_equip
    def send_hero_change_equip(self):
        self.dispatch(OP_CODE.CS_HERO_CHANGE_EQUIP)(OP_CODE.CS_HERO_CHANGE_EQUIP)
    
    # handle SC_HERO_CHANGE_EQUIP
    @CallbackBase.callback(OP_CODE.SC_HERO_CHANGE_EQUIP)
    def handle_hero_change_equip_decorate(self, recv_buff):
        packet = sc_hero_change_equip()
        packet.deserialize(recv_buff)
        return self.handle_hero_change_equip(packet)    
    def handle_hero_change_equip(self, packet):
        return None

    
    # CS_CORPS_GUARD_LIST
    @CallbackBase.callback(OP_CODE.CS_CORPS_GUARD_LIST)
    def send_corps_guard_list_decorate(self, code):
        packet = cs_corps_guard_list()
        self.make_corps_guard_list_packet(packet)
        self.mes_que[code] = packet
    # makeup corps_guard_list packet
    def make_corps_guard_list_packet(self, packet):
        return None
    # send corps_guard_list
    def send_corps_guard_list(self):
        self.dispatch(OP_CODE.CS_CORPS_GUARD_LIST)(OP_CODE.CS_CORPS_GUARD_LIST)
    
    # handle SC_CORPS_GUARD_LIST
    @CallbackBase.callback(OP_CODE.SC_CORPS_GUARD_LIST)
    def handle_corps_guard_list_decorate(self, recv_buff):
        packet = sc_corps_guard_list()
        packet.deserialize(recv_buff)
        return self.handle_corps_guard_list(packet)    
    def handle_corps_guard_list(self, packet):
        return None

    
    # CS_CORPS_GUARD_BACK
    @CallbackBase.callback(OP_CODE.CS_CORPS_GUARD_BACK)
    def send_corps_guard_back_decorate(self, code):
        packet = cs_corps_guard_back()
        self.make_corps_guard_back_packet(packet)
        self.mes_que[code] = packet
    # makeup corps_guard_back packet
    def make_corps_guard_back_packet(self, packet):
        return None
    # send corps_guard_back
    def send_corps_guard_back(self):
        self.dispatch(OP_CODE.CS_CORPS_GUARD_BACK)(OP_CODE.CS_CORPS_GUARD_BACK)
    
    # handle SC_CORPS_GUARD_BACK
    @CallbackBase.callback(OP_CODE.SC_CORPS_GUARD_BACK)
    def handle_corps_guard_back_decorate(self, recv_buff):
        packet = sc_corps_guard_back()
        packet.deserialize(recv_buff)
        return self.handle_corps_guard_back(packet)    
    def handle_corps_guard_back(self, packet):
        return None

    
    # CS_CHANGE_MEDAL
    @CallbackBase.callback(OP_CODE.CS_CHANGE_MEDAL)
    def send_change_medal_decorate(self, code):
        packet = cs_change_medal()
        self.make_change_medal_packet(packet)
        self.mes_que[code] = packet
    # makeup change_medal packet
    def make_change_medal_packet(self, packet):
        return None
    # send change_medal
    def send_change_medal(self):
        self.dispatch(OP_CODE.CS_CHANGE_MEDAL)(OP_CODE.CS_CHANGE_MEDAL)
    
    # handle SC_CHANGE_MEDAL
    @CallbackBase.callback(OP_CODE.SC_CHANGE_MEDAL)
    def handle_change_medal_decorate(self, recv_buff):
        packet = sc_change_medal()
        packet.deserialize(recv_buff)
        return self.handle_change_medal(packet)    
    def handle_change_medal(self, packet):
        return None

    
    # CS_LEVY_TAX
    @CallbackBase.callback(OP_CODE.CS_LEVY_TAX)
    def send_levy_tax_decorate(self, code):
        packet = cs_levy_tax()
        self.make_levy_tax_packet(packet)
        self.mes_que[code] = packet
    # makeup levy_tax packet
    def make_levy_tax_packet(self, packet):
        return None
    # send levy_tax
    def send_levy_tax(self):
        self.dispatch(OP_CODE.CS_LEVY_TAX)(OP_CODE.CS_LEVY_TAX)
    
    # handle SC_LEVY_TAX
    @CallbackBase.callback(OP_CODE.SC_LEVY_TAX)
    def handle_levy_tax_decorate(self, recv_buff):
        packet = sc_levy_tax()
        packet.deserialize(recv_buff)
        return self.handle_levy_tax(packet)    
    def handle_levy_tax(self, packet):
        return None

    
    # CS_GET_TAX_INFO
    @CallbackBase.callback(OP_CODE.CS_GET_TAX_INFO)
    def send_get_tax_info_decorate(self, code):
        packet = cs_get_tax_info()
        self.make_get_tax_info_packet(packet)
        self.mes_que[code] = packet
    # makeup get_tax_info packet
    def make_get_tax_info_packet(self, packet):
        return None
    # send get_tax_info
    def send_get_tax_info(self):
        self.dispatch(OP_CODE.CS_GET_TAX_INFO)(OP_CODE.CS_GET_TAX_INFO)
    
    # handle SC_GET_TAX_INFO
    @CallbackBase.callback(OP_CODE.SC_GET_TAX_INFO)
    def handle_get_tax_info_decorate(self, recv_buff):
        packet = sc_get_tax_info()
        packet.deserialize(recv_buff)
        return self.handle_get_tax_info(packet)    
    def handle_get_tax_info(self, packet):
        return None

    
    # CS_GET_FORT_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_FORT_LIST)
    def send_get_fort_list_decorate(self, code):
        packet = cs_get_fort_list()
        self.make_get_fort_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_fort_list packet
    def make_get_fort_list_packet(self, packet):
        return None
    # send get_fort_list
    def send_get_fort_list(self):
        self.dispatch(OP_CODE.CS_GET_FORT_LIST)(OP_CODE.CS_GET_FORT_LIST)
    
    # handle SC_GET_FORT_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_FORT_LIST)
    def handle_get_fort_list_decorate(self, recv_buff):
        packet = sc_get_fort_list()
        packet.deserialize(recv_buff)
        return self.handle_get_fort_list(packet)    
    def handle_get_fort_list(self, packet):
        return None

    
    # CS_GARRISON_FORT
    @CallbackBase.callback(OP_CODE.CS_GARRISON_FORT)
    def send_garrison_fort_decorate(self, code):
        packet = cs_garrison_fort()
        self.make_garrison_fort_packet(packet)
        self.mes_que[code] = packet
    # makeup garrison_fort packet
    def make_garrison_fort_packet(self, packet):
        return None
    # send garrison_fort
    def send_garrison_fort(self):
        self.dispatch(OP_CODE.CS_GARRISON_FORT)(OP_CODE.CS_GARRISON_FORT)
    
    # handle SC_GARRISON_FORT
    @CallbackBase.callback(OP_CODE.SC_GARRISON_FORT)
    def handle_garrison_fort_decorate(self, recv_buff):
        packet = sc_garrison_fort()
        packet.deserialize(recv_buff)
        return self.handle_garrison_fort(packet)    
    def handle_garrison_fort(self, packet):
        return None

    
    # CS_LEAVE_FORT
    @CallbackBase.callback(OP_CODE.CS_LEAVE_FORT)
    def send_leave_fort_decorate(self, code):
        packet = cs_leave_fort()
        self.make_leave_fort_packet(packet)
        self.mes_que[code] = packet
    # makeup leave_fort packet
    def make_leave_fort_packet(self, packet):
        return None
    # send leave_fort
    def send_leave_fort(self):
        self.dispatch(OP_CODE.CS_LEAVE_FORT)(OP_CODE.CS_LEAVE_FORT)
    
    # handle SC_LEAVE_FORT
    @CallbackBase.callback(OP_CODE.SC_LEAVE_FORT)
    def handle_leave_fort_decorate(self, recv_buff):
        packet = sc_leave_fort()
        packet.deserialize(recv_buff)
        return self.handle_leave_fort(packet)    
    def handle_leave_fort(self, packet):
        return None

    
    # CS_MARKET_EXCHANGE
    @CallbackBase.callback(OP_CODE.CS_MARKET_EXCHANGE)
    def send_market_exchange_decorate(self, code):
        packet = cs_market_exchange()
        self.make_market_exchange_packet(packet)
        self.mes_que[code] = packet
    # makeup market_exchange packet
    def make_market_exchange_packet(self, packet):
        return None
    # send market_exchange
    def send_market_exchange(self):
        self.dispatch(OP_CODE.CS_MARKET_EXCHANGE)(OP_CODE.CS_MARKET_EXCHANGE)
    
    # handle SC_MARKET_EXCHANGE
    @CallbackBase.callback(OP_CODE.SC_MARKET_EXCHANGE)
    def handle_market_exchange_decorate(self, recv_buff):
        packet = sc_market_exchange()
        packet.deserialize(recv_buff)
        return self.handle_market_exchange(packet)    
    def handle_market_exchange(self, packet):
        return None

    
    # CS_MARKET_BUY
    @CallbackBase.callback(OP_CODE.CS_MARKET_BUY)
    def send_market_buy_decorate(self, code):
        packet = cs_market_buy()
        self.make_market_buy_packet(packet)
        self.mes_que[code] = packet
    # makeup market_buy packet
    def make_market_buy_packet(self, packet):
        return None
    # send market_buy
    def send_market_buy(self):
        self.dispatch(OP_CODE.CS_MARKET_BUY)(OP_CODE.CS_MARKET_BUY)
    
    # handle SC_MARKET_BUY
    @CallbackBase.callback(OP_CODE.SC_MARKET_BUY)
    def handle_market_buy_decorate(self, recv_buff):
        packet = sc_market_buy()
        packet.deserialize(recv_buff)
        return self.handle_market_buy(packet)    
    def handle_market_buy(self, packet):
        return None

    
    # CS_BUILD_TRAP
    @CallbackBase.callback(OP_CODE.CS_BUILD_TRAP)
    def send_build_trap_decorate(self, code):
        packet = cs_build_trap()
        self.make_build_trap_packet(packet)
        self.mes_que[code] = packet
    # makeup build_trap packet
    def make_build_trap_packet(self, packet):
        return None
    # send build_trap
    def send_build_trap(self):
        self.dispatch(OP_CODE.CS_BUILD_TRAP)(OP_CODE.CS_BUILD_TRAP)
    
    # handle SC_BUILD_TRAP
    @CallbackBase.callback(OP_CODE.SC_BUILD_TRAP)
    def handle_build_trap_decorate(self, recv_buff):
        packet = sc_build_trap()
        packet.deserialize(recv_buff)
        return self.handle_build_trap(packet)    
    def handle_build_trap(self, packet):
        return None

    
    # CS_GET_TRAP_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_TRAP_LIST)
    def send_get_trap_list_decorate(self, code):
        packet = cs_get_trap_list()
        self.make_get_trap_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_trap_list packet
    def make_get_trap_list_packet(self, packet):
        return None
    # send get_trap_list
    def send_get_trap_list(self):
        self.dispatch(OP_CODE.CS_GET_TRAP_LIST)(OP_CODE.CS_GET_TRAP_LIST)
    
    # handle SC_GET_TRAP_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_TRAP_LIST)
    def handle_get_trap_list_decorate(self, recv_buff):
        packet = sc_get_trap_list()
        packet.deserialize(recv_buff)
        return self.handle_get_trap_list(packet)    
    def handle_get_trap_list(self, packet):
        return None

    
    # CS_CANCEL_BUILD_TRAP
    @CallbackBase.callback(OP_CODE.CS_CANCEL_BUILD_TRAP)
    def send_cancel_build_trap_decorate(self, code):
        packet = cs_cancel_build_trap()
        self.make_cancel_build_trap_packet(packet)
        self.mes_que[code] = packet
    # makeup cancel_build_trap packet
    def make_cancel_build_trap_packet(self, packet):
        return None
    # send cancel_build_trap
    def send_cancel_build_trap(self):
        self.dispatch(OP_CODE.CS_CANCEL_BUILD_TRAP)(OP_CODE.CS_CANCEL_BUILD_TRAP)
    
    # handle SC_CANCEL_BUILD_TRAP
    @CallbackBase.callback(OP_CODE.SC_CANCEL_BUILD_TRAP)
    def handle_cancel_build_trap_decorate(self, recv_buff):
        packet = sc_cancel_build_trap()
        packet.deserialize(recv_buff)
        return self.handle_cancel_build_trap(packet)    
    def handle_cancel_build_trap(self, packet):
        return None

    
    # CS_ACCELERATE_BUILD_TRAP
    @CallbackBase.callback(OP_CODE.CS_ACCELERATE_BUILD_TRAP)
    def send_accelerate_build_trap_decorate(self, code):
        packet = cs_accelerate_build_trap()
        self.make_accelerate_build_trap_packet(packet)
        self.mes_que[code] = packet
    # makeup accelerate_build_trap packet
    def make_accelerate_build_trap_packet(self, packet):
        return None
    # send accelerate_build_trap
    def send_accelerate_build_trap(self):
        self.dispatch(OP_CODE.CS_ACCELERATE_BUILD_TRAP)(OP_CODE.CS_ACCELERATE_BUILD_TRAP)
    
    # handle SC_ACCELERATE_BUILD_TRAP
    @CallbackBase.callback(OP_CODE.SC_ACCELERATE_BUILD_TRAP)
    def handle_accelerate_build_trap_decorate(self, recv_buff):
        packet = sc_accelerate_build_trap()
        packet.deserialize(recv_buff)
        return self.handle_accelerate_build_trap(packet)    
    def handle_accelerate_build_trap(self, packet):
        return None

    
    # CS_DEMOLISH_TRAP
    @CallbackBase.callback(OP_CODE.CS_DEMOLISH_TRAP)
    def send_demolish_trap_decorate(self, code):
        packet = cs_demolish_trap()
        self.make_demolish_trap_packet(packet)
        self.mes_que[code] = packet
    # makeup demolish_trap packet
    def make_demolish_trap_packet(self, packet):
        return None
    # send demolish_trap
    def send_demolish_trap(self):
        self.dispatch(OP_CODE.CS_DEMOLISH_TRAP)(OP_CODE.CS_DEMOLISH_TRAP)
    
    # handle SC_DEMOLISH_TRAP
    @CallbackBase.callback(OP_CODE.SC_DEMOLISH_TRAP)
    def handle_demolish_trap_decorate(self, recv_buff):
        packet = sc_demolish_trap()
        packet.deserialize(recv_buff)
        return self.handle_demolish_trap(packet)    
    def handle_demolish_trap(self, packet):
        return None

    
    # CS_GET_ONE_CORPS_INFO
    @CallbackBase.callback(OP_CODE.CS_GET_ONE_CORPS_INFO)
    def send_get_one_corps_info_decorate(self, code):
        packet = cs_get_one_corps_info()
        self.make_get_one_corps_info_packet(packet)
        self.mes_que[code] = packet
    # makeup get_one_corps_info packet
    def make_get_one_corps_info_packet(self, packet):
        return None
    # send get_one_corps_info
    def send_get_one_corps_info(self):
        self.dispatch(OP_CODE.CS_GET_ONE_CORPS_INFO)(OP_CODE.CS_GET_ONE_CORPS_INFO)
    
    # handle SC_GET_ONE_CORPS_INFO
    @CallbackBase.callback(OP_CODE.SC_GET_ONE_CORPS_INFO)
    def handle_get_one_corps_info_decorate(self, recv_buff):
        packet = sc_get_one_corps_info()
        packet.deserialize(recv_buff)
        return self.handle_get_one_corps_info(packet)    
    def handle_get_one_corps_info(self, packet):
        return None

    
    # CS_GET_LAND_INFO
    @CallbackBase.callback(OP_CODE.CS_GET_LAND_INFO)
    def send_get_land_info_decorate(self, code):
        packet = cs_get_land_info()
        self.make_get_land_info_packet(packet)
        self.mes_que[code] = packet
    # makeup get_land_info packet
    def make_get_land_info_packet(self, packet):
        return None
    # send get_land_info
    def send_get_land_info(self):
        self.dispatch(OP_CODE.CS_GET_LAND_INFO)(OP_CODE.CS_GET_LAND_INFO)
    
    # handle SC_GET_LAND_INFO
    @CallbackBase.callback(OP_CODE.SC_GET_LAND_INFO)
    def handle_get_land_info_decorate(self, recv_buff):
        packet = sc_get_land_info()
        packet.deserialize(recv_buff)
        return self.handle_get_land_info(packet)    
    def handle_get_land_info(self, packet):
        return None

    
    # CS_GET_MORE_BLOCK_INFO
    @CallbackBase.callback(OP_CODE.CS_GET_MORE_BLOCK_INFO)
    def send_get_more_block_info_decorate(self, code):
        packet = cs_get_more_block_info()
        self.make_get_more_block_info_packet(packet)
        self.mes_que[code] = packet
    # makeup get_more_block_info packet
    def make_get_more_block_info_packet(self, packet):
        return None
    # send get_more_block_info
    def send_get_more_block_info(self):
        self.dispatch(OP_CODE.CS_GET_MORE_BLOCK_INFO)(OP_CODE.CS_GET_MORE_BLOCK_INFO)
    
    # handle SC_GET_MORE_BLOCK_INFO
    @CallbackBase.callback(OP_CODE.SC_GET_MORE_BLOCK_INFO)
    def handle_get_more_block_info_decorate(self, recv_buff):
        packet = sc_get_more_block_info()
        packet.deserialize(recv_buff)
        return self.handle_get_more_block_info(packet)    
    def handle_get_more_block_info(self, packet):
        return None

    
    # CS_GET_SUMMARY_USER_INFO
    @CallbackBase.callback(OP_CODE.CS_GET_SUMMARY_USER_INFO)
    def send_get_summary_user_info_decorate(self, code):
        packet = cs_get_summary_user_info()
        self.make_get_summary_user_info_packet(packet)
        self.mes_que[code] = packet
    # makeup get_summary_user_info packet
    def make_get_summary_user_info_packet(self, packet):
        return None
    # send get_summary_user_info
    def send_get_summary_user_info(self):
        self.dispatch(OP_CODE.CS_GET_SUMMARY_USER_INFO)(OP_CODE.CS_GET_SUMMARY_USER_INFO)
    
    # handle SC_GET_SUMMARY_USER_INFO
    @CallbackBase.callback(OP_CODE.SC_GET_SUMMARY_USER_INFO)
    def handle_get_summary_user_info_decorate(self, recv_buff):
        packet = sc_get_summary_user_info()
        packet.deserialize(recv_buff)
        return self.handle_get_summary_user_info(packet)    
    def handle_get_summary_user_info(self, packet):
        return None

    
    # CS_GET_BATTLE_RECORD
    @CallbackBase.callback(OP_CODE.CS_GET_BATTLE_RECORD)
    def send_get_battle_record_decorate(self, code):
        packet = cs_get_battle_record()
        self.make_get_battle_record_packet(packet)
        self.mes_que[code] = packet
    # makeup get_battle_record packet
    def make_get_battle_record_packet(self, packet):
        return None
    # send get_battle_record
    def send_get_battle_record(self):
        self.dispatch(OP_CODE.CS_GET_BATTLE_RECORD)(OP_CODE.CS_GET_BATTLE_RECORD)
    
    # handle SC_GET_BATTLE_RECORD
    @CallbackBase.callback(OP_CODE.SC_GET_BATTLE_RECORD)
    def handle_get_battle_record_decorate(self, recv_buff):
        packet = sc_get_battle_record()
        packet.deserialize(recv_buff)
        return self.handle_get_battle_record(packet)    
    def handle_get_battle_record(self, packet):
        return None

    
    # CS_GET_BATTLE_RECORD_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_BATTLE_RECORD_LIST)
    def send_get_battle_record_list_decorate(self, code):
        packet = cs_get_battle_record_list()
        self.make_get_battle_record_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_battle_record_list packet
    def make_get_battle_record_list_packet(self, packet):
        return None
    # send get_battle_record_list
    def send_get_battle_record_list(self):
        self.dispatch(OP_CODE.CS_GET_BATTLE_RECORD_LIST)(OP_CODE.CS_GET_BATTLE_RECORD_LIST)
    
    # handle SC_GET_BATTLE_RECORD_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_BATTLE_RECORD_LIST)
    def handle_get_battle_record_list_decorate(self, recv_buff):
        packet = sc_get_battle_record_list()
        packet.deserialize(recv_buff)
        return self.handle_get_battle_record_list(packet)    
    def handle_get_battle_record_list(self, packet):
        return None

    
    # CS_SYN_USER_RESOURCE
    @CallbackBase.callback(OP_CODE.CS_SYN_USER_RESOURCE)
    def send_syn_user_resource_decorate(self, code):
        packet = cs_syn_user_resource()
        self.make_syn_user_resource_packet(packet)
        self.mes_que[code] = packet
    # makeup syn_user_resource packet
    def make_syn_user_resource_packet(self, packet):
        return None
    # send syn_user_resource
    def send_syn_user_resource(self):
        self.dispatch(OP_CODE.CS_SYN_USER_RESOURCE)(OP_CODE.CS_SYN_USER_RESOURCE)
    
    # handle SC_SYN_USER_RESOURCE
    @CallbackBase.callback(OP_CODE.SC_SYN_USER_RESOURCE)
    def handle_syn_user_resource_decorate(self, recv_buff):
        packet = sc_syn_user_resource()
        packet.deserialize(recv_buff)
        return self.handle_syn_user_resource(packet)    
    def handle_syn_user_resource(self, packet):
        return None

    
    # CS_SYN_USER_RESOURCE_LIMIT
    @CallbackBase.callback(OP_CODE.CS_SYN_USER_RESOURCE_LIMIT)
    def send_syn_user_resource_limit_decorate(self, code):
        packet = cs_syn_user_resource_limit()
        self.make_syn_user_resource_limit_packet(packet)
        self.mes_que[code] = packet
    # makeup syn_user_resource_limit packet
    def make_syn_user_resource_limit_packet(self, packet):
        return None
    # send syn_user_resource_limit
    def send_syn_user_resource_limit(self):
        self.dispatch(OP_CODE.CS_SYN_USER_RESOURCE_LIMIT)(OP_CODE.CS_SYN_USER_RESOURCE_LIMIT)
    
    # handle SC_SYN_USER_RESOURCE_LIMIT
    @CallbackBase.callback(OP_CODE.SC_SYN_USER_RESOURCE_LIMIT)
    def handle_syn_user_resource_limit_decorate(self, recv_buff):
        packet = sc_syn_user_resource_limit()
        packet.deserialize(recv_buff)
        return self.handle_syn_user_resource_limit(packet)    
    def handle_syn_user_resource_limit(self, packet):
        return None

    
    # CS_CHANGE_HEAD_ENTRY
    @CallbackBase.callback(OP_CODE.CS_CHANGE_HEAD_ENTRY)
    def send_change_head_entry_decorate(self, code):
        packet = cs_change_head_entry()
        self.make_change_head_entry_packet(packet)
        self.mes_que[code] = packet
    # makeup change_head_entry packet
    def make_change_head_entry_packet(self, packet):
        return None
    # send change_head_entry
    def send_change_head_entry(self):
        self.dispatch(OP_CODE.CS_CHANGE_HEAD_ENTRY)(OP_CODE.CS_CHANGE_HEAD_ENTRY)
    
    # handle SC_CHANGE_HEAD_ENTRY
    @CallbackBase.callback(OP_CODE.SC_CHANGE_HEAD_ENTRY)
    def handle_change_head_entry_decorate(self, recv_buff):
        packet = sc_change_head_entry()
        packet.deserialize(recv_buff)
        return self.handle_change_head_entry(packet)    
    def handle_change_head_entry(self, packet):
        return None

    
    # CS_CHANGE_SIGNATURE
    @CallbackBase.callback(OP_CODE.CS_CHANGE_SIGNATURE)
    def send_change_signature_decorate(self, code):
        packet = cs_change_signature()
        self.make_change_signature_packet(packet)
        self.mes_que[code] = packet
    # makeup change_signature packet
    def make_change_signature_packet(self, packet):
        return None
    # send change_signature
    def send_change_signature(self):
        self.dispatch(OP_CODE.CS_CHANGE_SIGNATURE)(OP_CODE.CS_CHANGE_SIGNATURE)
    
    # handle SC_CHANGE_SIGNATURE
    @CallbackBase.callback(OP_CODE.SC_CHANGE_SIGNATURE)
    def handle_change_signature_decorate(self, recv_buff):
        packet = sc_change_signature()
        packet.deserialize(recv_buff)
        return self.handle_change_signature(packet)    
    def handle_change_signature(self, packet):
        return None

    
    # CS_PAY_FOR_FREE
    @CallbackBase.callback(OP_CODE.CS_PAY_FOR_FREE)
    def send_pay_for_free_decorate(self, code):
        packet = cs_pay_for_free()
        self.make_pay_for_free_packet(packet)
        self.mes_que[code] = packet
    # makeup pay_for_free packet
    def make_pay_for_free_packet(self, packet):
        return None
    # send pay_for_free
    def send_pay_for_free(self):
        self.dispatch(OP_CODE.CS_PAY_FOR_FREE)(OP_CODE.CS_PAY_FOR_FREE)
    
    # handle SC_PAY_FOR_FREE
    @CallbackBase.callback(OP_CODE.SC_PAY_FOR_FREE)
    def handle_pay_for_free_decorate(self, recv_buff):
        packet = sc_pay_for_free()
        packet.deserialize(recv_buff)
        return self.handle_pay_for_free(packet)    
    def handle_pay_for_free(self, packet):
        return None

    
    # CS_LIBERATE
    @CallbackBase.callback(OP_CODE.CS_LIBERATE)
    def send_liberate_decorate(self, code):
        packet = cs_liberate()
        self.make_liberate_packet(packet)
        self.mes_que[code] = packet
    # makeup liberate packet
    def make_liberate_packet(self, packet):
        return None
    # send liberate
    def send_liberate(self):
        self.dispatch(OP_CODE.CS_LIBERATE)(OP_CODE.CS_LIBERATE)
    
    # handle SC_LIBERATE
    @CallbackBase.callback(OP_CODE.SC_LIBERATE)
    def handle_liberate_decorate(self, recv_buff):
        packet = sc_liberate()
        packet.deserialize(recv_buff)
        return self.handle_liberate(packet)    
    def handle_liberate(self, packet):
        return None

    
    # CS_GET_INVADER_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_INVADER_LIST)
    def send_get_invader_list_decorate(self, code):
        packet = cs_get_invader_list()
        self.make_get_invader_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_invader_list packet
    def make_get_invader_list_packet(self, packet):
        return None
    # send get_invader_list
    def send_get_invader_list(self):
        self.dispatch(OP_CODE.CS_GET_INVADER_LIST)(OP_CODE.CS_GET_INVADER_LIST)
    
    # handle SC_GET_INVADER_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_INVADER_LIST)
    def handle_get_invader_list_decorate(self, recv_buff):
        packet = sc_get_invader_list()
        packet.deserialize(recv_buff)
        return self.handle_get_invader_list(packet)    
    def handle_get_invader_list(self, packet):
        return None

    
    # CS_CHANGE_NICK_NAME
    @CallbackBase.callback(OP_CODE.CS_CHANGE_NICK_NAME)
    def send_change_nick_name_decorate(self, code):
        packet = cs_change_nick_name()
        self.make_change_nick_name_packet(packet)
        self.mes_que[code] = packet
    # makeup change_nick_name packet
    def make_change_nick_name_packet(self, packet):
        return None
    # send change_nick_name
    def send_change_nick_name(self):
        self.dispatch(OP_CODE.CS_CHANGE_NICK_NAME)(OP_CODE.CS_CHANGE_NICK_NAME)
    
    # handle SC_CHANGE_NICK_NAME
    @CallbackBase.callback(OP_CODE.SC_CHANGE_NICK_NAME)
    def handle_change_nick_name_decorate(self, recv_buff):
        packet = sc_change_nick_name()
        packet.deserialize(recv_buff)
        return self.handle_change_nick_name(packet)    
    def handle_change_nick_name(self, packet):
        return None

    
    # CS_USER_POWER_DATA
    @CallbackBase.callback(OP_CODE.CS_USER_POWER_DATA)
    def send_user_power_data_decorate(self, code):
        packet = cs_user_power_data()
        self.make_user_power_data_packet(packet)
        self.mes_que[code] = packet
    # makeup user_power_data packet
    def make_user_power_data_packet(self, packet):
        return None
    # send user_power_data
    def send_user_power_data(self):
        self.dispatch(OP_CODE.CS_USER_POWER_DATA)(OP_CODE.CS_USER_POWER_DATA)
    
    # handle SC_USER_POWER_DATA
    @CallbackBase.callback(OP_CODE.SC_USER_POWER_DATA)
    def handle_user_power_data_decorate(self, recv_buff):
        packet = sc_user_power_data()
        packet.deserialize(recv_buff)
        return self.handle_user_power_data(packet)    
    def handle_user_power_data(self, packet):
        return None

    
    # CS_GO_HOME_IMMEDIATELY
    @CallbackBase.callback(OP_CODE.CS_GO_HOME_IMMEDIATELY)
    def send_go_home_immediately_decorate(self, code):
        packet = cs_go_home_immediately()
        self.make_go_home_immediately_packet(packet)
        self.mes_que[code] = packet
    # makeup go_home_immediately packet
    def make_go_home_immediately_packet(self, packet):
        return None
    # send go_home_immediately
    def send_go_home_immediately(self):
        self.dispatch(OP_CODE.CS_GO_HOME_IMMEDIATELY)(OP_CODE.CS_GO_HOME_IMMEDIATELY)
    
    # handle SC_GO_HOME_IMMEDIATELY
    @CallbackBase.callback(OP_CODE.SC_GO_HOME_IMMEDIATELY)
    def handle_go_home_immediately_decorate(self, recv_buff):
        packet = sc_go_home_immediately()
        packet.deserialize(recv_buff)
        return self.handle_go_home_immediately(packet)    
    def handle_go_home_immediately(self, packet):
        return None

    
    # CS_GUILD_DATA_REQ
    @CallbackBase.callback(OP_CODE.CS_GUILD_DATA_REQ)
    def send_guild_data_req_decorate(self, code):
        packet = cs_guild_data_req()
        self.make_guild_data_req_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_data_req packet
    def make_guild_data_req_packet(self, packet):
        return None
    # send guild_data_req
    def send_guild_data_req(self):
        self.dispatch(OP_CODE.CS_GUILD_DATA_REQ)(OP_CODE.CS_GUILD_DATA_REQ)
    
    # handle SC_GUILD_DATA_REQ
    @CallbackBase.callback(OP_CODE.SC_GUILD_DATA_REQ)
    def handle_guild_data_req_decorate(self, recv_buff):
        packet = sc_guild_data_req()
        packet.deserialize(recv_buff)
        return self.handle_guild_data_req(packet)    
    def handle_guild_data_req(self, packet):
        return None

    
    # CS_GUILD_CREATE
    @CallbackBase.callback(OP_CODE.CS_GUILD_CREATE)
    def send_guild_create_decorate(self, code):
        packet = cs_guild_create()
        self.make_guild_create_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_create packet
    def make_guild_create_packet(self, packet):
        return None
    # send guild_create
    def send_guild_create(self):
        self.dispatch(OP_CODE.CS_GUILD_CREATE)(OP_CODE.CS_GUILD_CREATE)
    
    # handle SC_GUILD_CREATE
    @CallbackBase.callback(OP_CODE.SC_GUILD_CREATE)
    def handle_guild_create_decorate(self, recv_buff):
        packet = sc_guild_create()
        packet.deserialize(recv_buff)
        return self.handle_guild_create(packet)    
    def handle_guild_create(self, packet):
        return None

    
    # CS_GUILD_CONTRIBUTE
    @CallbackBase.callback(OP_CODE.CS_GUILD_CONTRIBUTE)
    def send_guild_contribute_decorate(self, code):
        packet = cs_guild_contribute()
        self.make_guild_contribute_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_contribute packet
    def make_guild_contribute_packet(self, packet):
        return None
    # send guild_contribute
    def send_guild_contribute(self):
        self.dispatch(OP_CODE.CS_GUILD_CONTRIBUTE)(OP_CODE.CS_GUILD_CONTRIBUTE)
    
    # handle SC_GUILD_CONTRIBUTE
    @CallbackBase.callback(OP_CODE.SC_GUILD_CONTRIBUTE)
    def handle_guild_contribute_decorate(self, recv_buff):
        packet = sc_guild_contribute()
        packet.deserialize(recv_buff)
        return self.handle_guild_contribute(packet)    
    def handle_guild_contribute(self, packet):
        return None

    
    # CS_GUILD_APPLY
    @CallbackBase.callback(OP_CODE.CS_GUILD_APPLY)
    def send_guild_apply_decorate(self, code):
        packet = cs_guild_apply()
        self.make_guild_apply_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_apply packet
    def make_guild_apply_packet(self, packet):
        return None
    # send guild_apply
    def send_guild_apply(self):
        self.dispatch(OP_CODE.CS_GUILD_APPLY)(OP_CODE.CS_GUILD_APPLY)
    
    # handle SC_GUILD_APPLY
    @CallbackBase.callback(OP_CODE.SC_GUILD_APPLY)
    def handle_guild_apply_decorate(self, recv_buff):
        packet = sc_guild_apply()
        packet.deserialize(recv_buff)
        return self.handle_guild_apply(packet)    
    def handle_guild_apply(self, packet):
        return None

    
    # CS_GUILD_APPLICATION_REQ
    @CallbackBase.callback(OP_CODE.CS_GUILD_APPLICATION_REQ)
    def send_guild_application_req_decorate(self, code):
        packet = cs_guild_application_req()
        self.make_guild_application_req_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_application_req packet
    def make_guild_application_req_packet(self, packet):
        return None
    # send guild_application_req
    def send_guild_application_req(self):
        self.dispatch(OP_CODE.CS_GUILD_APPLICATION_REQ)(OP_CODE.CS_GUILD_APPLICATION_REQ)
    
    # handle SC_GUILD_APPLICATION_REQ
    @CallbackBase.callback(OP_CODE.SC_GUILD_APPLICATION_REQ)
    def handle_guild_application_req_decorate(self, recv_buff):
        packet = sc_guild_application_req()
        packet.deserialize(recv_buff)
        return self.handle_guild_application_req(packet)    
    def handle_guild_application_req(self, packet):
        return None

    
    # CS_GUILD_APPLICATION_PROCESS
    @CallbackBase.callback(OP_CODE.CS_GUILD_APPLICATION_PROCESS)
    def send_guild_application_process_decorate(self, code):
        packet = cs_guild_application_process()
        self.make_guild_application_process_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_application_process packet
    def make_guild_application_process_packet(self, packet):
        return None
    # send guild_application_process
    def send_guild_application_process(self):
        self.dispatch(OP_CODE.CS_GUILD_APPLICATION_PROCESS)(OP_CODE.CS_GUILD_APPLICATION_PROCESS)
    
    # handle SC_GUILD_APPLICATION_PROCESS
    @CallbackBase.callback(OP_CODE.SC_GUILD_APPLICATION_PROCESS)
    def handle_guild_application_process_decorate(self, recv_buff):
        packet = sc_guild_application_process()
        packet.deserialize(recv_buff)
        return self.handle_guild_application_process(packet)    
    def handle_guild_application_process(self, packet):
        return None

    
    # CS_GUILD_EXPEL_MEMBER
    @CallbackBase.callback(OP_CODE.CS_GUILD_EXPEL_MEMBER)
    def send_guild_expel_member_decorate(self, code):
        packet = cs_guild_expel_member()
        self.make_guild_expel_member_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_expel_member packet
    def make_guild_expel_member_packet(self, packet):
        return None
    # send guild_expel_member
    def send_guild_expel_member(self):
        self.dispatch(OP_CODE.CS_GUILD_EXPEL_MEMBER)(OP_CODE.CS_GUILD_EXPEL_MEMBER)
    
    # handle SC_GUILD_EXPEL_MEMBER
    @CallbackBase.callback(OP_CODE.SC_GUILD_EXPEL_MEMBER)
    def handle_guild_expel_member_decorate(self, recv_buff):
        packet = sc_guild_expel_member()
        packet.deserialize(recv_buff)
        return self.handle_guild_expel_member(packet)    
    def handle_guild_expel_member(self, packet):
        return None

    
    # CS_GUILD_QUIT
    @CallbackBase.callback(OP_CODE.CS_GUILD_QUIT)
    def send_guild_quit_decorate(self, code):
        packet = cs_guild_quit()
        self.make_guild_quit_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_quit packet
    def make_guild_quit_packet(self, packet):
        return None
    # send guild_quit
    def send_guild_quit(self):
        self.dispatch(OP_CODE.CS_GUILD_QUIT)(OP_CODE.CS_GUILD_QUIT)
    
    # handle SC_GUILD_QUIT
    @CallbackBase.callback(OP_CODE.SC_GUILD_QUIT)
    def handle_guild_quit_decorate(self, recv_buff):
        packet = sc_guild_quit()
        packet.deserialize(recv_buff)
        return self.handle_guild_quit(packet)    
    def handle_guild_quit(self, packet):
        return None

    
    # CS_GUILD_TRANSFER
    @CallbackBase.callback(OP_CODE.CS_GUILD_TRANSFER)
    def send_guild_transfer_decorate(self, code):
        packet = cs_guild_transfer()
        self.make_guild_transfer_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_transfer packet
    def make_guild_transfer_packet(self, packet):
        return None
    # send guild_transfer
    def send_guild_transfer(self):
        self.dispatch(OP_CODE.CS_GUILD_TRANSFER)(OP_CODE.CS_GUILD_TRANSFER)
    
    # handle SC_GUILD_TRANSFER
    @CallbackBase.callback(OP_CODE.SC_GUILD_TRANSFER)
    def handle_guild_transfer_decorate(self, recv_buff):
        packet = sc_guild_transfer()
        packet.deserialize(recv_buff)
        return self.handle_guild_transfer(packet)    
    def handle_guild_transfer(self, packet):
        return None

    
    # CS_GUILD_COMMISSION
    @CallbackBase.callback(OP_CODE.CS_GUILD_COMMISSION)
    def send_guild_commission_decorate(self, code):
        packet = cs_guild_commission()
        self.make_guild_commission_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_commission packet
    def make_guild_commission_packet(self, packet):
        return None
    # send guild_commission
    def send_guild_commission(self):
        self.dispatch(OP_CODE.CS_GUILD_COMMISSION)(OP_CODE.CS_GUILD_COMMISSION)
    
    # handle SC_GUILD_COMMISSION
    @CallbackBase.callback(OP_CODE.SC_GUILD_COMMISSION)
    def handle_guild_commission_decorate(self, recv_buff):
        packet = sc_guild_commission()
        packet.deserialize(recv_buff)
        return self.handle_guild_commission(packet)    
    def handle_guild_commission(self, packet):
        return None

    
    # CS_GUILD_DISMISS
    @CallbackBase.callback(OP_CODE.CS_GUILD_DISMISS)
    def send_guild_dismiss_decorate(self, code):
        packet = cs_guild_dismiss()
        self.make_guild_dismiss_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_dismiss packet
    def make_guild_dismiss_packet(self, packet):
        return None
    # send guild_dismiss
    def send_guild_dismiss(self):
        self.dispatch(OP_CODE.CS_GUILD_DISMISS)(OP_CODE.CS_GUILD_DISMISS)
    
    # handle SC_GUILD_DISMISS
    @CallbackBase.callback(OP_CODE.SC_GUILD_DISMISS)
    def handle_guild_dismiss_decorate(self, recv_buff):
        packet = sc_guild_dismiss()
        packet.deserialize(recv_buff)
        return self.handle_guild_dismiss(packet)    
    def handle_guild_dismiss(self, packet):
        return None

    
    # CS_GUILD_SET_NOITCE
    @CallbackBase.callback(OP_CODE.CS_GUILD_SET_NOITCE)
    def send_guild_set_noitce_decorate(self, code):
        packet = cs_guild_set_noitce()
        self.make_guild_set_noitce_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_set_noitce packet
    def make_guild_set_noitce_packet(self, packet):
        return None
    # send guild_set_noitce
    def send_guild_set_noitce(self):
        self.dispatch(OP_CODE.CS_GUILD_SET_NOITCE)(OP_CODE.CS_GUILD_SET_NOITCE)
    
    # handle SC_GUILD_SET_NOITCE
    @CallbackBase.callback(OP_CODE.SC_GUILD_SET_NOITCE)
    def handle_guild_set_noitce_decorate(self, recv_buff):
        packet = sc_guild_set_noitce()
        packet.deserialize(recv_buff)
        return self.handle_guild_set_noitce(packet)    
    def handle_guild_set_noitce(self, packet):
        return None

    
    # CS_GUILD_SEARCH
    @CallbackBase.callback(OP_CODE.CS_GUILD_SEARCH)
    def send_guild_search_decorate(self, code):
        packet = cs_guild_search()
        self.make_guild_search_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_search packet
    def make_guild_search_packet(self, packet):
        return None
    # send guild_search
    def send_guild_search(self):
        self.dispatch(OP_CODE.CS_GUILD_SEARCH)(OP_CODE.CS_GUILD_SEARCH)
    
    # handle SC_GUILD_SEARCH
    @CallbackBase.callback(OP_CODE.SC_GUILD_SEARCH)
    def handle_guild_search_decorate(self, recv_buff):
        packet = sc_guild_search()
        packet.deserialize(recv_buff)
        return self.handle_guild_search(packet)    
    def handle_guild_search(self, packet):
        return None

    
    # CS_GUILD_LIST_REQ
    @CallbackBase.callback(OP_CODE.CS_GUILD_LIST_REQ)
    def send_guild_list_req_decorate(self, code):
        packet = cs_guild_list_req()
        self.make_guild_list_req_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_list_req packet
    def make_guild_list_req_packet(self, packet):
        return None
    # send guild_list_req
    def send_guild_list_req(self):
        self.dispatch(OP_CODE.CS_GUILD_LIST_REQ)(OP_CODE.CS_GUILD_LIST_REQ)
    
    # handle SC_GUILD_LIST_REQ
    @CallbackBase.callback(OP_CODE.SC_GUILD_LIST_REQ)
    def handle_guild_list_req_decorate(self, recv_buff):
        packet = sc_guild_list_req()
        packet.deserialize(recv_buff)
        return self.handle_guild_list_req(packet)    
    def handle_guild_list_req(self, packet):
        return None

    
    # CS_GUILD_INVITE
    @CallbackBase.callback(OP_CODE.CS_GUILD_INVITE)
    def send_guild_invite_decorate(self, code):
        packet = cs_guild_invite()
        self.make_guild_invite_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_invite packet
    def make_guild_invite_packet(self, packet):
        return None
    # send guild_invite
    def send_guild_invite(self):
        self.dispatch(OP_CODE.CS_GUILD_INVITE)(OP_CODE.CS_GUILD_INVITE)
    
    # handle SC_GUILD_INVITE
    @CallbackBase.callback(OP_CODE.SC_GUILD_INVITE)
    def handle_guild_invite_decorate(self, recv_buff):
        packet = sc_guild_invite()
        packet.deserialize(recv_buff)
        return self.handle_guild_invite(packet)    
    def handle_guild_invite(self, packet):
        return None

    
    # CS_GUILD_INVITATION_REQ
    @CallbackBase.callback(OP_CODE.CS_GUILD_INVITATION_REQ)
    def send_guild_invitation_req_decorate(self, code):
        packet = cs_guild_invitation_req()
        self.make_guild_invitation_req_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_invitation_req packet
    def make_guild_invitation_req_packet(self, packet):
        return None
    # send guild_invitation_req
    def send_guild_invitation_req(self):
        self.dispatch(OP_CODE.CS_GUILD_INVITATION_REQ)(OP_CODE.CS_GUILD_INVITATION_REQ)
    
    # handle SC_GUILD_INVITATION_REQ
    @CallbackBase.callback(OP_CODE.SC_GUILD_INVITATION_REQ)
    def handle_guild_invitation_req_decorate(self, recv_buff):
        packet = sc_guild_invitation_req()
        packet.deserialize(recv_buff)
        return self.handle_guild_invitation_req(packet)    
    def handle_guild_invitation_req(self, packet):
        return None

    
    # CS_GUILD_INVITATION_PROCESS
    @CallbackBase.callback(OP_CODE.CS_GUILD_INVITATION_PROCESS)
    def send_guild_invitation_process_decorate(self, code):
        packet = cs_guild_invitation_process()
        self.make_guild_invitation_process_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_invitation_process packet
    def make_guild_invitation_process_packet(self, packet):
        return None
    # send guild_invitation_process
    def send_guild_invitation_process(self):
        self.dispatch(OP_CODE.CS_GUILD_INVITATION_PROCESS)(OP_CODE.CS_GUILD_INVITATION_PROCESS)
    
    # handle SC_GUILD_INVITATION_PROCESS
    @CallbackBase.callback(OP_CODE.SC_GUILD_INVITATION_PROCESS)
    def handle_guild_invitation_process_decorate(self, recv_buff):
        packet = sc_guild_invitation_process()
        packet.deserialize(recv_buff)
        return self.handle_guild_invitation_process(packet)    
    def handle_guild_invitation_process(self, packet):
        return None

    
    # CS_GET_MISSION_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_MISSION_LIST)
    def send_get_mission_list_decorate(self, code):
        packet = cs_get_mission_list()
        self.make_get_mission_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_mission_list packet
    def make_get_mission_list_packet(self, packet):
        return None
    # send get_mission_list
    def send_get_mission_list(self):
        self.dispatch(OP_CODE.CS_GET_MISSION_LIST)(OP_CODE.CS_GET_MISSION_LIST)
    
    # handle SC_GET_MISSION_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_MISSION_LIST)
    def handle_get_mission_list_decorate(self, recv_buff):
        packet = sc_get_mission_list()
        packet.deserialize(recv_buff)
        return self.handle_get_mission_list(packet)    
    def handle_get_mission_list(self, packet):
        return None

    
    # CS_GET_MISSION_REWARDS
    @CallbackBase.callback(OP_CODE.CS_GET_MISSION_REWARDS)
    def send_get_mission_rewards_decorate(self, code):
        packet = cs_get_mission_rewards()
        self.make_get_mission_rewards_packet(packet)
        self.mes_que[code] = packet
    # makeup get_mission_rewards packet
    def make_get_mission_rewards_packet(self, packet):
        return None
    # send get_mission_rewards
    def send_get_mission_rewards(self):
        self.dispatch(OP_CODE.CS_GET_MISSION_REWARDS)(OP_CODE.CS_GET_MISSION_REWARDS)
    
    # handle SC_GET_MISSION_REWARDS
    @CallbackBase.callback(OP_CODE.SC_GET_MISSION_REWARDS)
    def handle_get_mission_rewards_decorate(self, recv_buff):
        packet = sc_get_mission_rewards()
        packet.deserialize(recv_buff)
        return self.handle_get_mission_rewards(packet)    
    def handle_get_mission_rewards(self, packet):
        return None

    
    # CS_GET_ACHIEVEMENT_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_ACHIEVEMENT_LIST)
    def send_get_achievement_list_decorate(self, code):
        packet = cs_get_achievement_list()
        self.make_get_achievement_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_achievement_list packet
    def make_get_achievement_list_packet(self, packet):
        return None
    # send get_achievement_list
    def send_get_achievement_list(self):
        self.dispatch(OP_CODE.CS_GET_ACHIEVEMENT_LIST)(OP_CODE.CS_GET_ACHIEVEMENT_LIST)
    
    # handle SC_GET_ACHIEVEMENT_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_ACHIEVEMENT_LIST)
    def handle_get_achievement_list_decorate(self, recv_buff):
        packet = sc_get_achievement_list()
        packet.deserialize(recv_buff)
        return self.handle_get_achievement_list(packet)    
    def handle_get_achievement_list(self, packet):
        return None

    
    # CS_GET_ACHIEVEMENT_REWARDS
    @CallbackBase.callback(OP_CODE.CS_GET_ACHIEVEMENT_REWARDS)
    def send_get_achievement_rewards_decorate(self, code):
        packet = cs_get_achievement_rewards()
        self.make_get_achievement_rewards_packet(packet)
        self.mes_que[code] = packet
    # makeup get_achievement_rewards packet
    def make_get_achievement_rewards_packet(self, packet):
        return None
    # send get_achievement_rewards
    def send_get_achievement_rewards(self):
        self.dispatch(OP_CODE.CS_GET_ACHIEVEMENT_REWARDS)(OP_CODE.CS_GET_ACHIEVEMENT_REWARDS)
    
    # handle SC_GET_ACHIEVEMENT_REWARDS
    @CallbackBase.callback(OP_CODE.SC_GET_ACHIEVEMENT_REWARDS)
    def handle_get_achievement_rewards_decorate(self, recv_buff):
        packet = sc_get_achievement_rewards()
        packet.deserialize(recv_buff)
        return self.handle_get_achievement_rewards(packet)    
    def handle_get_achievement_rewards(self, packet):
        return None

    
    # CS_GUILD_GET_RELATIONSHIP
    @CallbackBase.callback(OP_CODE.CS_GUILD_GET_RELATIONSHIP)
    def send_guild_get_relationship_decorate(self, code):
        packet = cs_guild_get_relationship()
        self.make_guild_get_relationship_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_get_relationship packet
    def make_guild_get_relationship_packet(self, packet):
        return None
    # send guild_get_relationship
    def send_guild_get_relationship(self):
        self.dispatch(OP_CODE.CS_GUILD_GET_RELATIONSHIP)(OP_CODE.CS_GUILD_GET_RELATIONSHIP)
    
    # handle SC_GUILD_GET_RELATIONSHIP
    @CallbackBase.callback(OP_CODE.SC_GUILD_GET_RELATIONSHIP)
    def handle_guild_get_relationship_decorate(self, recv_buff):
        packet = sc_guild_get_relationship()
        packet.deserialize(recv_buff)
        return self.handle_guild_get_relationship(packet)    
    def handle_guild_get_relationship(self, packet):
        return None

    
    # CS_GUILD_SET_RELATIONSHIP
    @CallbackBase.callback(OP_CODE.CS_GUILD_SET_RELATIONSHIP)
    def send_guild_set_relationship_decorate(self, code):
        packet = cs_guild_set_relationship()
        self.make_guild_set_relationship_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_set_relationship packet
    def make_guild_set_relationship_packet(self, packet):
        return None
    # send guild_set_relationship
    def send_guild_set_relationship(self):
        self.dispatch(OP_CODE.CS_GUILD_SET_RELATIONSHIP)(OP_CODE.CS_GUILD_SET_RELATIONSHIP)
    
    # handle SC_GUILD_SET_RELATIONSHIP
    @CallbackBase.callback(OP_CODE.SC_GUILD_SET_RELATIONSHIP)
    def handle_guild_set_relationship_decorate(self, recv_buff):
        packet = sc_guild_set_relationship()
        packet.deserialize(recv_buff)
        return self.handle_guild_set_relationship(packet)    
    def handle_guild_set_relationship(self, packet):
        return None

    
    # CS_SHOP_BUY
    @CallbackBase.callback(OP_CODE.CS_SHOP_BUY)
    def send_shop_buy_decorate(self, code):
        packet = cs_shop_buy()
        self.make_shop_buy_packet(packet)
        self.mes_que[code] = packet
    # makeup shop_buy packet
    def make_shop_buy_packet(self, packet):
        return None
    # send shop_buy
    def send_shop_buy(self):
        self.dispatch(OP_CODE.CS_SHOP_BUY)(OP_CODE.CS_SHOP_BUY)
    
    # handle SC_SHOP_BUY
    @CallbackBase.callback(OP_CODE.SC_SHOP_BUY)
    def handle_shop_buy_decorate(self, recv_buff):
        packet = sc_shop_buy()
        packet.deserialize(recv_buff)
        return self.handle_shop_buy(packet)    
    def handle_shop_buy(self, packet):
        return None

    
    # CS_FREE_MAN_LIST
    @CallbackBase.callback(OP_CODE.CS_FREE_MAN_LIST)
    def send_free_man_list_decorate(self, code):
        packet = cs_free_man_list()
        self.make_free_man_list_packet(packet)
        self.mes_que[code] = packet
    # makeup free_man_list packet
    def make_free_man_list_packet(self, packet):
        return None
    # send free_man_list
    def send_free_man_list(self):
        self.dispatch(OP_CODE.CS_FREE_MAN_LIST)(OP_CODE.CS_FREE_MAN_LIST)
    
    # handle SC_FREE_MAN_LIST
    @CallbackBase.callback(OP_CODE.SC_FREE_MAN_LIST)
    def handle_free_man_list_decorate(self, recv_buff):
        packet = sc_free_man_list()
        packet.deserialize(recv_buff)
        return self.handle_free_man_list(packet)    
    def handle_free_man_list(self, packet):
        return None

    
    # CS_EQUIP_COMBINE
    @CallbackBase.callback(OP_CODE.CS_EQUIP_COMBINE)
    def send_equip_combine_decorate(self, code):
        packet = cs_equip_combine()
        self.make_equip_combine_packet(packet)
        self.mes_que[code] = packet
    # makeup equip_combine packet
    def make_equip_combine_packet(self, packet):
        return None
    # send equip_combine
    def send_equip_combine(self):
        self.dispatch(OP_CODE.CS_EQUIP_COMBINE)(OP_CODE.CS_EQUIP_COMBINE)
    
    # handle SC_EQUIP_COMBINE
    @CallbackBase.callback(OP_CODE.SC_EQUIP_COMBINE)
    def handle_equip_combine_decorate(self, recv_buff):
        packet = sc_equip_combine()
        packet.deserialize(recv_buff)
        return self.handle_equip_combine(packet)    
    def handle_equip_combine(self, packet):
        return None

    
    # CS_EQUIP_RESOLVE
    @CallbackBase.callback(OP_CODE.CS_EQUIP_RESOLVE)
    def send_equip_resolve_decorate(self, code):
        packet = cs_equip_resolve()
        self.make_equip_resolve_packet(packet)
        self.mes_que[code] = packet
    # makeup equip_resolve packet
    def make_equip_resolve_packet(self, packet):
        return None
    # send equip_resolve
    def send_equip_resolve(self):
        self.dispatch(OP_CODE.CS_EQUIP_RESOLVE)(OP_CODE.CS_EQUIP_RESOLVE)
    
    # handle SC_EQUIP_RESOLVE
    @CallbackBase.callback(OP_CODE.SC_EQUIP_RESOLVE)
    def handle_equip_resolve_decorate(self, recv_buff):
        packet = sc_equip_resolve()
        packet.deserialize(recv_buff)
        return self.handle_equip_resolve(packet)    
    def handle_equip_resolve(self, packet):
        return None

    
    # CS_HERO_EQUIP_SLOT_STRENGTHEN
    @CallbackBase.callback(OP_CODE.CS_HERO_EQUIP_SLOT_STRENGTHEN)
    def send_hero_equip_slot_strengthen_decorate(self, code):
        packet = cs_hero_equip_slot_strengthen()
        self.make_hero_equip_slot_strengthen_packet(packet)
        self.mes_que[code] = packet
    # makeup hero_equip_slot_strengthen packet
    def make_hero_equip_slot_strengthen_packet(self, packet):
        return None
    # send hero_equip_slot_strengthen
    def send_hero_equip_slot_strengthen(self):
        self.dispatch(OP_CODE.CS_HERO_EQUIP_SLOT_STRENGTHEN)(OP_CODE.CS_HERO_EQUIP_SLOT_STRENGTHEN)
    
    # handle SC_HERO_EQUIP_SLOT_STRENGTHEN
    @CallbackBase.callback(OP_CODE.SC_HERO_EQUIP_SLOT_STRENGTHEN)
    def handle_hero_equip_slot_strengthen_decorate(self, recv_buff):
        packet = sc_hero_equip_slot_strengthen()
        packet.deserialize(recv_buff)
        return self.handle_hero_equip_slot_strengthen(packet)    
    def handle_hero_equip_slot_strengthen(self, packet):
        return None

    
    # CS_GUILDLOG_LIST
    @CallbackBase.callback(OP_CODE.CS_GUILDLOG_LIST)
    def send_guildlog_list_decorate(self, code):
        packet = cs_guildlog_list()
        self.make_guildlog_list_packet(packet)
        self.mes_que[code] = packet
    # makeup guildlog_list packet
    def make_guildlog_list_packet(self, packet):
        return None
    # send guildlog_list
    def send_guildlog_list(self):
        self.dispatch(OP_CODE.CS_GUILDLOG_LIST)(OP_CODE.CS_GUILDLOG_LIST)
    
    # handle SC_GUILDLOG_LIST
    @CallbackBase.callback(OP_CODE.SC_GUILDLOG_LIST)
    def handle_guildlog_list_decorate(self, recv_buff):
        packet = sc_guildlog_list()
        packet.deserialize(recv_buff)
        return self.handle_guildlog_list(packet)    
    def handle_guildlog_list(self, packet):
        return None

    
    # CS_GUILD_MARK_REQ
    @CallbackBase.callback(OP_CODE.CS_GUILD_MARK_REQ)
    def send_guild_mark_req_decorate(self, code):
        packet = cs_guild_mark_req()
        self.make_guild_mark_req_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_mark_req packet
    def make_guild_mark_req_packet(self, packet):
        return None
    # send guild_mark_req
    def send_guild_mark_req(self):
        self.dispatch(OP_CODE.CS_GUILD_MARK_REQ)(OP_CODE.CS_GUILD_MARK_REQ)
    
    # handle SC_GUILD_MARK_REQ
    @CallbackBase.callback(OP_CODE.SC_GUILD_MARK_REQ)
    def handle_guild_mark_req_decorate(self, recv_buff):
        packet = sc_guild_mark_req()
        packet.deserialize(recv_buff)
        return self.handle_guild_mark_req(packet)    
    def handle_guild_mark_req(self, packet):
        return None

    
    # CS_GUILD_MARK
    @CallbackBase.callback(OP_CODE.CS_GUILD_MARK)
    def send_guild_mark_decorate(self, code):
        packet = cs_guild_mark()
        self.make_guild_mark_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_mark packet
    def make_guild_mark_packet(self, packet):
        return None
    # send guild_mark
    def send_guild_mark(self):
        self.dispatch(OP_CODE.CS_GUILD_MARK)(OP_CODE.CS_GUILD_MARK)
    
    # handle SC_GUILD_MARK
    @CallbackBase.callback(OP_CODE.SC_GUILD_MARK)
    def handle_guild_mark_decorate(self, recv_buff):
        packet = sc_guild_mark()
        packet.deserialize(recv_buff)
        return self.handle_guild_mark(packet)    
    def handle_guild_mark(self, packet):
        return None

    
    # CS_GUILD_DEL_MARK
    @CallbackBase.callback(OP_CODE.CS_GUILD_DEL_MARK)
    def send_guild_del_mark_decorate(self, code):
        packet = cs_guild_del_mark()
        self.make_guild_del_mark_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_del_mark packet
    def make_guild_del_mark_packet(self, packet):
        return None
    # send guild_del_mark
    def send_guild_del_mark(self):
        self.dispatch(OP_CODE.CS_GUILD_DEL_MARK)(OP_CODE.CS_GUILD_DEL_MARK)
    
    # handle SC_GUILD_DEL_MARK
    @CallbackBase.callback(OP_CODE.SC_GUILD_DEL_MARK)
    def handle_guild_del_mark_decorate(self, recv_buff):
        packet = sc_guild_del_mark()
        packet.deserialize(recv_buff)
        return self.handle_guild_del_mark(packet)    
    def handle_guild_del_mark(self, packet):
        return None

    
    # CS_GET_LOTTERY_DATA_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_LOTTERY_DATA_LIST)
    def send_get_lottery_data_list_decorate(self, code):
        packet = cs_get_lottery_data_list()
        self.make_get_lottery_data_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_lottery_data_list packet
    def make_get_lottery_data_list_packet(self, packet):
        return None
    # send get_lottery_data_list
    def send_get_lottery_data_list(self):
        self.dispatch(OP_CODE.CS_GET_LOTTERY_DATA_LIST)(OP_CODE.CS_GET_LOTTERY_DATA_LIST)
    
    # handle SC_GET_LOTTERY_DATA_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_LOTTERY_DATA_LIST)
    def handle_get_lottery_data_list_decorate(self, recv_buff):
        packet = sc_get_lottery_data_list()
        packet.deserialize(recv_buff)
        return self.handle_get_lottery_data_list(packet)    
    def handle_get_lottery_data_list(self, packet):
        return None

    
    # CS_LOTTERY_DRAW
    @CallbackBase.callback(OP_CODE.CS_LOTTERY_DRAW)
    def send_lottery_draw_decorate(self, code):
        packet = cs_lottery_draw()
        self.make_lottery_draw_packet(packet)
        self.mes_que[code] = packet
    # makeup lottery_draw packet
    def make_lottery_draw_packet(self, packet):
        return None
    # send lottery_draw
    def send_lottery_draw(self):
        self.dispatch(OP_CODE.CS_LOTTERY_DRAW)(OP_CODE.CS_LOTTERY_DRAW)
    
    # handle SC_LOTTERY_DRAW
    @CallbackBase.callback(OP_CODE.SC_LOTTERY_DRAW)
    def handle_lottery_draw_decorate(self, recv_buff):
        packet = sc_lottery_draw()
        packet.deserialize(recv_buff)
        return self.handle_lottery_draw(packet)    
    def handle_lottery_draw(self, packet):
        return None

    
    # CS_LOTTERY_RESET
    @CallbackBase.callback(OP_CODE.CS_LOTTERY_RESET)
    def send_lottery_reset_decorate(self, code):
        packet = cs_lottery_reset()
        self.make_lottery_reset_packet(packet)
        self.mes_que[code] = packet
    # makeup lottery_reset packet
    def make_lottery_reset_packet(self, packet):
        return None
    # send lottery_reset
    def send_lottery_reset(self):
        self.dispatch(OP_CODE.CS_LOTTERY_RESET)(OP_CODE.CS_LOTTERY_RESET)
    
    # handle SC_LOTTERY_RESET
    @CallbackBase.callback(OP_CODE.SC_LOTTERY_RESET)
    def handle_lottery_reset_decorate(self, recv_buff):
        packet = sc_lottery_reset()
        packet.deserialize(recv_buff)
        return self.handle_lottery_reset(packet)    
    def handle_lottery_reset(self, packet):
        return None

    
    # CS_GET_SHOP_BUY_COUNT
    @CallbackBase.callback(OP_CODE.CS_GET_SHOP_BUY_COUNT)
    def send_get_shop_buy_count_decorate(self, code):
        packet = cs_get_shop_buy_count()
        self.make_get_shop_buy_count_packet(packet)
        self.mes_que[code] = packet
    # makeup get_shop_buy_count packet
    def make_get_shop_buy_count_packet(self, packet):
        return None
    # send get_shop_buy_count
    def send_get_shop_buy_count(self):
        self.dispatch(OP_CODE.CS_GET_SHOP_BUY_COUNT)(OP_CODE.CS_GET_SHOP_BUY_COUNT)
    
    # handle SC_GET_SHOP_BUY_COUNT
    @CallbackBase.callback(OP_CODE.SC_GET_SHOP_BUY_COUNT)
    def handle_get_shop_buy_count_decorate(self, recv_buff):
        packet = sc_get_shop_buy_count()
        packet.deserialize(recv_buff)
        return self.handle_get_shop_buy_count(packet)    
    def handle_get_shop_buy_count(self, packet):
        return None

    
    # CS_BLOCK_REAP_REQ
    @CallbackBase.callback(OP_CODE.CS_BLOCK_REAP_REQ)
    def send_block_reap_req_decorate(self, code):
        packet = cs_block_reap_req()
        self.make_block_reap_req_packet(packet)
        self.mes_que[code] = packet
    # makeup block_reap_req packet
    def make_block_reap_req_packet(self, packet):
        return None
    # send block_reap_req
    def send_block_reap_req(self):
        self.dispatch(OP_CODE.CS_BLOCK_REAP_REQ)(OP_CODE.CS_BLOCK_REAP_REQ)
    
    # handle SC_BLOCK_REAP_REQ
    @CallbackBase.callback(OP_CODE.SC_BLOCK_REAP_REQ)
    def handle_block_reap_req_decorate(self, recv_buff):
        packet = sc_block_reap_req()
        packet.deserialize(recv_buff)
        return self.handle_block_reap_req(packet)    
    def handle_block_reap_req(self, packet):
        return None

    
    # CS_BLOCK_REAP
    @CallbackBase.callback(OP_CODE.CS_BLOCK_REAP)
    def send_block_reap_decorate(self, code):
        packet = cs_block_reap()
        self.make_block_reap_packet(packet)
        self.mes_que[code] = packet
    # makeup block_reap packet
    def make_block_reap_packet(self, packet):
        return None
    # send block_reap
    def send_block_reap(self):
        self.dispatch(OP_CODE.CS_BLOCK_REAP)(OP_CODE.CS_BLOCK_REAP)
    
    # handle SC_BLOCK_REAP
    @CallbackBase.callback(OP_CODE.SC_BLOCK_REAP)
    def handle_block_reap_decorate(self, recv_buff):
        packet = sc_block_reap()
        packet.deserialize(recv_buff)
        return self.handle_block_reap(packet)    
    def handle_block_reap(self, packet):
        return None

    
    # CS_GET_EFFECT_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_EFFECT_LIST)
    def send_get_effect_list_decorate(self, code):
        packet = cs_get_effect_list()
        self.make_get_effect_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_effect_list packet
    def make_get_effect_list_packet(self, packet):
        return None
    # send get_effect_list
    def send_get_effect_list(self):
        self.dispatch(OP_CODE.CS_GET_EFFECT_LIST)(OP_CODE.CS_GET_EFFECT_LIST)
    
    # handle SC_GET_EFFECT_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_EFFECT_LIST)
    def handle_get_effect_list_decorate(self, recv_buff):
        packet = sc_get_effect_list()
        packet.deserialize(recv_buff)
        return self.handle_get_effect_list(packet)    
    def handle_get_effect_list(self, packet):
        return None

    
    # CS_GET_CHAT_INFO
    @CallbackBase.callback(OP_CODE.CS_GET_CHAT_INFO)
    def send_get_chat_info_decorate(self, code):
        packet = cs_get_chat_info()
        self.make_get_chat_info_packet(packet)
        self.mes_que[code] = packet
    # makeup get_chat_info packet
    def make_get_chat_info_packet(self, packet):
        return None
    # send get_chat_info
    def send_get_chat_info(self):
        self.dispatch(OP_CODE.CS_GET_CHAT_INFO)(OP_CODE.CS_GET_CHAT_INFO)
    
    # handle SC_GET_CHAT_INFO
    @CallbackBase.callback(OP_CODE.SC_GET_CHAT_INFO)
    def handle_get_chat_info_decorate(self, recv_buff):
        packet = sc_get_chat_info()
        packet.deserialize(recv_buff)
        return self.handle_get_chat_info(packet)    
    def handle_get_chat_info(self, packet):
        return None

    
    # CS_GET_CHAT_CHANNEL_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_CHAT_CHANNEL_LIST)
    def send_get_chat_channel_list_decorate(self, code):
        packet = cs_get_chat_channel_list()
        self.make_get_chat_channel_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_chat_channel_list packet
    def make_get_chat_channel_list_packet(self, packet):
        return None
    # send get_chat_channel_list
    def send_get_chat_channel_list(self):
        self.dispatch(OP_CODE.CS_GET_CHAT_CHANNEL_LIST)(OP_CODE.CS_GET_CHAT_CHANNEL_LIST)
    
    # handle SC_GET_CHAT_CHANNEL_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_CHAT_CHANNEL_LIST)
    def handle_get_chat_channel_list_decorate(self, recv_buff):
        packet = sc_get_chat_channel_list()
        packet.deserialize(recv_buff)
        return self.handle_get_chat_channel_list(packet)    
    def handle_get_chat_channel_list(self, packet):
        return None

    
    # CS_GUILD_GROUP_REQ
    @CallbackBase.callback(OP_CODE.CS_GUILD_GROUP_REQ)
    def send_guild_group_req_decorate(self, code):
        packet = cs_guild_group_req()
        self.make_guild_group_req_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_group_req packet
    def make_guild_group_req_packet(self, packet):
        return None
    # send guild_group_req
    def send_guild_group_req(self):
        self.dispatch(OP_CODE.CS_GUILD_GROUP_REQ)(OP_CODE.CS_GUILD_GROUP_REQ)
    
    # handle SC_GUILD_GROUP_REQ
    @CallbackBase.callback(OP_CODE.SC_GUILD_GROUP_REQ)
    def handle_guild_group_req_decorate(self, recv_buff):
        packet = sc_guild_group_req()
        packet.deserialize(recv_buff)
        return self.handle_guild_group_req(packet)    
    def handle_guild_group_req(self, packet):
        return None

    
    # CS_GUILD_GROUP_INFO
    @CallbackBase.callback(OP_CODE.CS_GUILD_GROUP_INFO)
    def send_guild_group_info_decorate(self, code):
        packet = cs_guild_group_info()
        self.make_guild_group_info_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_group_info packet
    def make_guild_group_info_packet(self, packet):
        return None
    # send guild_group_info
    def send_guild_group_info(self):
        self.dispatch(OP_CODE.CS_GUILD_GROUP_INFO)(OP_CODE.CS_GUILD_GROUP_INFO)
    
    # handle SC_GUILD_GROUP_INFO
    @CallbackBase.callback(OP_CODE.SC_GUILD_GROUP_INFO)
    def handle_guild_group_info_decorate(self, recv_buff):
        packet = sc_guild_group_info()
        packet.deserialize(recv_buff)
        return self.handle_guild_group_info(packet)    
    def handle_guild_group_info(self, packet):
        return None

    
    # CS_GUILD_GROUP_MOD
    @CallbackBase.callback(OP_CODE.CS_GUILD_GROUP_MOD)
    def send_guild_group_mod_decorate(self, code):
        packet = cs_guild_group_mod()
        self.make_guild_group_mod_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_group_mod packet
    def make_guild_group_mod_packet(self, packet):
        return None
    # send guild_group_mod
    def send_guild_group_mod(self):
        self.dispatch(OP_CODE.CS_GUILD_GROUP_MOD)(OP_CODE.CS_GUILD_GROUP_MOD)
    
    # handle SC_GUILD_GROUP_MOD
    @CallbackBase.callback(OP_CODE.SC_GUILD_GROUP_MOD)
    def handle_guild_group_mod_decorate(self, recv_buff):
        packet = sc_guild_group_mod()
        packet.deserialize(recv_buff)
        return self.handle_guild_group_mod(packet)    
    def handle_guild_group_mod(self, packet):
        return None

    
    # CS_GUILD_GROUP_CREATE
    @CallbackBase.callback(OP_CODE.CS_GUILD_GROUP_CREATE)
    def send_guild_group_create_decorate(self, code):
        packet = cs_guild_group_create()
        self.make_guild_group_create_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_group_create packet
    def make_guild_group_create_packet(self, packet):
        return None
    # send guild_group_create
    def send_guild_group_create(self):
        self.dispatch(OP_CODE.CS_GUILD_GROUP_CREATE)(OP_CODE.CS_GUILD_GROUP_CREATE)
    
    # handle SC_GUILD_GROUP_CREATE
    @CallbackBase.callback(OP_CODE.SC_GUILD_GROUP_CREATE)
    def handle_guild_group_create_decorate(self, recv_buff):
        packet = sc_guild_group_create()
        packet.deserialize(recv_buff)
        return self.handle_guild_group_create(packet)    
    def handle_guild_group_create(self, packet):
        return None

    
    # CS_GUILD_GROUP_DEL
    @CallbackBase.callback(OP_CODE.CS_GUILD_GROUP_DEL)
    def send_guild_group_del_decorate(self, code):
        packet = cs_guild_group_del()
        self.make_guild_group_del_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_group_del packet
    def make_guild_group_del_packet(self, packet):
        return None
    # send guild_group_del
    def send_guild_group_del(self):
        self.dispatch(OP_CODE.CS_GUILD_GROUP_DEL)(OP_CODE.CS_GUILD_GROUP_DEL)
    
    # handle SC_GUILD_GROUP_DEL
    @CallbackBase.callback(OP_CODE.SC_GUILD_GROUP_DEL)
    def handle_guild_group_del_decorate(self, recv_buff):
        packet = sc_guild_group_del()
        packet.deserialize(recv_buff)
        return self.handle_guild_group_del(packet)    
    def handle_guild_group_del(self, packet):
        return None

    
    # CS_GUILD_GROUP_ADD
    @CallbackBase.callback(OP_CODE.CS_GUILD_GROUP_ADD)
    def send_guild_group_add_decorate(self, code):
        packet = cs_guild_group_add()
        self.make_guild_group_add_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_group_add packet
    def make_guild_group_add_packet(self, packet):
        return None
    # send guild_group_add
    def send_guild_group_add(self):
        self.dispatch(OP_CODE.CS_GUILD_GROUP_ADD)(OP_CODE.CS_GUILD_GROUP_ADD)
    
    # handle SC_GUILD_GROUP_ADD
    @CallbackBase.callback(OP_CODE.SC_GUILD_GROUP_ADD)
    def handle_guild_group_add_decorate(self, recv_buff):
        packet = sc_guild_group_add()
        packet.deserialize(recv_buff)
        return self.handle_guild_group_add(packet)    
    def handle_guild_group_add(self, packet):
        return None

    
    # CS_GUILD_GROUP_REMOVE
    @CallbackBase.callback(OP_CODE.CS_GUILD_GROUP_REMOVE)
    def send_guild_group_remove_decorate(self, code):
        packet = cs_guild_group_remove()
        self.make_guild_group_remove_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_group_remove packet
    def make_guild_group_remove_packet(self, packet):
        return None
    # send guild_group_remove
    def send_guild_group_remove(self):
        self.dispatch(OP_CODE.CS_GUILD_GROUP_REMOVE)(OP_CODE.CS_GUILD_GROUP_REMOVE)
    
    # handle SC_GUILD_GROUP_REMOVE
    @CallbackBase.callback(OP_CODE.SC_GUILD_GROUP_REMOVE)
    def handle_guild_group_remove_decorate(self, recv_buff):
        packet = sc_guild_group_remove()
        packet.deserialize(recv_buff)
        return self.handle_guild_group_remove(packet)    
    def handle_guild_group_remove(self, packet):
        return None

    
    # CS_GUILD_GROUP_LEADER
    @CallbackBase.callback(OP_CODE.CS_GUILD_GROUP_LEADER)
    def send_guild_group_leader_decorate(self, code):
        packet = cs_guild_group_leader()
        self.make_guild_group_leader_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_group_leader packet
    def make_guild_group_leader_packet(self, packet):
        return None
    # send guild_group_leader
    def send_guild_group_leader(self):
        self.dispatch(OP_CODE.CS_GUILD_GROUP_LEADER)(OP_CODE.CS_GUILD_GROUP_LEADER)
    
    # handle SC_GUILD_GROUP_LEADER
    @CallbackBase.callback(OP_CODE.SC_GUILD_GROUP_LEADER)
    def handle_guild_group_leader_decorate(self, recv_buff):
        packet = sc_guild_group_leader()
        packet.deserialize(recv_buff)
        return self.handle_guild_group_leader(packet)    
    def handle_guild_group_leader(self, packet):
        return None

    
    # CS_GET_SIGN_CONFIG
    @CallbackBase.callback(OP_CODE.CS_GET_SIGN_CONFIG)
    def send_get_sign_config_decorate(self, code):
        packet = cs_get_sign_config()
        self.make_get_sign_config_packet(packet)
        self.mes_que[code] = packet
    # makeup get_sign_config packet
    def make_get_sign_config_packet(self, packet):
        return None
    # send get_sign_config
    def send_get_sign_config(self):
        self.dispatch(OP_CODE.CS_GET_SIGN_CONFIG)(OP_CODE.CS_GET_SIGN_CONFIG)
    
    # handle SC_GET_SIGN_CONFIG
    @CallbackBase.callback(OP_CODE.SC_GET_SIGN_CONFIG)
    def handle_get_sign_config_decorate(self, recv_buff):
        packet = sc_get_sign_config()
        packet.deserialize(recv_buff)
        return self.handle_get_sign_config(packet)    
    def handle_get_sign_config(self, packet):
        return None

    
    # CS_SIGN
    @CallbackBase.callback(OP_CODE.CS_SIGN)
    def send_sign_decorate(self, code):
        packet = cs_sign()
        self.make_sign_packet(packet)
        self.mes_que[code] = packet
    # makeup sign packet
    def make_sign_packet(self, packet):
        return None
    # send sign
    def send_sign(self):
        self.dispatch(OP_CODE.CS_SIGN)(OP_CODE.CS_SIGN)
    
    # handle SC_SIGN
    @CallbackBase.callback(OP_CODE.SC_SIGN)
    def handle_sign_decorate(self, recv_buff):
        packet = sc_sign()
        packet.deserialize(recv_buff)
        return self.handle_sign(packet)    
    def handle_sign(self, packet):
        return None

    
    # CS_GET_ACTIVE_OPEN
    @CallbackBase.callback(OP_CODE.CS_GET_ACTIVE_OPEN)
    def send_get_active_open_decorate(self, code):
        packet = cs_get_active_open()
        self.make_get_active_open_packet(packet)
        self.mes_que[code] = packet
    # makeup get_active_open packet
    def make_get_active_open_packet(self, packet):
        return None
    # send get_active_open
    def send_get_active_open(self):
        self.dispatch(OP_CODE.CS_GET_ACTIVE_OPEN)(OP_CODE.CS_GET_ACTIVE_OPEN)
    
    # handle SC_GET_ACTIVE_OPEN
    @CallbackBase.callback(OP_CODE.SC_GET_ACTIVE_OPEN)
    def handle_get_active_open_decorate(self, recv_buff):
        packet = sc_get_active_open()
        packet.deserialize(recv_buff)
        return self.handle_get_active_open(packet)    
    def handle_get_active_open(self, packet):
        return None

    
    # CS_GET_ACTIVITY_DETAIL
    @CallbackBase.callback(OP_CODE.CS_GET_ACTIVITY_DETAIL)
    def send_get_activity_detail_decorate(self, code):
        packet = cs_get_activity_detail()
        self.make_get_activity_detail_packet(packet)
        self.mes_que[code] = packet
    # makeup get_activity_detail packet
    def make_get_activity_detail_packet(self, packet):
        return None
    # send get_activity_detail
    def send_get_activity_detail(self):
        self.dispatch(OP_CODE.CS_GET_ACTIVITY_DETAIL)(OP_CODE.CS_GET_ACTIVITY_DETAIL)
    
    # handle SC_GET_ACTIVITY_DETAIL
    @CallbackBase.callback(OP_CODE.SC_GET_ACTIVITY_DETAIL)
    def handle_get_activity_detail_decorate(self, recv_buff):
        packet = sc_get_activity_detail()
        packet.deserialize(recv_buff)
        return self.handle_get_activity_detail(packet)    
    def handle_get_activity_detail(self, packet):
        return None

    
    # CS_GET_ACTIVITY_REWARD
    @CallbackBase.callback(OP_CODE.CS_GET_ACTIVITY_REWARD)
    def send_get_activity_reward_decorate(self, code):
        packet = cs_get_activity_reward()
        self.make_get_activity_reward_packet(packet)
        self.mes_que[code] = packet
    # makeup get_activity_reward packet
    def make_get_activity_reward_packet(self, packet):
        return None
    # send get_activity_reward
    def send_get_activity_reward(self):
        self.dispatch(OP_CODE.CS_GET_ACTIVITY_REWARD)(OP_CODE.CS_GET_ACTIVITY_REWARD)
    
    # handle SC_GET_ACTIVITY_REWARD
    @CallbackBase.callback(OP_CODE.SC_GET_ACTIVITY_REWARD)
    def handle_get_activity_reward_decorate(self, recv_buff):
        packet = sc_get_activity_reward()
        packet.deserialize(recv_buff)
        return self.handle_get_activity_reward(packet)    
    def handle_get_activity_reward(self, packet):
        return None

    
    # handle SCHAT_LOGIN
    @CallbackBase.callback(OP_CODE.SCHAT_LOGIN)
    def handle_at_login_decorate(self, recv_buff):
        packet = schat_login()
        packet.deserialize(recv_buff)
        return self.handle_at_login(packet)    
    def handle_at_login(self, packet):
        return None

    
    # CS_GET_USER_FORCE_RANK
    @CallbackBase.callback(OP_CODE.CS_GET_USER_FORCE_RANK)
    def send_get_user_force_rank_decorate(self, code):
        packet = cs_get_user_force_rank()
        self.make_get_user_force_rank_packet(packet)
        self.mes_que[code] = packet
    # makeup get_user_force_rank packet
    def make_get_user_force_rank_packet(self, packet):
        return None
    # send get_user_force_rank
    def send_get_user_force_rank(self):
        self.dispatch(OP_CODE.CS_GET_USER_FORCE_RANK)(OP_CODE.CS_GET_USER_FORCE_RANK)
    
    # handle SC_GET_USER_FORCE_RANK
    @CallbackBase.callback(OP_CODE.SC_GET_USER_FORCE_RANK)
    def handle_get_user_force_rank_decorate(self, recv_buff):
        packet = sc_get_user_force_rank()
        packet.deserialize(recv_buff)
        return self.handle_get_user_force_rank(packet)    
    def handle_get_user_force_rank(self, packet):
        return None

    
    # CS_GET_GUILD_FORCE_RANK
    @CallbackBase.callback(OP_CODE.CS_GET_GUILD_FORCE_RANK)
    def send_get_guild_force_rank_decorate(self, code):
        packet = cs_get_guild_force_rank()
        self.make_get_guild_force_rank_packet(packet)
        self.mes_que[code] = packet
    # makeup get_guild_force_rank packet
    def make_get_guild_force_rank_packet(self, packet):
        return None
    # send get_guild_force_rank
    def send_get_guild_force_rank(self):
        self.dispatch(OP_CODE.CS_GET_GUILD_FORCE_RANK)(OP_CODE.CS_GET_GUILD_FORCE_RANK)
    
    # handle SC_GET_GUILD_FORCE_RANK
    @CallbackBase.callback(OP_CODE.SC_GET_GUILD_FORCE_RANK)
    def handle_get_guild_force_rank_decorate(self, recv_buff):
        packet = sc_get_guild_force_rank()
        packet.deserialize(recv_buff)
        return self.handle_get_guild_force_rank(packet)    
    def handle_get_guild_force_rank(self, packet):
        return None

    
    # CS_GET_USER_WAR_RANK
    @CallbackBase.callback(OP_CODE.CS_GET_USER_WAR_RANK)
    def send_get_user_war_rank_decorate(self, code):
        packet = cs_get_user_war_rank()
        self.make_get_user_war_rank_packet(packet)
        self.mes_que[code] = packet
    # makeup get_user_war_rank packet
    def make_get_user_war_rank_packet(self, packet):
        return None
    # send get_user_war_rank
    def send_get_user_war_rank(self):
        self.dispatch(OP_CODE.CS_GET_USER_WAR_RANK)(OP_CODE.CS_GET_USER_WAR_RANK)
    
    # handle SC_GET_USER_WAR_RANK
    @CallbackBase.callback(OP_CODE.SC_GET_USER_WAR_RANK)
    def handle_get_user_war_rank_decorate(self, recv_buff):
        packet = sc_get_user_war_rank()
        packet.deserialize(recv_buff)
        return self.handle_get_user_war_rank(packet)    
    def handle_get_user_war_rank(self, packet):
        return None

    
    # CS_GET_INVEST_INFO
    @CallbackBase.callback(OP_CODE.CS_GET_INVEST_INFO)
    def send_get_invest_info_decorate(self, code):
        packet = cs_get_invest_info()
        self.make_get_invest_info_packet(packet)
        self.mes_que[code] = packet
    # makeup get_invest_info packet
    def make_get_invest_info_packet(self, packet):
        return None
    # send get_invest_info
    def send_get_invest_info(self):
        self.dispatch(OP_CODE.CS_GET_INVEST_INFO)(OP_CODE.CS_GET_INVEST_INFO)
    
    # handle SC_GET_INVEST_INFO
    @CallbackBase.callback(OP_CODE.SC_GET_INVEST_INFO)
    def handle_get_invest_info_decorate(self, recv_buff):
        packet = sc_get_invest_info()
        packet.deserialize(recv_buff)
        return self.handle_get_invest_info(packet)    
    def handle_get_invest_info(self, packet):
        return None

    
    # CS_DRAW_INVEST_REFUND
    @CallbackBase.callback(OP_CODE.CS_DRAW_INVEST_REFUND)
    def send_draw_invest_refund_decorate(self, code):
        packet = cs_draw_invest_refund()
        self.make_draw_invest_refund_packet(packet)
        self.mes_que[code] = packet
    # makeup draw_invest_refund packet
    def make_draw_invest_refund_packet(self, packet):
        return None
    # send draw_invest_refund
    def send_draw_invest_refund(self):
        self.dispatch(OP_CODE.CS_DRAW_INVEST_REFUND)(OP_CODE.CS_DRAW_INVEST_REFUND)
    
    # handle SC_DRAW_INVEST_REFUND
    @CallbackBase.callback(OP_CODE.SC_DRAW_INVEST_REFUND)
    def handle_draw_invest_refund_decorate(self, recv_buff):
        packet = sc_draw_invest_refund()
        packet.deserialize(recv_buff)
        return self.handle_draw_invest_refund(packet)    
    def handle_draw_invest_refund(self, packet):
        return None

    
    # CS_INVEST
    @CallbackBase.callback(OP_CODE.CS_INVEST)
    def send_invest_decorate(self, code):
        packet = cs_invest()
        self.make_invest_packet(packet)
        self.mes_que[code] = packet
    # makeup invest packet
    def make_invest_packet(self, packet):
        return None
    # send invest
    def send_invest(self):
        self.dispatch(OP_CODE.CS_INVEST)(OP_CODE.CS_INVEST)
    
    # handle SC_INVEST
    @CallbackBase.callback(OP_CODE.SC_INVEST)
    def handle_invest_decorate(self, recv_buff):
        packet = sc_invest()
        packet.deserialize(recv_buff)
        return self.handle_invest(packet)    
    def handle_invest(self, packet):
        return None

    
    # CS_GET_LIVENESS_INFO
    @CallbackBase.callback(OP_CODE.CS_GET_LIVENESS_INFO)
    def send_get_liveness_info_decorate(self, code):
        packet = cs_get_liveness_info()
        self.make_get_liveness_info_packet(packet)
        self.mes_que[code] = packet
    # makeup get_liveness_info packet
    def make_get_liveness_info_packet(self, packet):
        return None
    # send get_liveness_info
    def send_get_liveness_info(self):
        self.dispatch(OP_CODE.CS_GET_LIVENESS_INFO)(OP_CODE.CS_GET_LIVENESS_INFO)
    
    # handle SC_GET_LIVENESS_INFO
    @CallbackBase.callback(OP_CODE.SC_GET_LIVENESS_INFO)
    def handle_get_liveness_info_decorate(self, recv_buff):
        packet = sc_get_liveness_info()
        packet.deserialize(recv_buff)
        return self.handle_get_liveness_info(packet)    
    def handle_get_liveness_info(self, packet):
        return None

    
    # CS_DRAW_LIVENESS_REWARD
    @CallbackBase.callback(OP_CODE.CS_DRAW_LIVENESS_REWARD)
    def send_draw_liveness_reward_decorate(self, code):
        packet = cs_draw_liveness_reward()
        self.make_draw_liveness_reward_packet(packet)
        self.mes_que[code] = packet
    # makeup draw_liveness_reward packet
    def make_draw_liveness_reward_packet(self, packet):
        return None
    # send draw_liveness_reward
    def send_draw_liveness_reward(self):
        self.dispatch(OP_CODE.CS_DRAW_LIVENESS_REWARD)(OP_CODE.CS_DRAW_LIVENESS_REWARD)
    
    # handle SC_DRAW_LIVENESS_REWARD
    @CallbackBase.callback(OP_CODE.SC_DRAW_LIVENESS_REWARD)
    def handle_draw_liveness_reward_decorate(self, recv_buff):
        packet = sc_draw_liveness_reward()
        packet.deserialize(recv_buff)
        return self.handle_draw_liveness_reward(packet)    
    def handle_draw_liveness_reward(self, packet):
        return None

    
    # handle SCHAT_FORWARD
    @CallbackBase.callback(OP_CODE.SCHAT_FORWARD)
    def handle_at_forward_decorate(self, recv_buff):
        packet = schat_forward()
        packet.deserialize(recv_buff)
        return self.handle_at_forward(packet)    
    def handle_at_forward(self, packet):
        return None

    
    # CS_GET_MAIL_HEAD_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_MAIL_HEAD_LIST)
    def send_get_mail_head_list_decorate(self, code):
        packet = cs_get_mail_head_list()
        self.make_get_mail_head_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_mail_head_list packet
    def make_get_mail_head_list_packet(self, packet):
        return None
    # send get_mail_head_list
    def send_get_mail_head_list(self):
        self.dispatch(OP_CODE.CS_GET_MAIL_HEAD_LIST)(OP_CODE.CS_GET_MAIL_HEAD_LIST)
    
    # handle SC_GET_MAIL_HEAD_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_MAIL_HEAD_LIST)
    def handle_get_mail_head_list_decorate(self, recv_buff):
        packet = sc_get_mail_head_list()
        packet.deserialize(recv_buff)
        return self.handle_get_mail_head_list(packet)    
    def handle_get_mail_head_list(self, packet):
        return None

    
    # CS_GET_MAIL_BODY_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_MAIL_BODY_LIST)
    def send_get_mail_body_list_decorate(self, code):
        packet = cs_get_mail_body_list()
        self.make_get_mail_body_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_mail_body_list packet
    def make_get_mail_body_list_packet(self, packet):
        return None
    # send get_mail_body_list
    def send_get_mail_body_list(self):
        self.dispatch(OP_CODE.CS_GET_MAIL_BODY_LIST)(OP_CODE.CS_GET_MAIL_BODY_LIST)
    
    # handle SC_GET_MAIL_BODY_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_MAIL_BODY_LIST)
    def handle_get_mail_body_list_decorate(self, recv_buff):
        packet = sc_get_mail_body_list()
        packet.deserialize(recv_buff)
        return self.handle_get_mail_body_list(packet)    
    def handle_get_mail_body_list(self, packet):
        return None

    
    # CS_MAIL_SEND
    @CallbackBase.callback(OP_CODE.CS_MAIL_SEND)
    def send_mail_send_decorate(self, code):
        packet = cs_mail_send()
        self.make_mail_send_packet(packet)
        self.mes_que[code] = packet
    # makeup mail_send packet
    def make_mail_send_packet(self, packet):
        return None
    # send mail_send
    def send_mail_send(self):
        self.dispatch(OP_CODE.CS_MAIL_SEND)(OP_CODE.CS_MAIL_SEND)
    
    # handle SC_MAIL_SEND
    @CallbackBase.callback(OP_CODE.SC_MAIL_SEND)
    def handle_mail_send_decorate(self, recv_buff):
        packet = sc_mail_send()
        packet.deserialize(recv_buff)
        return self.handle_mail_send(packet)    
    def handle_mail_send(self, packet):
        return None

    
    # CS_MAIL_AFFIX_PICK
    @CallbackBase.callback(OP_CODE.CS_MAIL_AFFIX_PICK)
    def send_mail_affix_pick_decorate(self, code):
        packet = cs_mail_affix_pick()
        self.make_mail_affix_pick_packet(packet)
        self.mes_que[code] = packet
    # makeup mail_affix_pick packet
    def make_mail_affix_pick_packet(self, packet):
        return None
    # send mail_affix_pick
    def send_mail_affix_pick(self):
        self.dispatch(OP_CODE.CS_MAIL_AFFIX_PICK)(OP_CODE.CS_MAIL_AFFIX_PICK)
    
    # handle SC_MAIL_AFFIX_PICK
    @CallbackBase.callback(OP_CODE.SC_MAIL_AFFIX_PICK)
    def handle_mail_affix_pick_decorate(self, recv_buff):
        packet = sc_mail_affix_pick()
        packet.deserialize(recv_buff)
        return self.handle_mail_affix_pick(packet)    
    def handle_mail_affix_pick(self, packet):
        return None

    
    # handle SCHAT_ADD_CHANNEL
    @CallbackBase.callback(OP_CODE.SCHAT_ADD_CHANNEL)
    def handle_at_add_channel_decorate(self, recv_buff):
        packet = schat_add_channel()
        packet.deserialize(recv_buff)
        return self.handle_at_add_channel(packet)    
    def handle_at_add_channel(self, packet):
        return None

    
    # handle SCHAT_DEL_CHANNEL
    @CallbackBase.callback(OP_CODE.SCHAT_DEL_CHANNEL)
    def handle_at_del_channel_decorate(self, recv_buff):
        packet = schat_del_channel()
        packet.deserialize(recv_buff)
        return self.handle_at_del_channel(packet)    
    def handle_at_del_channel(self, packet):
        return None

    
    # handle SCHAT_JOIN_CHANNEL
    @CallbackBase.callback(OP_CODE.SCHAT_JOIN_CHANNEL)
    def handle_at_join_channel_decorate(self, recv_buff):
        packet = schat_join_channel()
        packet.deserialize(recv_buff)
        return self.handle_at_join_channel(packet)    
    def handle_at_join_channel(self, packet):
        return None

    
    # handle SCHAT_QUIT_CHANNEL
    @CallbackBase.callback(OP_CODE.SCHAT_QUIT_CHANNEL)
    def handle_at_quit_channel_decorate(self, recv_buff):
        packet = schat_quit_channel()
        packet.deserialize(recv_buff)
        return self.handle_at_quit_channel(packet)    
    def handle_at_quit_channel(self, packet):
        return None

    
    # CS_REQ_USER_DETAIL
    @CallbackBase.callback(OP_CODE.CS_REQ_USER_DETAIL)
    def send_req_user_detail_decorate(self, code):
        packet = cs_req_user_detail()
        self.make_req_user_detail_packet(packet)
        self.mes_que[code] = packet
    # makeup req_user_detail packet
    def make_req_user_detail_packet(self, packet):
        return None
    # send req_user_detail
    def send_req_user_detail(self):
        self.dispatch(OP_CODE.CS_REQ_USER_DETAIL)(OP_CODE.CS_REQ_USER_DETAIL)
    
    # handle SC_REQ_USER_DETAIL
    @CallbackBase.callback(OP_CODE.SC_REQ_USER_DETAIL)
    def handle_req_user_detail_decorate(self, recv_buff):
        packet = sc_req_user_detail()
        packet.deserialize(recv_buff)
        return self.handle_req_user_detail(packet)    
    def handle_req_user_detail(self, packet):
        return None

    
    # CS_REQ_GUILD_USER_DETAIL
    @CallbackBase.callback(OP_CODE.CS_REQ_GUILD_USER_DETAIL)
    def send_req_guild_user_detail_decorate(self, code):
        packet = cs_req_guild_user_detail()
        self.make_req_guild_user_detail_packet(packet)
        self.mes_que[code] = packet
    # makeup req_guild_user_detail packet
    def make_req_guild_user_detail_packet(self, packet):
        return None
    # send req_guild_user_detail
    def send_req_guild_user_detail(self):
        self.dispatch(OP_CODE.CS_REQ_GUILD_USER_DETAIL)(OP_CODE.CS_REQ_GUILD_USER_DETAIL)
    
    # handle SC_REQ_GUILD_USER_DETAIL
    @CallbackBase.callback(OP_CODE.SC_REQ_GUILD_USER_DETAIL)
    def handle_req_guild_user_detail_decorate(self, recv_buff):
        packet = sc_req_guild_user_detail()
        packet.deserialize(recv_buff)
        return self.handle_req_guild_user_detail(packet)    
    def handle_req_guild_user_detail(self, packet):
        return None

    
    # CS_GUILD_CREATE_CHANNEL
    @CallbackBase.callback(OP_CODE.CS_GUILD_CREATE_CHANNEL)
    def send_guild_create_channel_decorate(self, code):
        packet = cs_guild_create_channel()
        self.make_guild_create_channel_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_create_channel packet
    def make_guild_create_channel_packet(self, packet):
        return None
    # send guild_create_channel
    def send_guild_create_channel(self):
        self.dispatch(OP_CODE.CS_GUILD_CREATE_CHANNEL)(OP_CODE.CS_GUILD_CREATE_CHANNEL)
    
    # handle SC_GUILD_CREATE_CHANNEL
    @CallbackBase.callback(OP_CODE.SC_GUILD_CREATE_CHANNEL)
    def handle_guild_create_channel_decorate(self, recv_buff):
        packet = sc_guild_create_channel()
        packet.deserialize(recv_buff)
        return self.handle_guild_create_channel(packet)    
    def handle_guild_create_channel(self, packet):
        return None

    
    # CS_GUILD_DISOLUTION_CHANNEL
    @CallbackBase.callback(OP_CODE.CS_GUILD_DISOLUTION_CHANNEL)
    def send_guild_disolution_channel_decorate(self, code):
        packet = cs_guild_disolution_channel()
        self.make_guild_disolution_channel_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_disolution_channel packet
    def make_guild_disolution_channel_packet(self, packet):
        return None
    # send guild_disolution_channel
    def send_guild_disolution_channel(self):
        self.dispatch(OP_CODE.CS_GUILD_DISOLUTION_CHANNEL)(OP_CODE.CS_GUILD_DISOLUTION_CHANNEL)
    
    # handle SC_GUILD_DISOLUTION_CHANNEL
    @CallbackBase.callback(OP_CODE.SC_GUILD_DISOLUTION_CHANNEL)
    def handle_guild_disolution_channel_decorate(self, recv_buff):
        packet = sc_guild_disolution_channel()
        packet.deserialize(recv_buff)
        return self.handle_guild_disolution_channel(packet)    
    def handle_guild_disolution_channel(self, packet):
        return None

    
    # CS_GUILD_QUIT_CHANNEL
    @CallbackBase.callback(OP_CODE.CS_GUILD_QUIT_CHANNEL)
    def send_guild_quit_channel_decorate(self, code):
        packet = cs_guild_quit_channel()
        self.make_guild_quit_channel_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_quit_channel packet
    def make_guild_quit_channel_packet(self, packet):
        return None
    # send guild_quit_channel
    def send_guild_quit_channel(self):
        self.dispatch(OP_CODE.CS_GUILD_QUIT_CHANNEL)(OP_CODE.CS_GUILD_QUIT_CHANNEL)
    
    # handle SC_GUILD_QUIT_CHANNEL
    @CallbackBase.callback(OP_CODE.SC_GUILD_QUIT_CHANNEL)
    def handle_guild_quit_channel_decorate(self, recv_buff):
        packet = sc_guild_quit_channel()
        packet.deserialize(recv_buff)
        return self.handle_guild_quit_channel(packet)    
    def handle_guild_quit_channel(self, packet):
        return None

    
    # CS_GUILD_INVITE_JOIN_CHANNEL
    @CallbackBase.callback(OP_CODE.CS_GUILD_INVITE_JOIN_CHANNEL)
    def send_guild_invite_join_channel_decorate(self, code):
        packet = cs_guild_invite_join_channel()
        self.make_guild_invite_join_channel_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_invite_join_channel packet
    def make_guild_invite_join_channel_packet(self, packet):
        return None
    # send guild_invite_join_channel
    def send_guild_invite_join_channel(self):
        self.dispatch(OP_CODE.CS_GUILD_INVITE_JOIN_CHANNEL)(OP_CODE.CS_GUILD_INVITE_JOIN_CHANNEL)
    
    # handle SC_GUILD_INVITE_JOIN_CHANNEL
    @CallbackBase.callback(OP_CODE.SC_GUILD_INVITE_JOIN_CHANNEL)
    def handle_guild_invite_join_channel_decorate(self, recv_buff):
        packet = sc_guild_invite_join_channel()
        packet.deserialize(recv_buff)
        return self.handle_guild_invite_join_channel(packet)    
    def handle_guild_invite_join_channel(self, packet):
        return None

    
    # CS_REQ_GUILD_MEMBER
    @CallbackBase.callback(OP_CODE.CS_REQ_GUILD_MEMBER)
    def send_req_guild_member_decorate(self, code):
        packet = cs_req_guild_member()
        self.make_req_guild_member_packet(packet)
        self.mes_que[code] = packet
    # makeup req_guild_member packet
    def make_req_guild_member_packet(self, packet):
        return None
    # send req_guild_member
    def send_req_guild_member(self):
        self.dispatch(OP_CODE.CS_REQ_GUILD_MEMBER)(OP_CODE.CS_REQ_GUILD_MEMBER)
    
    # handle SC_REQ_GUILD_MEMBER
    @CallbackBase.callback(OP_CODE.SC_REQ_GUILD_MEMBER)
    def handle_req_guild_member_decorate(self, recv_buff):
        packet = sc_req_guild_member()
        packet.deserialize(recv_buff)
        return self.handle_req_guild_member(packet)    
    def handle_req_guild_member(self, packet):
        return None

    
    # CS_GUILD_EXPEL_CHANNEL
    @CallbackBase.callback(OP_CODE.CS_GUILD_EXPEL_CHANNEL)
    def send_guild_expel_channel_decorate(self, code):
        packet = cs_guild_expel_channel()
        self.make_guild_expel_channel_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_expel_channel packet
    def make_guild_expel_channel_packet(self, packet):
        return None
    # send guild_expel_channel
    def send_guild_expel_channel(self):
        self.dispatch(OP_CODE.CS_GUILD_EXPEL_CHANNEL)(OP_CODE.CS_GUILD_EXPEL_CHANNEL)
    
    # handle SC_GUILD_EXPEL_CHANNEL
    @CallbackBase.callback(OP_CODE.SC_GUILD_EXPEL_CHANNEL)
    def handle_guild_expel_channel_decorate(self, recv_buff):
        packet = sc_guild_expel_channel()
        packet.deserialize(recv_buff)
        return self.handle_guild_expel_channel(packet)    
    def handle_guild_expel_channel(self, packet):
        return None

    
    # CS_GUARD_HOME
    @CallbackBase.callback(OP_CODE.CS_GUARD_HOME)
    def send_guard_home_decorate(self, code):
        packet = cs_guard_home()
        self.make_guard_home_packet(packet)
        self.mes_que[code] = packet
    # makeup guard_home packet
    def make_guard_home_packet(self, packet):
        return None
    # send guard_home
    def send_guard_home(self):
        self.dispatch(OP_CODE.CS_GUARD_HOME)(OP_CODE.CS_GUARD_HOME)
    
    # handle SC_GUARD_HOME
    @CallbackBase.callback(OP_CODE.SC_GUARD_HOME)
    def handle_guard_home_decorate(self, recv_buff):
        packet = sc_guard_home()
        packet.deserialize(recv_buff)
        return self.handle_guard_home(packet)    
    def handle_guard_home(self, packet):
        return None

    
    # CS_GUARD_HOME_CANCEL
    @CallbackBase.callback(OP_CODE.CS_GUARD_HOME_CANCEL)
    def send_guard_home_cancel_decorate(self, code):
        packet = cs_guard_home_cancel()
        self.make_guard_home_cancel_packet(packet)
        self.mes_que[code] = packet
    # makeup guard_home_cancel packet
    def make_guard_home_cancel_packet(self, packet):
        return None
    # send guard_home_cancel
    def send_guard_home_cancel(self):
        self.dispatch(OP_CODE.CS_GUARD_HOME_CANCEL)(OP_CODE.CS_GUARD_HOME_CANCEL)
    
    # handle SC_GUARD_HOME_CANCEL
    @CallbackBase.callback(OP_CODE.SC_GUARD_HOME_CANCEL)
    def handle_guard_home_cancel_decorate(self, recv_buff):
        packet = sc_guard_home_cancel()
        packet.deserialize(recv_buff)
        return self.handle_guard_home_cancel(packet)    
    def handle_guard_home_cancel(self, packet):
        return None

    
    # CS_WORLD_CHAT
    @CallbackBase.callback(OP_CODE.CS_WORLD_CHAT)
    def send_world_chat_decorate(self, code):
        packet = cs_world_chat()
        self.make_world_chat_packet(packet)
        self.mes_que[code] = packet
    # makeup world_chat packet
    def make_world_chat_packet(self, packet):
        return None
    # send world_chat
    def send_world_chat(self):
        self.dispatch(OP_CODE.CS_WORLD_CHAT)(OP_CODE.CS_WORLD_CHAT)
    
    # handle SC_WORLD_CHAT
    @CallbackBase.callback(OP_CODE.SC_WORLD_CHAT)
    def handle_world_chat_decorate(self, recv_buff):
        packet = sc_world_chat()
        packet.deserialize(recv_buff)
        return self.handle_world_chat(packet)    
    def handle_world_chat(self, packet):
        return None

    
    # handle SCHAT_WORLD_CHAT
    @CallbackBase.callback(OP_CODE.SCHAT_WORLD_CHAT)
    def handle_at_world_chat_decorate(self, recv_buff):
        packet = schat_world_chat()
        packet.deserialize(recv_buff)
        return self.handle_at_world_chat(packet)    
    def handle_at_world_chat(self, packet):
        return None

    
    # CS_SYNC_USER_EVENT_FLAG
    @CallbackBase.callback(OP_CODE.CS_SYNC_USER_EVENT_FLAG)
    def send_sync_user_event_flag_decorate(self, code):
        packet = cs_sync_user_event_flag()
        self.make_sync_user_event_flag_packet(packet)
        self.mes_que[code] = packet
    # makeup sync_user_event_flag packet
    def make_sync_user_event_flag_packet(self, packet):
        return None
    # send sync_user_event_flag
    def send_sync_user_event_flag(self):
        self.dispatch(OP_CODE.CS_SYNC_USER_EVENT_FLAG)(OP_CODE.CS_SYNC_USER_EVENT_FLAG)
    
    # handle SC_SYNC_USER_EVENT_FLAG
    @CallbackBase.callback(OP_CODE.SC_SYNC_USER_EVENT_FLAG)
    def handle_sync_user_event_flag_decorate(self, recv_buff):
        packet = sc_sync_user_event_flag()
        packet.deserialize(recv_buff)
        return self.handle_sync_user_event_flag(packet)    
    def handle_sync_user_event_flag(self, packet):
        return None

    
    # CS_GET_GUILD_MEMBER_BRIEF
    @CallbackBase.callback(OP_CODE.CS_GET_GUILD_MEMBER_BRIEF)
    def send_get_guild_member_brief_decorate(self, code):
        packet = cs_get_guild_member_brief()
        self.make_get_guild_member_brief_packet(packet)
        self.mes_que[code] = packet
    # makeup get_guild_member_brief packet
    def make_get_guild_member_brief_packet(self, packet):
        return None
    # send get_guild_member_brief
    def send_get_guild_member_brief(self):
        self.dispatch(OP_CODE.CS_GET_GUILD_MEMBER_BRIEF)(OP_CODE.CS_GET_GUILD_MEMBER_BRIEF)
    
    # handle SC_GET_GUILD_MEMBER_BRIEF
    @CallbackBase.callback(OP_CODE.SC_GET_GUILD_MEMBER_BRIEF)
    def handle_get_guild_member_brief_decorate(self, recv_buff):
        packet = sc_get_guild_member_brief()
        packet.deserialize(recv_buff)
        return self.handle_get_guild_member_brief(packet)    
    def handle_get_guild_member_brief(self, packet):
        return None

    
    # CS_HERO_ASSIGN_JUNXIAN
    @CallbackBase.callback(OP_CODE.CS_HERO_ASSIGN_JUNXIAN)
    def send_hero_assign_junxian_decorate(self, code):
        packet = cs_hero_assign_junxian()
        self.make_hero_assign_junxian_packet(packet)
        self.mes_que[code] = packet
    # makeup hero_assign_junxian packet
    def make_hero_assign_junxian_packet(self, packet):
        return None
    # send hero_assign_junxian
    def send_hero_assign_junxian(self):
        self.dispatch(OP_CODE.CS_HERO_ASSIGN_JUNXIAN)(OP_CODE.CS_HERO_ASSIGN_JUNXIAN)
    
    # handle SC_HERO_ASSIGN_JUNXIAN
    @CallbackBase.callback(OP_CODE.SC_HERO_ASSIGN_JUNXIAN)
    def handle_hero_assign_junxian_decorate(self, recv_buff):
        packet = sc_hero_assign_junxian()
        packet.deserialize(recv_buff)
        return self.handle_hero_assign_junxian(packet)    
    def handle_hero_assign_junxian(self, packet):
        return None

    
    # CS_USER_ITEM
    @CallbackBase.callback(OP_CODE.CS_USER_ITEM)
    def send_user_item_decorate(self, code):
        packet = cs_user_item()
        self.make_user_item_packet(packet)
        self.mes_que[code] = packet
    # makeup user_item packet
    def make_user_item_packet(self, packet):
        return None
    # send user_item
    def send_user_item(self):
        self.dispatch(OP_CODE.CS_USER_ITEM)(OP_CODE.CS_USER_ITEM)
    
    # handle SC_USER_ITEM
    @CallbackBase.callback(OP_CODE.SC_USER_ITEM)
    def handle_user_item_decorate(self, recv_buff):
        packet = sc_user_item()
        packet.deserialize(recv_buff)
        return self.handle_user_item(packet)    
    def handle_user_item(self, packet):
        return None

    
    # CS_PUSH_ONE_MAIL
    @CallbackBase.callback(OP_CODE.CS_PUSH_ONE_MAIL)
    def send_push_one_mail_decorate(self, code):
        packet = cs_push_one_mail()
        self.make_push_one_mail_packet(packet)
        self.mes_que[code] = packet
    # makeup push_one_mail packet
    def make_push_one_mail_packet(self, packet):
        return None
    # send push_one_mail
    def send_push_one_mail(self):
        self.dispatch(OP_CODE.CS_PUSH_ONE_MAIL)(OP_CODE.CS_PUSH_ONE_MAIL)
    
    # handle SC_PUSH_ONE_MAIL
    @CallbackBase.callback(OP_CODE.SC_PUSH_ONE_MAIL)
    def handle_push_one_mail_decorate(self, recv_buff):
        packet = sc_push_one_mail()
        packet.deserialize(recv_buff)
        return self.handle_push_one_mail(packet)    
    def handle_push_one_mail(self, packet):
        return None

    
    # CS_MAIL_READ_SET
    @CallbackBase.callback(OP_CODE.CS_MAIL_READ_SET)
    def send_mail_read_set_decorate(self, code):
        packet = cs_mail_read_set()
        self.make_mail_read_set_packet(packet)
        self.mes_que[code] = packet
    # makeup mail_read_set packet
    def make_mail_read_set_packet(self, packet):
        return None
    # send mail_read_set
    def send_mail_read_set(self):
        self.dispatch(OP_CODE.CS_MAIL_READ_SET)(OP_CODE.CS_MAIL_READ_SET)
    
    # handle SC_MAIL_READ_SET
    @CallbackBase.callback(OP_CODE.SC_MAIL_READ_SET)
    def handle_mail_read_set_decorate(self, recv_buff):
        packet = sc_mail_read_set()
        packet.deserialize(recv_buff)
        return self.handle_mail_read_set(packet)    
    def handle_mail_read_set(self, packet):
        return None

    
    # CS_GET_GUILD_BATTLE_RECORD_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_GUILD_BATTLE_RECORD_LIST)
    def send_get_guild_battle_record_list_decorate(self, code):
        packet = cs_get_guild_battle_record_list()
        self.make_get_guild_battle_record_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_guild_battle_record_list packet
    def make_get_guild_battle_record_list_packet(self, packet):
        return None
    # send get_guild_battle_record_list
    def send_get_guild_battle_record_list(self):
        self.dispatch(OP_CODE.CS_GET_GUILD_BATTLE_RECORD_LIST)(OP_CODE.CS_GET_GUILD_BATTLE_RECORD_LIST)
    
    # handle SC_GET_GUILD_BATTLE_RECORD_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_GUILD_BATTLE_RECORD_LIST)
    def handle_get_guild_battle_record_list_decorate(self, recv_buff):
        packet = sc_get_guild_battle_record_list()
        packet.deserialize(recv_buff)
        return self.handle_get_guild_battle_record_list(packet)    
    def handle_get_guild_battle_record_list(self, packet):
        return None

    
    # CS_GET_NO_READ_MAIL_NUM
    @CallbackBase.callback(OP_CODE.CS_GET_NO_READ_MAIL_NUM)
    def send_get_no_read_mail_num_decorate(self, code):
        packet = cs_get_no_read_mail_num()
        self.make_get_no_read_mail_num_packet(packet)
        self.mes_que[code] = packet
    # makeup get_no_read_mail_num packet
    def make_get_no_read_mail_num_packet(self, packet):
        return None
    # send get_no_read_mail_num
    def send_get_no_read_mail_num(self):
        self.dispatch(OP_CODE.CS_GET_NO_READ_MAIL_NUM)(OP_CODE.CS_GET_NO_READ_MAIL_NUM)
    
    # handle SC_GET_NO_READ_MAIL_NUM
    @CallbackBase.callback(OP_CODE.SC_GET_NO_READ_MAIL_NUM)
    def handle_get_no_read_mail_num_decorate(self, recv_buff):
        packet = sc_get_no_read_mail_num()
        packet.deserialize(recv_buff)
        return self.handle_get_no_read_mail_num(packet)    
    def handle_get_no_read_mail_num(self, packet):
        return None

    
    # handle SCHAT_SYS_INFO
    @CallbackBase.callback(OP_CODE.SCHAT_SYS_INFO)
    def handle_at_sys_info_decorate(self, recv_buff):
        packet = schat_sys_info()
        packet.deserialize(recv_buff)
        return self.handle_at_sys_info(packet)    
    def handle_at_sys_info(self, packet):
        return None

    
    # CS_SELL_ITEM
    @CallbackBase.callback(OP_CODE.CS_SELL_ITEM)
    def send_sell_item_decorate(self, code):
        packet = cs_sell_item()
        self.make_sell_item_packet(packet)
        self.mes_que[code] = packet
    # makeup sell_item packet
    def make_sell_item_packet(self, packet):
        return None
    # send sell_item
    def send_sell_item(self):
        self.dispatch(OP_CODE.CS_SELL_ITEM)(OP_CODE.CS_SELL_ITEM)
    
    # handle SC_SELL_ITEM
    @CallbackBase.callback(OP_CODE.SC_SELL_ITEM)
    def handle_sell_item_decorate(self, recv_buff):
        packet = sc_sell_item()
        packet.deserialize(recv_buff)
        return self.handle_sell_item(packet)    
    def handle_sell_item(self, packet):
        return None

    
    # CS_GET_FANJIQING
    @CallbackBase.callback(OP_CODE.CS_GET_FANJIQING)
    def send_get_fanjiqing_decorate(self, code):
        packet = cs_get_fanjiqing()
        self.make_get_fanjiqing_packet(packet)
        self.mes_que[code] = packet
    # makeup get_fanjiqing packet
    def make_get_fanjiqing_packet(self, packet):
        return None
    # send get_fanjiqing
    def send_get_fanjiqing(self):
        self.dispatch(OP_CODE.CS_GET_FANJIQING)(OP_CODE.CS_GET_FANJIQING)
    
    # handle SC_GET_FANJIQING
    @CallbackBase.callback(OP_CODE.SC_GET_FANJIQING)
    def handle_get_fanjiqing_decorate(self, recv_buff):
        packet = sc_get_fanjiqing()
        packet.deserialize(recv_buff)
        return self.handle_get_fanjiqing(packet)    
    def handle_get_fanjiqing(self, packet):
        return None

    
    # CS_GET_MY_BLOCKS
    @CallbackBase.callback(OP_CODE.CS_GET_MY_BLOCKS)
    def send_get_my_blocks_decorate(self, code):
        packet = cs_get_my_blocks()
        self.make_get_my_blocks_packet(packet)
        self.mes_que[code] = packet
    # makeup get_my_blocks packet
    def make_get_my_blocks_packet(self, packet):
        return None
    # send get_my_blocks
    def send_get_my_blocks(self):
        self.dispatch(OP_CODE.CS_GET_MY_BLOCKS)(OP_CODE.CS_GET_MY_BLOCKS)
    
    # handle SC_GET_MY_BLOCKS
    @CallbackBase.callback(OP_CODE.SC_GET_MY_BLOCKS)
    def handle_get_my_blocks_decorate(self, recv_buff):
        packet = sc_get_my_blocks()
        packet.deserialize(recv_buff)
        return self.handle_get_my_blocks(packet)    
    def handle_get_my_blocks(self, packet):
        return None

    
    # CS_CHANGE_DEFEND_HERO
    @CallbackBase.callback(OP_CODE.CS_CHANGE_DEFEND_HERO)
    def send_change_defend_hero_decorate(self, code):
        packet = cs_change_defend_hero()
        self.make_change_defend_hero_packet(packet)
        self.mes_que[code] = packet
    # makeup change_defend_hero packet
    def make_change_defend_hero_packet(self, packet):
        return None
    # send change_defend_hero
    def send_change_defend_hero(self):
        self.dispatch(OP_CODE.CS_CHANGE_DEFEND_HERO)(OP_CODE.CS_CHANGE_DEFEND_HERO)
    
    # handle SC_CHANGE_DEFEND_HERO
    @CallbackBase.callback(OP_CODE.SC_CHANGE_DEFEND_HERO)
    def handle_change_defend_hero_decorate(self, recv_buff):
        packet = sc_change_defend_hero()
        packet.deserialize(recv_buff)
        return self.handle_change_defend_hero(packet)    
    def handle_change_defend_hero(self, packet):
        return None

    
    # CS_GET_BUILDING_LV
    @CallbackBase.callback(OP_CODE.CS_GET_BUILDING_LV)
    def send_get_building_lv_decorate(self, code):
        packet = cs_get_building_lv()
        self.make_get_building_lv_packet(packet)
        self.mes_que[code] = packet
    # makeup get_building_lv packet
    def make_get_building_lv_packet(self, packet):
        return None
    # send get_building_lv
    def send_get_building_lv(self):
        self.dispatch(OP_CODE.CS_GET_BUILDING_LV)(OP_CODE.CS_GET_BUILDING_LV)
    
    # handle SC_GET_BUILDING_LV
    @CallbackBase.callback(OP_CODE.SC_GET_BUILDING_LV)
    def handle_get_building_lv_decorate(self, recv_buff):
        packet = sc_get_building_lv()
        packet.deserialize(recv_buff)
        return self.handle_get_building_lv(packet)    
    def handle_get_building_lv(self, packet):
        return None

    
    # CS_ACCELERATE_BLOCK_BUILDING_LVUP
    @CallbackBase.callback(OP_CODE.CS_ACCELERATE_BLOCK_BUILDING_LVUP)
    def send_accelerate_block_building_lvup_decorate(self, code):
        packet = cs_accelerate_block_building_lvup()
        self.make_accelerate_block_building_lvup_packet(packet)
        self.mes_que[code] = packet
    # makeup accelerate_block_building_lvup packet
    def make_accelerate_block_building_lvup_packet(self, packet):
        return None
    # send accelerate_block_building_lvup
    def send_accelerate_block_building_lvup(self):
        self.dispatch(OP_CODE.CS_ACCELERATE_BLOCK_BUILDING_LVUP)(OP_CODE.CS_ACCELERATE_BLOCK_BUILDING_LVUP)
    
    # handle SC_ACCELERATE_BLOCK_BUILDING_LVUP
    @CallbackBase.callback(OP_CODE.SC_ACCELERATE_BLOCK_BUILDING_LVUP)
    def handle_accelerate_block_building_lvup_decorate(self, recv_buff):
        packet = sc_accelerate_block_building_lvup()
        packet.deserialize(recv_buff)
        return self.handle_accelerate_block_building_lvup(packet)    
    def handle_accelerate_block_building_lvup(self, packet):
        return None

    
    # CS_GET_NOBILITY_ENTRY
    @CallbackBase.callback(OP_CODE.CS_GET_NOBILITY_ENTRY)
    def send_get_nobility_entry_decorate(self, code):
        packet = cs_get_nobility_entry()
        self.make_get_nobility_entry_packet(packet)
        self.mes_que[code] = packet
    # makeup get_nobility_entry packet
    def make_get_nobility_entry_packet(self, packet):
        return None
    # send get_nobility_entry
    def send_get_nobility_entry(self):
        self.dispatch(OP_CODE.CS_GET_NOBILITY_ENTRY)(OP_CODE.CS_GET_NOBILITY_ENTRY)
    
    # handle SC_GET_NOBILITY_ENTRY
    @CallbackBase.callback(OP_CODE.SC_GET_NOBILITY_ENTRY)
    def handle_get_nobility_entry_decorate(self, recv_buff):
        packet = sc_get_nobility_entry()
        packet.deserialize(recv_buff)
        return self.handle_get_nobility_entry(packet)    
    def handle_get_nobility_entry(self, packet):
        return None

    
    # CS_SILVER_COIN_LOTTERY_DRAW
    @CallbackBase.callback(OP_CODE.CS_SILVER_COIN_LOTTERY_DRAW)
    def send_silver_coin_lottery_draw_decorate(self, code):
        packet = cs_silver_coin_lottery_draw()
        self.make_silver_coin_lottery_draw_packet(packet)
        self.mes_que[code] = packet
    # makeup silver_coin_lottery_draw packet
    def make_silver_coin_lottery_draw_packet(self, packet):
        return None
    # send silver_coin_lottery_draw
    def send_silver_coin_lottery_draw(self):
        self.dispatch(OP_CODE.CS_SILVER_COIN_LOTTERY_DRAW)(OP_CODE.CS_SILVER_COIN_LOTTERY_DRAW)
    
    # handle SC_SILVER_COIN_LOTTERY_DRAW
    @CallbackBase.callback(OP_CODE.SC_SILVER_COIN_LOTTERY_DRAW)
    def handle_silver_coin_lottery_draw_decorate(self, recv_buff):
        packet = sc_silver_coin_lottery_draw()
        packet.deserialize(recv_buff)
        return self.handle_silver_coin_lottery_draw(packet)    
    def handle_silver_coin_lottery_draw(self, packet):
        return None

    
    # CS_BROADCAST_MSG
    @CallbackBase.callback(OP_CODE.CS_BROADCAST_MSG)
    def send_broadcast_msg_decorate(self, code):
        packet = cs_broadcast_msg()
        self.make_broadcast_msg_packet(packet)
        self.mes_que[code] = packet
    # makeup broadcast_msg packet
    def make_broadcast_msg_packet(self, packet):
        return None
    # send broadcast_msg
    def send_broadcast_msg(self):
        self.dispatch(OP_CODE.CS_BROADCAST_MSG)(OP_CODE.CS_BROADCAST_MSG)
    
    # handle SC_BROADCAST_MSG
    @CallbackBase.callback(OP_CODE.SC_BROADCAST_MSG)
    def handle_broadcast_msg_decorate(self, recv_buff):
        packet = sc_broadcast_msg()
        packet.deserialize(recv_buff)
        return self.handle_broadcast_msg(packet)    
    def handle_broadcast_msg(self, packet):
        return None

    
    # CS_GET_NEWBIE_STEP
    @CallbackBase.callback(OP_CODE.CS_GET_NEWBIE_STEP)
    def send_get_newbie_step_decorate(self, code):
        packet = cs_get_newbie_step()
        self.make_get_newbie_step_packet(packet)
        self.mes_que[code] = packet
    # makeup get_newbie_step packet
    def make_get_newbie_step_packet(self, packet):
        return None
    # send get_newbie_step
    def send_get_newbie_step(self):
        self.dispatch(OP_CODE.CS_GET_NEWBIE_STEP)(OP_CODE.CS_GET_NEWBIE_STEP)
    
    # handle SC_GET_NEWBIE_STEP
    @CallbackBase.callback(OP_CODE.SC_GET_NEWBIE_STEP)
    def handle_get_newbie_step_decorate(self, recv_buff):
        packet = sc_get_newbie_step()
        packet.deserialize(recv_buff)
        return self.handle_get_newbie_step(packet)    
    def handle_get_newbie_step(self, packet):
        return None

    
    # CS_SET_NEWBIE_STEP
    @CallbackBase.callback(OP_CODE.CS_SET_NEWBIE_STEP)
    def send_set_newbie_step_decorate(self, code):
        packet = cs_set_newbie_step()
        self.make_set_newbie_step_packet(packet)
        self.mes_que[code] = packet
    # makeup set_newbie_step packet
    def make_set_newbie_step_packet(self, packet):
        return None
    # send set_newbie_step
    def send_set_newbie_step(self):
        self.dispatch(OP_CODE.CS_SET_NEWBIE_STEP)(OP_CODE.CS_SET_NEWBIE_STEP)
    
    # handle SC_SET_NEWBIE_STEP
    @CallbackBase.callback(OP_CODE.SC_SET_NEWBIE_STEP)
    def handle_set_newbie_step_decorate(self, recv_buff):
        packet = sc_set_newbie_step()
        packet.deserialize(recv_buff)
        return self.handle_set_newbie_step(packet)    
    def handle_set_newbie_step(self, packet):
        return None

    
    # CS_GET_WORLD_CITIES
    @CallbackBase.callback(OP_CODE.CS_GET_WORLD_CITIES)
    def send_get_world_cities_decorate(self, code):
        packet = cs_get_world_cities()
        self.make_get_world_cities_packet(packet)
        self.mes_que[code] = packet
    # makeup get_world_cities packet
    def make_get_world_cities_packet(self, packet):
        return None
    # send get_world_cities
    def send_get_world_cities(self):
        self.dispatch(OP_CODE.CS_GET_WORLD_CITIES)(OP_CODE.CS_GET_WORLD_CITIES)
    
    # handle SC_GET_WORLD_CITIES
    @CallbackBase.callback(OP_CODE.SC_GET_WORLD_CITIES)
    def handle_get_world_cities_decorate(self, recv_buff):
        packet = sc_get_world_cities()
        packet.deserialize(recv_buff)
        return self.handle_get_world_cities(packet)    
    def handle_get_world_cities(self, packet):
        return None

    
    # CS_GET_STATE_CITIES
    @CallbackBase.callback(OP_CODE.CS_GET_STATE_CITIES)
    def send_get_state_cities_decorate(self, code):
        packet = cs_get_state_cities()
        self.make_get_state_cities_packet(packet)
        self.mes_que[code] = packet
    # makeup get_state_cities packet
    def make_get_state_cities_packet(self, packet):
        return None
    # send get_state_cities
    def send_get_state_cities(self):
        self.dispatch(OP_CODE.CS_GET_STATE_CITIES)(OP_CODE.CS_GET_STATE_CITIES)
    
    # handle SC_GET_STATE_CITIES
    @CallbackBase.callback(OP_CODE.SC_GET_STATE_CITIES)
    def handle_get_state_cities_decorate(self, recv_buff):
        packet = sc_get_state_cities()
        packet.deserialize(recv_buff)
        return self.handle_get_state_cities(packet)    
    def handle_get_state_cities(self, packet):
        return None

    
    # CS_GET_SEASON_DATA
    @CallbackBase.callback(OP_CODE.CS_GET_SEASON_DATA)
    def send_get_season_data_decorate(self, code):
        packet = cs_get_season_data()
        self.make_get_season_data_packet(packet)
        self.mes_que[code] = packet
    # makeup get_season_data packet
    def make_get_season_data_packet(self, packet):
        return None
    # send get_season_data
    def send_get_season_data(self):
        self.dispatch(OP_CODE.CS_GET_SEASON_DATA)(OP_CODE.CS_GET_SEASON_DATA)
    
    # handle SC_GET_SEASON_DATA
    @CallbackBase.callback(OP_CODE.SC_GET_SEASON_DATA)
    def handle_get_season_data_decorate(self, recv_buff):
        packet = sc_get_season_data()
        packet.deserialize(recv_buff)
        return self.handle_get_season_data(packet)    
    def handle_get_season_data(self, packet):
        return None

    
    # CS_BUY_SEASON_REWARD
    @CallbackBase.callback(OP_CODE.CS_BUY_SEASON_REWARD)
    def send_buy_season_reward_decorate(self, code):
        packet = cs_buy_season_reward()
        self.make_buy_season_reward_packet(packet)
        self.mes_que[code] = packet
    # makeup buy_season_reward packet
    def make_buy_season_reward_packet(self, packet):
        return None
    # send buy_season_reward
    def send_buy_season_reward(self):
        self.dispatch(OP_CODE.CS_BUY_SEASON_REWARD)(OP_CODE.CS_BUY_SEASON_REWARD)
    
    # handle SC_BUY_SEASON_REWARD
    @CallbackBase.callback(OP_CODE.SC_BUY_SEASON_REWARD)
    def handle_buy_season_reward_decorate(self, recv_buff):
        packet = sc_buy_season_reward()
        packet.deserialize(recv_buff)
        return self.handle_buy_season_reward(packet)    
    def handle_buy_season_reward(self, packet):
        return None

    
    # CS_READ_BATTLE_REPORT
    @CallbackBase.callback(OP_CODE.CS_READ_BATTLE_REPORT)
    def send_read_battle_report_decorate(self, code):
        packet = cs_read_battle_report()
        self.make_read_battle_report_packet(packet)
        self.mes_que[code] = packet
    # makeup read_battle_report packet
    def make_read_battle_report_packet(self, packet):
        return None
    # send read_battle_report
    def send_read_battle_report(self):
        self.dispatch(OP_CODE.CS_READ_BATTLE_REPORT)(OP_CODE.CS_READ_BATTLE_REPORT)
    
    # handle SC_READ_BATTLE_REPORT
    @CallbackBase.callback(OP_CODE.SC_READ_BATTLE_REPORT)
    def handle_read_battle_report_decorate(self, recv_buff):
        packet = sc_read_battle_report()
        packet.deserialize(recv_buff)
        return self.handle_read_battle_report(packet)    
    def handle_read_battle_report(self, packet):
        return None

    
    # CS_GET_WORLD_TREND_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_WORLD_TREND_LIST)
    def send_get_world_trend_list_decorate(self, code):
        packet = cs_get_world_trend_list()
        self.make_get_world_trend_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_world_trend_list packet
    def make_get_world_trend_list_packet(self, packet):
        return None
    # send get_world_trend_list
    def send_get_world_trend_list(self):
        self.dispatch(OP_CODE.CS_GET_WORLD_TREND_LIST)(OP_CODE.CS_GET_WORLD_TREND_LIST)
    
    # handle SC_GET_WORLD_TREND_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_WORLD_TREND_LIST)
    def handle_get_world_trend_list_decorate(self, recv_buff):
        packet = sc_get_world_trend_list()
        packet.deserialize(recv_buff)
        return self.handle_get_world_trend_list(packet)    
    def handle_get_world_trend_list(self, packet):
        return None

    
    # CS_GET_WORLD_TREND_REWARDS
    @CallbackBase.callback(OP_CODE.CS_GET_WORLD_TREND_REWARDS)
    def send_get_world_trend_rewards_decorate(self, code):
        packet = cs_get_world_trend_rewards()
        self.make_get_world_trend_rewards_packet(packet)
        self.mes_que[code] = packet
    # makeup get_world_trend_rewards packet
    def make_get_world_trend_rewards_packet(self, packet):
        return None
    # send get_world_trend_rewards
    def send_get_world_trend_rewards(self):
        self.dispatch(OP_CODE.CS_GET_WORLD_TREND_REWARDS)(OP_CODE.CS_GET_WORLD_TREND_REWARDS)
    
    # handle SC_GET_WORLD_TREND_REWARDS
    @CallbackBase.callback(OP_CODE.SC_GET_WORLD_TREND_REWARDS)
    def handle_get_world_trend_rewards_decorate(self, recv_buff):
        packet = sc_get_world_trend_rewards()
        packet.deserialize(recv_buff)
        return self.handle_get_world_trend_rewards(packet)    
    def handle_get_world_trend_rewards(self, packet):
        return None

    
    # CS_GET_STATE_ACHI_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_STATE_ACHI_LIST)
    def send_get_state_achi_list_decorate(self, code):
        packet = cs_get_state_achi_list()
        self.make_get_state_achi_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_state_achi_list packet
    def make_get_state_achi_list_packet(self, packet):
        return None
    # send get_state_achi_list
    def send_get_state_achi_list(self):
        self.dispatch(OP_CODE.CS_GET_STATE_ACHI_LIST)(OP_CODE.CS_GET_STATE_ACHI_LIST)
    
    # handle SC_GET_STATE_ACHI_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_STATE_ACHI_LIST)
    def handle_get_state_achi_list_decorate(self, recv_buff):
        packet = sc_get_state_achi_list()
        packet.deserialize(recv_buff)
        return self.handle_get_state_achi_list(packet)    
    def handle_get_state_achi_list(self, packet):
        return None

    
    # CS_GET_STATE_ACHI_REWARDS
    @CallbackBase.callback(OP_CODE.CS_GET_STATE_ACHI_REWARDS)
    def send_get_state_achi_rewards_decorate(self, code):
        packet = cs_get_state_achi_rewards()
        self.make_get_state_achi_rewards_packet(packet)
        self.mes_que[code] = packet
    # makeup get_state_achi_rewards packet
    def make_get_state_achi_rewards_packet(self, packet):
        return None
    # send get_state_achi_rewards
    def send_get_state_achi_rewards(self):
        self.dispatch(OP_CODE.CS_GET_STATE_ACHI_REWARDS)(OP_CODE.CS_GET_STATE_ACHI_REWARDS)
    
    # handle SC_GET_STATE_ACHI_REWARDS
    @CallbackBase.callback(OP_CODE.SC_GET_STATE_ACHI_REWARDS)
    def handle_get_state_achi_rewards_decorate(self, recv_buff):
        packet = sc_get_state_achi_rewards()
        packet.deserialize(recv_buff)
        return self.handle_get_state_achi_rewards(packet)    
    def handle_get_state_achi_rewards(self, packet):
        return None

    
    # CS_ONEBTN_CONSCRIPT_SOLDIER
    @CallbackBase.callback(OP_CODE.CS_ONEBTN_CONSCRIPT_SOLDIER)
    def send_onebtn_conscript_soldier_decorate(self, code):
        packet = cs_onebtn_conscript_soldier()
        self.make_onebtn_conscript_soldier_packet(packet)
        self.mes_que[code] = packet
    # makeup onebtn_conscript_soldier packet
    def make_onebtn_conscript_soldier_packet(self, packet):
        return None
    # send onebtn_conscript_soldier
    def send_onebtn_conscript_soldier(self):
        self.dispatch(OP_CODE.CS_ONEBTN_CONSCRIPT_SOLDIER)(OP_CODE.CS_ONEBTN_CONSCRIPT_SOLDIER)
    
    # handle SC_ONEBTN_CONSCRIPT_SOLDIER
    @CallbackBase.callback(OP_CODE.SC_ONEBTN_CONSCRIPT_SOLDIER)
    def handle_onebtn_conscript_soldier_decorate(self, recv_buff):
        packet = sc_onebtn_conscript_soldier()
        packet.deserialize(recv_buff)
        return self.handle_onebtn_conscript_soldier(packet)    
    def handle_onebtn_conscript_soldier(self, packet):
        return None

    
    # CS_QUERY_PAY_RESULT
    @CallbackBase.callback(OP_CODE.CS_QUERY_PAY_RESULT)
    def send_query_pay_result_decorate(self, code):
        packet = cs_query_pay_result()
        self.make_query_pay_result_packet(packet)
        self.mes_que[code] = packet
    # makeup query_pay_result packet
    def make_query_pay_result_packet(self, packet):
        return None
    # send query_pay_result
    def send_query_pay_result(self):
        self.dispatch(OP_CODE.CS_QUERY_PAY_RESULT)(OP_CODE.CS_QUERY_PAY_RESULT)
    
    # handle SC_QUERY_PAY_RESULT
    @CallbackBase.callback(OP_CODE.SC_QUERY_PAY_RESULT)
    def handle_query_pay_result_decorate(self, recv_buff):
        packet = sc_query_pay_result()
        packet.deserialize(recv_buff)
        return self.handle_query_pay_result(packet)    
    def handle_query_pay_result(self, packet):
        return None

    
    # CS_HERO_STAR_LVUP
    @CallbackBase.callback(OP_CODE.CS_HERO_STAR_LVUP)
    def send_hero_star_lvup_decorate(self, code):
        packet = cs_hero_star_lvup()
        self.make_hero_star_lvup_packet(packet)
        self.mes_que[code] = packet
    # makeup hero_star_lvup packet
    def make_hero_star_lvup_packet(self, packet):
        return None
    # send hero_star_lvup
    def send_hero_star_lvup(self):
        self.dispatch(OP_CODE.CS_HERO_STAR_LVUP)(OP_CODE.CS_HERO_STAR_LVUP)
    
    # handle SC_HERO_STAR_LVUP
    @CallbackBase.callback(OP_CODE.SC_HERO_STAR_LVUP)
    def handle_hero_star_lvup_decorate(self, recv_buff):
        packet = sc_hero_star_lvup()
        packet.deserialize(recv_buff)
        return self.handle_hero_star_lvup(packet)    
    def handle_hero_star_lvup(self, packet):
        return None

    
    # CS_GET_VIP_REWARD_STATUS
    @CallbackBase.callback(OP_CODE.CS_GET_VIP_REWARD_STATUS)
    def send_get_vip_reward_status_decorate(self, code):
        packet = cs_get_vip_reward_status()
        self.make_get_vip_reward_status_packet(packet)
        self.mes_que[code] = packet
    # makeup get_vip_reward_status packet
    def make_get_vip_reward_status_packet(self, packet):
        return None
    # send get_vip_reward_status
    def send_get_vip_reward_status(self):
        self.dispatch(OP_CODE.CS_GET_VIP_REWARD_STATUS)(OP_CODE.CS_GET_VIP_REWARD_STATUS)
    
    # handle SC_GET_VIP_REWARD_STATUS
    @CallbackBase.callback(OP_CODE.SC_GET_VIP_REWARD_STATUS)
    def handle_get_vip_reward_status_decorate(self, recv_buff):
        packet = sc_get_vip_reward_status()
        packet.deserialize(recv_buff)
        return self.handle_get_vip_reward_status(packet)    
    def handle_get_vip_reward_status(self, packet):
        return None

    
    # CS_GET_VIP_REWARD
    @CallbackBase.callback(OP_CODE.CS_GET_VIP_REWARD)
    def send_get_vip_reward_decorate(self, code):
        packet = cs_get_vip_reward()
        self.make_get_vip_reward_packet(packet)
        self.mes_que[code] = packet
    # makeup get_vip_reward packet
    def make_get_vip_reward_packet(self, packet):
        return None
    # send get_vip_reward
    def send_get_vip_reward(self):
        self.dispatch(OP_CODE.CS_GET_VIP_REWARD)(OP_CODE.CS_GET_VIP_REWARD)
    
    # handle SC_GET_VIP_REWARD
    @CallbackBase.callback(OP_CODE.SC_GET_VIP_REWARD)
    def handle_get_vip_reward_decorate(self, recv_buff):
        packet = sc_get_vip_reward()
        packet.deserialize(recv_buff)
        return self.handle_get_vip_reward(packet)    
    def handle_get_vip_reward(self, packet):
        return None

    
    # CS_MIRACLE_BATTLE
    @CallbackBase.callback(OP_CODE.CS_MIRACLE_BATTLE)
    def send_miracle_battle_decorate(self, code):
        packet = cs_miracle_battle()
        self.make_miracle_battle_packet(packet)
        self.mes_que[code] = packet
    # makeup miracle_battle packet
    def make_miracle_battle_packet(self, packet):
        return None
    # send miracle_battle
    def send_miracle_battle(self):
        self.dispatch(OP_CODE.CS_MIRACLE_BATTLE)(OP_CODE.CS_MIRACLE_BATTLE)
    
    # handle SC_MIRACLE_BATTLE
    @CallbackBase.callback(OP_CODE.SC_MIRACLE_BATTLE)
    def handle_miracle_battle_decorate(self, recv_buff):
        packet = sc_miracle_battle()
        packet.deserialize(recv_buff)
        return self.handle_miracle_battle(packet)    
    def handle_miracle_battle(self, packet):
        return None

    
    # CS_HERO_QUALITY_LVUP
    @CallbackBase.callback(OP_CODE.CS_HERO_QUALITY_LVUP)
    def send_hero_quality_lvup_decorate(self, code):
        packet = cs_hero_quality_lvup()
        self.make_hero_quality_lvup_packet(packet)
        self.mes_que[code] = packet
    # makeup hero_quality_lvup packet
    def make_hero_quality_lvup_packet(self, packet):
        return None
    # send hero_quality_lvup
    def send_hero_quality_lvup(self):
        self.dispatch(OP_CODE.CS_HERO_QUALITY_LVUP)(OP_CODE.CS_HERO_QUALITY_LVUP)
    
    # handle SC_HERO_QUALITY_LVUP
    @CallbackBase.callback(OP_CODE.SC_HERO_QUALITY_LVUP)
    def handle_hero_quality_lvup_decorate(self, recv_buff):
        packet = sc_hero_quality_lvup()
        packet.deserialize(recv_buff)
        return self.handle_hero_quality_lvup(packet)    
    def handle_hero_quality_lvup(self, packet):
        return None

    
    # CS_HANGUP_DATA_REQ
    @CallbackBase.callback(OP_CODE.CS_HANGUP_DATA_REQ)
    def send_hangup_data_req_decorate(self, code):
        packet = cs_hangup_data_req()
        self.make_hangup_data_req_packet(packet)
        self.mes_que[code] = packet
    # makeup hangup_data_req packet
    def make_hangup_data_req_packet(self, packet):
        return None
    # send hangup_data_req
    def send_hangup_data_req(self):
        self.dispatch(OP_CODE.CS_HANGUP_DATA_REQ)(OP_CODE.CS_HANGUP_DATA_REQ)
    
    # handle SC_HANGUP_DATA_REQ
    @CallbackBase.callback(OP_CODE.SC_HANGUP_DATA_REQ)
    def handle_hangup_data_req_decorate(self, recv_buff):
        packet = sc_hangup_data_req()
        packet.deserialize(recv_buff)
        return self.handle_hangup_data_req(packet)    
    def handle_hangup_data_req(self, packet):
        return None

    
    # CS_HANGUP_REWARD
    @CallbackBase.callback(OP_CODE.CS_HANGUP_REWARD)
    def send_hangup_reward_decorate(self, code):
        packet = cs_hangup_reward()
        self.make_hangup_reward_packet(packet)
        self.mes_que[code] = packet
    # makeup hangup_reward packet
    def make_hangup_reward_packet(self, packet):
        return None
    # send hangup_reward
    def send_hangup_reward(self):
        self.dispatch(OP_CODE.CS_HANGUP_REWARD)(OP_CODE.CS_HANGUP_REWARD)
    
    # handle SC_HANGUP_REWARD
    @CallbackBase.callback(OP_CODE.SC_HANGUP_REWARD)
    def handle_hangup_reward_decorate(self, recv_buff):
        packet = sc_hangup_reward()
        packet.deserialize(recv_buff)
        return self.handle_hangup_reward(packet)    
    def handle_hangup_reward(self, packet):
        return None

    
    # CS_HANGUP_SEND
    @CallbackBase.callback(OP_CODE.CS_HANGUP_SEND)
    def send_hangup_send_decorate(self, code):
        packet = cs_hangup_send()
        self.make_hangup_send_packet(packet)
        self.mes_que[code] = packet
    # makeup hangup_send packet
    def make_hangup_send_packet(self, packet):
        return None
    # send hangup_send
    def send_hangup_send(self):
        self.dispatch(OP_CODE.CS_HANGUP_SEND)(OP_CODE.CS_HANGUP_SEND)
    
    # handle SC_HANGUP_SEND
    @CallbackBase.callback(OP_CODE.SC_HANGUP_SEND)
    def handle_hangup_send_decorate(self, recv_buff):
        packet = sc_hangup_send()
        packet.deserialize(recv_buff)
        return self.handle_hangup_send(packet)    
    def handle_hangup_send(self, packet):
        return None

    
    # CS_WANDERING
    @CallbackBase.callback(OP_CODE.CS_WANDERING)
    def send_wandering_decorate(self, code):
        packet = cs_wandering()
        self.make_wandering_packet(packet)
        self.mes_que[code] = packet
    # makeup wandering packet
    def make_wandering_packet(self, packet):
        return None
    # send wandering
    def send_wandering(self):
        self.dispatch(OP_CODE.CS_WANDERING)(OP_CODE.CS_WANDERING)
    
    # handle SC_WANDERING
    @CallbackBase.callback(OP_CODE.SC_WANDERING)
    def handle_wandering_decorate(self, recv_buff):
        packet = sc_wandering()
        packet.deserialize(recv_buff)
        return self.handle_wandering(packet)    
    def handle_wandering(self, packet):
        return None

    
    # CS_HERO_CHANGE_EQUIP_ONE_KEY
    @CallbackBase.callback(OP_CODE.CS_HERO_CHANGE_EQUIP_ONE_KEY)
    def send_hero_change_equip_one_key_decorate(self, code):
        packet = cs_hero_change_equip_one_key()
        self.make_hero_change_equip_one_key_packet(packet)
        self.mes_que[code] = packet
    # makeup hero_change_equip_one_key packet
    def make_hero_change_equip_one_key_packet(self, packet):
        return None
    # send hero_change_equip_one_key
    def send_hero_change_equip_one_key(self):
        self.dispatch(OP_CODE.CS_HERO_CHANGE_EQUIP_ONE_KEY)(OP_CODE.CS_HERO_CHANGE_EQUIP_ONE_KEY)
    
    # handle SC_HERO_CHANGE_EQUIP_ONE_KEY
    @CallbackBase.callback(OP_CODE.SC_HERO_CHANGE_EQUIP_ONE_KEY)
    def handle_hero_change_equip_one_key_decorate(self, recv_buff):
        packet = sc_hero_change_equip_one_key()
        packet.deserialize(recv_buff)
        return self.handle_hero_change_equip_one_key(packet)    
    def handle_hero_change_equip_one_key(self, packet):
        return None

    
    # CS_ARENA_DATA_REQ
    @CallbackBase.callback(OP_CODE.CS_ARENA_DATA_REQ)
    def send_arena_data_req_decorate(self, code):
        packet = cs_arena_data_req()
        self.make_arena_data_req_packet(packet)
        self.mes_que[code] = packet
    # makeup arena_data_req packet
    def make_arena_data_req_packet(self, packet):
        return None
    # send arena_data_req
    def send_arena_data_req(self):
        self.dispatch(OP_CODE.CS_ARENA_DATA_REQ)(OP_CODE.CS_ARENA_DATA_REQ)
    
    # handle SC_ARENA_DATA_REQ
    @CallbackBase.callback(OP_CODE.SC_ARENA_DATA_REQ)
    def handle_arena_data_req_decorate(self, recv_buff):
        packet = sc_arena_data_req()
        packet.deserialize(recv_buff)
        return self.handle_arena_data_req(packet)    
    def handle_arena_data_req(self, packet):
        return None

    
    # CS_ARENA_SET_FORMATION
    @CallbackBase.callback(OP_CODE.CS_ARENA_SET_FORMATION)
    def send_arena_set_formation_decorate(self, code):
        packet = cs_arena_set_formation()
        self.make_arena_set_formation_packet(packet)
        self.mes_que[code] = packet
    # makeup arena_set_formation packet
    def make_arena_set_formation_packet(self, packet):
        return None
    # send arena_set_formation
    def send_arena_set_formation(self):
        self.dispatch(OP_CODE.CS_ARENA_SET_FORMATION)(OP_CODE.CS_ARENA_SET_FORMATION)
    
    # handle SC_ARENA_SET_FORMATION
    @CallbackBase.callback(OP_CODE.SC_ARENA_SET_FORMATION)
    def handle_arena_set_formation_decorate(self, recv_buff):
        packet = sc_arena_set_formation()
        packet.deserialize(recv_buff)
        return self.handle_arena_set_formation(packet)    
    def handle_arena_set_formation(self, packet):
        return None

    
    # CS_ARENA_RANK_REQ
    @CallbackBase.callback(OP_CODE.CS_ARENA_RANK_REQ)
    def send_arena_rank_req_decorate(self, code):
        packet = cs_arena_rank_req()
        self.make_arena_rank_req_packet(packet)
        self.mes_que[code] = packet
    # makeup arena_rank_req packet
    def make_arena_rank_req_packet(self, packet):
        return None
    # send arena_rank_req
    def send_arena_rank_req(self):
        self.dispatch(OP_CODE.CS_ARENA_RANK_REQ)(OP_CODE.CS_ARENA_RANK_REQ)
    
    # handle SC_ARENA_RANK_REQ
    @CallbackBase.callback(OP_CODE.SC_ARENA_RANK_REQ)
    def handle_arena_rank_req_decorate(self, recv_buff):
        packet = sc_arena_rank_req()
        packet.deserialize(recv_buff)
        return self.handle_arena_rank_req(packet)    
    def handle_arena_rank_req(self, packet):
        return None

    
    # CS_ARENA_FRESH
    @CallbackBase.callback(OP_CODE.CS_ARENA_FRESH)
    def send_arena_fresh_decorate(self, code):
        packet = cs_arena_fresh()
        self.make_arena_fresh_packet(packet)
        self.mes_que[code] = packet
    # makeup arena_fresh packet
    def make_arena_fresh_packet(self, packet):
        return None
    # send arena_fresh
    def send_arena_fresh(self):
        self.dispatch(OP_CODE.CS_ARENA_FRESH)(OP_CODE.CS_ARENA_FRESH)
    
    # handle SC_ARENA_FRESH
    @CallbackBase.callback(OP_CODE.SC_ARENA_FRESH)
    def handle_arena_fresh_decorate(self, recv_buff):
        packet = sc_arena_fresh()
        packet.deserialize(recv_buff)
        return self.handle_arena_fresh(packet)    
    def handle_arena_fresh(self, packet):
        return None

    
    # CS_ARENA_FIGHT
    @CallbackBase.callback(OP_CODE.CS_ARENA_FIGHT)
    def send_arena_fight_decorate(self, code):
        packet = cs_arena_fight()
        self.make_arena_fight_packet(packet)
        self.mes_que[code] = packet
    # makeup arena_fight packet
    def make_arena_fight_packet(self, packet):
        return None
    # send arena_fight
    def send_arena_fight(self):
        self.dispatch(OP_CODE.CS_ARENA_FIGHT)(OP_CODE.CS_ARENA_FIGHT)
    
    # handle SC_ARENA_FIGHT
    @CallbackBase.callback(OP_CODE.SC_ARENA_FIGHT)
    def handle_arena_fight_decorate(self, recv_buff):
        packet = sc_arena_fight()
        packet.deserialize(recv_buff)
        return self.handle_arena_fight(packet)    
    def handle_arena_fight(self, packet):
        return None

    
    # CS_ARENA_BUY_TIMES
    @CallbackBase.callback(OP_CODE.CS_ARENA_BUY_TIMES)
    def send_arena_buy_times_decorate(self, code):
        packet = cs_arena_buy_times()
        self.make_arena_buy_times_packet(packet)
        self.mes_que[code] = packet
    # makeup arena_buy_times packet
    def make_arena_buy_times_packet(self, packet):
        return None
    # send arena_buy_times
    def send_arena_buy_times(self):
        self.dispatch(OP_CODE.CS_ARENA_BUY_TIMES)(OP_CODE.CS_ARENA_BUY_TIMES)
    
    # handle SC_ARENA_BUY_TIMES
    @CallbackBase.callback(OP_CODE.SC_ARENA_BUY_TIMES)
    def handle_arena_buy_times_decorate(self, recv_buff):
        packet = sc_arena_buy_times()
        packet.deserialize(recv_buff)
        return self.handle_arena_buy_times(packet)    
    def handle_arena_buy_times(self, packet):
        return None

    
    # CS_ARENA_PICK_DAY_REWARD
    @CallbackBase.callback(OP_CODE.CS_ARENA_PICK_DAY_REWARD)
    def send_arena_pick_day_reward_decorate(self, code):
        packet = cs_arena_pick_day_reward()
        self.make_arena_pick_day_reward_packet(packet)
        self.mes_que[code] = packet
    # makeup arena_pick_day_reward packet
    def make_arena_pick_day_reward_packet(self, packet):
        return None
    # send arena_pick_day_reward
    def send_arena_pick_day_reward(self):
        self.dispatch(OP_CODE.CS_ARENA_PICK_DAY_REWARD)(OP_CODE.CS_ARENA_PICK_DAY_REWARD)
    
    # handle SC_ARENA_PICK_DAY_REWARD
    @CallbackBase.callback(OP_CODE.SC_ARENA_PICK_DAY_REWARD)
    def handle_arena_pick_day_reward_decorate(self, recv_buff):
        packet = sc_arena_pick_day_reward()
        packet.deserialize(recv_buff)
        return self.handle_arena_pick_day_reward(packet)    
    def handle_arena_pick_day_reward(self, packet):
        return None

    
    # CS_ARENA_PICK_SEASON_REWARD
    @CallbackBase.callback(OP_CODE.CS_ARENA_PICK_SEASON_REWARD)
    def send_arena_pick_season_reward_decorate(self, code):
        packet = cs_arena_pick_season_reward()
        self.make_arena_pick_season_reward_packet(packet)
        self.mes_que[code] = packet
    # makeup arena_pick_season_reward packet
    def make_arena_pick_season_reward_packet(self, packet):
        return None
    # send arena_pick_season_reward
    def send_arena_pick_season_reward(self):
        self.dispatch(OP_CODE.CS_ARENA_PICK_SEASON_REWARD)(OP_CODE.CS_ARENA_PICK_SEASON_REWARD)
    
    # handle SC_ARENA_PICK_SEASON_REWARD
    @CallbackBase.callback(OP_CODE.SC_ARENA_PICK_SEASON_REWARD)
    def handle_arena_pick_season_reward_decorate(self, recv_buff):
        packet = sc_arena_pick_season_reward()
        packet.deserialize(recv_buff)
        return self.handle_arena_pick_season_reward(packet)    
    def handle_arena_pick_season_reward(self, packet):
        return None

    
    # CS_ARENA_BATTLE_RECORD_LIST
    @CallbackBase.callback(OP_CODE.CS_ARENA_BATTLE_RECORD_LIST)
    def send_arena_battle_record_list_decorate(self, code):
        packet = cs_arena_battle_record_list()
        self.make_arena_battle_record_list_packet(packet)
        self.mes_que[code] = packet
    # makeup arena_battle_record_list packet
    def make_arena_battle_record_list_packet(self, packet):
        return None
    # send arena_battle_record_list
    def send_arena_battle_record_list(self):
        self.dispatch(OP_CODE.CS_ARENA_BATTLE_RECORD_LIST)(OP_CODE.CS_ARENA_BATTLE_RECORD_LIST)
    
    # handle SC_ARENA_BATTLE_RECORD_LIST
    @CallbackBase.callback(OP_CODE.SC_ARENA_BATTLE_RECORD_LIST)
    def handle_arena_battle_record_list_decorate(self, recv_buff):
        packet = sc_arena_battle_record_list()
        packet.deserialize(recv_buff)
        return self.handle_arena_battle_record_list(packet)    
    def handle_arena_battle_record_list(self, packet):
        return None

    
    # CS_GET_TOWER_INFO
    @CallbackBase.callback(OP_CODE.CS_GET_TOWER_INFO)
    def send_get_tower_info_decorate(self, code):
        packet = cs_get_tower_info()
        self.make_get_tower_info_packet(packet)
        self.mes_que[code] = packet
    # makeup get_tower_info packet
    def make_get_tower_info_packet(self, packet):
        return None
    # send get_tower_info
    def send_get_tower_info(self):
        self.dispatch(OP_CODE.CS_GET_TOWER_INFO)(OP_CODE.CS_GET_TOWER_INFO)
    
    # handle SC_GET_TOWER_INFO
    @CallbackBase.callback(OP_CODE.SC_GET_TOWER_INFO)
    def handle_get_tower_info_decorate(self, recv_buff):
        packet = sc_get_tower_info()
        packet.deserialize(recv_buff)
        return self.handle_get_tower_info(packet)    
    def handle_get_tower_info(self, packet):
        return None

    
    # CS_GET_TOWER_FLOOR_INFO
    @CallbackBase.callback(OP_CODE.CS_GET_TOWER_FLOOR_INFO)
    def send_get_tower_floor_info_decorate(self, code):
        packet = cs_get_tower_floor_info()
        self.make_get_tower_floor_info_packet(packet)
        self.mes_que[code] = packet
    # makeup get_tower_floor_info packet
    def make_get_tower_floor_info_packet(self, packet):
        return None
    # send get_tower_floor_info
    def send_get_tower_floor_info(self):
        self.dispatch(OP_CODE.CS_GET_TOWER_FLOOR_INFO)(OP_CODE.CS_GET_TOWER_FLOOR_INFO)
    
    # handle SC_GET_TOWER_FLOOR_INFO
    @CallbackBase.callback(OP_CODE.SC_GET_TOWER_FLOOR_INFO)
    def handle_get_tower_floor_info_decorate(self, recv_buff):
        packet = sc_get_tower_floor_info()
        packet.deserialize(recv_buff)
        return self.handle_get_tower_floor_info(packet)    
    def handle_get_tower_floor_info(self, packet):
        return None

    
    # CS_TOWER_FLOOR_TRIAL
    @CallbackBase.callback(OP_CODE.CS_TOWER_FLOOR_TRIAL)
    def send_tower_floor_trial_decorate(self, code):
        packet = cs_tower_floor_trial()
        self.make_tower_floor_trial_packet(packet)
        self.mes_que[code] = packet
    # makeup tower_floor_trial packet
    def make_tower_floor_trial_packet(self, packet):
        return None
    # send tower_floor_trial
    def send_tower_floor_trial(self):
        self.dispatch(OP_CODE.CS_TOWER_FLOOR_TRIAL)(OP_CODE.CS_TOWER_FLOOR_TRIAL)
    
    # handle SC_TOWER_FLOOR_TRIAL
    @CallbackBase.callback(OP_CODE.SC_TOWER_FLOOR_TRIAL)
    def handle_tower_floor_trial_decorate(self, recv_buff):
        packet = sc_tower_floor_trial()
        packet.deserialize(recv_buff)
        return self.handle_tower_floor_trial(packet)    
    def handle_tower_floor_trial(self, packet):
        return None

    
    # CS_USER_SHOP_INFO
    @CallbackBase.callback(OP_CODE.CS_USER_SHOP_INFO)
    def send_user_shop_info_decorate(self, code):
        packet = cs_user_shop_info()
        self.make_user_shop_info_packet(packet)
        self.mes_que[code] = packet
    # makeup user_shop_info packet
    def make_user_shop_info_packet(self, packet):
        return None
    # send user_shop_info
    def send_user_shop_info(self):
        self.dispatch(OP_CODE.CS_USER_SHOP_INFO)(OP_CODE.CS_USER_SHOP_INFO)
    
    # handle SC_USER_SHOP_INFO
    @CallbackBase.callback(OP_CODE.SC_USER_SHOP_INFO)
    def handle_user_shop_info_decorate(self, recv_buff):
        packet = sc_user_shop_info()
        packet.deserialize(recv_buff)
        return self.handle_user_shop_info(packet)    
    def handle_user_shop_info(self, packet):
        return None

    
    # CS_USER_SHOP_BUY
    @CallbackBase.callback(OP_CODE.CS_USER_SHOP_BUY)
    def send_user_shop_buy_decorate(self, code):
        packet = cs_user_shop_buy()
        self.make_user_shop_buy_packet(packet)
        self.mes_que[code] = packet
    # makeup user_shop_buy packet
    def make_user_shop_buy_packet(self, packet):
        return None
    # send user_shop_buy
    def send_user_shop_buy(self):
        self.dispatch(OP_CODE.CS_USER_SHOP_BUY)(OP_CODE.CS_USER_SHOP_BUY)
    
    # handle SC_USER_SHOP_BUY
    @CallbackBase.callback(OP_CODE.SC_USER_SHOP_BUY)
    def handle_user_shop_buy_decorate(self, recv_buff):
        packet = sc_user_shop_buy()
        packet.deserialize(recv_buff)
        return self.handle_user_shop_buy(packet)    
    def handle_user_shop_buy(self, packet):
        return None

    
    # CS_USER_SHOP_REFRESH
    @CallbackBase.callback(OP_CODE.CS_USER_SHOP_REFRESH)
    def send_user_shop_refresh_decorate(self, code):
        packet = cs_user_shop_refresh()
        self.make_user_shop_refresh_packet(packet)
        self.mes_que[code] = packet
    # makeup user_shop_refresh packet
    def make_user_shop_refresh_packet(self, packet):
        return None
    # send user_shop_refresh
    def send_user_shop_refresh(self):
        self.dispatch(OP_CODE.CS_USER_SHOP_REFRESH)(OP_CODE.CS_USER_SHOP_REFRESH)
    
    # handle SC_USER_SHOP_REFRESH
    @CallbackBase.callback(OP_CODE.SC_USER_SHOP_REFRESH)
    def handle_user_shop_refresh_decorate(self, recv_buff):
        packet = sc_user_shop_refresh()
        packet.deserialize(recv_buff)
        return self.handle_user_shop_refresh(packet)    
    def handle_user_shop_refresh(self, packet):
        return None

    
    # CS_USE_EXP_ITEM
    @CallbackBase.callback(OP_CODE.CS_USE_EXP_ITEM)
    def send_use_exp_item_decorate(self, code):
        packet = cs_use_exp_item()
        self.make_use_exp_item_packet(packet)
        self.mes_que[code] = packet
    # makeup use_exp_item packet
    def make_use_exp_item_packet(self, packet):
        return None
    # send use_exp_item
    def send_use_exp_item(self):
        self.dispatch(OP_CODE.CS_USE_EXP_ITEM)(OP_CODE.CS_USE_EXP_ITEM)
    
    # handle SC_USE_EXP_ITEM
    @CallbackBase.callback(OP_CODE.SC_USE_EXP_ITEM)
    def handle_use_exp_item_decorate(self, recv_buff):
        packet = sc_use_exp_item()
        packet.deserialize(recv_buff)
        return self.handle_use_exp_item(packet)    
    def handle_use_exp_item(self, packet):
        return None

    
    # CS_TOWER_FLOOR_REPORT
    @CallbackBase.callback(OP_CODE.CS_TOWER_FLOOR_REPORT)
    def send_tower_floor_report_decorate(self, code):
        packet = cs_tower_floor_report()
        self.make_tower_floor_report_packet(packet)
        self.mes_que[code] = packet
    # makeup tower_floor_report packet
    def make_tower_floor_report_packet(self, packet):
        return None
    # send tower_floor_report
    def send_tower_floor_report(self):
        self.dispatch(OP_CODE.CS_TOWER_FLOOR_REPORT)(OP_CODE.CS_TOWER_FLOOR_REPORT)
    
    # handle SC_TOWER_FLOOR_REPORT
    @CallbackBase.callback(OP_CODE.SC_TOWER_FLOOR_REPORT)
    def handle_tower_floor_report_decorate(self, recv_buff):
        packet = sc_tower_floor_report()
        packet.deserialize(recv_buff)
        return self.handle_tower_floor_report(packet)    
    def handle_tower_floor_report(self, packet):
        return None

    
    # CS_GET_STATE_STATUS
    @CallbackBase.callback(OP_CODE.CS_GET_STATE_STATUS)
    def send_get_state_status_decorate(self, code):
        packet = cs_get_state_status()
        self.make_get_state_status_packet(packet)
        self.mes_que[code] = packet
    # makeup get_state_status packet
    def make_get_state_status_packet(self, packet):
        return None
    # send get_state_status
    def send_get_state_status(self):
        self.dispatch(OP_CODE.CS_GET_STATE_STATUS)(OP_CODE.CS_GET_STATE_STATUS)
    
    # handle SC_GET_STATE_STATUS
    @CallbackBase.callback(OP_CODE.SC_GET_STATE_STATUS)
    def handle_get_state_status_decorate(self, recv_buff):
        packet = sc_get_state_status()
        packet.deserialize(recv_buff)
        return self.handle_get_state_status(packet)    
    def handle_get_state_status(self, packet):
        return None

    
    # CS_GET_NEWBIE_ZHAOYU
    @CallbackBase.callback(OP_CODE.CS_GET_NEWBIE_ZHAOYU)
    def send_get_newbie_zhaoyu_decorate(self, code):
        packet = cs_get_newbie_zhaoyu()
        self.make_get_newbie_zhaoyu_packet(packet)
        self.mes_que[code] = packet
    # makeup get_newbie_zhaoyu packet
    def make_get_newbie_zhaoyu_packet(self, packet):
        return None
    # send get_newbie_zhaoyu
    def send_get_newbie_zhaoyu(self):
        self.dispatch(OP_CODE.CS_GET_NEWBIE_ZHAOYU)(OP_CODE.CS_GET_NEWBIE_ZHAOYU)
    
    # handle SC_GET_NEWBIE_ZHAOYU
    @CallbackBase.callback(OP_CODE.SC_GET_NEWBIE_ZHAOYU)
    def handle_get_newbie_zhaoyu_decorate(self, recv_buff):
        packet = sc_get_newbie_zhaoyu()
        packet.deserialize(recv_buff)
        return self.handle_get_newbie_zhaoyu(packet)    
    def handle_get_newbie_zhaoyu(self, packet):
        return None

    
    # CS_SET_NEWBIE_ZHAOYU
    @CallbackBase.callback(OP_CODE.CS_SET_NEWBIE_ZHAOYU)
    def send_set_newbie_zhaoyu_decorate(self, code):
        packet = cs_set_newbie_zhaoyu()
        self.make_set_newbie_zhaoyu_packet(packet)
        self.mes_que[code] = packet
    # makeup set_newbie_zhaoyu packet
    def make_set_newbie_zhaoyu_packet(self, packet):
        return None
    # send set_newbie_zhaoyu
    def send_set_newbie_zhaoyu(self):
        self.dispatch(OP_CODE.CS_SET_NEWBIE_ZHAOYU)(OP_CODE.CS_SET_NEWBIE_ZHAOYU)
    
    # handle SC_SET_NEWBIE_ZHAOYU
    @CallbackBase.callback(OP_CODE.SC_SET_NEWBIE_ZHAOYU)
    def handle_set_newbie_zhaoyu_decorate(self, recv_buff):
        packet = sc_set_newbie_zhaoyu()
        packet.deserialize(recv_buff)
        return self.handle_set_newbie_zhaoyu(packet)    
    def handle_set_newbie_zhaoyu(self, packet):
        return None

    
    # CS_PICK_GIFT
    @CallbackBase.callback(OP_CODE.CS_PICK_GIFT)
    def send_pick_gift_decorate(self, code):
        packet = cs_pick_gift()
        self.make_pick_gift_packet(packet)
        self.mes_que[code] = packet
    # makeup pick_gift packet
    def make_pick_gift_packet(self, packet):
        return None
    # send pick_gift
    def send_pick_gift(self):
        self.dispatch(OP_CODE.CS_PICK_GIFT)(OP_CODE.CS_PICK_GIFT)
    
    # handle SC_PICK_GIFT
    @CallbackBase.callback(OP_CODE.SC_PICK_GIFT)
    def handle_pick_gift_decorate(self, recv_buff):
        packet = sc_pick_gift()
        packet.deserialize(recv_buff)
        return self.handle_pick_gift(packet)    
    def handle_pick_gift(self, packet):
        return None

    
    # CS_SHARE_REPORT
    @CallbackBase.callback(OP_CODE.CS_SHARE_REPORT)
    def send_share_report_decorate(self, code):
        packet = cs_share_report()
        self.make_share_report_packet(packet)
        self.mes_que[code] = packet
    # makeup share_report packet
    def make_share_report_packet(self, packet):
        return None
    # send share_report
    def send_share_report(self):
        self.dispatch(OP_CODE.CS_SHARE_REPORT)(OP_CODE.CS_SHARE_REPORT)
    
    # handle SC_SHARE_REPORT
    @CallbackBase.callback(OP_CODE.SC_SHARE_REPORT)
    def handle_share_report_decorate(self, recv_buff):
        packet = sc_share_report()
        packet.deserialize(recv_buff)
        return self.handle_share_report(packet)    
    def handle_share_report(self, packet):
        return None

    
    # CS_GET_ARENA_RECORD
    @CallbackBase.callback(OP_CODE.CS_GET_ARENA_RECORD)
    def send_get_arena_record_decorate(self, code):
        packet = cs_get_arena_record()
        self.make_get_arena_record_packet(packet)
        self.mes_que[code] = packet
    # makeup get_arena_record packet
    def make_get_arena_record_packet(self, packet):
        return None
    # send get_arena_record
    def send_get_arena_record(self):
        self.dispatch(OP_CODE.CS_GET_ARENA_RECORD)(OP_CODE.CS_GET_ARENA_RECORD)
    
    # handle SC_GET_ARENA_RECORD
    @CallbackBase.callback(OP_CODE.SC_GET_ARENA_RECORD)
    def handle_get_arena_record_decorate(self, recv_buff):
        packet = sc_get_arena_record()
        packet.deserialize(recv_buff)
        return self.handle_get_arena_record(packet)    
    def handle_get_arena_record(self, packet):
        return None

    
    # CS_MATCH_DATA_REQ
    @CallbackBase.callback(OP_CODE.CS_MATCH_DATA_REQ)
    def send_match_data_req_decorate(self, code):
        packet = cs_match_data_req()
        self.make_match_data_req_packet(packet)
        self.mes_que[code] = packet
    # makeup match_data_req packet
    def make_match_data_req_packet(self, packet):
        return None
    # send match_data_req
    def send_match_data_req(self):
        self.dispatch(OP_CODE.CS_MATCH_DATA_REQ)(OP_CODE.CS_MATCH_DATA_REQ)
    
    # handle SC_MATCH_DATA_REQ
    @CallbackBase.callback(OP_CODE.SC_MATCH_DATA_REQ)
    def handle_match_data_req_decorate(self, recv_buff):
        packet = sc_match_data_req()
        packet.deserialize(recv_buff)
        return self.handle_match_data_req(packet)    
    def handle_match_data_req(self, packet):
        return None

    
    # CS_MATCH_SET_FORMATION
    @CallbackBase.callback(OP_CODE.CS_MATCH_SET_FORMATION)
    def send_match_set_formation_decorate(self, code):
        packet = cs_match_set_formation()
        self.make_match_set_formation_packet(packet)
        self.mes_que[code] = packet
    # makeup match_set_formation packet
    def make_match_set_formation_packet(self, packet):
        return None
    # send match_set_formation
    def send_match_set_formation(self):
        self.dispatch(OP_CODE.CS_MATCH_SET_FORMATION)(OP_CODE.CS_MATCH_SET_FORMATION)
    
    # handle SC_MATCH_SET_FORMATION
    @CallbackBase.callback(OP_CODE.SC_MATCH_SET_FORMATION)
    def handle_match_set_formation_decorate(self, recv_buff):
        packet = sc_match_set_formation()
        packet.deserialize(recv_buff)
        return self.handle_match_set_formation(packet)    
    def handle_match_set_formation(self, packet):
        return None

    
    # CS_MATCH_RANK_REQ
    @CallbackBase.callback(OP_CODE.CS_MATCH_RANK_REQ)
    def send_match_rank_req_decorate(self, code):
        packet = cs_match_rank_req()
        self.make_match_rank_req_packet(packet)
        self.mes_que[code] = packet
    # makeup match_rank_req packet
    def make_match_rank_req_packet(self, packet):
        return None
    # send match_rank_req
    def send_match_rank_req(self):
        self.dispatch(OP_CODE.CS_MATCH_RANK_REQ)(OP_CODE.CS_MATCH_RANK_REQ)
    
    # handle SC_MATCH_RANK_REQ
    @CallbackBase.callback(OP_CODE.SC_MATCH_RANK_REQ)
    def handle_match_rank_req_decorate(self, recv_buff):
        packet = sc_match_rank_req()
        packet.deserialize(recv_buff)
        return self.handle_match_rank_req(packet)    
    def handle_match_rank_req(self, packet):
        return None

    
    # CS_MATCH_FIGHT
    @CallbackBase.callback(OP_CODE.CS_MATCH_FIGHT)
    def send_match_fight_decorate(self, code):
        packet = cs_match_fight()
        self.make_match_fight_packet(packet)
        self.mes_que[code] = packet
    # makeup match_fight packet
    def make_match_fight_packet(self, packet):
        return None
    # send match_fight
    def send_match_fight(self):
        self.dispatch(OP_CODE.CS_MATCH_FIGHT)(OP_CODE.CS_MATCH_FIGHT)
    
    # handle SC_MATCH_FIGHT
    @CallbackBase.callback(OP_CODE.SC_MATCH_FIGHT)
    def handle_match_fight_decorate(self, recv_buff):
        packet = sc_match_fight()
        packet.deserialize(recv_buff)
        return self.handle_match_fight(packet)    
    def handle_match_fight(self, packet):
        return None

    
    # CS_GET_MATCH_RECORD
    @CallbackBase.callback(OP_CODE.CS_GET_MATCH_RECORD)
    def send_get_match_record_decorate(self, code):
        packet = cs_get_match_record()
        self.make_get_match_record_packet(packet)
        self.mes_que[code] = packet
    # makeup get_match_record packet
    def make_get_match_record_packet(self, packet):
        return None
    # send get_match_record
    def send_get_match_record(self):
        self.dispatch(OP_CODE.CS_GET_MATCH_RECORD)(OP_CODE.CS_GET_MATCH_RECORD)
    
    # handle SC_GET_MATCH_RECORD
    @CallbackBase.callback(OP_CODE.SC_GET_MATCH_RECORD)
    def handle_get_match_record_decorate(self, recv_buff):
        packet = sc_get_match_record()
        packet.deserialize(recv_buff)
        return self.handle_get_match_record(packet)    
    def handle_get_match_record(self, packet):
        return None

    
    # CS_MATCH_BATTLE_RECORD_LIST
    @CallbackBase.callback(OP_CODE.CS_MATCH_BATTLE_RECORD_LIST)
    def send_match_battle_record_list_decorate(self, code):
        packet = cs_match_battle_record_list()
        self.make_match_battle_record_list_packet(packet)
        self.mes_que[code] = packet
    # makeup match_battle_record_list packet
    def make_match_battle_record_list_packet(self, packet):
        return None
    # send match_battle_record_list
    def send_match_battle_record_list(self):
        self.dispatch(OP_CODE.CS_MATCH_BATTLE_RECORD_LIST)(OP_CODE.CS_MATCH_BATTLE_RECORD_LIST)
    
    # handle SC_MATCH_BATTLE_RECORD_LIST
    @CallbackBase.callback(OP_CODE.SC_MATCH_BATTLE_RECORD_LIST)
    def handle_match_battle_record_list_decorate(self, recv_buff):
        packet = sc_match_battle_record_list()
        packet.deserialize(recv_buff)
        return self.handle_match_battle_record_list(packet)    
    def handle_match_battle_record_list(self, packet):
        return None

    
    # CS_MATCH_REFRESH_ENEMY_REQ
    @CallbackBase.callback(OP_CODE.CS_MATCH_REFRESH_ENEMY_REQ)
    def send_match_refresh_enemy_req_decorate(self, code):
        packet = cs_match_refresh_enemy_req()
        self.make_match_refresh_enemy_req_packet(packet)
        self.mes_que[code] = packet
    # makeup match_refresh_enemy_req packet
    def make_match_refresh_enemy_req_packet(self, packet):
        return None
    # send match_refresh_enemy_req
    def send_match_refresh_enemy_req(self):
        self.dispatch(OP_CODE.CS_MATCH_REFRESH_ENEMY_REQ)(OP_CODE.CS_MATCH_REFRESH_ENEMY_REQ)
    
    # handle SC_MATCH_REFRESH_ENEMY_REQ
    @CallbackBase.callback(OP_CODE.SC_MATCH_REFRESH_ENEMY_REQ)
    def handle_match_refresh_enemy_req_decorate(self, recv_buff):
        packet = sc_match_refresh_enemy_req()
        packet.deserialize(recv_buff)
        return self.handle_match_refresh_enemy_req(packet)    
    def handle_match_refresh_enemy_req(self, packet):
        return None

    
    # CS_MATCH_BUY_TIMES
    @CallbackBase.callback(OP_CODE.CS_MATCH_BUY_TIMES)
    def send_match_buy_times_decorate(self, code):
        packet = cs_match_buy_times()
        self.make_match_buy_times_packet(packet)
        self.mes_que[code] = packet
    # makeup match_buy_times packet
    def make_match_buy_times_packet(self, packet):
        return None
    # send match_buy_times
    def send_match_buy_times(self):
        self.dispatch(OP_CODE.CS_MATCH_BUY_TIMES)(OP_CODE.CS_MATCH_BUY_TIMES)
    
    # handle SC_MATCH_BUY_TIMES
    @CallbackBase.callback(OP_CODE.SC_MATCH_BUY_TIMES)
    def handle_match_buy_times_decorate(self, recv_buff):
        packet = sc_match_buy_times()
        packet.deserialize(recv_buff)
        return self.handle_match_buy_times(packet)    
    def handle_match_buy_times(self, packet):
        return None

    
    # CS_BATTLE_FOR_CP
    @CallbackBase.callback(OP_CODE.CS_BATTLE_FOR_CP)
    def send_battle_for_cp_decorate(self, code):
        packet = cs_battle_for_cp()
        self.make_battle_for_cp_packet(packet)
        self.mes_que[code] = packet
    # makeup battle_for_cp packet
    def make_battle_for_cp_packet(self, packet):
        return None
    # send battle_for_cp
    def send_battle_for_cp(self):
        self.dispatch(OP_CODE.CS_BATTLE_FOR_CP)(OP_CODE.CS_BATTLE_FOR_CP)
    
    # handle SC_BATTLE_FOR_CP
    @CallbackBase.callback(OP_CODE.SC_BATTLE_FOR_CP)
    def handle_battle_for_cp_decorate(self, recv_buff):
        packet = sc_battle_for_cp()
        packet.deserialize(recv_buff)
        return self.handle_battle_for_cp(packet)    
    def handle_battle_for_cp(self, packet):
        return None

    
    # CS_GET_TOWER_FLOOR_REWARD
    @CallbackBase.callback(OP_CODE.CS_GET_TOWER_FLOOR_REWARD)
    def send_get_tower_floor_reward_decorate(self, code):
        packet = cs_get_tower_floor_reward()
        self.make_get_tower_floor_reward_packet(packet)
        self.mes_que[code] = packet
    # makeup get_tower_floor_reward packet
    def make_get_tower_floor_reward_packet(self, packet):
        return None
    # send get_tower_floor_reward
    def send_get_tower_floor_reward(self):
        self.dispatch(OP_CODE.CS_GET_TOWER_FLOOR_REWARD)(OP_CODE.CS_GET_TOWER_FLOOR_REWARD)
    
    # handle SC_GET_TOWER_FLOOR_REWARD
    @CallbackBase.callback(OP_CODE.SC_GET_TOWER_FLOOR_REWARD)
    def handle_get_tower_floor_reward_decorate(self, recv_buff):
        packet = sc_get_tower_floor_reward()
        packet.deserialize(recv_buff)
        return self.handle_get_tower_floor_reward(packet)    
    def handle_get_tower_floor_reward(self, packet):
        return None

    
    # CS_GET_STORAGE_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_STORAGE_LIST)
    def send_get_storage_list_decorate(self, code):
        packet = cs_get_storage_list()
        self.make_get_storage_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_storage_list packet
    def make_get_storage_list_packet(self, packet):
        return None
    # send get_storage_list
    def send_get_storage_list(self):
        self.dispatch(OP_CODE.CS_GET_STORAGE_LIST)(OP_CODE.CS_GET_STORAGE_LIST)
    
    # handle SC_GET_STORAGE_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_STORAGE_LIST)
    def handle_get_storage_list_decorate(self, recv_buff):
        packet = sc_get_storage_list()
        packet.deserialize(recv_buff)
        return self.handle_get_storage_list(packet)    
    def handle_get_storage_list(self, packet):
        return None

    
    # CS_TOWER_HANGUP_SEND
    @CallbackBase.callback(OP_CODE.CS_TOWER_HANGUP_SEND)
    def send_tower_hangup_send_decorate(self, code):
        packet = cs_tower_hangup_send()
        self.make_tower_hangup_send_packet(packet)
        self.mes_que[code] = packet
    # makeup tower_hangup_send packet
    def make_tower_hangup_send_packet(self, packet):
        return None
    # send tower_hangup_send
    def send_tower_hangup_send(self):
        self.dispatch(OP_CODE.CS_TOWER_HANGUP_SEND)(OP_CODE.CS_TOWER_HANGUP_SEND)
    
    # handle SC_TOWER_HANGUP_SEND
    @CallbackBase.callback(OP_CODE.SC_TOWER_HANGUP_SEND)
    def handle_tower_hangup_send_decorate(self, recv_buff):
        packet = sc_tower_hangup_send()
        packet.deserialize(recv_buff)
        return self.handle_tower_hangup_send(packet)    
    def handle_tower_hangup_send(self, packet):
        return None

    
    # CS_TOWER_HANGUP_REWARD
    @CallbackBase.callback(OP_CODE.CS_TOWER_HANGUP_REWARD)
    def send_tower_hangup_reward_decorate(self, code):
        packet = cs_tower_hangup_reward()
        self.make_tower_hangup_reward_packet(packet)
        self.mes_que[code] = packet
    # makeup tower_hangup_reward packet
    def make_tower_hangup_reward_packet(self, packet):
        return None
    # send tower_hangup_reward
    def send_tower_hangup_reward(self):
        self.dispatch(OP_CODE.CS_TOWER_HANGUP_REWARD)(OP_CODE.CS_TOWER_HANGUP_REWARD)
    
    # handle SC_TOWER_HANGUP_REWARD
    @CallbackBase.callback(OP_CODE.SC_TOWER_HANGUP_REWARD)
    def handle_tower_hangup_reward_decorate(self, recv_buff):
        packet = sc_tower_hangup_reward()
        packet.deserialize(recv_buff)
        return self.handle_tower_hangup_reward(packet)    
    def handle_tower_hangup_reward(self, packet):
        return None

    
    # CS_TOWER_HANGUP_STOP
    @CallbackBase.callback(OP_CODE.CS_TOWER_HANGUP_STOP)
    def send_tower_hangup_stop_decorate(self, code):
        packet = cs_tower_hangup_stop()
        self.make_tower_hangup_stop_packet(packet)
        self.mes_que[code] = packet
    # makeup tower_hangup_stop packet
    def make_tower_hangup_stop_packet(self, packet):
        return None
    # send tower_hangup_stop
    def send_tower_hangup_stop(self):
        self.dispatch(OP_CODE.CS_TOWER_HANGUP_STOP)(OP_CODE.CS_TOWER_HANGUP_STOP)
    
    # handle SC_TOWER_HANGUP_STOP
    @CallbackBase.callback(OP_CODE.SC_TOWER_HANGUP_STOP)
    def handle_tower_hangup_stop_decorate(self, recv_buff):
        packet = sc_tower_hangup_stop()
        packet.deserialize(recv_buff)
        return self.handle_tower_hangup_stop(packet)    
    def handle_tower_hangup_stop(self, packet):
        return None

    
    # CS_EQUIP_MAKE
    @CallbackBase.callback(OP_CODE.CS_EQUIP_MAKE)
    def send_equip_make_decorate(self, code):
        packet = cs_equip_make()
        self.make_equip_make_packet(packet)
        self.mes_que[code] = packet
    # makeup equip_make packet
    def make_equip_make_packet(self, packet):
        return None
    # send equip_make
    def send_equip_make(self):
        self.dispatch(OP_CODE.CS_EQUIP_MAKE)(OP_CODE.CS_EQUIP_MAKE)
    
    # handle SC_EQUIP_MAKE
    @CallbackBase.callback(OP_CODE.SC_EQUIP_MAKE)
    def handle_equip_make_decorate(self, recv_buff):
        packet = sc_equip_make()
        packet.deserialize(recv_buff)
        return self.handle_equip_make(packet)    
    def handle_equip_make(self, packet):
        return None

    
    # CS_GET_TOWER_RECORD
    @CallbackBase.callback(OP_CODE.CS_GET_TOWER_RECORD)
    def send_get_tower_record_decorate(self, code):
        packet = cs_get_tower_record()
        self.make_get_tower_record_packet(packet)
        self.mes_que[code] = packet
    # makeup get_tower_record packet
    def make_get_tower_record_packet(self, packet):
        return None
    # send get_tower_record
    def send_get_tower_record(self):
        self.dispatch(OP_CODE.CS_GET_TOWER_RECORD)(OP_CODE.CS_GET_TOWER_RECORD)
    
    # handle SC_GET_TOWER_RECORD
    @CallbackBase.callback(OP_CODE.SC_GET_TOWER_RECORD)
    def handle_get_tower_record_decorate(self, recv_buff):
        packet = sc_get_tower_record()
        packet.deserialize(recv_buff)
        return self.handle_get_tower_record(packet)    
    def handle_get_tower_record(self, packet):
        return None

    
    # CS_GET_TOWER_RANK
    @CallbackBase.callback(OP_CODE.CS_GET_TOWER_RANK)
    def send_get_tower_rank_decorate(self, code):
        packet = cs_get_tower_rank()
        self.make_get_tower_rank_packet(packet)
        self.mes_que[code] = packet
    # makeup get_tower_rank packet
    def make_get_tower_rank_packet(self, packet):
        return None
    # send get_tower_rank
    def send_get_tower_rank(self):
        self.dispatch(OP_CODE.CS_GET_TOWER_RANK)(OP_CODE.CS_GET_TOWER_RANK)
    
    # handle SC_GET_TOWER_RANK
    @CallbackBase.callback(OP_CODE.SC_GET_TOWER_RANK)
    def handle_get_tower_rank_decorate(self, recv_buff):
        packet = sc_get_tower_rank()
        packet.deserialize(recv_buff)
        return self.handle_get_tower_rank(packet)    
    def handle_get_tower_rank(self, packet):
        return None

    
    # CS_TOWER_BATTLE_RECORD_LIST
    @CallbackBase.callback(OP_CODE.CS_TOWER_BATTLE_RECORD_LIST)
    def send_tower_battle_record_list_decorate(self, code):
        packet = cs_tower_battle_record_list()
        self.make_tower_battle_record_list_packet(packet)
        self.mes_que[code] = packet
    # makeup tower_battle_record_list packet
    def make_tower_battle_record_list_packet(self, packet):
        return None
    # send tower_battle_record_list
    def send_tower_battle_record_list(self):
        self.dispatch(OP_CODE.CS_TOWER_BATTLE_RECORD_LIST)(OP_CODE.CS_TOWER_BATTLE_RECORD_LIST)
    
    # handle SC_TOWER_BATTLE_RECORD_LIST
    @CallbackBase.callback(OP_CODE.SC_TOWER_BATTLE_RECORD_LIST)
    def handle_tower_battle_record_list_decorate(self, recv_buff):
        packet = sc_tower_battle_record_list()
        packet.deserialize(recv_buff)
        return self.handle_tower_battle_record_list(packet)    
    def handle_tower_battle_record_list(self, packet):
        return None

    
    # CS_GET_GUILD_COMMAND
    @CallbackBase.callback(OP_CODE.CS_GET_GUILD_COMMAND)
    def send_get_guild_command_decorate(self, code):
        packet = cs_get_guild_command()
        self.make_get_guild_command_packet(packet)
        self.mes_que[code] = packet
    # makeup get_guild_command packet
    def make_get_guild_command_packet(self, packet):
        return None
    # send get_guild_command
    def send_get_guild_command(self):
        self.dispatch(OP_CODE.CS_GET_GUILD_COMMAND)(OP_CODE.CS_GET_GUILD_COMMAND)
    
    # handle SC_GET_GUILD_COMMAND
    @CallbackBase.callback(OP_CODE.SC_GET_GUILD_COMMAND)
    def handle_get_guild_command_decorate(self, recv_buff):
        packet = sc_get_guild_command()
        packet.deserialize(recv_buff)
        return self.handle_get_guild_command(packet)    
    def handle_get_guild_command(self, packet):
        return None

    
    # CS_BUY_GUILD_COMMAND
    @CallbackBase.callback(OP_CODE.CS_BUY_GUILD_COMMAND)
    def send_buy_guild_command_decorate(self, code):
        packet = cs_buy_guild_command()
        self.make_buy_guild_command_packet(packet)
        self.mes_que[code] = packet
    # makeup buy_guild_command packet
    def make_buy_guild_command_packet(self, packet):
        return None
    # send buy_guild_command
    def send_buy_guild_command(self):
        self.dispatch(OP_CODE.CS_BUY_GUILD_COMMAND)(OP_CODE.CS_BUY_GUILD_COMMAND)
    
    # handle SC_BUY_GUILD_COMMAND
    @CallbackBase.callback(OP_CODE.SC_BUY_GUILD_COMMAND)
    def handle_buy_guild_command_decorate(self, recv_buff):
        packet = sc_buy_guild_command()
        packet.deserialize(recv_buff)
        return self.handle_buy_guild_command(packet)    
    def handle_buy_guild_command(self, packet):
        return None

    
    # CS_ADD_GUILD_COMMAND
    @CallbackBase.callback(OP_CODE.CS_ADD_GUILD_COMMAND)
    def send_add_guild_command_decorate(self, code):
        packet = cs_add_guild_command()
        self.make_add_guild_command_packet(packet)
        self.mes_que[code] = packet
    # makeup add_guild_command packet
    def make_add_guild_command_packet(self, packet):
        return None
    # send add_guild_command
    def send_add_guild_command(self):
        self.dispatch(OP_CODE.CS_ADD_GUILD_COMMAND)(OP_CODE.CS_ADD_GUILD_COMMAND)
    
    # handle SC_ADD_GUILD_COMMAND
    @CallbackBase.callback(OP_CODE.SC_ADD_GUILD_COMMAND)
    def handle_add_guild_command_decorate(self, recv_buff):
        packet = sc_add_guild_command()
        packet.deserialize(recv_buff)
        return self.handle_add_guild_command(packet)    
    def handle_add_guild_command(self, packet):
        return None

    
    # CS_DEL_GUILD_COMMAND
    @CallbackBase.callback(OP_CODE.CS_DEL_GUILD_COMMAND)
    def send_del_guild_command_decorate(self, code):
        packet = cs_del_guild_command()
        self.make_del_guild_command_packet(packet)
        self.mes_que[code] = packet
    # makeup del_guild_command packet
    def make_del_guild_command_packet(self, packet):
        return None
    # send del_guild_command
    def send_del_guild_command(self):
        self.dispatch(OP_CODE.CS_DEL_GUILD_COMMAND)(OP_CODE.CS_DEL_GUILD_COMMAND)
    
    # handle SC_DEL_GUILD_COMMAND
    @CallbackBase.callback(OP_CODE.SC_DEL_GUILD_COMMAND)
    def handle_del_guild_command_decorate(self, recv_buff):
        packet = sc_del_guild_command()
        packet.deserialize(recv_buff)
        return self.handle_del_guild_command(packet)    
    def handle_del_guild_command(self, packet):
        return None

    
    # CS_GET_PLOT_QUEST_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_PLOT_QUEST_LIST)
    def send_get_plot_quest_list_decorate(self, code):
        packet = cs_get_plot_quest_list()
        self.make_get_plot_quest_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_plot_quest_list packet
    def make_get_plot_quest_list_packet(self, packet):
        return None
    # send get_plot_quest_list
    def send_get_plot_quest_list(self):
        self.dispatch(OP_CODE.CS_GET_PLOT_QUEST_LIST)(OP_CODE.CS_GET_PLOT_QUEST_LIST)
    
    # handle SC_GET_PLOT_QUEST_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_PLOT_QUEST_LIST)
    def handle_get_plot_quest_list_decorate(self, recv_buff):
        packet = sc_get_plot_quest_list()
        packet.deserialize(recv_buff)
        return self.handle_get_plot_quest_list(packet)    
    def handle_get_plot_quest_list(self, packet):
        return None

    
    # CS_GET_PLOT_QUEST_REWARDS
    @CallbackBase.callback(OP_CODE.CS_GET_PLOT_QUEST_REWARDS)
    def send_get_plot_quest_rewards_decorate(self, code):
        packet = cs_get_plot_quest_rewards()
        self.make_get_plot_quest_rewards_packet(packet)
        self.mes_que[code] = packet
    # makeup get_plot_quest_rewards packet
    def make_get_plot_quest_rewards_packet(self, packet):
        return None
    # send get_plot_quest_rewards
    def send_get_plot_quest_rewards(self):
        self.dispatch(OP_CODE.CS_GET_PLOT_QUEST_REWARDS)(OP_CODE.CS_GET_PLOT_QUEST_REWARDS)
    
    # handle SC_GET_PLOT_QUEST_REWARDS
    @CallbackBase.callback(OP_CODE.SC_GET_PLOT_QUEST_REWARDS)
    def handle_get_plot_quest_rewards_decorate(self, recv_buff):
        packet = sc_get_plot_quest_rewards()
        packet.deserialize(recv_buff)
        return self.handle_get_plot_quest_rewards(packet)    
    def handle_get_plot_quest_rewards(self, packet):
        return None

    
    # CS_GET_ADVISE
    @CallbackBase.callback(OP_CODE.CS_GET_ADVISE)
    def send_get_advise_decorate(self, code):
        packet = cs_get_advise()
        self.make_get_advise_packet(packet)
        self.mes_que[code] = packet
    # makeup get_advise packet
    def make_get_advise_packet(self, packet):
        return None
    # send get_advise
    def send_get_advise(self):
        self.dispatch(OP_CODE.CS_GET_ADVISE)(OP_CODE.CS_GET_ADVISE)
    
    # handle SC_GET_ADVISE
    @CallbackBase.callback(OP_CODE.SC_GET_ADVISE)
    def handle_get_advise_decorate(self, recv_buff):
        packet = sc_get_advise()
        packet.deserialize(recv_buff)
        return self.handle_get_advise(packet)    
    def handle_get_advise(self, packet):
        return None

    
    # CS_GET_GUILD_QUEST_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_GUILD_QUEST_LIST)
    def send_get_guild_quest_list_decorate(self, code):
        packet = cs_get_guild_quest_list()
        self.make_get_guild_quest_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_guild_quest_list packet
    def make_get_guild_quest_list_packet(self, packet):
        return None
    # send get_guild_quest_list
    def send_get_guild_quest_list(self):
        self.dispatch(OP_CODE.CS_GET_GUILD_QUEST_LIST)(OP_CODE.CS_GET_GUILD_QUEST_LIST)
    
    # handle SC_GET_GUILD_QUEST_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_GUILD_QUEST_LIST)
    def handle_get_guild_quest_list_decorate(self, recv_buff):
        packet = sc_get_guild_quest_list()
        packet.deserialize(recv_buff)
        return self.handle_get_guild_quest_list(packet)    
    def handle_get_guild_quest_list(self, packet):
        return None

    
    # CS_GET_GUILD_QUEST_REWARDS
    @CallbackBase.callback(OP_CODE.CS_GET_GUILD_QUEST_REWARDS)
    def send_get_guild_quest_rewards_decorate(self, code):
        packet = cs_get_guild_quest_rewards()
        self.make_get_guild_quest_rewards_packet(packet)
        self.mes_que[code] = packet
    # makeup get_guild_quest_rewards packet
    def make_get_guild_quest_rewards_packet(self, packet):
        return None
    # send get_guild_quest_rewards
    def send_get_guild_quest_rewards(self):
        self.dispatch(OP_CODE.CS_GET_GUILD_QUEST_REWARDS)(OP_CODE.CS_GET_GUILD_QUEST_REWARDS)
    
    # handle SC_GET_GUILD_QUEST_REWARDS
    @CallbackBase.callback(OP_CODE.SC_GET_GUILD_QUEST_REWARDS)
    def handle_get_guild_quest_rewards_decorate(self, recv_buff):
        packet = sc_get_guild_quest_rewards()
        packet.deserialize(recv_buff)
        return self.handle_get_guild_quest_rewards(packet)    
    def handle_get_guild_quest_rewards(self, packet):
        return None

    
    # CS_HERO_SKILL_LVUP
    @CallbackBase.callback(OP_CODE.CS_HERO_SKILL_LVUP)
    def send_hero_skill_lvup_decorate(self, code):
        packet = cs_hero_skill_lvup()
        self.make_hero_skill_lvup_packet(packet)
        self.mes_que[code] = packet
    # makeup hero_skill_lvup packet
    def make_hero_skill_lvup_packet(self, packet):
        return None
    # send hero_skill_lvup
    def send_hero_skill_lvup(self):
        self.dispatch(OP_CODE.CS_HERO_SKILL_LVUP)(OP_CODE.CS_HERO_SKILL_LVUP)
    
    # handle SC_HERO_SKILL_LVUP
    @CallbackBase.callback(OP_CODE.SC_HERO_SKILL_LVUP)
    def handle_hero_skill_lvup_decorate(self, recv_buff):
        packet = sc_hero_skill_lvup()
        packet.deserialize(recv_buff)
        return self.handle_hero_skill_lvup(packet)    
    def handle_hero_skill_lvup(self, packet):
        return None

    
    # CS_CAL_HERO_POWER
    @CallbackBase.callback(OP_CODE.CS_CAL_HERO_POWER)
    def send_cal_hero_power_decorate(self, code):
        packet = cs_cal_hero_power()
        self.make_cal_hero_power_packet(packet)
        self.mes_que[code] = packet
    # makeup cal_hero_power packet
    def make_cal_hero_power_packet(self, packet):
        return None
    # send cal_hero_power
    def send_cal_hero_power(self):
        self.dispatch(OP_CODE.CS_CAL_HERO_POWER)(OP_CODE.CS_CAL_HERO_POWER)
    
    # handle SC_CAL_HERO_POWER
    @CallbackBase.callback(OP_CODE.SC_CAL_HERO_POWER)
    def handle_cal_hero_power_decorate(self, recv_buff):
        packet = sc_cal_hero_power()
        packet.deserialize(recv_buff)
        return self.handle_cal_hero_power(packet)    
    def handle_cal_hero_power(self, packet):
        return None

    
    # CS_TOWER_HANGUP_DATA
    @CallbackBase.callback(OP_CODE.CS_TOWER_HANGUP_DATA)
    def send_tower_hangup_data_decorate(self, code):
        packet = cs_tower_hangup_data()
        self.make_tower_hangup_data_packet(packet)
        self.mes_que[code] = packet
    # makeup tower_hangup_data packet
    def make_tower_hangup_data_packet(self, packet):
        return None
    # send tower_hangup_data
    def send_tower_hangup_data(self):
        self.dispatch(OP_CODE.CS_TOWER_HANGUP_DATA)(OP_CODE.CS_TOWER_HANGUP_DATA)
    
    # handle SC_TOWER_HANGUP_DATA
    @CallbackBase.callback(OP_CODE.SC_TOWER_HANGUP_DATA)
    def handle_tower_hangup_data_decorate(self, recv_buff):
        packet = sc_tower_hangup_data()
        packet.deserialize(recv_buff)
        return self.handle_tower_hangup_data(packet)    
    def handle_tower_hangup_data(self, packet):
        return None

    
    # CS_GET_FORMATION_POWER
    @CallbackBase.callback(OP_CODE.CS_GET_FORMATION_POWER)
    def send_get_formation_power_decorate(self, code):
        packet = cs_get_formation_power()
        self.make_get_formation_power_packet(packet)
        self.mes_que[code] = packet
    # makeup get_formation_power packet
    def make_get_formation_power_packet(self, packet):
        return None
    # send get_formation_power
    def send_get_formation_power(self):
        self.dispatch(OP_CODE.CS_GET_FORMATION_POWER)(OP_CODE.CS_GET_FORMATION_POWER)
    
    # handle SC_GET_FORMATION_POWER
    @CallbackBase.callback(OP_CODE.SC_GET_FORMATION_POWER)
    def handle_get_formation_power_decorate(self, recv_buff):
        packet = sc_get_formation_power()
        packet.deserialize(recv_buff)
        return self.handle_get_formation_power(packet)    
    def handle_get_formation_power(self, packet):
        return None

    
    # CS_GET_FUND_DATA
    @CallbackBase.callback(OP_CODE.CS_GET_FUND_DATA)
    def send_get_fund_data_decorate(self, code):
        packet = cs_get_fund_data()
        self.make_get_fund_data_packet(packet)
        self.mes_que[code] = packet
    # makeup get_fund_data packet
    def make_get_fund_data_packet(self, packet):
        return None
    # send get_fund_data
    def send_get_fund_data(self):
        self.dispatch(OP_CODE.CS_GET_FUND_DATA)(OP_CODE.CS_GET_FUND_DATA)
    
    # handle SC_GET_FUND_DATA
    @CallbackBase.callback(OP_CODE.SC_GET_FUND_DATA)
    def handle_get_fund_data_decorate(self, recv_buff):
        packet = sc_get_fund_data()
        packet.deserialize(recv_buff)
        return self.handle_get_fund_data(packet)    
    def handle_get_fund_data(self, packet):
        return None

    
    # CS_GET_MONTH_CARD_DATA
    @CallbackBase.callback(OP_CODE.CS_GET_MONTH_CARD_DATA)
    def send_get_month_card_data_decorate(self, code):
        packet = cs_get_month_card_data()
        self.make_get_month_card_data_packet(packet)
        self.mes_que[code] = packet
    # makeup get_month_card_data packet
    def make_get_month_card_data_packet(self, packet):
        return None
    # send get_month_card_data
    def send_get_month_card_data(self):
        self.dispatch(OP_CODE.CS_GET_MONTH_CARD_DATA)(OP_CODE.CS_GET_MONTH_CARD_DATA)
    
    # handle SC_GET_MONTH_CARD_DATA
    @CallbackBase.callback(OP_CODE.SC_GET_MONTH_CARD_DATA)
    def handle_get_month_card_data_decorate(self, recv_buff):
        packet = sc_get_month_card_data()
        packet.deserialize(recv_buff)
        return self.handle_get_month_card_data(packet)    
    def handle_get_month_card_data(self, packet):
        return None

    
    # CS_PICK_MONTH_CARD_DATA
    @CallbackBase.callback(OP_CODE.CS_PICK_MONTH_CARD_DATA)
    def send_pick_month_card_data_decorate(self, code):
        packet = cs_pick_month_card_data()
        self.make_pick_month_card_data_packet(packet)
        self.mes_que[code] = packet
    # makeup pick_month_card_data packet
    def make_pick_month_card_data_packet(self, packet):
        return None
    # send pick_month_card_data
    def send_pick_month_card_data(self):
        self.dispatch(OP_CODE.CS_PICK_MONTH_CARD_DATA)(OP_CODE.CS_PICK_MONTH_CARD_DATA)
    
    # handle SC_PICK_MONTH_CARD_DATA
    @CallbackBase.callback(OP_CODE.SC_PICK_MONTH_CARD_DATA)
    def handle_pick_month_card_data_decorate(self, recv_buff):
        packet = sc_pick_month_card_data()
        packet.deserialize(recv_buff)
        return self.handle_pick_month_card_data(packet)    
    def handle_pick_month_card_data(self, packet):
        return None

    
    # CS_SOLDIER_TRANSFORM
    @CallbackBase.callback(OP_CODE.CS_SOLDIER_TRANSFORM)
    def send_soldier_transform_decorate(self, code):
        packet = cs_soldier_transform()
        self.make_soldier_transform_packet(packet)
        self.mes_que[code] = packet
    # makeup soldier_transform packet
    def make_soldier_transform_packet(self, packet):
        return None
    # send soldier_transform
    def send_soldier_transform(self):
        self.dispatch(OP_CODE.CS_SOLDIER_TRANSFORM)(OP_CODE.CS_SOLDIER_TRANSFORM)
    
    # handle SC_SOLDIER_TRANSFORM
    @CallbackBase.callback(OP_CODE.SC_SOLDIER_TRANSFORM)
    def handle_soldier_transform_decorate(self, recv_buff):
        packet = sc_soldier_transform()
        packet.deserialize(recv_buff)
        return self.handle_soldier_transform(packet)    
    def handle_soldier_transform(self, packet):
        return None

    
    # CS_MODIFY_NAME
    @CallbackBase.callback(OP_CODE.CS_MODIFY_NAME)
    def send_modify_name_decorate(self, code):
        packet = cs_modify_name()
        self.make_modify_name_packet(packet)
        self.mes_que[code] = packet
    # makeup modify_name packet
    def make_modify_name_packet(self, packet):
        return None
    # send modify_name
    def send_modify_name(self):
        self.dispatch(OP_CODE.CS_MODIFY_NAME)(OP_CODE.CS_MODIFY_NAME)
    
    # handle SC_MODIFY_NAME
    @CallbackBase.callback(OP_CODE.SC_MODIFY_NAME)
    def handle_modify_name_decorate(self, recv_buff):
        packet = sc_modify_name()
        packet.deserialize(recv_buff)
        return self.handle_modify_name(packet)    
    def handle_modify_name(self, packet):
        return None

    
    # CS_HERO_COMBINE
    @CallbackBase.callback(OP_CODE.CS_HERO_COMBINE)
    def send_hero_combine_decorate(self, code):
        packet = cs_hero_combine()
        self.make_hero_combine_packet(packet)
        self.mes_que[code] = packet
    # makeup hero_combine packet
    def make_hero_combine_packet(self, packet):
        return None
    # send hero_combine
    def send_hero_combine(self):
        self.dispatch(OP_CODE.CS_HERO_COMBINE)(OP_CODE.CS_HERO_COMBINE)
    
    # handle SC_HERO_COMBINE
    @CallbackBase.callback(OP_CODE.SC_HERO_COMBINE)
    def handle_hero_combine_decorate(self, recv_buff):
        packet = sc_hero_combine()
        packet.deserialize(recv_buff)
        return self.handle_hero_combine(packet)    
    def handle_hero_combine(self, packet):
        return None

    
    # CS_BLOCK_SPY
    @CallbackBase.callback(OP_CODE.CS_BLOCK_SPY)
    def send_block_spy_decorate(self, code):
        packet = cs_block_spy()
        self.make_block_spy_packet(packet)
        self.mes_que[code] = packet
    # makeup block_spy packet
    def make_block_spy_packet(self, packet):
        return None
    # send block_spy
    def send_block_spy(self):
        self.dispatch(OP_CODE.CS_BLOCK_SPY)(OP_CODE.CS_BLOCK_SPY)
    
    # handle SC_BLOCK_SPY
    @CallbackBase.callback(OP_CODE.SC_BLOCK_SPY)
    def handle_block_spy_decorate(self, recv_buff):
        packet = sc_block_spy()
        packet.deserialize(recv_buff)
        return self.handle_block_spy(packet)    
    def handle_block_spy(self, packet):
        return None

    
    # CS_BUY_TOKEN
    @CallbackBase.callback(OP_CODE.CS_BUY_TOKEN)
    def send_buy_token_decorate(self, code):
        packet = cs_buy_token()
        self.make_buy_token_packet(packet)
        self.mes_que[code] = packet
    # makeup buy_token packet
    def make_buy_token_packet(self, packet):
        return None
    # send buy_token
    def send_buy_token(self):
        self.dispatch(OP_CODE.CS_BUY_TOKEN)(OP_CODE.CS_BUY_TOKEN)
    
    # handle SC_BUY_TOKEN
    @CallbackBase.callback(OP_CODE.SC_BUY_TOKEN)
    def handle_buy_token_decorate(self, recv_buff):
        packet = sc_buy_token()
        packet.deserialize(recv_buff)
        return self.handle_buy_token(packet)    
    def handle_buy_token(self, packet):
        return None

    
    # CS_SHOP_REFRESH_BUY_TIMES
    @CallbackBase.callback(OP_CODE.CS_SHOP_REFRESH_BUY_TIMES)
    def send_shop_refresh_buy_times_decorate(self, code):
        packet = cs_shop_refresh_buy_times()
        self.make_shop_refresh_buy_times_packet(packet)
        self.mes_que[code] = packet
    # makeup shop_refresh_buy_times packet
    def make_shop_refresh_buy_times_packet(self, packet):
        return None
    # send shop_refresh_buy_times
    def send_shop_refresh_buy_times(self):
        self.dispatch(OP_CODE.CS_SHOP_REFRESH_BUY_TIMES)(OP_CODE.CS_SHOP_REFRESH_BUY_TIMES)
    
    # handle SC_SHOP_REFRESH_BUY_TIMES
    @CallbackBase.callback(OP_CODE.SC_SHOP_REFRESH_BUY_TIMES)
    def handle_shop_refresh_buy_times_decorate(self, recv_buff):
        packet = sc_shop_refresh_buy_times()
        packet.deserialize(recv_buff)
        return self.handle_shop_refresh_buy_times(packet)    
    def handle_shop_refresh_buy_times(self, packet):
        return None

    
    # CS_GUILD_USER_MARK
    @CallbackBase.callback(OP_CODE.CS_GUILD_USER_MARK)
    def send_guild_user_mark_decorate(self, code):
        packet = cs_guild_user_mark()
        self.make_guild_user_mark_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_user_mark packet
    def make_guild_user_mark_packet(self, packet):
        return None
    # send guild_user_mark
    def send_guild_user_mark(self):
        self.dispatch(OP_CODE.CS_GUILD_USER_MARK)(OP_CODE.CS_GUILD_USER_MARK)
    
    # handle SC_GUILD_USER_MARK
    @CallbackBase.callback(OP_CODE.SC_GUILD_USER_MARK)
    def handle_guild_user_mark_decorate(self, recv_buff):
        packet = sc_guild_user_mark()
        packet.deserialize(recv_buff)
        return self.handle_guild_user_mark(packet)    
    def handle_guild_user_mark(self, packet):
        return None

    
    # CS_GUILD_CONDITION
    @CallbackBase.callback(OP_CODE.CS_GUILD_CONDITION)
    def send_guild_condition_decorate(self, code):
        packet = cs_guild_condition()
        self.make_guild_condition_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_condition packet
    def make_guild_condition_packet(self, packet):
        return None
    # send guild_condition
    def send_guild_condition(self):
        self.dispatch(OP_CODE.CS_GUILD_CONDITION)(OP_CODE.CS_GUILD_CONDITION)
    
    # handle SC_GUILD_CONDITION
    @CallbackBase.callback(OP_CODE.SC_GUILD_CONDITION)
    def handle_guild_condition_decorate(self, recv_buff):
        packet = sc_guild_condition()
        packet.deserialize(recv_buff)
        return self.handle_guild_condition(packet)    
    def handle_guild_condition(self, packet):
        return None

    
    # CS_WASH_SKILL
    @CallbackBase.callback(OP_CODE.CS_WASH_SKILL)
    def send_wash_skill_decorate(self, code):
        packet = cs_wash_skill()
        self.make_wash_skill_packet(packet)
        self.mes_que[code] = packet
    # makeup wash_skill packet
    def make_wash_skill_packet(self, packet):
        return None
    # send wash_skill
    def send_wash_skill(self):
        self.dispatch(OP_CODE.CS_WASH_SKILL)(OP_CODE.CS_WASH_SKILL)
    
    # handle SC_WASH_SKILL
    @CallbackBase.callback(OP_CODE.SC_WASH_SKILL)
    def handle_wash_skill_decorate(self, recv_buff):
        packet = sc_wash_skill()
        packet.deserialize(recv_buff)
        return self.handle_wash_skill(packet)    
    def handle_wash_skill(self, packet):
        return None

    
    # CS_WASH_SKILL_AFFIRM
    @CallbackBase.callback(OP_CODE.CS_WASH_SKILL_AFFIRM)
    def send_wash_skill_affirm_decorate(self, code):
        packet = cs_wash_skill_affirm()
        self.make_wash_skill_affirm_packet(packet)
        self.mes_que[code] = packet
    # makeup wash_skill_affirm packet
    def make_wash_skill_affirm_packet(self, packet):
        return None
    # send wash_skill_affirm
    def send_wash_skill_affirm(self):
        self.dispatch(OP_CODE.CS_WASH_SKILL_AFFIRM)(OP_CODE.CS_WASH_SKILL_AFFIRM)
    
    # handle SC_WASH_SKILL_AFFIRM
    @CallbackBase.callback(OP_CODE.SC_WASH_SKILL_AFFIRM)
    def handle_wash_skill_affirm_decorate(self, recv_buff):
        packet = sc_wash_skill_affirm()
        packet.deserialize(recv_buff)
        return self.handle_wash_skill_affirm(packet)    
    def handle_wash_skill_affirm(self, packet):
        return None

    
    # CS_GET_USER_MARK
    @CallbackBase.callback(OP_CODE.CS_GET_USER_MARK)
    def send_get_user_mark_decorate(self, code):
        packet = cs_get_user_mark()
        self.make_get_user_mark_packet(packet)
        self.mes_que[code] = packet
    # makeup get_user_mark packet
    def make_get_user_mark_packet(self, packet):
        return None
    # send get_user_mark
    def send_get_user_mark(self):
        self.dispatch(OP_CODE.CS_GET_USER_MARK)(OP_CODE.CS_GET_USER_MARK)
    
    # handle SC_GET_USER_MARK
    @CallbackBase.callback(OP_CODE.SC_GET_USER_MARK)
    def handle_get_user_mark_decorate(self, recv_buff):
        packet = sc_get_user_mark()
        packet.deserialize(recv_buff)
        return self.handle_get_user_mark(packet)    
    def handle_get_user_mark(self, packet):
        return None

    
    # CS_SET_USER_MARK
    @CallbackBase.callback(OP_CODE.CS_SET_USER_MARK)
    def send_set_user_mark_decorate(self, code):
        packet = cs_set_user_mark()
        self.make_set_user_mark_packet(packet)
        self.mes_que[code] = packet
    # makeup set_user_mark packet
    def make_set_user_mark_packet(self, packet):
        return None
    # send set_user_mark
    def send_set_user_mark(self):
        self.dispatch(OP_CODE.CS_SET_USER_MARK)(OP_CODE.CS_SET_USER_MARK)
    
    # handle SC_SET_USER_MARK
    @CallbackBase.callback(OP_CODE.SC_SET_USER_MARK)
    def handle_set_user_mark_decorate(self, recv_buff):
        packet = sc_set_user_mark()
        packet.deserialize(recv_buff)
        return self.handle_set_user_mark(packet)    
    def handle_set_user_mark(self, packet):
        return None

    
    # CS_GET_BLOCK_MARK
    @CallbackBase.callback(OP_CODE.CS_GET_BLOCK_MARK)
    def send_get_block_mark_decorate(self, code):
        packet = cs_get_block_mark()
        self.make_get_block_mark_packet(packet)
        self.mes_que[code] = packet
    # makeup get_block_mark packet
    def make_get_block_mark_packet(self, packet):
        return None
    # send get_block_mark
    def send_get_block_mark(self):
        self.dispatch(OP_CODE.CS_GET_BLOCK_MARK)(OP_CODE.CS_GET_BLOCK_MARK)
    
    # handle SC_GET_BLOCK_MARK
    @CallbackBase.callback(OP_CODE.SC_GET_BLOCK_MARK)
    def handle_get_block_mark_decorate(self, recv_buff):
        packet = sc_get_block_mark()
        packet.deserialize(recv_buff)
        return self.handle_get_block_mark(packet)    
    def handle_get_block_mark(self, packet):
        return None

    
    # CS_ADD_BLOCK_MARK
    @CallbackBase.callback(OP_CODE.CS_ADD_BLOCK_MARK)
    def send_add_block_mark_decorate(self, code):
        packet = cs_add_block_mark()
        self.make_add_block_mark_packet(packet)
        self.mes_que[code] = packet
    # makeup add_block_mark packet
    def make_add_block_mark_packet(self, packet):
        return None
    # send add_block_mark
    def send_add_block_mark(self):
        self.dispatch(OP_CODE.CS_ADD_BLOCK_MARK)(OP_CODE.CS_ADD_BLOCK_MARK)
    
    # handle SC_ADD_BLOCK_MARK
    @CallbackBase.callback(OP_CODE.SC_ADD_BLOCK_MARK)
    def handle_add_block_mark_decorate(self, recv_buff):
        packet = sc_add_block_mark()
        packet.deserialize(recv_buff)
        return self.handle_add_block_mark(packet)    
    def handle_add_block_mark(self, packet):
        return None

    
    # CS_DEL_BLOCK_MARK
    @CallbackBase.callback(OP_CODE.CS_DEL_BLOCK_MARK)
    def send_del_block_mark_decorate(self, code):
        packet = cs_del_block_mark()
        self.make_del_block_mark_packet(packet)
        self.mes_que[code] = packet
    # makeup del_block_mark packet
    def make_del_block_mark_packet(self, packet):
        return None
    # send del_block_mark
    def send_del_block_mark(self):
        self.dispatch(OP_CODE.CS_DEL_BLOCK_MARK)(OP_CODE.CS_DEL_BLOCK_MARK)
    
    # handle SC_DEL_BLOCK_MARK
    @CallbackBase.callback(OP_CODE.SC_DEL_BLOCK_MARK)
    def handle_del_block_mark_decorate(self, recv_buff):
        packet = sc_del_block_mark()
        packet.deserialize(recv_buff)
        return self.handle_del_block_mark(packet)    
    def handle_del_block_mark(self, packet):
        return None

    
    # CS_GET_CHAPTER_REWARDS
    @CallbackBase.callback(OP_CODE.CS_GET_CHAPTER_REWARDS)
    def send_get_chapter_rewards_decorate(self, code):
        packet = cs_get_chapter_rewards()
        self.make_get_chapter_rewards_packet(packet)
        self.mes_que[code] = packet
    # makeup get_chapter_rewards packet
    def make_get_chapter_rewards_packet(self, packet):
        return None
    # send get_chapter_rewards
    def send_get_chapter_rewards(self):
        self.dispatch(OP_CODE.CS_GET_CHAPTER_REWARDS)(OP_CODE.CS_GET_CHAPTER_REWARDS)
    
    # handle SC_GET_CHAPTER_REWARDS
    @CallbackBase.callback(OP_CODE.SC_GET_CHAPTER_REWARDS)
    def handle_get_chapter_rewards_decorate(self, recv_buff):
        packet = sc_get_chapter_rewards()
        packet.deserialize(recv_buff)
        return self.handle_get_chapter_rewards(packet)    
    def handle_get_chapter_rewards(self, packet):
        return None

    
    # CS_GET_FAME_REWARDS
    @CallbackBase.callback(OP_CODE.CS_GET_FAME_REWARDS)
    def send_get_fame_rewards_decorate(self, code):
        packet = cs_get_fame_rewards()
        self.make_get_fame_rewards_packet(packet)
        self.mes_que[code] = packet
    # makeup get_fame_rewards packet
    def make_get_fame_rewards_packet(self, packet):
        return None
    # send get_fame_rewards
    def send_get_fame_rewards(self):
        self.dispatch(OP_CODE.CS_GET_FAME_REWARDS)(OP_CODE.CS_GET_FAME_REWARDS)
    
    # handle SC_GET_FAME_REWARDS
    @CallbackBase.callback(OP_CODE.SC_GET_FAME_REWARDS)
    def handle_get_fame_rewards_decorate(self, recv_buff):
        packet = sc_get_fame_rewards()
        packet.deserialize(recv_buff)
        return self.handle_get_fame_rewards(packet)    
    def handle_get_fame_rewards(self, packet):
        return None

    
    # CS_GET_NPC_INFO
    @CallbackBase.callback(OP_CODE.CS_GET_NPC_INFO)
    def send_get_npc_info_decorate(self, code):
        packet = cs_get_npc_info()
        self.make_get_npc_info_packet(packet)
        self.mes_que[code] = packet
    # makeup get_npc_info packet
    def make_get_npc_info_packet(self, packet):
        return None
    # send get_npc_info
    def send_get_npc_info(self):
        self.dispatch(OP_CODE.CS_GET_NPC_INFO)(OP_CODE.CS_GET_NPC_INFO)
    
    # handle SC_GET_NPC_INFO
    @CallbackBase.callback(OP_CODE.SC_GET_NPC_INFO)
    def handle_get_npc_info_decorate(self, recv_buff):
        packet = sc_get_npc_info()
        packet.deserialize(recv_buff)
        return self.handle_get_npc_info(packet)    
    def handle_get_npc_info(self, packet):
        return None

    
    # CS_GET_NPC_GROUP_INFO
    @CallbackBase.callback(OP_CODE.CS_GET_NPC_GROUP_INFO)
    def send_get_npc_group_info_decorate(self, code):
        packet = cs_get_npc_group_info()
        self.make_get_npc_group_info_packet(packet)
        self.mes_que[code] = packet
    # makeup get_npc_group_info packet
    def make_get_npc_group_info_packet(self, packet):
        return None
    # send get_npc_group_info
    def send_get_npc_group_info(self):
        self.dispatch(OP_CODE.CS_GET_NPC_GROUP_INFO)(OP_CODE.CS_GET_NPC_GROUP_INFO)
    
    # handle SC_GET_NPC_GROUP_INFO
    @CallbackBase.callback(OP_CODE.SC_GET_NPC_GROUP_INFO)
    def handle_get_npc_group_info_decorate(self, recv_buff):
        packet = sc_get_npc_group_info()
        packet.deserialize(recv_buff)
        return self.handle_get_npc_group_info(packet)    
    def handle_get_npc_group_info(self, packet):
        return None

    
    # CS_OPEN_NPC_DIALOGUE
    @CallbackBase.callback(OP_CODE.CS_OPEN_NPC_DIALOGUE)
    def send_open_npc_dialogue_decorate(self, code):
        packet = cs_open_npc_dialogue()
        self.make_open_npc_dialogue_packet(packet)
        self.mes_que[code] = packet
    # makeup open_npc_dialogue packet
    def make_open_npc_dialogue_packet(self, packet):
        return None
    # send open_npc_dialogue
    def send_open_npc_dialogue(self):
        self.dispatch(OP_CODE.CS_OPEN_NPC_DIALOGUE)(OP_CODE.CS_OPEN_NPC_DIALOGUE)
    
    # handle SC_OPEN_NPC_DIALOGUE
    @CallbackBase.callback(OP_CODE.SC_OPEN_NPC_DIALOGUE)
    def handle_open_npc_dialogue_decorate(self, recv_buff):
        packet = sc_open_npc_dialogue()
        packet.deserialize(recv_buff)
        return self.handle_open_npc_dialogue(packet)    
    def handle_open_npc_dialogue(self, packet):
        return None

    
    # CS_GET_NPC_REWARDS
    @CallbackBase.callback(OP_CODE.CS_GET_NPC_REWARDS)
    def send_get_npc_rewards_decorate(self, code):
        packet = cs_get_npc_rewards()
        self.make_get_npc_rewards_packet(packet)
        self.mes_que[code] = packet
    # makeup get_npc_rewards packet
    def make_get_npc_rewards_packet(self, packet):
        return None
    # send get_npc_rewards
    def send_get_npc_rewards(self):
        self.dispatch(OP_CODE.CS_GET_NPC_REWARDS)(OP_CODE.CS_GET_NPC_REWARDS)
    
    # handle SC_GET_NPC_REWARDS
    @CallbackBase.callback(OP_CODE.SC_GET_NPC_REWARDS)
    def handle_get_npc_rewards_decorate(self, recv_buff):
        packet = sc_get_npc_rewards()
        packet.deserialize(recv_buff)
        return self.handle_get_npc_rewards(packet)    
    def handle_get_npc_rewards(self, packet):
        return None

    
    # CS_NPC_EXCHANGE
    @CallbackBase.callback(OP_CODE.CS_NPC_EXCHANGE)
    def send_npc_exchange_decorate(self, code):
        packet = cs_npc_exchange()
        self.make_npc_exchange_packet(packet)
        self.mes_que[code] = packet
    # makeup npc_exchange packet
    def make_npc_exchange_packet(self, packet):
        return None
    # send npc_exchange
    def send_npc_exchange(self):
        self.dispatch(OP_CODE.CS_NPC_EXCHANGE)(OP_CODE.CS_NPC_EXCHANGE)
    
    # handle SC_NPC_EXCHANGE
    @CallbackBase.callback(OP_CODE.SC_NPC_EXCHANGE)
    def handle_npc_exchange_decorate(self, recv_buff):
        packet = sc_npc_exchange()
        packet.deserialize(recv_buff)
        return self.handle_npc_exchange(packet)    
    def handle_npc_exchange(self, packet):
        return None

    
    # CS_GET_MUSEUM_COLLECTION_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_MUSEUM_COLLECTION_LIST)
    def send_get_museum_collection_list_decorate(self, code):
        packet = cs_get_museum_collection_list()
        self.make_get_museum_collection_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_museum_collection_list packet
    def make_get_museum_collection_list_packet(self, packet):
        return None
    # send get_museum_collection_list
    def send_get_museum_collection_list(self):
        self.dispatch(OP_CODE.CS_GET_MUSEUM_COLLECTION_LIST)(OP_CODE.CS_GET_MUSEUM_COLLECTION_LIST)
    
    # handle SC_GET_MUSEUM_COLLECTION_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_MUSEUM_COLLECTION_LIST)
    def handle_get_museum_collection_list_decorate(self, recv_buff):
        packet = sc_get_museum_collection_list()
        packet.deserialize(recv_buff)
        return self.handle_get_museum_collection_list(packet)    
    def handle_get_museum_collection_list(self, packet):
        return None

    
    # CS_MUSEUM_COLLECTION_REWARD_DRAW
    @CallbackBase.callback(OP_CODE.CS_MUSEUM_COLLECTION_REWARD_DRAW)
    def send_museum_collection_reward_draw_decorate(self, code):
        packet = cs_museum_collection_reward_draw()
        self.make_museum_collection_reward_draw_packet(packet)
        self.mes_que[code] = packet
    # makeup museum_collection_reward_draw packet
    def make_museum_collection_reward_draw_packet(self, packet):
        return None
    # send museum_collection_reward_draw
    def send_museum_collection_reward_draw(self):
        self.dispatch(OP_CODE.CS_MUSEUM_COLLECTION_REWARD_DRAW)(OP_CODE.CS_MUSEUM_COLLECTION_REWARD_DRAW)
    
    # handle SC_MUSEUM_COLLECTION_REWARD_DRAW
    @CallbackBase.callback(OP_CODE.SC_MUSEUM_COLLECTION_REWARD_DRAW)
    def handle_museum_collection_reward_draw_decorate(self, recv_buff):
        packet = sc_museum_collection_reward_draw()
        packet.deserialize(recv_buff)
        return self.handle_museum_collection_reward_draw(packet)    
    def handle_museum_collection_reward_draw(self, packet):
        return None

    
    # CS_GET_MUSEUM_GROUP_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_MUSEUM_GROUP_LIST)
    def send_get_museum_group_list_decorate(self, code):
        packet = cs_get_museum_group_list()
        self.make_get_museum_group_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_museum_group_list packet
    def make_get_museum_group_list_packet(self, packet):
        return None
    # send get_museum_group_list
    def send_get_museum_group_list(self):
        self.dispatch(OP_CODE.CS_GET_MUSEUM_GROUP_LIST)(OP_CODE.CS_GET_MUSEUM_GROUP_LIST)
    
    # handle SC_GET_MUSEUM_GROUP_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_MUSEUM_GROUP_LIST)
    def handle_get_museum_group_list_decorate(self, recv_buff):
        packet = sc_get_museum_group_list()
        packet.deserialize(recv_buff)
        return self.handle_get_museum_group_list(packet)    
    def handle_get_museum_group_list(self, packet):
        return None

    
    # CS_MUSEUM_GROUP_ACTIVE
    @CallbackBase.callback(OP_CODE.CS_MUSEUM_GROUP_ACTIVE)
    def send_museum_group_active_decorate(self, code):
        packet = cs_museum_group_active()
        self.make_museum_group_active_packet(packet)
        self.mes_que[code] = packet
    # makeup museum_group_active packet
    def make_museum_group_active_packet(self, packet):
        return None
    # send museum_group_active
    def send_museum_group_active(self):
        self.dispatch(OP_CODE.CS_MUSEUM_GROUP_ACTIVE)(OP_CODE.CS_MUSEUM_GROUP_ACTIVE)
    
    # handle SC_MUSEUM_GROUP_ACTIVE
    @CallbackBase.callback(OP_CODE.SC_MUSEUM_GROUP_ACTIVE)
    def handle_museum_group_active_decorate(self, recv_buff):
        packet = sc_museum_group_active()
        packet.deserialize(recv_buff)
        return self.handle_museum_group_active(packet)    
    def handle_museum_group_active(self, packet):
        return None

    
    # CS_GUILD_ASSIST
    @CallbackBase.callback(OP_CODE.CS_GUILD_ASSIST)
    def send_guild_assist_decorate(self, code):
        packet = cs_guild_assist()
        self.make_guild_assist_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_assist packet
    def make_guild_assist_packet(self, packet):
        return None
    # send guild_assist
    def send_guild_assist(self):
        self.dispatch(OP_CODE.CS_GUILD_ASSIST)(OP_CODE.CS_GUILD_ASSIST)
    
    # handle SC_GUILD_ASSIST
    @CallbackBase.callback(OP_CODE.SC_GUILD_ASSIST)
    def handle_guild_assist_decorate(self, recv_buff):
        packet = sc_guild_assist()
        packet.deserialize(recv_buff)
        return self.handle_guild_assist(packet)    
    def handle_guild_assist(self, packet):
        return None

    
    # CS_GET_GUILD_ASSIST
    @CallbackBase.callback(OP_CODE.CS_GET_GUILD_ASSIST)
    def send_get_guild_assist_decorate(self, code):
        packet = cs_get_guild_assist()
        self.make_get_guild_assist_packet(packet)
        self.mes_que[code] = packet
    # makeup get_guild_assist packet
    def make_get_guild_assist_packet(self, packet):
        return None
    # send get_guild_assist
    def send_get_guild_assist(self):
        self.dispatch(OP_CODE.CS_GET_GUILD_ASSIST)(OP_CODE.CS_GET_GUILD_ASSIST)
    
    # handle SC_GET_GUILD_ASSIST
    @CallbackBase.callback(OP_CODE.SC_GET_GUILD_ASSIST)
    def handle_get_guild_assist_decorate(self, recv_buff):
        packet = sc_get_guild_assist()
        packet.deserialize(recv_buff)
        return self.handle_get_guild_assist(packet)    
    def handle_get_guild_assist(self, packet):
        return None

    
    # CS_GUILD_ASSIST_OTHER
    @CallbackBase.callback(OP_CODE.CS_GUILD_ASSIST_OTHER)
    def send_guild_assist_other_decorate(self, code):
        packet = cs_guild_assist_other()
        self.make_guild_assist_other_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_assist_other packet
    def make_guild_assist_other_packet(self, packet):
        return None
    # send guild_assist_other
    def send_guild_assist_other(self):
        self.dispatch(OP_CODE.CS_GUILD_ASSIST_OTHER)(OP_CODE.CS_GUILD_ASSIST_OTHER)
    
    # handle SC_GUILD_ASSIST_OTHER
    @CallbackBase.callback(OP_CODE.SC_GUILD_ASSIST_OTHER)
    def handle_guild_assist_other_decorate(self, recv_buff):
        packet = sc_guild_assist_other()
        packet.deserialize(recv_buff)
        return self.handle_guild_assist_other(packet)    
    def handle_guild_assist_other(self, packet):
        return None

    
    # CS_SYNC_USER_EVENT_FLAG_WITH_PARAM
    @CallbackBase.callback(OP_CODE.CS_SYNC_USER_EVENT_FLAG_WITH_PARAM)
    def send_sync_user_event_flag_with_param_decorate(self, code):
        packet = cs_sync_user_event_flag_with_param()
        self.make_sync_user_event_flag_with_param_packet(packet)
        self.mes_que[code] = packet
    # makeup sync_user_event_flag_with_param packet
    def make_sync_user_event_flag_with_param_packet(self, packet):
        return None
    # send sync_user_event_flag_with_param
    def send_sync_user_event_flag_with_param(self):
        self.dispatch(OP_CODE.CS_SYNC_USER_EVENT_FLAG_WITH_PARAM)(OP_CODE.CS_SYNC_USER_EVENT_FLAG_WITH_PARAM)
    
    # handle SC_SYNC_USER_EVENT_FLAG_WITH_PARAM
    @CallbackBase.callback(OP_CODE.SC_SYNC_USER_EVENT_FLAG_WITH_PARAM)
    def handle_sync_user_event_flag_with_param_decorate(self, recv_buff):
        packet = sc_sync_user_event_flag_with_param()
        packet.deserialize(recv_buff)
        return self.handle_sync_user_event_flag_with_param(packet)    
    def handle_sync_user_event_flag_with_param(self, packet):
        return None

    
    # CS_GET_GAME_EVENT
    @CallbackBase.callback(OP_CODE.CS_GET_GAME_EVENT)
    def send_get_game_event_decorate(self, code):
        packet = cs_get_game_event()
        self.make_get_game_event_packet(packet)
        self.mes_que[code] = packet
    # makeup get_game_event packet
    def make_get_game_event_packet(self, packet):
        return None
    # send get_game_event
    def send_get_game_event(self):
        self.dispatch(OP_CODE.CS_GET_GAME_EVENT)(OP_CODE.CS_GET_GAME_EVENT)
    
    # handle SC_GET_GAME_EVENT
    @CallbackBase.callback(OP_CODE.SC_GET_GAME_EVENT)
    def handle_get_game_event_decorate(self, recv_buff):
        packet = sc_get_game_event()
        packet.deserialize(recv_buff)
        return self.handle_get_game_event(packet)    
    def handle_get_game_event(self, packet):
        return None

    
    # CS_DISCOVERY_GET
    @CallbackBase.callback(OP_CODE.CS_DISCOVERY_GET)
    def send_discovery_get_decorate(self, code):
        packet = cs_discovery_get()
        self.make_discovery_get_packet(packet)
        self.mes_que[code] = packet
    # makeup discovery_get packet
    def make_discovery_get_packet(self, packet):
        return None
    # send discovery_get
    def send_discovery_get(self):
        self.dispatch(OP_CODE.CS_DISCOVERY_GET)(OP_CODE.CS_DISCOVERY_GET)
    
    # handle SC_DISCOVERY_GET
    @CallbackBase.callback(OP_CODE.SC_DISCOVERY_GET)
    def handle_discovery_get_decorate(self, recv_buff):
        packet = sc_discovery_get()
        packet.deserialize(recv_buff)
        return self.handle_discovery_get(packet)    
    def handle_discovery_get(self, packet):
        return None

    
    # CS_DISCOVERY_FIND
    @CallbackBase.callback(OP_CODE.CS_DISCOVERY_FIND)
    def send_discovery_find_decorate(self, code):
        packet = cs_discovery_find()
        self.make_discovery_find_packet(packet)
        self.mes_que[code] = packet
    # makeup discovery_find packet
    def make_discovery_find_packet(self, packet):
        return None
    # send discovery_find
    def send_discovery_find(self):
        self.dispatch(OP_CODE.CS_DISCOVERY_FIND)(OP_CODE.CS_DISCOVERY_FIND)
    
    # handle SC_DISCOVERY_FIND
    @CallbackBase.callback(OP_CODE.SC_DISCOVERY_FIND)
    def handle_discovery_find_decorate(self, recv_buff):
        packet = sc_discovery_find()
        packet.deserialize(recv_buff)
        return self.handle_discovery_find(packet)    
    def handle_discovery_find(self, packet):
        return None

    
    # CS_DISCOVERY_CATCH
    @CallbackBase.callback(OP_CODE.CS_DISCOVERY_CATCH)
    def send_discovery_catch_decorate(self, code):
        packet = cs_discovery_catch()
        self.make_discovery_catch_packet(packet)
        self.mes_que[code] = packet
    # makeup discovery_catch packet
    def make_discovery_catch_packet(self, packet):
        return None
    # send discovery_catch
    def send_discovery_catch(self):
        self.dispatch(OP_CODE.CS_DISCOVERY_CATCH)(OP_CODE.CS_DISCOVERY_CATCH)
    
    # handle SC_DISCOVERY_CATCH
    @CallbackBase.callback(OP_CODE.SC_DISCOVERY_CATCH)
    def handle_discovery_catch_decorate(self, recv_buff):
        packet = sc_discovery_catch()
        packet.deserialize(recv_buff)
        return self.handle_discovery_catch(packet)    
    def handle_discovery_catch(self, packet):
        return None

    
    # CS_DISCOVERY_TRIGGER
    @CallbackBase.callback(OP_CODE.CS_DISCOVERY_TRIGGER)
    def send_discovery_trigger_decorate(self, code):
        packet = cs_discovery_trigger()
        self.make_discovery_trigger_packet(packet)
        self.mes_que[code] = packet
    # makeup discovery_trigger packet
    def make_discovery_trigger_packet(self, packet):
        return None
    # send discovery_trigger
    def send_discovery_trigger(self):
        self.dispatch(OP_CODE.CS_DISCOVERY_TRIGGER)(OP_CODE.CS_DISCOVERY_TRIGGER)
    
    # handle SC_DISCOVERY_TRIGGER
    @CallbackBase.callback(OP_CODE.SC_DISCOVERY_TRIGGER)
    def handle_discovery_trigger_decorate(self, recv_buff):
        packet = sc_discovery_trigger()
        packet.deserialize(recv_buff)
        return self.handle_discovery_trigger(packet)    
    def handle_discovery_trigger(self, packet):
        return None

    
    # CS_DISCOVERY_QUIT
    @CallbackBase.callback(OP_CODE.CS_DISCOVERY_QUIT)
    def send_discovery_quit_decorate(self, code):
        packet = cs_discovery_quit()
        self.make_discovery_quit_packet(packet)
        self.mes_que[code] = packet
    # makeup discovery_quit packet
    def make_discovery_quit_packet(self, packet):
        return None
    # send discovery_quit
    def send_discovery_quit(self):
        self.dispatch(OP_CODE.CS_DISCOVERY_QUIT)(OP_CODE.CS_DISCOVERY_QUIT)
    
    # handle SC_DISCOVERY_QUIT
    @CallbackBase.callback(OP_CODE.SC_DISCOVERY_QUIT)
    def handle_discovery_quit_decorate(self, recv_buff):
        packet = sc_discovery_quit()
        packet.deserialize(recv_buff)
        return self.handle_discovery_quit(packet)    
    def handle_discovery_quit(self, packet):
        return None

    
    # CS_GET_GUILD_ASSIST_RESOURCE_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_GUILD_ASSIST_RESOURCE_LIST)
    def send_get_guild_assist_resource_list_decorate(self, code):
        packet = cs_get_guild_assist_resource_list()
        self.make_get_guild_assist_resource_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_guild_assist_resource_list packet
    def make_get_guild_assist_resource_list_packet(self, packet):
        return None
    # send get_guild_assist_resource_list
    def send_get_guild_assist_resource_list(self):
        self.dispatch(OP_CODE.CS_GET_GUILD_ASSIST_RESOURCE_LIST)(OP_CODE.CS_GET_GUILD_ASSIST_RESOURCE_LIST)
    
    # handle SC_GET_GUILD_ASSIST_RESOURCE_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_GUILD_ASSIST_RESOURCE_LIST)
    def handle_get_guild_assist_resource_list_decorate(self, recv_buff):
        packet = sc_get_guild_assist_resource_list()
        packet.deserialize(recv_buff)
        return self.handle_get_guild_assist_resource_list(packet)    
    def handle_get_guild_assist_resource_list(self, packet):
        return None

    
    # CS_GUILD_ASSIST_RES_OTHER
    @CallbackBase.callback(OP_CODE.CS_GUILD_ASSIST_RES_OTHER)
    def send_guild_assist_res_other_decorate(self, code):
        packet = cs_guild_assist_res_other()
        self.make_guild_assist_res_other_packet(packet)
        self.mes_que[code] = packet
    # makeup guild_assist_res_other packet
    def make_guild_assist_res_other_packet(self, packet):
        return None
    # send guild_assist_res_other
    def send_guild_assist_res_other(self):
        self.dispatch(OP_CODE.CS_GUILD_ASSIST_RES_OTHER)(OP_CODE.CS_GUILD_ASSIST_RES_OTHER)
    
    # handle SC_GUILD_ASSIST_RES_OTHER
    @CallbackBase.callback(OP_CODE.SC_GUILD_ASSIST_RES_OTHER)
    def handle_guild_assist_res_other_decorate(self, recv_buff):
        packet = sc_guild_assist_res_other()
        packet.deserialize(recv_buff)
        return self.handle_guild_assist_res_other(packet)    
    def handle_guild_assist_res_other(self, packet):
        return None

    
    # CS_GET_ADVENTURE_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_ADVENTURE_LIST)
    def send_get_adventure_list_decorate(self, code):
        packet = cs_get_adventure_list()
        self.make_get_adventure_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_adventure_list packet
    def make_get_adventure_list_packet(self, packet):
        return None
    # send get_adventure_list
    def send_get_adventure_list(self):
        self.dispatch(OP_CODE.CS_GET_ADVENTURE_LIST)(OP_CODE.CS_GET_ADVENTURE_LIST)
    
    # handle SC_GET_ADVENTURE_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_ADVENTURE_LIST)
    def handle_get_adventure_list_decorate(self, recv_buff):
        packet = sc_get_adventure_list()
        packet.deserialize(recv_buff)
        return self.handle_get_adventure_list(packet)    
    def handle_get_adventure_list(self, packet):
        return None

    
    # CS_GET_ADVENTURE_EVENT
    @CallbackBase.callback(OP_CODE.CS_GET_ADVENTURE_EVENT)
    def send_get_adventure_event_decorate(self, code):
        packet = cs_get_adventure_event()
        self.make_get_adventure_event_packet(packet)
        self.mes_que[code] = packet
    # makeup get_adventure_event packet
    def make_get_adventure_event_packet(self, packet):
        return None
    # send get_adventure_event
    def send_get_adventure_event(self):
        self.dispatch(OP_CODE.CS_GET_ADVENTURE_EVENT)(OP_CODE.CS_GET_ADVENTURE_EVENT)
    
    # handle SC_GET_ADVENTURE_EVENT
    @CallbackBase.callback(OP_CODE.SC_GET_ADVENTURE_EVENT)
    def handle_get_adventure_event_decorate(self, recv_buff):
        packet = sc_get_adventure_event()
        packet.deserialize(recv_buff)
        return self.handle_get_adventure_event(packet)    
    def handle_get_adventure_event(self, packet):
        return None

    
    # CS_ADVENTURE_STEP
    @CallbackBase.callback(OP_CODE.CS_ADVENTURE_STEP)
    def send_adventure_step_decorate(self, code):
        packet = cs_adventure_step()
        self.make_adventure_step_packet(packet)
        self.mes_que[code] = packet
    # makeup adventure_step packet
    def make_adventure_step_packet(self, packet):
        return None
    # send adventure_step
    def send_adventure_step(self):
        self.dispatch(OP_CODE.CS_ADVENTURE_STEP)(OP_CODE.CS_ADVENTURE_STEP)
    
    # handle SC_ADVENTURE_STEP
    @CallbackBase.callback(OP_CODE.SC_ADVENTURE_STEP)
    def handle_adventure_step_decorate(self, recv_buff):
        packet = sc_adventure_step()
        packet.deserialize(recv_buff)
        return self.handle_adventure_step(packet)    
    def handle_adventure_step(self, packet):
        return None

    
    # CS_ADVENTURE_BUY_TIMES
    @CallbackBase.callback(OP_CODE.CS_ADVENTURE_BUY_TIMES)
    def send_adventure_buy_times_decorate(self, code):
        packet = cs_adventure_buy_times()
        self.make_adventure_buy_times_packet(packet)
        self.mes_que[code] = packet
    # makeup adventure_buy_times packet
    def make_adventure_buy_times_packet(self, packet):
        return None
    # send adventure_buy_times
    def send_adventure_buy_times(self):
        self.dispatch(OP_CODE.CS_ADVENTURE_BUY_TIMES)(OP_CODE.CS_ADVENTURE_BUY_TIMES)
    
    # handle SC_ADVENTURE_BUY_TIMES
    @CallbackBase.callback(OP_CODE.SC_ADVENTURE_BUY_TIMES)
    def handle_adventure_buy_times_decorate(self, recv_buff):
        packet = sc_adventure_buy_times()
        packet.deserialize(recv_buff)
        return self.handle_adventure_buy_times(packet)    
    def handle_adventure_buy_times(self, packet):
        return None

    
    # CS_QUERY_RESERVER_SOLDIER
    @CallbackBase.callback(OP_CODE.CS_QUERY_RESERVER_SOLDIER)
    def send_query_reserver_soldier_decorate(self, code):
        packet = cs_query_reserver_soldier()
        self.make_query_reserver_soldier_packet(packet)
        self.mes_que[code] = packet
    # makeup query_reserver_soldier packet
    def make_query_reserver_soldier_packet(self, packet):
        return None
    # send query_reserver_soldier
    def send_query_reserver_soldier(self):
        self.dispatch(OP_CODE.CS_QUERY_RESERVER_SOLDIER)(OP_CODE.CS_QUERY_RESERVER_SOLDIER)
    
    # handle SC_QUERY_RESERVER_SOLDIER
    @CallbackBase.callback(OP_CODE.SC_QUERY_RESERVER_SOLDIER)
    def handle_query_reserver_soldier_decorate(self, recv_buff):
        packet = sc_query_reserver_soldier()
        packet.deserialize(recv_buff)
        return self.handle_query_reserver_soldier(packet)    
    def handle_query_reserver_soldier(self, packet):
        return None

    
    # CS_USE_RESERVER_SOLDIER
    @CallbackBase.callback(OP_CODE.CS_USE_RESERVER_SOLDIER)
    def send_use_reserver_soldier_decorate(self, code):
        packet = cs_use_reserver_soldier()
        self.make_use_reserver_soldier_packet(packet)
        self.mes_que[code] = packet
    # makeup use_reserver_soldier packet
    def make_use_reserver_soldier_packet(self, packet):
        return None
    # send use_reserver_soldier
    def send_use_reserver_soldier(self):
        self.dispatch(OP_CODE.CS_USE_RESERVER_SOLDIER)(OP_CODE.CS_USE_RESERVER_SOLDIER)
    
    # handle SC_USE_RESERVER_SOLDIER
    @CallbackBase.callback(OP_CODE.SC_USE_RESERVER_SOLDIER)
    def handle_use_reserver_soldier_decorate(self, recv_buff):
        packet = sc_use_reserver_soldier()
        packet.deserialize(recv_buff)
        return self.handle_use_reserver_soldier(packet)    
    def handle_use_reserver_soldier(self, packet):
        return None

    
    # CS_ADVENTURE_EXIT
    @CallbackBase.callback(OP_CODE.CS_ADVENTURE_EXIT)
    def send_adventure_exit_decorate(self, code):
        packet = cs_adventure_exit()
        self.make_adventure_exit_packet(packet)
        self.mes_que[code] = packet
    # makeup adventure_exit packet
    def make_adventure_exit_packet(self, packet):
        return None
    # send adventure_exit
    def send_adventure_exit(self):
        self.dispatch(OP_CODE.CS_ADVENTURE_EXIT)(OP_CODE.CS_ADVENTURE_EXIT)
    
    # handle SC_ADVENTURE_EXIT
    @CallbackBase.callback(OP_CODE.SC_ADVENTURE_EXIT)
    def handle_adventure_exit_decorate(self, recv_buff):
        packet = sc_adventure_exit()
        packet.deserialize(recv_buff)
        return self.handle_adventure_exit(packet)    
    def handle_adventure_exit(self, packet):
        return None

    
    # CS_GET_RAFFLE_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_RAFFLE_LIST)
    def send_get_raffle_list_decorate(self, code):
        packet = cs_get_raffle_list()
        self.make_get_raffle_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_raffle_list packet
    def make_get_raffle_list_packet(self, packet):
        return None
    # send get_raffle_list
    def send_get_raffle_list(self):
        self.dispatch(OP_CODE.CS_GET_RAFFLE_LIST)(OP_CODE.CS_GET_RAFFLE_LIST)
    
    # handle SC_GET_RAFFLE_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_RAFFLE_LIST)
    def handle_get_raffle_list_decorate(self, recv_buff):
        packet = sc_get_raffle_list()
        packet.deserialize(recv_buff)
        return self.handle_get_raffle_list(packet)    
    def handle_get_raffle_list(self, packet):
        return None

    
    # CS_RAFFLE_DRAW
    @CallbackBase.callback(OP_CODE.CS_RAFFLE_DRAW)
    def send_raffle_draw_decorate(self, code):
        packet = cs_raffle_draw()
        self.make_raffle_draw_packet(packet)
        self.mes_que[code] = packet
    # makeup raffle_draw packet
    def make_raffle_draw_packet(self, packet):
        return None
    # send raffle_draw
    def send_raffle_draw(self):
        self.dispatch(OP_CODE.CS_RAFFLE_DRAW)(OP_CODE.CS_RAFFLE_DRAW)
    
    # handle SC_RAFFLE_DRAW
    @CallbackBase.callback(OP_CODE.SC_RAFFLE_DRAW)
    def handle_raffle_draw_decorate(self, recv_buff):
        packet = sc_raffle_draw()
        packet.deserialize(recv_buff)
        return self.handle_raffle_draw(packet)    
    def handle_raffle_draw(self, packet):
        return None

    
    # CS_HERO_CHIP_REPLACE
    @CallbackBase.callback(OP_CODE.CS_HERO_CHIP_REPLACE)
    def send_hero_chip_replace_decorate(self, code):
        packet = cs_hero_chip_replace()
        self.make_hero_chip_replace_packet(packet)
        self.mes_que[code] = packet
    # makeup hero_chip_replace packet
    def make_hero_chip_replace_packet(self, packet):
        return None
    # send hero_chip_replace
    def send_hero_chip_replace(self):
        self.dispatch(OP_CODE.CS_HERO_CHIP_REPLACE)(OP_CODE.CS_HERO_CHIP_REPLACE)
    
    # handle SC_HERO_CHIP_REPLACE
    @CallbackBase.callback(OP_CODE.SC_HERO_CHIP_REPLACE)
    def handle_hero_chip_replace_decorate(self, recv_buff):
        packet = sc_hero_chip_replace()
        packet.deserialize(recv_buff)
        return self.handle_hero_chip_replace(packet)    
    def handle_hero_chip_replace(self, packet):
        return None

    
    # CS_GET_RAFFLE_DATA
    @CallbackBase.callback(OP_CODE.CS_GET_RAFFLE_DATA)
    def send_get_raffle_data_decorate(self, code):
        packet = cs_get_raffle_data()
        self.make_get_raffle_data_packet(packet)
        self.mes_que[code] = packet
    # makeup get_raffle_data packet
    def make_get_raffle_data_packet(self, packet):
        return None
    # send get_raffle_data
    def send_get_raffle_data(self):
        self.dispatch(OP_CODE.CS_GET_RAFFLE_DATA)(OP_CODE.CS_GET_RAFFLE_DATA)
    
    # handle SC_GET_RAFFLE_DATA
    @CallbackBase.callback(OP_CODE.SC_GET_RAFFLE_DATA)
    def handle_get_raffle_data_decorate(self, recv_buff):
        packet = sc_get_raffle_data()
        packet.deserialize(recv_buff)
        return self.handle_get_raffle_data(packet)    
    def handle_get_raffle_data(self, packet):
        return None

    
    # CS_DEL_MAIL_LIST
    @CallbackBase.callback(OP_CODE.CS_DEL_MAIL_LIST)
    def send_del_mail_list_decorate(self, code):
        packet = cs_del_mail_list()
        self.make_del_mail_list_packet(packet)
        self.mes_que[code] = packet
    # makeup del_mail_list packet
    def make_del_mail_list_packet(self, packet):
        return None
    # send del_mail_list
    def send_del_mail_list(self):
        self.dispatch(OP_CODE.CS_DEL_MAIL_LIST)(OP_CODE.CS_DEL_MAIL_LIST)
    
    # handle SC_DEL_MAIL_LIST
    @CallbackBase.callback(OP_CODE.SC_DEL_MAIL_LIST)
    def handle_del_mail_list_decorate(self, recv_buff):
        packet = sc_del_mail_list()
        packet.deserialize(recv_buff)
        return self.handle_del_mail_list(packet)    
    def handle_del_mail_list(self, packet):
        return None

    
    # CS_ONE_KEY_MAIL_AFFIX_PICK
    @CallbackBase.callback(OP_CODE.CS_ONE_KEY_MAIL_AFFIX_PICK)
    def send_one_key_mail_affix_pick_decorate(self, code):
        packet = cs_one_key_mail_affix_pick()
        self.make_one_key_mail_affix_pick_packet(packet)
        self.mes_que[code] = packet
    # makeup one_key_mail_affix_pick packet
    def make_one_key_mail_affix_pick_packet(self, packet):
        return None
    # send one_key_mail_affix_pick
    def send_one_key_mail_affix_pick(self):
        self.dispatch(OP_CODE.CS_ONE_KEY_MAIL_AFFIX_PICK)(OP_CODE.CS_ONE_KEY_MAIL_AFFIX_PICK)
    
    # handle SC_ONE_KEY_MAIL_AFFIX_PICK
    @CallbackBase.callback(OP_CODE.SC_ONE_KEY_MAIL_AFFIX_PICK)
    def handle_one_key_mail_affix_pick_decorate(self, recv_buff):
        packet = sc_one_key_mail_affix_pick()
        packet.deserialize(recv_buff)
        return self.handle_one_key_mail_affix_pick(packet)    
    def handle_one_key_mail_affix_pick(self, packet):
        return None

    
    # CS_CORPS_RECOVER_PHY
    @CallbackBase.callback(OP_CODE.CS_CORPS_RECOVER_PHY)
    def send_corps_recover_phy_decorate(self, code):
        packet = cs_corps_recover_phy()
        self.make_corps_recover_phy_packet(packet)
        self.mes_que[code] = packet
    # makeup corps_recover_phy packet
    def make_corps_recover_phy_packet(self, packet):
        return None
    # send corps_recover_phy
    def send_corps_recover_phy(self):
        self.dispatch(OP_CODE.CS_CORPS_RECOVER_PHY)(OP_CODE.CS_CORPS_RECOVER_PHY)
    
    # handle SC_CORPS_RECOVER_PHY
    @CallbackBase.callback(OP_CODE.SC_CORPS_RECOVER_PHY)
    def handle_corps_recover_phy_decorate(self, recv_buff):
        packet = sc_corps_recover_phy()
        packet.deserialize(recv_buff)
        return self.handle_corps_recover_phy(packet)    
    def handle_corps_recover_phy(self, packet):
        return None

    
    # CS_ACCELERATE_GAME_EVENT
    @CallbackBase.callback(OP_CODE.CS_ACCELERATE_GAME_EVENT)
    def send_accelerate_game_event_decorate(self, code):
        packet = cs_accelerate_game_event()
        self.make_accelerate_game_event_packet(packet)
        self.mes_que[code] = packet
    # makeup accelerate_game_event packet
    def make_accelerate_game_event_packet(self, packet):
        return None
    # send accelerate_game_event
    def send_accelerate_game_event(self):
        self.dispatch(OP_CODE.CS_ACCELERATE_GAME_EVENT)(OP_CODE.CS_ACCELERATE_GAME_EVENT)
    
    # handle SC_ACCELERATE_GAME_EVENT
    @CallbackBase.callback(OP_CODE.SC_ACCELERATE_GAME_EVENT)
    def handle_accelerate_game_event_decorate(self, recv_buff):
        packet = sc_accelerate_game_event()
        packet.deserialize(recv_buff)
        return self.handle_accelerate_game_event(packet)    
    def handle_accelerate_game_event(self, packet):
        return None

    
    # CS_DISCOVERY_BUY_TIMES
    @CallbackBase.callback(OP_CODE.CS_DISCOVERY_BUY_TIMES)
    def send_discovery_buy_times_decorate(self, code):
        packet = cs_discovery_buy_times()
        self.make_discovery_buy_times_packet(packet)
        self.mes_que[code] = packet
    # makeup discovery_buy_times packet
    def make_discovery_buy_times_packet(self, packet):
        return None
    # send discovery_buy_times
    def send_discovery_buy_times(self):
        self.dispatch(OP_CODE.CS_DISCOVERY_BUY_TIMES)(OP_CODE.CS_DISCOVERY_BUY_TIMES)
    
    # handle SC_DISCOVERY_BUY_TIMES
    @CallbackBase.callback(OP_CODE.SC_DISCOVERY_BUY_TIMES)
    def handle_discovery_buy_times_decorate(self, recv_buff):
        packet = sc_discovery_buy_times()
        packet.deserialize(recv_buff)
        return self.handle_discovery_buy_times(packet)    
    def handle_discovery_buy_times(self, packet):
        return None

    
    # CS_GET_MISSION_BY_ENTRY
    @CallbackBase.callback(OP_CODE.CS_GET_MISSION_BY_ENTRY)
    def send_get_mission_by_entry_decorate(self, code):
        packet = cs_get_mission_by_entry()
        self.make_get_mission_by_entry_packet(packet)
        self.mes_que[code] = packet
    # makeup get_mission_by_entry packet
    def make_get_mission_by_entry_packet(self, packet):
        return None
    # send get_mission_by_entry
    def send_get_mission_by_entry(self):
        self.dispatch(OP_CODE.CS_GET_MISSION_BY_ENTRY)(OP_CODE.CS_GET_MISSION_BY_ENTRY)
    
    # handle SC_GET_MISSION_BY_ENTRY
    @CallbackBase.callback(OP_CODE.SC_GET_MISSION_BY_ENTRY)
    def handle_get_mission_by_entry_decorate(self, recv_buff):
        packet = sc_get_mission_by_entry()
        packet.deserialize(recv_buff)
        return self.handle_get_mission_by_entry(packet)    
    def handle_get_mission_by_entry(self, packet):
        return None

    
    # CS_HERO_RESET
    @CallbackBase.callback(OP_CODE.CS_HERO_RESET)
    def send_hero_reset_decorate(self, code):
        packet = cs_hero_reset()
        self.make_hero_reset_packet(packet)
        self.mes_que[code] = packet
    # makeup hero_reset packet
    def make_hero_reset_packet(self, packet):
        return None
    # send hero_reset
    def send_hero_reset(self):
        self.dispatch(OP_CODE.CS_HERO_RESET)(OP_CODE.CS_HERO_RESET)
    
    # handle SC_HERO_RESET
    @CallbackBase.callback(OP_CODE.SC_HERO_RESET)
    def handle_hero_reset_decorate(self, recv_buff):
        packet = sc_hero_reset()
        packet.deserialize(recv_buff)
        return self.handle_hero_reset(packet)    
    def handle_hero_reset(self, packet):
        return None

    
    # CS_HERO_RESET_INFO
    @CallbackBase.callback(OP_CODE.CS_HERO_RESET_INFO)
    def send_hero_reset_info_decorate(self, code):
        packet = cs_hero_reset_info()
        self.make_hero_reset_info_packet(packet)
        self.mes_que[code] = packet
    # makeup hero_reset_info packet
    def make_hero_reset_info_packet(self, packet):
        return None
    # send hero_reset_info
    def send_hero_reset_info(self):
        self.dispatch(OP_CODE.CS_HERO_RESET_INFO)(OP_CODE.CS_HERO_RESET_INFO)
    
    # handle SC_HERO_RESET_INFO
    @CallbackBase.callback(OP_CODE.SC_HERO_RESET_INFO)
    def handle_hero_reset_info_decorate(self, recv_buff):
        packet = sc_hero_reset_info()
        packet.deserialize(recv_buff)
        return self.handle_hero_reset_info(packet)    
    def handle_hero_reset_info(self, packet):
        return None

    
    # CS_GET_BLOCK_ARRAY_BY_INDEX
    @CallbackBase.callback(OP_CODE.CS_GET_BLOCK_ARRAY_BY_INDEX)
    def send_get_block_array_by_index_decorate(self, code):
        packet = cs_get_block_array_by_index()
        self.make_get_block_array_by_index_packet(packet)
        self.mes_que[code] = packet
    # makeup get_block_array_by_index packet
    def make_get_block_array_by_index_packet(self, packet):
        return None
    # send get_block_array_by_index
    def send_get_block_array_by_index(self):
        self.dispatch(OP_CODE.CS_GET_BLOCK_ARRAY_BY_INDEX)(OP_CODE.CS_GET_BLOCK_ARRAY_BY_INDEX)
    
    # handle SC_GET_BLOCK_ARRAY_BY_INDEX
    @CallbackBase.callback(OP_CODE.SC_GET_BLOCK_ARRAY_BY_INDEX)
    def handle_get_block_array_by_index_decorate(self, recv_buff):
        packet = sc_get_block_array_by_index()
        packet.deserialize(recv_buff)
        return self.handle_get_block_array_by_index(packet)    
    def handle_get_block_array_by_index(self, packet):
        return None

    
    # CS_BUY_RESERVER_SOLDIER
    @CallbackBase.callback(OP_CODE.CS_BUY_RESERVER_SOLDIER)
    def send_buy_reserver_soldier_decorate(self, code):
        packet = cs_buy_reserver_soldier()
        self.make_buy_reserver_soldier_packet(packet)
        self.mes_que[code] = packet
    # makeup buy_reserver_soldier packet
    def make_buy_reserver_soldier_packet(self, packet):
        return None
    # send buy_reserver_soldier
    def send_buy_reserver_soldier(self):
        self.dispatch(OP_CODE.CS_BUY_RESERVER_SOLDIER)(OP_CODE.CS_BUY_RESERVER_SOLDIER)
    
    # handle SC_BUY_RESERVER_SOLDIER
    @CallbackBase.callback(OP_CODE.SC_BUY_RESERVER_SOLDIER)
    def handle_buy_reserver_soldier_decorate(self, recv_buff):
        packet = sc_buy_reserver_soldier()
        packet.deserialize(recv_buff)
        return self.handle_buy_reserver_soldier(packet)    
    def handle_buy_reserver_soldier(self, packet):
        return None

    
    # CS_CORPS_CRUSADE
    @CallbackBase.callback(OP_CODE.CS_CORPS_CRUSADE)
    def send_corps_crusade_decorate(self, code):
        packet = cs_corps_crusade()
        self.make_corps_crusade_packet(packet)
        self.mes_que[code] = packet
    # makeup corps_crusade packet
    def make_corps_crusade_packet(self, packet):
        return None
    # send corps_crusade
    def send_corps_crusade(self):
        self.dispatch(OP_CODE.CS_CORPS_CRUSADE)(OP_CODE.CS_CORPS_CRUSADE)
    
    # handle SC_CORPS_CRUSADE
    @CallbackBase.callback(OP_CODE.SC_CORPS_CRUSADE)
    def handle_corps_crusade_decorate(self, recv_buff):
        packet = sc_corps_crusade()
        packet.deserialize(recv_buff)
        return self.handle_corps_crusade(packet)    
    def handle_corps_crusade(self, packet):
        return None

    
    # CS_GET_WTQUEST_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_WTQUEST_LIST)
    def send_get_wtquest_list_decorate(self, code):
        packet = cs_get_wtquest_list()
        self.make_get_wtquest_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_wtquest_list packet
    def make_get_wtquest_list_packet(self, packet):
        return None
    # send get_wtquest_list
    def send_get_wtquest_list(self):
        self.dispatch(OP_CODE.CS_GET_WTQUEST_LIST)(OP_CODE.CS_GET_WTQUEST_LIST)
    
    # handle SC_GET_WTQUEST_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_WTQUEST_LIST)
    def handle_get_wtquest_list_decorate(self, recv_buff):
        packet = sc_get_wtquest_list()
        packet.deserialize(recv_buff)
        return self.handle_get_wtquest_list(packet)    
    def handle_get_wtquest_list(self, packet):
        return None

    
    # CS_GET_WTQUEST_REWARDS
    @CallbackBase.callback(OP_CODE.CS_GET_WTQUEST_REWARDS)
    def send_get_wtquest_rewards_decorate(self, code):
        packet = cs_get_wtquest_rewards()
        self.make_get_wtquest_rewards_packet(packet)
        self.mes_que[code] = packet
    # makeup get_wtquest_rewards packet
    def make_get_wtquest_rewards_packet(self, packet):
        return None
    # send get_wtquest_rewards
    def send_get_wtquest_rewards(self):
        self.dispatch(OP_CODE.CS_GET_WTQUEST_REWARDS)(OP_CODE.CS_GET_WTQUEST_REWARDS)
    
    # handle SC_GET_WTQUEST_REWARDS
    @CallbackBase.callback(OP_CODE.SC_GET_WTQUEST_REWARDS)
    def handle_get_wtquest_rewards_decorate(self, recv_buff):
        packet = sc_get_wtquest_rewards()
        packet.deserialize(recv_buff)
        return self.handle_get_wtquest_rewards(packet)    
    def handle_get_wtquest_rewards(self, packet):
        return None

    
    # CS_GET_WT_GUILD_RANK
    @CallbackBase.callback(OP_CODE.CS_GET_WT_GUILD_RANK)
    def send_get_wt_guild_rank_decorate(self, code):
        packet = cs_get_wt_guild_rank()
        self.make_get_wt_guild_rank_packet(packet)
        self.mes_que[code] = packet
    # makeup get_wt_guild_rank packet
    def make_get_wt_guild_rank_packet(self, packet):
        return None
    # send get_wt_guild_rank
    def send_get_wt_guild_rank(self):
        self.dispatch(OP_CODE.CS_GET_WT_GUILD_RANK)(OP_CODE.CS_GET_WT_GUILD_RANK)
    
    # handle SC_GET_WT_GUILD_RANK
    @CallbackBase.callback(OP_CODE.SC_GET_WT_GUILD_RANK)
    def handle_get_wt_guild_rank_decorate(self, recv_buff):
        packet = sc_get_wt_guild_rank()
        packet.deserialize(recv_buff)
        return self.handle_get_wt_guild_rank(packet)    
    def handle_get_wt_guild_rank(self, packet):
        return None

    
    # CS_GET_WT_USER_RANK
    @CallbackBase.callback(OP_CODE.CS_GET_WT_USER_RANK)
    def send_get_wt_user_rank_decorate(self, code):
        packet = cs_get_wt_user_rank()
        self.make_get_wt_user_rank_packet(packet)
        self.mes_que[code] = packet
    # makeup get_wt_user_rank packet
    def make_get_wt_user_rank_packet(self, packet):
        return None
    # send get_wt_user_rank
    def send_get_wt_user_rank(self):
        self.dispatch(OP_CODE.CS_GET_WT_USER_RANK)(OP_CODE.CS_GET_WT_USER_RANK)
    
    # handle SC_GET_WT_USER_RANK
    @CallbackBase.callback(OP_CODE.SC_GET_WT_USER_RANK)
    def handle_get_wt_user_rank_decorate(self, recv_buff):
        packet = sc_get_wt_user_rank()
        packet.deserialize(recv_buff)
        return self.handle_get_wt_user_rank(packet)    
    def handle_get_wt_user_rank(self, packet):
        return None

    
    # CS_HERO_BUY_SPIRIT
    @CallbackBase.callback(OP_CODE.CS_HERO_BUY_SPIRIT)
    def send_hero_buy_spirit_decorate(self, code):
        packet = cs_hero_buy_spirit()
        self.make_hero_buy_spirit_packet(packet)
        self.mes_que[code] = packet
    # makeup hero_buy_spirit packet
    def make_hero_buy_spirit_packet(self, packet):
        return None
    # send hero_buy_spirit
    def send_hero_buy_spirit(self):
        self.dispatch(OP_CODE.CS_HERO_BUY_SPIRIT)(OP_CODE.CS_HERO_BUY_SPIRIT)
    
    # handle SC_HERO_BUY_SPIRIT
    @CallbackBase.callback(OP_CODE.SC_HERO_BUY_SPIRIT)
    def handle_hero_buy_spirit_decorate(self, recv_buff):
        packet = sc_hero_buy_spirit()
        packet.deserialize(recv_buff)
        return self.handle_hero_buy_spirit(packet)    
    def handle_hero_buy_spirit(self, packet):
        return None

    
    # CS_QUERY_REBEL
    @CallbackBase.callback(OP_CODE.CS_QUERY_REBEL)
    def send_query_rebel_decorate(self, code):
        packet = cs_query_rebel()
        self.make_query_rebel_packet(packet)
        self.mes_que[code] = packet
    # makeup query_rebel packet
    def make_query_rebel_packet(self, packet):
        return None
    # send query_rebel
    def send_query_rebel(self):
        self.dispatch(OP_CODE.CS_QUERY_REBEL)(OP_CODE.CS_QUERY_REBEL)
    
    # handle SC_QUERY_REBEL
    @CallbackBase.callback(OP_CODE.SC_QUERY_REBEL)
    def handle_query_rebel_decorate(self, recv_buff):
        packet = sc_query_rebel()
        packet.deserialize(recv_buff)
        return self.handle_query_rebel(packet)    
    def handle_query_rebel(self, packet):
        return None

    
    # CS_REBEL_SEARCH
    @CallbackBase.callback(OP_CODE.CS_REBEL_SEARCH)
    def send_rebel_search_decorate(self, code):
        packet = cs_rebel_search()
        self.make_rebel_search_packet(packet)
        self.mes_que[code] = packet
    # makeup rebel_search packet
    def make_rebel_search_packet(self, packet):
        return None
    # send rebel_search
    def send_rebel_search(self):
        self.dispatch(OP_CODE.CS_REBEL_SEARCH)(OP_CODE.CS_REBEL_SEARCH)
    
    # handle SC_REBEL_SEARCH
    @CallbackBase.callback(OP_CODE.SC_REBEL_SEARCH)
    def handle_rebel_search_decorate(self, recv_buff):
        packet = sc_rebel_search()
        packet.deserialize(recv_buff)
        return self.handle_rebel_search(packet)    
    def handle_rebel_search(self, packet):
        return None

    
    # CS_REBEL_BUY_TIMES
    @CallbackBase.callback(OP_CODE.CS_REBEL_BUY_TIMES)
    def send_rebel_buy_times_decorate(self, code):
        packet = cs_rebel_buy_times()
        self.make_rebel_buy_times_packet(packet)
        self.mes_que[code] = packet
    # makeup rebel_buy_times packet
    def make_rebel_buy_times_packet(self, packet):
        return None
    # send rebel_buy_times
    def send_rebel_buy_times(self):
        self.dispatch(OP_CODE.CS_REBEL_BUY_TIMES)(OP_CODE.CS_REBEL_BUY_TIMES)
    
    # handle SC_REBEL_BUY_TIMES
    @CallbackBase.callback(OP_CODE.SC_REBEL_BUY_TIMES)
    def handle_rebel_buy_times_decorate(self, recv_buff):
        packet = sc_rebel_buy_times()
        packet.deserialize(recv_buff)
        return self.handle_rebel_buy_times(packet)    
    def handle_rebel_buy_times(self, packet):
        return None

    
    # CS_KILLPOINT_REWARD
    @CallbackBase.callback(OP_CODE.CS_KILLPOINT_REWARD)
    def send_killpoint_reward_decorate(self, code):
        packet = cs_killpoint_reward()
        self.make_killpoint_reward_packet(packet)
        self.mes_que[code] = packet
    # makeup killpoint_reward packet
    def make_killpoint_reward_packet(self, packet):
        return None
    # send killpoint_reward
    def send_killpoint_reward(self):
        self.dispatch(OP_CODE.CS_KILLPOINT_REWARD)(OP_CODE.CS_KILLPOINT_REWARD)
    
    # handle SC_KILLPOINT_REWARD
    @CallbackBase.callback(OP_CODE.SC_KILLPOINT_REWARD)
    def handle_killpoint_reward_decorate(self, recv_buff):
        packet = sc_killpoint_reward()
        packet.deserialize(recv_buff)
        return self.handle_killpoint_reward(packet)    
    def handle_killpoint_reward(self, packet):
        return None

    
    # CS_KILLPOINT_LVUP
    @CallbackBase.callback(OP_CODE.CS_KILLPOINT_LVUP)
    def send_killpoint_lvup_decorate(self, code):
        packet = cs_killpoint_lvup()
        self.make_killpoint_lvup_packet(packet)
        self.mes_que[code] = packet
    # makeup killpoint_lvup packet
    def make_killpoint_lvup_packet(self, packet):
        return None
    # send killpoint_lvup
    def send_killpoint_lvup(self):
        self.dispatch(OP_CODE.CS_KILLPOINT_LVUP)(OP_CODE.CS_KILLPOINT_LVUP)
    
    # handle SC_KILLPOINT_LVUP
    @CallbackBase.callback(OP_CODE.SC_KILLPOINT_LVUP)
    def handle_killpoint_lvup_decorate(self, recv_buff):
        packet = sc_killpoint_lvup()
        packet.deserialize(recv_buff)
        return self.handle_killpoint_lvup(packet)    
    def handle_killpoint_lvup(self, packet):
        return None

    
    # CS_GET_GUILD_CRUSADE_CITY_RANK
    @CallbackBase.callback(OP_CODE.CS_GET_GUILD_CRUSADE_CITY_RANK)
    def send_get_guild_crusade_city_rank_decorate(self, code):
        packet = cs_get_guild_crusade_city_rank()
        self.make_get_guild_crusade_city_rank_packet(packet)
        self.mes_que[code] = packet
    # makeup get_guild_crusade_city_rank packet
    def make_get_guild_crusade_city_rank_packet(self, packet):
        return None
    # send get_guild_crusade_city_rank
    def send_get_guild_crusade_city_rank(self):
        self.dispatch(OP_CODE.CS_GET_GUILD_CRUSADE_CITY_RANK)(OP_CODE.CS_GET_GUILD_CRUSADE_CITY_RANK)
    
    # handle SC_GET_GUILD_CRUSADE_CITY_RANK
    @CallbackBase.callback(OP_CODE.SC_GET_GUILD_CRUSADE_CITY_RANK)
    def handle_get_guild_crusade_city_rank_decorate(self, recv_buff):
        packet = sc_get_guild_crusade_city_rank()
        packet.deserialize(recv_buff)
        return self.handle_get_guild_crusade_city_rank(packet)    
    def handle_get_guild_crusade_city_rank(self, packet):
        return None

    
    # CS_CORPS_EXCHANGE_HERO_INCORP
    @CallbackBase.callback(OP_CODE.CS_CORPS_EXCHANGE_HERO_INCORP)
    def send_corps_exchange_hero_incorp_decorate(self, code):
        packet = cs_corps_exchange_hero_incorp()
        self.make_corps_exchange_hero_incorp_packet(packet)
        self.mes_que[code] = packet
    # makeup corps_exchange_hero_incorp packet
    def make_corps_exchange_hero_incorp_packet(self, packet):
        return None
    # send corps_exchange_hero_incorp
    def send_corps_exchange_hero_incorp(self):
        self.dispatch(OP_CODE.CS_CORPS_EXCHANGE_HERO_INCORP)(OP_CODE.CS_CORPS_EXCHANGE_HERO_INCORP)
    
    # handle SC_CORPS_EXCHANGE_HERO_INCORP
    @CallbackBase.callback(OP_CODE.SC_CORPS_EXCHANGE_HERO_INCORP)
    def handle_corps_exchange_hero_incorp_decorate(self, recv_buff):
        packet = sc_corps_exchange_hero_incorp()
        packet.deserialize(recv_buff)
        return self.handle_corps_exchange_hero_incorp(packet)    
    def handle_corps_exchange_hero_incorp(self, packet):
        return None

    
    # CS_GET_GUILD_GIFT_LIST
    @CallbackBase.callback(OP_CODE.CS_GET_GUILD_GIFT_LIST)
    def send_get_guild_gift_list_decorate(self, code):
        packet = cs_get_guild_gift_list()
        self.make_get_guild_gift_list_packet(packet)
        self.mes_que[code] = packet
    # makeup get_guild_gift_list packet
    def make_get_guild_gift_list_packet(self, packet):
        return None
    # send get_guild_gift_list
    def send_get_guild_gift_list(self):
        self.dispatch(OP_CODE.CS_GET_GUILD_GIFT_LIST)(OP_CODE.CS_GET_GUILD_GIFT_LIST)
    
    # handle SC_GET_GUILD_GIFT_LIST
    @CallbackBase.callback(OP_CODE.SC_GET_GUILD_GIFT_LIST)
    def handle_get_guild_gift_list_decorate(self, recv_buff):
        packet = sc_get_guild_gift_list()
        packet.deserialize(recv_buff)
        return self.handle_get_guild_gift_list(packet)    
    def handle_get_guild_gift_list(self, packet):
        return None

    
    # CS_REWARD_GUILD_GIFT
    @CallbackBase.callback(OP_CODE.CS_REWARD_GUILD_GIFT)
    def send_reward_guild_gift_decorate(self, code):
        packet = cs_reward_guild_gift()
        self.make_reward_guild_gift_packet(packet)
        self.mes_que[code] = packet
    # makeup reward_guild_gift packet
    def make_reward_guild_gift_packet(self, packet):
        return None
    # send reward_guild_gift
    def send_reward_guild_gift(self):
        self.dispatch(OP_CODE.CS_REWARD_GUILD_GIFT)(OP_CODE.CS_REWARD_GUILD_GIFT)
    
    # handle SC_REWARD_GUILD_GIFT
    @CallbackBase.callback(OP_CODE.SC_REWARD_GUILD_GIFT)
    def handle_reward_guild_gift_decorate(self, recv_buff):
        packet = sc_reward_guild_gift()
        packet.deserialize(recv_buff)
        return self.handle_reward_guild_gift(packet)    
    def handle_reward_guild_gift(self, packet):
        return None

    
    # CS_SEASON_CHAT
    @CallbackBase.callback(OP_CODE.CS_SEASON_CHAT)
    def send_season_chat_decorate(self, code):
        packet = cs_season_chat()
        self.make_season_chat_packet(packet)
        self.mes_que[code] = packet
    # makeup season_chat packet
    def make_season_chat_packet(self, packet):
        return None
    # send season_chat
    def send_season_chat(self):
        self.dispatch(OP_CODE.CS_SEASON_CHAT)(OP_CODE.CS_SEASON_CHAT)
    
    # handle SC_SEASON_CHAT
    @CallbackBase.callback(OP_CODE.SC_SEASON_CHAT)
    def handle_season_chat_decorate(self, recv_buff):
        packet = sc_season_chat()
        packet.deserialize(recv_buff)
        return self.handle_season_chat(packet)    
    def handle_season_chat(self, packet):
        return None

    
    # CS_OPENID_REQ
    @CallbackBase.callback(OP_CODE.CS_OPENID_REQ)
    def send_openid_req_decorate(self, code):
        packet = cs_openid_req()
        self.make_openid_req_packet(packet)
        self.mes_que[code] = packet
    # makeup openid_req packet
    def make_openid_req_packet(self, packet):
        return None
    # send openid_req
    def send_openid_req(self):
        self.dispatch(OP_CODE.CS_OPENID_REQ)(OP_CODE.CS_OPENID_REQ)
    
    # handle SC_OPENID_REQ
    @CallbackBase.callback(OP_CODE.SC_OPENID_REQ)
    def handle_openid_req_decorate(self, recv_buff):
        packet = sc_openid_req()
        packet.deserialize(recv_buff)
        return self.handle_openid_req(packet)    
    def handle_openid_req(self, packet):
        return None

    
    # handle SCHAT_HERAT_BEAT
    @CallbackBase.callback(OP_CODE.SCHAT_HERAT_BEAT)
    def handle_at_herat_beat_decorate(self, recv_buff):
        packet = schat_herat_beat()
        packet.deserialize(recv_buff)
        return self.handle_at_herat_beat(packet)    
    def handle_at_herat_beat(self, packet):
        return None

    
    # CS_QUERY_BALANCE
    @CallbackBase.callback(OP_CODE.CS_QUERY_BALANCE)
    def send_query_balance_decorate(self, code):
        packet = cs_query_balance()
        self.make_query_balance_packet(packet)
        self.mes_que[code] = packet
    # makeup query_balance packet
    def make_query_balance_packet(self, packet):
        return None
    # send query_balance
    def send_query_balance(self):
        self.dispatch(OP_CODE.CS_QUERY_BALANCE)(OP_CODE.CS_QUERY_BALANCE)
    
    # handle SC_QUERY_BALANCE
    @CallbackBase.callback(OP_CODE.SC_QUERY_BALANCE)
    def handle_query_balance_decorate(self, recv_buff):
        packet = sc_query_balance()
        packet.deserialize(recv_buff)
        return self.handle_query_balance(packet)    
    def handle_query_balance(self, packet):
        return None

    
    # CS_GET_MAP_COLOR
    @CallbackBase.callback(OP_CODE.CS_GET_MAP_COLOR)
    def send_get_map_color_decorate(self, code):
        packet = cs_get_map_color()
        self.make_get_map_color_packet(packet)
        self.mes_que[code] = packet
    # makeup get_map_color packet
    def make_get_map_color_packet(self, packet):
        return None
    # send get_map_color
    def send_get_map_color(self):
        self.dispatch(OP_CODE.CS_GET_MAP_COLOR)(OP_CODE.CS_GET_MAP_COLOR)
    
    # handle SC_GET_MAP_COLOR
    @CallbackBase.callback(OP_CODE.SC_GET_MAP_COLOR)
    def handle_get_map_color_decorate(self, recv_buff):
        packet = sc_get_map_color()
        packet.deserialize(recv_buff)
        return self.handle_get_map_color(packet)    
    def handle_get_map_color(self, packet):
        return None

    
    # CS_LUCKY_TREASUER_REQ
    @CallbackBase.callback(OP_CODE.CS_LUCKY_TREASUER_REQ)
    def send_lucky_treasuer_req_decorate(self, code):
        packet = cs_lucky_treasuer_req()
        self.make_lucky_treasuer_req_packet(packet)
        self.mes_que[code] = packet
    # makeup lucky_treasuer_req packet
    def make_lucky_treasuer_req_packet(self, packet):
        return None
    # send lucky_treasuer_req
    def send_lucky_treasuer_req(self):
        self.dispatch(OP_CODE.CS_LUCKY_TREASUER_REQ)(OP_CODE.CS_LUCKY_TREASUER_REQ)
    
    # handle SC_LUCKY_TREASUER_REQ
    @CallbackBase.callback(OP_CODE.SC_LUCKY_TREASUER_REQ)
    def handle_lucky_treasuer_req_decorate(self, recv_buff):
        packet = sc_lucky_treasuer_req()
        packet.deserialize(recv_buff)
        return self.handle_lucky_treasuer_req(packet)    
    def handle_lucky_treasuer_req(self, packet):
        return None

    
    # CS_LUCKY_GETBOX_REQ
    @CallbackBase.callback(OP_CODE.CS_LUCKY_GETBOX_REQ)
    def send_lucky_getbox_req_decorate(self, code):
        packet = cs_lucky_getbox_req()
        self.make_lucky_getbox_req_packet(packet)
        self.mes_que[code] = packet
    # makeup lucky_getbox_req packet
    def make_lucky_getbox_req_packet(self, packet):
        return None
    # send lucky_getbox_req
    def send_lucky_getbox_req(self):
        self.dispatch(OP_CODE.CS_LUCKY_GETBOX_REQ)(OP_CODE.CS_LUCKY_GETBOX_REQ)
    
    # handle SC_LUCKY_GETBOX_REQ
    @CallbackBase.callback(OP_CODE.SC_LUCKY_GETBOX_REQ)
    def handle_lucky_getbox_req_decorate(self, recv_buff):
        packet = sc_lucky_getbox_req()
        packet.deserialize(recv_buff)
        return self.handle_lucky_getbox_req(packet)    
    def handle_lucky_getbox_req(self, packet):
        return None

    