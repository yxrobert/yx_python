from basetype import *
class e_op_result(enum):
	pass

class e_op_result_ok(e_op_result):
	def __init__(self):
		self.value=0

class e_op_result_re_login(e_op_result):
	def __init__(self):
		self.value=1

class e_op_result_re_create_account(e_op_result):
	def __init__(self):
		self.value=2

class e_op_result_low_version(e_op_result):
	def __init__(self):
		self.value=3

class e_op_result_hig_version(e_op_result):
	def __init__(self):
		self.value=4

class e_op_result_err(e_op_result):
	def __init__(self):
		self.value=5

class e_op_result_too_frequently(e_op_result):
	def __init__(self):
		self.value=6

class e_op_result_re_load(e_op_result):
	def __init__(self):
		self.value=7

class e_op_result_kick(e_op_result):
	def __init__(self):
		self.value=8

class e_op_result_level_limit(e_op_result):
	def __init__(self):
		self.value=9

class e_op_result_illegal_char(e_op_result):
	def __init__(self):
		self.value=10

class e_op_result_ver_err(e_op_result):
	def __init__(self):
		self.value=11

class e_op_result_ver_err_0(e_op_result):
	def __init__(self):
		self.value=12

class e_op_result_ver_err_1(e_op_result):
	def __init__(self):
		self.value=13

class e_op_result_ver_err_2(e_op_result):
	def __init__(self):
		self.value=14

class e_op_result_ver_err_3(e_op_result):
	def __init__(self):
		self.value=15

class e_op_result_repeated_req(e_op_result):
	def __init__(self):
		self.value=16

class e_op_result_reach_tps_limit(e_op_result):
	def __init__(self):
		self.value=17

class e_op_result_lock_mutex_failed(e_op_result):
	def __init__(self):
		self.value=18

class e_op_result_acc_frozen(e_op_result):
	def __init__(self):
		self.value=19

class e_op_result_target_id_not_exist(e_op_result):
	def __init__(self):
		self.value=20

class e_op_result_login_failed(e_op_result):
	def __init__(self):
		self.value=21

class e_op_result_login_s(e_op_result):
	def __init__(self):
		self.value=22

class e_op_result_login_nochar(e_op_result):
	def __init__(self):
		self.value=23

class e_op_result_use_tip_msg(e_op_result):
	def __init__(self):
		self.value=24

class e_op_result_gm_kick(e_op_result):
	def __init__(self):
		self.value=25

class e_op_result_register_failed(e_op_result):
	def __init__(self):
		self.value=26

class e_op_result_register_success(e_op_result):
	def __init__(self):
		self.value=27

class e_op_result_wood_not_enough(e_op_result):
	def __init__(self):
		self.value=28

class e_op_result_stone_not_enough(e_op_result):
	def __init__(self):
		self.value=29

class e_op_result_iron_not_enough(e_op_result):
	def __init__(self):
		self.value=30

class e_op_result_grain_not_enough(e_op_result):
	def __init__(self):
		self.value=31

class e_op_result_copper_not_enough(e_op_result):
	def __init__(self):
		self.value=32

class e_op_result_oil_not_enough(e_op_result):
	def __init__(self):
		self.value=33

class e_op_result_gold_coin_not_enough(e_op_result):
	def __init__(self):
		self.value=34

class e_op_result_building_max_lv(e_op_result):
	def __init__(self):
		self.value=35

class e_op_result_building_queue_full(e_op_result):
	def __init__(self):
		self.value=36

class e_op_result_prebuilding_lv_limit(e_op_result):
	def __init__(self):
		self.value=37

class e_op_result_building_lvuping_castle_move(e_op_result):
	def __init__(self):
		self.value=38

class e_op_result_building_lvup_finished(e_op_result):
	def __init__(self):
		self.value=39

class e_op_result_block_discard_type_err(e_op_result):
	def __init__(self):
		self.value=40

class e_op_result_crop_soldier_limit(e_op_result):
	def __init__(self):
		self.value=41

class e_op_result_soldier_type_locked(e_op_result):
	def __init__(self):
		self.value=42

class e_op_result_parameter_err(e_op_result):
	def __init__(self):
		self.value=43

class e_op_result_none_soldier_to_dismiss(e_op_result):
	def __init__(self):
		self.value=44

class e_op_result_none_conscript_soldier_to_cancel(e_op_result):
	def __init__(self):
		self.value=45

class e_op_result_need_dismiss_soldier_first(e_op_result):
	def __init__(self):
		self.value=46

class e_op_result_item_not_enough(e_op_result):
	def __init__(self):
		self.value=47

class e_op_result_item_num_full(e_op_result):
	def __init__(self):
		self.value=48

class e_op_result_castle_centre(e_op_result):
	def __init__(self):
		self.value=49

class e_op_result_corps_index_error(e_op_result):
	def __init__(self):
		self.value=50

class e_op_result_corps_busy(e_op_result):
	def __init__(self):
		self.value=51

class e_op_result_block_be_self(e_op_result):
	def __init__(self):
		self.value=52

class e_op_result_block_not_mine(e_op_result):
	def __init__(self):
		self.value=53

class e_op_result_block_index_error(e_op_result):
	def __init__(self):
		self.value=54

class e_op_result_block_cant_build(e_op_result):
	def __init__(self):
		self.value=55

class e_op_result_block_building_type_error(e_op_result):
	def __init__(self):
		self.value=56

class e_op_result_medal_slot_isfull(e_op_result):
	def __init__(self):
		self.value=57

class e_op_result_corps_guarding(e_op_result):
	def __init__(self):
		self.value=58

class e_op_result_block_protect(e_op_result):
	def __init__(self):
		self.value=59

class e_op_result_fort_building(e_op_result):
	def __init__(self):
		self.value=60

class e_op_result_fort_not_exist(e_op_result):
	def __init__(self):
		self.value=61

class e_op_result_corps_not_home(e_op_result):
	def __init__(self):
		self.value=62

class e_op_result_corps_not_fort(e_op_result):
	def __init__(self):
		self.value=63

class e_op_result_not_time_to_levy_tax(e_op_result):
	def __init__(self):
		self.value=64

class e_op_result_max_levy_tax_times(e_op_result):
	def __init__(self):
		self.value=65

class e_op_result_silver_coin_not_enough(e_op_result):
	def __init__(self):
		self.value=66

class e_op_result_hero_is_training(e_op_result):
	def __init__(self):
		self.value=67

class e_op_result_hero_train_slot_is_full(e_op_result):
	def __init__(self):
		self.value=68

class e_op_result_hero_not_training(e_op_result):
	def __init__(self):
		self.value=69

class e_op_result_event_cant_be_discard(e_op_result):
	def __init__(self):
		self.value=70

class e_op_result_event_pass_discard_time(e_op_result):
	def __init__(self):
		self.value=71

class e_op_result_trap_is_building(e_op_result):
	def __init__(self):
		self.value=72

class e_op_result_trap_type_locked(e_op_result):
	def __init__(self):
		self.value=73

class e_op_result_trap_limit(e_op_result):
	def __init__(self):
		self.value=74

class e_op_result_trap_build_already_finish(e_op_result):
	def __init__(self):
		self.value=75

class e_op_result_corps_empty_hero(e_op_result):
	def __init__(self):
		self.value=76

class e_op_result_not_in_view(e_op_result):
	def __init__(self):
		self.value=77

class e_op_result_corps_count_limit(e_op_result):
	def __init__(self):
		self.value=78

class e_op_result_corps_hurt(e_op_result):
	def __init__(self):
		self.value=79

class e_op_battle_record_time_out(e_op_result):
	def __init__(self):
		self.value=80

class e_op_result_castle_area(e_op_result):
	def __init__(self):
		self.value=81

class e_op_result_need_pre_building(e_op_result):
	def __init__(self):
		self.value=82

class e_op_result_warehouse_overflow(e_op_result):
	def __init__(self):
		self.value=83

class e_op_result_result_lock_failed(e_op_result):
	def __init__(self):
		self.value=84

class e_op_result_error_event_id(e_op_result):
	def __init__(self):
		self.value=85

class e_op_result_be_invaded(e_op_result):
	def __init__(self):
		self.value=86

class e_op_result_not_be_invaded(e_op_result):
	def __init__(self):
		self.value=87

class e_op_result_nick_name_illegal(e_op_result):
	def __init__(self):
		self.value=88

class e_op_result_nick_name_exist(e_op_result):
	def __init__(self):
		self.value=89

class e_op_result_corps_dead(e_op_result):
	def __init__(self):
		self.value=90

class e_op_result_hero_exist(e_op_result):
	def __init__(self):
		self.value=91

class e_op_result_achi_processing(e_op_result):
	def __init__(self):
		self.value=92

class e_op_result_achi_close(e_op_result):
	def __init__(self):
		self.value=93

class e_op_result_guild_not_be(e_op_result):
	def __init__(self):
		self.value=94

class e_op_result_guild_be(e_op_result):
	def __init__(self):
		self.value=95

class e_op_result_tar_guild_be(e_op_result):
	def __init__(self):
		self.value=96

class e_op_result_guild_be_cd(e_op_result):
	def __init__(self):
		self.value=97

class e_op_result_guild_contribution_too_much(e_op_result):
	def __init__(self):
		self.value=98

class e_op_result_guild_application_repeated(e_op_result):
	def __init__(self):
		self.value=99

class e_op_result_guild_no_power(e_op_result):
	def __init__(self):
		self.value=100

class e_op_result_guild_is_full(e_op_result):
	def __init__(self):
		self.value=101

class e_op_result_mission_processing(e_op_result):
	def __init__(self):
		self.value=102

class e_op_result_mission_close(e_op_result):
	def __init__(self):
		self.value=103

class e_op_result_guild_position_full(e_op_result):
	def __init__(self):
		self.value=104

class e_op_result_guild_trans_time_err(e_op_result):
	def __init__(self):
		self.value=105

class e_op_result_guild_property(e_op_result):
	def __init__(self):
		self.value=106

class e_op_result_guild_mark_full(e_op_result):
	def __init__(self):
		self.value=107

class e_op_result_lottery_time_out(e_op_result):
	def __init__(self):
		self.value=108

class e_op_result_shop_buy_count_enouth(e_op_result):
	def __init__(self):
		self.value=109

class e_op_result_resource_full(e_op_result):
	def __init__(self):
		self.value=110

class e_op_result_hall_level_limit(e_op_result):
	def __init__(self):
		self.value=111

class e_op_result_hero_phy_not_enough(e_op_result):
	def __init__(self):
		self.value=112

class e_op_result_guild_relationship_full(e_op_result):
	def __init__(self):
		self.value=113

class e_op_result_hero_train_slot_locked(e_op_result):
	def __init__(self):
		self.value=114

class e_op_result_guild_group_had(e_op_result):
	def __init__(self):
		self.value=115

class e_op_result_guild_group_no_power(e_op_result):
	def __init__(self):
		self.value=116

class e_op_result_guild_group_someone_be(e_op_result):
	def __init__(self):
		self.value=117

class e_op_result_guild_group_not_be(e_op_result):
	def __init__(self):
		self.value=118

class e_op_result_guild_group_full(e_op_result):
	def __init__(self):
		self.value=119

class e_op_result_wait(e_op_result):
	def __init__(self):
		self.value=120

class e_op_result_hero_max_lv(e_op_result):
	def __init__(self):
		self.value=121

class e_op_result_in_inner_guild_channel(e_op_result):
	def __init__(self):
		self.value=122

class e_op_result_not_in_inner_guild_channel(e_op_result):
	def __init__(self):
		self.value=123

class e_op_result_not_channel_creator(e_op_result):
	def __init__(self):
		self.value=124

class e_op_result_channel_creator_cannot_quit(e_op_result):
	def __init__(self):
		self.value=125

class e_op_result_move_cd(e_op_result):
	def __init__(self):
		self.value=126

class e_op_result_mail_send_user_not_exist(e_op_result):
	def __init__(self):
		self.value=127

class e_op_result_guild_group_name_repeated(e_op_result):
	def __init__(self):
		self.value=128

class e_op_result_war_protected(e_op_result):
	def __init__(self):
		self.value=129

class e_op_result_guild_member_manager(e_op_result):
	def __init__(self):
		self.value=130

class e_op_result_guild_group_tar_had(e_op_result):
	def __init__(self):
		self.value=131

class e_op_result_world_channel_be_cd(e_op_result):
	def __init__(self):
		self.value=132

class e_op_result_do_nothing(e_op_result):
	def __init__(self):
		self.value=133

class e_op_result_guild_level_max(e_op_result):
	def __init__(self):
		self.value=134

class e_op_result_no_guild_no_invade(e_op_result):
	def __init__(self):
		self.value=135

class e_op_result_guard_home_cd(e_op_result):
	def __init__(self):
		self.value=136

class e_op_result_be_guard_home(e_op_result):
	def __init__(self):
		self.value=137

class e_op_result_hero_in_crop(e_op_result):
	def __init__(self):
		self.value=138

class e_op_result_hero_in_the_guarding(e_op_result):
	def __init__(self):
		self.value=139

class e_op_result_land_is_full(e_op_result):
	def __init__(self):
		self.value=140

class e_op_result_fort_is_full(e_op_result):
	def __init__(self):
		self.value=141

class e_op_result_castle_is_full(e_op_result):
	def __init__(self):
		self.value=142

class e_op_result_no_guild_no_city(e_op_result):
	def __init__(self):
		self.value=143

class e_op_result_city_is_mine(e_op_result):
	def __init__(self):
		self.value=144

class e_op_result_block_no_attach(e_op_result):
	def __init__(self):
		self.value=145

class e_op_result_crops_is_conscripting(e_op_result):
	def __init__(self):
		self.value=146

class e_op_result_tar_be_invaded(e_op_result):
	def __init__(self):
		self.value=147

class e_op_result_fame_upper_limit(e_op_result):
	def __init__(self):
		self.value=148

class e_op_result_tar_invaded(e_op_result):
	def __init__(self):
		self.value=149

class e_op_result_block_cant_smash(e_op_result):
	def __init__(self):
		self.value=150

class e_op_result_block_building(e_op_result):
	def __init__(self):
		self.value=151

class e_op_result_block_operating(e_op_result):
	def __init__(self):
		self.value=152

class e_op_result_season_not_open(e_op_result):
	def __init__(self):
		self.value=153

class e_op_result_build_not_in_range(e_op_result):
	def __init__(self):
		self.value=154

class e_op_result_not_be_guild_state(e_op_result):
	def __init__(self):
		self.value=155

class e_op_result_query_pay_ing(e_op_result):
	def __init__(self):
		self.value=156

class e_op_result_query_pay_success(e_op_result):
	def __init__(self):
		self.value=157

class e_op_result_login_account_no_activate(e_op_result):
	def __init__(self):
		self.value=158

class e_op_result_be_in_newbie_protect(e_op_result):
	def __init__(self):
		self.value=159

class e_op_result_change_nick_name_cd(e_op_result):
	def __init__(self):
		self.value=160

class e_op_result_lower_vip_lv(e_op_result):
	def __init__(self):
		self.value=161

class e_op_result_already_received(e_op_result):
	def __init__(self):
		self.value=162

class e_op_result_data_not_exist(e_op_result):
	def __init__(self):
		self.value=163

class e_op_result_guard_self(e_op_result):
	def __init__(self):
		self.value=164

class e_op_result_register_failed_user_full(e_op_result):
	def __init__(self):
		self.value=165

class e_op_result_miracle_no_effect(e_op_result):
	def __init__(self):
		self.value=166

class e_op_result_tar_be_invaded_2_no_fight(e_op_result):
	def __init__(self):
		self.value=167

class e_op_result_tar_be_invaded_2_no_guildapplication_process(e_op_result):
	def __init__(self):
		self.value=168

class e_op_result_tar_be_invaded_2_no_guild_transform(e_op_result):
	def __init__(self):
		self.value=169

class e_op_result_tar_be_invaded_2_no_guild_invite(e_op_result):
	def __init__(self):
		self.value=170

class e_op_result_tar_be_invaded_2_no_invitation_process(e_op_result):
	def __init__(self):
		self.value=171

class e_op_result_activity_over_time(e_op_result):
	def __init__(self):
		self.value=172

class e_op_result_building_lvuping(e_op_result):
	def __init__(self):
		self.value=173

class e_op_result_tech_queue_full(e_op_result):
	def __init__(self):
		self.value=174

class e_op_result_wandering_quit_guild_first(e_op_result):
	def __init__(self):
		self.value=175

class e_op_result_wandering_failed_user_full(e_op_result):
	def __init__(self):
		self.value=176

class e_op_result_hangup_ing(e_op_result):
	def __init__(self):
		self.value=177

class e_op_result_hangup_hero_ing(e_op_result):
	def __init__(self):
		self.value=178

class e_op_result_contribution_not_enough(e_op_result):
	def __init__(self):
		self.value=179

class e_op_result_shop_not_in_active(e_op_result):
	def __init__(self):
		self.value=180

class e_op_result_shop_not_enough_remain(e_op_result):
	def __init__(self):
		self.value=181

class e_op_result_shop_not_enough_fresh_times(e_op_result):
	def __init__(self):
		self.value=182

class e_op_result_wandering_be_cd(e_op_result):
	def __init__(self):
		self.value=183

class e_op_result_arena_formation_err(e_op_result):
	def __init__(self):
		self.value=184

class e_op_result_arena_times_err(e_op_result):
	def __init__(self):
		self.value=185

class e_op_result_arena_buy_times_err(e_op_result):
	def __init__(self):
		self.value=186

class e_op_result_tower_trival_times_short(e_op_result):
	def __init__(self):
		self.value=187

class e_op_result_tower_floor_locked(e_op_result):
	def __init__(self):
		self.value=188

class e_op_result_tower_floor_formation_error(e_op_result):
	def __init__(self):
		self.value=189

class e_op_result_block_not_main_castle(e_op_result):
	def __init__(self):
		self.value=190

class e_op_result_seize_protect(e_op_result):
	def __init__(self):
		self.value=191

class e_op_result_tar_out_range(e_op_result):
	def __init__(self):
		self.value=192

class e_op_result_tower_floor_pass(e_op_result):
	def __init__(self):
		self.value=193

class e_op_result_gift_wait(e_op_result):
	def __init__(self):
		self.value=194

class e_op_result_param_err(e_op_result):
	def __init__(self):
		self.value=195

class e_op_result_codenotexist(e_op_result):
	def __init__(self):
		self.value=196

class e_op_result_codeinvalid(e_op_result):
	def __init__(self):
		self.value=197

class e_op_result_alreadyuse(e_op_result):
	def __init__(self):
		self.value=198

class e_op_result_codetimeout(e_op_result):
	def __init__(self):
		self.value=199

class e_op_result_channel_not_join(e_op_result):
	def __init__(self):
		self.value=200

class e_op_result_server_not_join(e_op_result):
	def __init__(self):
		self.value=201

class e_op_result_alreadyuseother(e_op_result):
	def __init__(self):
		self.value=202

class e_op_result_nostart(e_op_result):
	def __init__(self):
		self.value=203

class e_op_result_arena_tar_change(e_op_result):
	def __init__(self):
		self.value=204

class e_op_result_arena_coin_not_enough(e_op_result):
	def __init__(self):
		self.value=205

class e_op_result_activity_coin_not_enough(e_op_result):
	def __init__(self):
		self.value=206

class e_op_result_fame_not_enough(e_op_result):
	def __init__(self):
		self.value=207

class e_op_result_force_not_enough(e_op_result):
	def __init__(self):
		self.value=208

class e_op_result_contribution_of_day_full(e_op_result):
	def __init__(self):
		self.value=209

class e_op_result_corps_phy_not_enough(e_op_result):
	def __init__(self):
		self.value=210

class e_op_result_shop_fresh_times_limit(e_op_result):
	def __init__(self):
		self.value=211

class e_op_result_arena_def_corps_change(e_op_result):
	def __init__(self):
		self.value=212

class e_op_result_arena_fight_timeline(e_op_result):
	def __init__(self):
		self.value=213

class e_op_result_storage_is_full(e_op_result):
	def __init__(self):
		self.value=214

class e_op_result_guild_command_is_full(e_op_result):
	def __init__(self):
		self.value=215

class e_op_result_enemy_formation_change(e_op_result):
	def __init__(self):
		self.value=216

class e_op_result_guild_command_tar_err(e_op_result):
	def __init__(self):
		self.value=217

class e_op_result_guild_command_running_err(e_op_result):
	def __init__(self):
		self.value=218

class e_op_result_stanima_upper_limit(e_op_result):
	def __init__(self):
		self.value=219

class e_op_result_guild_command_repeated(e_op_result):
	def __init__(self):
		self.value=220

class e_op_result_guild_command_cd(e_op_result):
	def __init__(self):
		self.value=221

class e_op_result_nobility_limit(e_op_result):
	def __init__(self):
		self.value=222

class e_op_result_match_rewarding(e_op_result):
	def __init__(self):
		self.value=223

class e_op_result_transform_soldier_err(e_op_result):
	def __init__(self):
		self.value=224

class e_op_result_month_card_outdate(e_op_result):
	def __init__(self):
		self.value=225

class e_op_result_month_card_reward_already(e_op_result):
	def __init__(self):
		self.value=226

class e_op_result_not_enough_buy_token_times(e_op_result):
	def __init__(self):
		self.value=227

class e_op_result_not_enough_token(e_op_result):
	def __init__(self):
		self.value=228

class e_op_result_res_building_is_full(e_op_result):
	def __init__(self):
		self.value=229

class e_op_result_shop_time_full(e_op_result):
	def __init__(self):
		self.value=230

class e_op_result_shop_refresh_month_card_need(e_op_result):
	def __init__(self):
		self.value=231

class e_op_result_user_mark_is_full(e_op_result):
	def __init__(self):
		self.value=232

class e_op_result_block_is_mark(e_op_result):
	def __init__(self):
		self.value=233

class e_op_result_hero_hungup_time_limit(e_op_result):
	def __init__(self):
		self.value=234

class e_op_result_guild_assisted(e_op_result):
	def __init__(self):
		self.value=235

class e_op_result_guild_changed(e_op_result):
	def __init__(self):
		self.value=236

class e_op_result_guild_assist_over(e_op_result):
	def __init__(self):
		self.value=237

class e_op_result_shop_close(e_op_result):
	def __init__(self):
		self.value=238

class e_op_result_dis_not_enough_times(e_op_result):
	def __init__(self):
		self.value=239

class e_op_result_dis_tar_out_range(e_op_result):
	def __init__(self):
		self.value=240

class e_op_result_dis_event_outdate(e_op_result):
	def __init__(self):
		self.value=241

class e_op_result_dis_event_be_rob(e_op_result):
	def __init__(self):
		self.value=242

class e_op_result_dis_rob_out_range(e_op_result):
	def __init__(self):
		self.value=243

class e_op_result_dis_not_enough_rob_times(e_op_result):
	def __init__(self):
		self.value=244

class e_op_result_hero_not_enough_phy(e_op_result):
	def __init__(self):
		self.value=245

class e_op_result_dis_event_full(e_op_result):
	def __init__(self):
		self.value=246

class e_op_result_reserver_soldier_limit(e_op_result):
	def __init__(self):
		self.value=247

class e_op_result_reserver_soldier_product_not_addition(e_op_result):
	def __init__(self):
		self.value=248

class e_op_result_reserver_soldier_not_enough(e_op_result):
	def __init__(self):
		self.value=249

class e_op_result_dis_event_is_catch(e_op_result):
	def __init__(self):
		self.value=250

class e_op_result_dis_region_cant_dis(e_op_result):
	def __init__(self):
		self.value=251

class e_op_result_npc_exchange_close(e_op_result):
	def __init__(self):
		self.value=252

class e_op_result_npc_exchange_limit(e_op_result):
	def __init__(self):
		self.value=253

class e_op_result_dis_hero_in_event(e_op_result):
	def __init__(self):
		self.value=254

class e_op_result_hero_not_have(e_op_result):
	def __init__(self):
		self.value=255

class e_op_result_block_already_mark(e_op_result):
	def __init__(self):
		self.value=256

class e_op_result_function_unlock(e_op_result):
	def __init__(self):
		self.value=257

class e_op_result_discovery_buy_time_upper_limit(e_op_result):
	def __init__(self):
		self.value=258

class e_op_result_dis_times_full(e_op_result):
	def __init__(self):
		self.value=259

class e_op_result_same_guild_no_fight(e_op_result):
	def __init__(self):
		self.value=260

class e_op_result_guild_not_exist(e_op_result):
	def __init__(self):
		self.value=261

class e_op_result_hero_in_corps_out(e_op_result):
	def __init__(self):
		self.value=262

class e_op_result_rs_buy_time_upper_limit(e_op_result):
	def __init__(self):
		self.value=263

class e_op_result_hero_chip_relace_not_enough_cond(e_op_result):
	def __init__(self):
		self.value=264

class e_op_result_city_not_in_reble(e_op_result):
	def __init__(self):
		self.value=265

class e_op_result_tar_is_not_city(e_op_result):
	def __init__(self):
		self.value=266

class e_op_result_not_in_same_region(e_op_result):
	def __init__(self):
		self.value=267

class e_op_result_cur_rebel_not_unlock(e_op_result):
	def __init__(self):
		self.value=268

class e_op_result_rebel_search_times_full(e_op_result):
	def __init__(self):
		self.value=269

class e_op_result_rebel_search_buy_time_upper_limit(e_op_result):
	def __init__(self):
		self.value=270

class e_op_result_not_mine_rebel_no_fight(e_op_result):
	def __init__(self):
		self.value=271

class e_op_result_rebel_no_search_time(e_op_result):
	def __init__(self):
		self.value=272

class e_op_result_cur_rebel_has_search(e_op_result):
	def __init__(self):
		self.value=273

class e_op_result_crusade_city_is_empty(e_op_result):
	def __init__(self):
		self.value=274

class e_op_result_quality_lv_limited(e_op_result):
	def __init__(self):
		self.value=275

class e_op_result_seize_times_not_enough(e_op_result):
	def __init__(self):
		self.value=276

class e_op_result_miracle_is_full(e_op_result):
	def __init__(self):
		self.value=277

class e_op_result_wt_limit(e_op_result):
	def __init__(self):
		self.value=278

class e_op_result_tar_city_not_open(e_op_result):
	def __init__(self):
		self.value=279

class e_op_result_corps_diff_castle(e_op_result):
	def __init__(self):
		self.value=280

class e_op_result_guild_gift_has_reward(e_op_result):
	def __init__(self):
		self.value=281

class e_op_result_guild_gift_time_limit(e_op_result):
	def __init__(self):
		self.value=282

class e_op_result_score_not_enough(e_op_result):
	def __init__(self):
		self.value=283

class e_op_result_register_failed_season_end(e_op_result):
	def __init__(self):
		self.value=284

class e_op_result_login_out_of_data(e_op_result):
	def __init__(self):
		self.value=285

class e_op_result_bd_wait_pay_gold_s(e_op_result):
	def __init__(self):
		self.value=286

class e_op_result_platform_login_invalid(e_op_result):
	def __init__(self):
		self.value=287

class e_op_result_channel_forbid_talk(e_op_result):
	def __init__(self):
		self.value=288

class e_op_result_operate_fast(e_op_result):
	def __init__(self):
		self.value=289

class e_op_result_illegal_chat(e_op_result):
	def __init__(self):
		self.value=290

class e_op_result_register_close(e_op_result):
	def __init__(self):
		self.value=291

class e_op_result_unenough_times(e_op_result):
	def __init__(self):
		self.value=292

class e_op_result_skill_lvup_failed(e_op_result):
	def __init__(self):
		self.value=293

class e_op_result_hero_starlv_limit(e_op_result):
	def __init__(self):
		self.value=294

class e_op_result_data_out_of_sync(e_op_result):
	def __init__(self):
		self.value=295

