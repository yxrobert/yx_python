from basetype import *
from constant import *
from err_code import *
class E_EVENT_TYPE(enum):
	pass

class e_event_type_invalid(E_EVENT_TYPE):
	def __init__(self):
		self.value=0

class e_event_type_battle(E_EVENT_TYPE):
	def __init__(self):
		self.value=1

class e_event_type_guard(E_EVENT_TYPE):
	def __init__(self):
		self.value=2

class e_event_type_go_home(E_EVENT_TYPE):
	def __init__(self):
		self.value=3

class e_event_type_building(E_EVENT_TYPE):
	def __init__(self):
		self.value=4

class e_event_type_block_discard(E_EVENT_TYPE):
	def __init__(self):
		self.value=5

class e_event_type_block_building(E_EVENT_TYPE):
	def __init__(self):
		self.value=6

class e_event_type_block_building_discard(E_EVENT_TYPE):
	def __init__(self):
		self.value=7

class e_event_type_block_seize(E_EVENT_TYPE):
	def __init__(self):
		self.value=8

class e_event_type_block_smash(E_EVENT_TYPE):
	def __init__(self):
		self.value=9

class e_event_type_guard_back(E_EVENT_TYPE):
	def __init__(self):
		self.value=10

class e_event_type_garrison_fort(E_EVENT_TYPE):
	def __init__(self):
		self.value=11

class e_event_type_leave_fort(E_EVENT_TYPE):
	def __init__(self):
		self.value=12

class e_event_type_combat(E_EVENT_TYPE):
	def __init__(self):
		self.value=13

class e_event_type_combat_seize(E_EVENT_TYPE):
	def __init__(self):
		self.value=14

class e_event_type_combat_smash(E_EVENT_TYPE):
	def __init__(self):
		self.value=15

class e_event_type_conscript_soldier(E_EVENT_TYPE):
	def __init__(self):
		self.value=16

class e_event_type_guild_transfer(E_EVENT_TYPE):
	def __init__(self):
		self.value=17

class e_event_type_miracle_timeout(E_EVENT_TYPE):
	def __init__(self):
		self.value=18

class e_event_type_block_training(E_EVENT_TYPE):
	def __init__(self):
		self.value=19

class e_event_type_combat_training(E_EVENT_TYPE):
	def __init__(self):
		self.value=20

class e_event_type_serial_smash(E_EVENT_TYPE):
	def __init__(self):
		self.value=21

class e_event_type_addition_effect(E_EVENT_TYPE):
	def __init__(self):
		self.value=22

class e_event_type_guild_accuse(E_EVENT_TYPE):
	def __init__(self):
		self.value=23

class e_event_type_discovery_point(E_EVENT_TYPE):
	def __init__(self):
		self.value=24

class e_event_type_discovery_catch(E_EVENT_TYPE):
	def __init__(self):
		self.value=25

class e_event_type_discovery_exploit(E_EVENT_TYPE):
	def __init__(self):
		self.value=26

class e_event_type_discovery_trigger(E_EVENT_TYPE):
	def __init__(self):
		self.value=27

class e_event_type_discovery_back(E_EVENT_TYPE):
	def __init__(self):
		self.value=28

class e_event_type_guild_assist_res(E_EVENT_TYPE):
	def __init__(self):
		self.value=29

class e_event_type_city_crusade(E_EVENT_TYPE):
	def __init__(self):
		self.value=30

class e_event_type_city_crusade_combat(E_EVENT_TYPE):
	def __init__(self):
		self.value=31

class e_event_type_produce_rebel(E_EVENT_TYPE):
	def __init__(self):
		self.value=32

class e_event_type_combat_rebel(E_EVENT_TYPE):
	def __init__(self):
		self.value=33

class e_event_type_rebel(E_EVENT_TYPE):
	def __init__(self):
		self.value=34

class e_event_type_max(E_EVENT_TYPE):
	def __init__(self):
		self.value=35

class E_NOFIGHT_TYPE(enum):
	pass

class e_nofight_type_none(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=-1

class e_nofight_type_my_block(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=0

class e_nofight_type_protected(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=1

class e_nofight_type_invaded(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=2

class e_nofight_type_be_invaded(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=3

class e_nofight_type_seize_self(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=4

class e_nofight_type_noguild_nocity(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=5

class e_nofight_type_my_city(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=6

class e_nofight_type_no_attach(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=7

class e_nofight_type_no_guild_no_invade(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=8

class e_nofight_type_guardhome(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=9

class e_nofight_type_newbie(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=10

class e_nofight_type_guardslef(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=11

class e_nofight_type_no_effect(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=12

class e_nofight_type_seize_protect(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=13

class e_nofight_type_no_target(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=14

class e_nofight_type_tar_out_range(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=15

class e_nofight_type_same_guild_no_att(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=16

class e_nofight_type_city_close_no_att(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=17

class e_nofight_type_miracle_full(E_NOFIGHT_TYPE):
	def __init__(self):
		self.value=18

class E_PVP_COMBAT_TYPE(enum):
	pass

class e_combat_type_invalid(E_PVP_COMBAT_TYPE):
	def __init__(self):
		self.value=-1

class e_combat_type_guard_others(E_PVP_COMBAT_TYPE):
	def __init__(self):
		self.value=0

class e_combat_type_guard_castle(E_PVP_COMBAT_TYPE):
	def __init__(self):
		self.value=1

class e_combat_type_fort(E_PVP_COMBAT_TYPE):
	def __init__(self):
		self.value=2

class e_combat_type_castle(E_PVP_COMBAT_TYPE):
	def __init__(self):
		self.value=3

class e_combat_type_arena(E_PVP_COMBAT_TYPE):
	def __init__(self):
		self.value=4

class e_combat_type_tower(E_PVP_COMBAT_TYPE):
	def __init__(self):
		self.value=5

class e_combat_type_for_cp(E_PVP_COMBAT_TYPE):
	def __init__(self):
		self.value=6

class E_COMBAT_TYPE(enum):
	pass

class e_combat_type_pve(E_COMBAT_TYPE):
	def __init__(self):
		self.value=0

class e_combat_type_pvp(E_COMBAT_TYPE):
	def __init__(self):
		self.value=1

class e_combat_type_pvw(E_COMBAT_TYPE):
	def __init__(self):
		self.value=2

class e_combat_type_pcp(E_COMBAT_TYPE):
	def __init__(self):
		self.value=3

class E_SHOP_REFRESH_TYPE(enum):
	pass

class e_refresh_type_system(E_SHOP_REFRESH_TYPE):
	def __init__(self):
		self.value=0

class e_refresh_type_gold(E_SHOP_REFRESH_TYPE):
	def __init__(self):
		self.value=1

class E_SHOP_FORCE_TYPE(enum):
	pass

class e_shop_force_type_user(E_SHOP_FORCE_TYPE):
	def __init__(self):
		self.value=0

class e_shop_force_type_guild(E_SHOP_FORCE_TYPE):
	def __init__(self):
		self.value=1

class e_shop_force_type_world(E_SHOP_FORCE_TYPE):
	def __init__(self):
		self.value=2

class E_STATE_STATUS(enum):
	pass

class e_state_status_green(E_STATE_STATUS):
	def __init__(self):
		self.value=0

class e_state_status_orange(E_STATE_STATUS):
	def __init__(self):
		self.value=1

class e_state_status_red(E_STATE_STATUS):
	def __init__(self):
		self.value=2

class E_EVENT_RESULT_TYPE(enum):
	pass

class e_event_result_type_invalid(E_EVENT_RESULT_TYPE):
	def __init__(self):
		self.value=-1

class e_event_result_type_battle_result(E_EVENT_RESULT_TYPE):
	def __init__(self):
		self.value=0

class e_event_result_type_new_event(E_EVENT_RESULT_TYPE):
	def __init__(self):
		self.value=1

class e_event_result_type_event_finish(E_EVENT_RESULT_TYPE):
	def __init__(self):
		self.value=2

class e_event_result_type_alarm(E_EVENT_RESULT_TYPE):
	def __init__(self):
		self.value=3

class E_BATTLE_RESULT_TYPE(enum):
	pass

class e_battle_result_type_win(E_BATTLE_RESULT_TYPE):
	def __init__(self):
		self.value=0

class e_battle_result_type_lose(E_BATTLE_RESULT_TYPE):
	def __init__(self):
		self.value=1

class e_battle_result_type_draw(E_BATTLE_RESULT_TYPE):
	def __init__(self):
		self.value=2

class E_BUILDING_CONFIG_TYPE(enum):
	pass

class e_building_config_type_building(E_BUILDING_CONFIG_TYPE):
	def __init__(self):
		self.value=0

class e_building_config_type_technology(E_BUILDING_CONFIG_TYPE):
	def __init__(self):
		self.value=1

class E_CITY_TYPE(enum):
	pass

class e_city_type_invalid(E_CITY_TYPE):
	def __init__(self):
		self.value=0

class e_city_type_capital_city(E_CITY_TYPE):
	def __init__(self):
		self.value=1

class e_city_type_main_city(E_CITY_TYPE):
	def __init__(self):
		self.value=2

class e_city_type_medium_city(E_CITY_TYPE):
	def __init__(self):
		self.value=3

class e_city_type_pass(E_CITY_TYPE):
	def __init__(self):
		self.value=4

class e_city_type_small_city(E_CITY_TYPE):
	def __init__(self):
		self.value=5

class E_BUILDING_TYPE(enum):
	pass

class e_building_type_invalid(E_BUILDING_TYPE):
	def __init__(self):
		self.value=-1

class e_building_type_town_hall(E_BUILDING_TYPE):
	def __init__(self):
		self.value=0

class e_building_type_market(E_BUILDING_TYPE):
	def __init__(self):
		self.value=1

class e_building_type_warehouse(E_BUILDING_TYPE):
	def __init__(self):
		self.value=2

class e_building_type_house(E_BUILDING_TYPE):
	def __init__(self):
		self.value=3

class e_building_type_sawmill(E_BUILDING_TYPE):
	def __init__(self):
		self.value=4

class e_building_type_quarry(E_BUILDING_TYPE):
	def __init__(self):
		self.value=5

class e_building_type_ironworks(E_BUILDING_TYPE):
	def __init__(self):
		self.value=6

class e_building_type_mill(E_BUILDING_TYPE):
	def __init__(self):
		self.value=7

class e_building_type_military_camp(E_BUILDING_TYPE):
	def __init__(self):
		self.value=8

class e_building_type_military_school(E_BUILDING_TYPE):
	def __init__(self):
		self.value=9

class e_building_type_recruitment(E_BUILDING_TYPE):
	def __init__(self):
		self.value=10

class e_building_type_walls(E_BUILDING_TYPE):
	def __init__(self):
		self.value=11

class e_building_type_academy(E_BUILDING_TYPE):
	def __init__(self):
		self.value=12

class e_building_type_pub(E_BUILDING_TYPE):
	def __init__(self):
		self.value=13

class e_building_type_smithy(E_BUILDING_TYPE):
	def __init__(self):
		self.value=14

class e_building_type_scouts(E_BUILDING_TYPE):
	def __init__(self):
		self.value=15

class e_building_type_rockwork(E_BUILDING_TYPE):
	def __init__(self):
		self.value=16

class e_building_type_reserve_duty(E_BUILDING_TYPE):
	def __init__(self):
		self.value=17

class e_building_type_guild(E_BUILDING_TYPE):
	def __init__(self):
		self.value=18

class e_building_type_arena(E_BUILDING_TYPE):
	def __init__(self):
		self.value=19

class e_building_type_ranking(E_BUILDING_TYPE):
	def __init__(self):
		self.value=20

class e_building_type_notice(E_BUILDING_TYPE):
	def __init__(self):
		self.value=21

class e_building_type_pirate_ship(E_BUILDING_TYPE):
	def __init__(self):
		self.value=22

class e_building_type_port(E_BUILDING_TYPE):
	def __init__(self):
		self.value=23

class e_building_type_visit(E_BUILDING_TYPE):
	def __init__(self):
		self.value=24

class e_building_type_museum(E_BUILDING_TYPE):
	def __init__(self):
		self.value=25

class e_building_type_drill_ground(E_BUILDING_TYPE):
	def __init__(self):
		self.value=26

class e_building_type_tower(E_BUILDING_TYPE):
	def __init__(self):
		self.value=27

class e_building_type_war_academy(E_BUILDING_TYPE):
	def __init__(self):
		self.value=28

class e_building_type_shop(E_BUILDING_TYPE):
	def __init__(self):
		self.value=29

class E_EFFECT_TYPE(enum):
	pass

class e_effect_type_global_invalid(E_EFFECT_TYPE):
	def __init__(self):
		self.value=-1

class e_effect_type_global_building_cost_time(E_EFFECT_TYPE):
	def __init__(self):
		self.value=0

class e_effect_type_global_crops_speed(E_EFFECT_TYPE):
	def __init__(self):
		self.value=1

class e_effect_type_global_resource_limit(E_EFFECT_TYPE):
	def __init__(self):
		self.value=2

class e_effect_type_global_wood_output_inc(E_EFFECT_TYPE):
	def __init__(self):
		self.value=3

class e_effect_type_global_iron_output_inc(E_EFFECT_TYPE):
	def __init__(self):
		self.value=4

class e_effect_type_global_grain_output_inc(E_EFFECT_TYPE):
	def __init__(self):
		self.value=5

class e_effect_type_global_stone_output_inc(E_EFFECT_TYPE):
	def __init__(self):
		self.value=6

class e_effect_type_global_tax_inc(E_EFFECT_TYPE):
	def __init__(self):
		self.value=7

class e_effect_type_global_equip_strengthen_cost(E_EFFECT_TYPE):
	def __init__(self):
		self.value=8

class e_effect_type_global_fight_exp(E_EFFECT_TYPE):
	def __init__(self):
		self.value=9

class e_effect_type_global_hero_phy_recover(E_EFFECT_TYPE):
	def __init__(self):
		self.value=10

class e_effect_type_global_walls_duration(E_EFFECT_TYPE):
	def __init__(self):
		self.value=11

class e_effect_type_global_hero_train_inc(E_EFFECT_TYPE):
	def __init__(self):
		self.value=12

class e_effect_type_global_corps_soldier_limit(E_EFFECT_TYPE):
	def __init__(self):
		self.value=13

class e_effect_type_global_wall_soldier_attribute(E_EFFECT_TYPE):
	def __init__(self):
		self.value=14

class e_effect_type_global_defend_soldier_attribute(E_EFFECT_TYPE):
	def __init__(self):
		self.value=15

class e_effect_type_global_free_acc_building_time(E_EFFECT_TYPE):
	def __init__(self):
		self.value=16

class e_effect_type_global_warning(E_EFFECT_TYPE):
	def __init__(self):
		self.value=17

class e_effect_type_global_research_cost_time(E_EFFECT_TYPE):
	def __init__(self):
		self.value=18

class e_effect_type_global_conscript_infantry_cost_time(E_EFFECT_TYPE):
	def __init__(self):
		self.value=19

class e_effect_type_global_build_trap_cost_time(E_EFFECT_TYPE):
	def __init__(self):
		self.value=20

class e_effect_type_global_conscript_cavalry_cost_time(E_EFFECT_TYPE):
	def __init__(self):
		self.value=21

class e_effect_type_global_conscript_archer_cost_time(E_EFFECT_TYPE):
	def __init__(self):
		self.value=22

class e_effect_type_global_soldier_attribute(E_EFFECT_TYPE):
	def __init__(self):
		self.value=23

class e_effect_type_global_unlock_soldier(E_EFFECT_TYPE):
	def __init__(self):
		self.value=24

class e_effect_type_global_guild_contribution(E_EFFECT_TYPE):
	def __init__(self):
		self.value=25

class e_effect_type_global_kill_point(E_EFFECT_TYPE):
	def __init__(self):
		self.value=26

class e_effect_type_global_tax_free_times(E_EFFECT_TYPE):
	def __init__(self):
		self.value=27

class e_effect_type_global_hero_phy_limit(E_EFFECT_TYPE):
	def __init__(self):
		self.value=28

class e_effect_type_global_corps_phy_limit(E_EFFECT_TYPE):
	def __init__(self):
		self.value=29

class e_effect_type_global_equip_make(E_EFFECT_TYPE):
	def __init__(self):
		self.value=30

class e_effect_type_global_corps_phy_recover(E_EFFECT_TYPE):
	def __init__(self):
		self.value=31

class e_effect_type_global_copper_output_inc(E_EFFECT_TYPE):
	def __init__(self):
		self.value=32

class e_effect_type_global_oil_output_inc(E_EFFECT_TYPE):
	def __init__(self):
		self.value=33

class e_effect_type_global_land_limit(E_EFFECT_TYPE):
	def __init__(self):
		self.value=34

class e_effect_type_global_seize_protect(E_EFFECT_TYPE):
	def __init__(self):
		self.value=35

class e_effect_type_global_building_range(E_EFFECT_TYPE):
	def __init__(self):
		self.value=36

class e_effect_type_global_corps_exp(E_EFFECT_TYPE):
	def __init__(self):
		self.value=37

class e_effect_type_global_seize_range(E_EFFECT_TYPE):
	def __init__(self):
		self.value=38

class e_effect_type_global_free_acc_tech_time(E_EFFECT_TYPE):
	def __init__(self):
		self.value=39

class e_effect_type_global_hero_add_attr(E_EFFECT_TYPE):
	def __init__(self):
		self.value=40

class e_effect_type_global_resbuilding_limit(E_EFFECT_TYPE):
	def __init__(self):
		self.value=41

class e_effect_type_global_revsoldier_speed(E_EFFECT_TYPE):
	def __init__(self):
		self.value=42

class e_effect_type_global_garrisonfort_speed(E_EFFECT_TYPE):
	def __init__(self):
		self.value=43

class e_effect_type_global_corps_hero_num(E_EFFECT_TYPE):
	def __init__(self):
		self.value=44

class e_effect_type_global_building_queue(E_EFFECT_TYPE):
	def __init__(self):
		self.value=45

class e_effect_type_global_tech_queue(E_EFFECT_TYPE):
	def __init__(self):
		self.value=46

class e_effect_type_global_guild_assist(E_EFFECT_TYPE):
	def __init__(self):
		self.value=47

class e_effect_type_global_guild_auto_assist(E_EFFECT_TYPE):
	def __init__(self):
		self.value=48

class e_effect_type_global_resource_exchange_rate(E_EFFECT_TYPE):
	def __init__(self):
		self.value=49

class e_effect_type_global_miracle_occupy(E_EFFECT_TYPE):
	def __init__(self):
		self.value=50

class e_effect_type_global_speed_back_home(E_EFFECT_TYPE):
	def __init__(self):
		self.value=51

class e_effect_type_global_hero_buy_spirit(E_EFFECT_TYPE):
	def __init__(self):
		self.value=52

class e_effect_type_global_building_resource(E_EFFECT_TYPE):
	def __init__(self):
		self.value=53

class e_effect_type_global_tech_resource(E_EFFECT_TYPE):
	def __init__(self):
		self.value=54

class e_effect_type_global_max(E_EFFECT_TYPE):
	def __init__(self):
		self.value=55

class E_EFFECT_CHANGE_TYPE(enum):
	pass

class e_effect_change_type_invalid(E_EFFECT_CHANGE_TYPE):
	def __init__(self):
		self.value=-1

class e_effect_change_type_value(E_EFFECT_CHANGE_TYPE):
	def __init__(self):
		self.value=0

class e_effect_change_type_percent(E_EFFECT_CHANGE_TYPE):
	def __init__(self):
		self.value=1

class e_effect_change_type_max(E_EFFECT_CHANGE_TYPE):
	def __init__(self):
		self.value=2

class E_RESOURCE_TYPE(enum):
	pass

class e_resource_type_invalid(E_RESOURCE_TYPE):
	def __init__(self):
		self.value=-1

class e_resource_type_wood(E_RESOURCE_TYPE):
	def __init__(self):
		self.value=1

class e_resource_type_stone(E_RESOURCE_TYPE):
	def __init__(self):
		self.value=2

class e_resource_type_grain(E_RESOURCE_TYPE):
	def __init__(self):
		self.value=3

class e_resource_type_iron(E_RESOURCE_TYPE):
	def __init__(self):
		self.value=4

class e_resource_type_gold_coin(E_RESOURCE_TYPE):
	def __init__(self):
		self.value=5

class e_resource_type_silver_coin(E_RESOURCE_TYPE):
	def __init__(self):
		self.value=6

class e_resource_type_guild_coin(E_RESOURCE_TYPE):
	def __init__(self):
		self.value=7

class e_resource_type_arena_coin(E_RESOURCE_TYPE):
	def __init__(self):
		self.value=8

class e_resource_type_activity_coin(E_RESOURCE_TYPE):
	def __init__(self):
		self.value=9

class e_resource_type_copper(E_RESOURCE_TYPE):
	def __init__(self):
		self.value=10

class e_resource_type_oil(E_RESOURCE_TYPE):
	def __init__(self):
		self.value=11

class e_resource_type_season_coin(E_RESOURCE_TYPE):
	def __init__(self):
		self.value=12

class e_resource_type_max(E_RESOURCE_TYPE):
	def __init__(self):
		self.value=13

class E_COMMAND_TYPE(enum):
	pass

class e_command_type_att(E_COMMAND_TYPE):
	def __init__(self):
		self.value=0

class e_command_type_def(E_COMMAND_TYPE):
	def __init__(self):
		self.value=1

class e_command_type_mass(E_COMMAND_TYPE):
	def __init__(self):
		self.value=2

class E_COMMAND_TARGET_TYPE(enum):
	pass

class e_command_target_type_npc(E_COMMAND_TARGET_TYPE):
	def __init__(self):
		self.value=0

class e_command_target_type_any(E_COMMAND_TARGET_TYPE):
	def __init__(self):
		self.value=1

class e_command_target_type_mine(E_COMMAND_TARGET_TYPE):
	def __init__(self):
		self.value=2

class E_BLOCK_TYPE(enum):
	pass

class e_block_type_land(E_BLOCK_TYPE):
	def __init__(self):
		self.value=0

class e_block_type_castle(E_BLOCK_TYPE):
	def __init__(self):
		self.value=1

class e_block_type_castle_area(E_BLOCK_TYPE):
	def __init__(self):
		self.value=2

class e_block_type_fort(E_BLOCK_TYPE):
	def __init__(self):
		self.value=3

class e_block_type_farm(E_BLOCK_TYPE):
	def __init__(self):
		self.value=4

class e_block_type_mine(E_BLOCK_TYPE):
	def __init__(self):
		self.value=5

class e_block_type_mill(E_BLOCK_TYPE):
	def __init__(self):
		self.value=6

class e_block_type_quarry(E_BLOCK_TYPE):
	def __init__(self):
		self.value=7

class e_block_type_vice_castle(E_BLOCK_TYPE):
	def __init__(self):
		self.value=8

class e_block_type_city(E_BLOCK_TYPE):
	def __init__(self):
		self.value=9

class e_block_type_city_area(E_BLOCK_TYPE):
	def __init__(self):
		self.value=10

class e_block_type_pass(E_BLOCK_TYPE):
	def __init__(self):
		self.value=11

class e_block_type_public_fort(E_BLOCK_TYPE):
	def __init__(self):
		self.value=12

class e_block_type_obstacle(E_BLOCK_TYPE):
	def __init__(self):
		self.value=13

class e_block_type_forest(E_BLOCK_TYPE):
	def __init__(self):
		self.value=14

class e_block_type_miracle(E_BLOCK_TYPE):
	def __init__(self):
		self.value=15

class e_block_type_storage(E_BLOCK_TYPE):
	def __init__(self):
		self.value=16

class e_block_type_gate(E_BLOCK_TYPE):
	def __init__(self):
		self.value=17

class e_block_type_max(E_BLOCK_TYPE):
	def __init__(self):
		self.value=18

class E_BLOCK_SHAPE(enum):
	pass

class e_block_shape_one(E_BLOCK_SHAPE):
	def __init__(self):
		self.value=0

class e_block_shape_tow_up(E_BLOCK_SHAPE):
	def __init__(self):
		self.value=1

class e_block_shape_tow_mid(E_BLOCK_SHAPE):
	def __init__(self):
		self.value=2

class e_block_shape_tow_down(E_BLOCK_SHAPE):
	def __init__(self):
		self.value=3

class e_block_shape_tri_angle(E_BLOCK_SHAPE):
	def __init__(self):
		self.value=4

class e_block_shape_tri_line(E_BLOCK_SHAPE):
	def __init__(self):
		self.value=5

class e_block_shape_tri_up(E_BLOCK_SHAPE):
	def __init__(self):
		self.value=6

class e_block_shape_tri_left(E_BLOCK_SHAPE):
	def __init__(self):
		self.value=7

class e_block_shape_tri_right(E_BLOCK_SHAPE):
	def __init__(self):
		self.value=8

class e_block_shape_tri_down(E_BLOCK_SHAPE):
	def __init__(self):
		self.value=9

class e_block_shape_tow_circle(E_BLOCK_SHAPE):
	def __init__(self):
		self.value=10

class E_REWARD_TYPE(enum):
	pass

class e_reward_type_invalid(E_REWARD_TYPE):
	def __init__(self):
		self.value=-1

class e_reward_type_resources(E_REWARD_TYPE):
	def __init__(self):
		self.value=0

class e_reward_type_item(E_REWARD_TYPE):
	def __init__(self):
		self.value=1

class e_reward_type_hero(E_REWARD_TYPE):
	def __init__(self):
		self.value=2

class e_reward_type_fame(E_REWARD_TYPE):
	def __init__(self):
		self.value=3

class e_reward_type_kill_point(E_REWARD_TYPE):
	def __init__(self):
		self.value=4

class e_reward_type_match_coin(E_REWARD_TYPE):
	def __init__(self):
		self.value=5

class e_reward_type_contribution(E_REWARD_TYPE):
	def __init__(self):
		self.value=6

class e_reward_type_museum_collection(E_REWARD_TYPE):
	def __init__(self):
		self.value=7

class e_reward_type_drop_box(E_REWARD_TYPE):
	def __init__(self):
		self.value=8

class e_reward_type_reserver_soldier(E_REWARD_TYPE):
	def __init__(self):
		self.value=9

class e_reward_type_guild_gift(E_REWARD_TYPE):
	def __init__(self):
		self.value=10

class e_reward_type_lucky_point(E_REWARD_TYPE):
	def __init__(self):
		self.value=11

class e_reward_type_max(E_REWARD_TYPE):
	def __init__(self):
		self.value=12

class E_ITEM_TYPE(enum):
	pass

class e_item_type_invalid(E_ITEM_TYPE):
	def __init__(self):
		self.value=-1

class e_item_type_equip(E_ITEM_TYPE):
	def __init__(self):
		self.value=0

class e_item_type_medal(E_ITEM_TYPE):
	def __init__(self):
		self.value=1

class e_item_type_hero_train(E_ITEM_TYPE):
	def __init__(self):
		self.value=2

class e_item_type_equip_chip(E_ITEM_TYPE):
	def __init__(self):
		self.value=3

class e_item_type_strengthen_item(E_ITEM_TYPE):
	def __init__(self):
		self.value=4

class e_item_type_res_pak(E_ITEM_TYPE):
	def __init__(self):
		self.value=5

class e_item_type_speed_item(E_ITEM_TYPE):
	def __init__(self):
		self.value=6

class e_item_type_other(E_ITEM_TYPE):
	def __init__(self):
		self.value=7

class e_item_type_use(E_ITEM_TYPE):
	def __init__(self):
		self.value=8

class e_item_type_vip(E_ITEM_TYPE):
	def __init__(self):
		self.value=9

class e_item_type_hero_exp(E_ITEM_TYPE):
	def __init__(self):
		self.value=10

class e_item_type_corps_exp(E_ITEM_TYPE):
	def __init__(self):
		self.value=11

class e_item_type_hero_chip(E_ITEM_TYPE):
	def __init__(self):
		self.value=12

class e_item_type_lottery_ticket(E_ITEM_TYPE):
	def __init__(self):
		self.value=13

class e_item_type_box(E_ITEM_TYPE):
	def __init__(self):
		self.value=14

class e_item_type_gift_drop(E_ITEM_TYPE):
	def __init__(self):
		self.value=15

class e_item_type_max(E_ITEM_TYPE):
	def __init__(self):
		self.value=16

class E_ITEM_SHOW_TYPE(enum):
	pass

class e_show_type_equip(E_ITEM_SHOW_TYPE):
	def __init__(self):
		self.value=0

class e_show_type_medal(E_ITEM_SHOW_TYPE):
	def __init__(self):
		self.value=1

class e_show_type_speed(E_ITEM_SHOW_TYPE):
	def __init__(self):
		self.value=2

class e_show_type_res_pak(E_ITEM_SHOW_TYPE):
	def __init__(self):
		self.value=3

class e_show_type_equip_chip(E_ITEM_SHOW_TYPE):
	def __init__(self):
		self.value=4

class e_show_type_other(E_ITEM_SHOW_TYPE):
	def __init__(self):
		self.value=5

class e_show_type_hero_chip(E_ITEM_SHOW_TYPE):
	def __init__(self):
		self.value=6

class E_EQUIP_SLOT(enum):
	pass

class e_equip_slot_0(E_EQUIP_SLOT):
	def __init__(self):
		self.value=0

class e_equip_slot_1(E_EQUIP_SLOT):
	def __init__(self):
		self.value=1

class e_equip_slot_2(E_EQUIP_SLOT):
	def __init__(self):
		self.value=2

class e_equip_slot_3(E_EQUIP_SLOT):
	def __init__(self):
		self.value=3

class e_equip_slot_4(E_EQUIP_SLOT):
	def __init__(self):
		self.value=4

class e_equip_slot_5(E_EQUIP_SLOT):
	def __init__(self):
		self.value=5

class e_equip_slot_max(E_EQUIP_SLOT):
	def __init__(self):
		self.value=6

class E_BLOCK_BUILDING_STATE(enum):
	pass

class e_block_building_none(E_BLOCK_BUILDING_STATE):
	def __init__(self):
		self.value=0

class e_block_building_complete(E_BLOCK_BUILDING_STATE):
	def __init__(self):
		self.value=1

class e_block_building_build(E_BLOCK_BUILDING_STATE):
	def __init__(self):
		self.value=2

class E_CORPS_STATE(enum):
	pass

class e_corps_state_err(E_CORPS_STATE):
	def __init__(self):
		self.value=-1

class e_corps_state_castle(E_CORPS_STATE):
	def __init__(self):
		self.value=0

class e_corps_state_fort(E_CORPS_STATE):
	def __init__(self):
		self.value=1

class e_corps_state_march(E_CORPS_STATE):
	def __init__(self):
		self.value=2

class e_corps_state_guard(E_CORPS_STATE):
	def __init__(self):
		self.value=3

class e_corps_state_conscript(E_CORPS_STATE):
	def __init__(self):
		self.value=4

class E_MISSION_STATUS(enum):
	pass

class e_mission_status_invalid(E_MISSION_STATUS):
	def __init__(self):
		self.value=-1

class e_mission_status_process(E_MISSION_STATUS):
	def __init__(self):
		self.value=0

class e_mission_status_finish(E_MISSION_STATUS):
	def __init__(self):
		self.value=1

class e_mission_status_close(E_MISSION_STATUS):
	def __init__(self):
		self.value=2

class E_ACHIEVEMENT_STATUS(enum):
	pass

class e_achievement_status_invalid(E_ACHIEVEMENT_STATUS):
	def __init__(self):
		self.value=-1

class e_achievement_status_process(E_ACHIEVEMENT_STATUS):
	def __init__(self):
		self.value=0

class e_achievement_status_finish(E_ACHIEVEMENT_STATUS):
	def __init__(self):
		self.value=1

class e_achievement_status_close(E_ACHIEVEMENT_STATUS):
	def __init__(self):
		self.value=2

class E_WORLDTREND_STATUS(enum):
	pass

class e_worldtrend_status_invalid(E_WORLDTREND_STATUS):
	def __init__(self):
		self.value=-1

class e_worldtrend_status_prepare(E_WORLDTREND_STATUS):
	def __init__(self):
		self.value=0

class e_worldtrend_status_process(E_WORLDTREND_STATUS):
	def __init__(self):
		self.value=1

class e_worldtrend_status_finish(E_WORLDTREND_STATUS):
	def __init__(self):
		self.value=2

class e_worldtrend_status_unfinished(E_WORLDTREND_STATUS):
	def __init__(self):
		self.value=3

class e_worldtrend_status_finish_get_rewards(E_WORLDTREND_STATUS):
	def __init__(self):
		self.value=4

class e_worldtrend_status_finish_no_rewards(E_WORLDTREND_STATUS):
	def __init__(self):
		self.value=5

class e_worldtrend_status_finish_received_rewards(E_WORLDTREND_STATUS):
	def __init__(self):
		self.value=6

class E_STATEACHI_STATUS(enum):
	pass

class e_stateachi_status_invalid(E_STATEACHI_STATUS):
	def __init__(self):
		self.value=-1

class e_stateachi_status_process(E_STATEACHI_STATUS):
	def __init__(self):
		self.value=0

class e_stateachi_status_finish(E_STATEACHI_STATUS):
	def __init__(self):
		self.value=1

class E_WORLD_TREND_TYPE(enum):
	pass

class e_world_trend_terriroty(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=1

class e_world_trend_guildlv(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=2

class e_world_trend_city(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=3

class e_world_trend_force(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=4

class e_world_trend_nonresource_capital(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=5

class e_world_trend_resource_capital(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=6

class e_world_trend_capital(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=7

class e_world_trend_state_capital_seize_byone(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=8

class e_world_trend_resource_building(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=9

class e_world_trend_kill_defenders(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=10

class e_world_trend_guild_members(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=11

class e_world_trend_miracle(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=12

class e_world_trend_county(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=13

class e_world_trend_state_capitals(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=14

class e_world_trend_resource_city(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=15

class e_world_trend_force_val(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=16

class e_world_trend_resource_county(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=17

class e_world_trend_pass(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=18

class e_world_trend_resource_medium_city(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=19

class e_world_trend_max(E_WORLD_TREND_TYPE):
	def __init__(self):
		self.value=20

class E_ACHIEVEMENT_TYPE(enum):
	pass

class e_achievement_type_user(E_ACHIEVEMENT_TYPE):
	def __init__(self):
		self.value=0

class E_ACHIEVEMENT_TYPE_STATE_CON(enum):
	pass

class e_achievement_type_state_con_land(E_ACHIEVEMENT_TYPE_STATE_CON):
	def __init__(self):
		self.value=1

class e_achievement_type_state_con_city(E_ACHIEVEMENT_TYPE_STATE_CON):
	def __init__(self):
		self.value=2

class e_achievement_type_state_con_main_city(E_ACHIEVEMENT_TYPE_STATE_CON):
	def __init__(self):
		self.value=3

class E_ACHIEVEMENT_USER_CON(enum):
	pass

class e_achievement_user_con_combat(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=0

class e_achievement_user_con_territory(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=1

class e_achievement_user_con_res_pro(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=2

class e_achievement_user_con_military_strength(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=3

class e_achievement_user_con_hero(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=4

class e_achievement_user_con_trap(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=5

class e_achievement_user_con_power(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=6

class e_achievement_user_con_killpoint(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=7

class e_achievement_user_con_medal_set(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=8

class e_achievement_user_con_equip_slot(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=9

class e_achievement_user_con_title(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=10

class e_achievement_user_con_equip_skill(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=11

class e_achievement_user_con_tec_research(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=12

class e_achievement_user_con_total_consume(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=13

class e_achievement_user_con_tower(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=14

class e_achievement_user_con_arena(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=15

class e_achievement_user_con_hangup(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=16

class e_achievement_user_con_seize(E_ACHIEVEMENT_USER_CON):
	def __init__(self):
		self.value=17

class E_ACHIEVEMENT_USER_CON_SEIZE(enum):
	pass

class e_achievement_user_con_seize_win(E_ACHIEVEMENT_USER_CON_SEIZE):
	def __init__(self):
		self.value=1

class e_achievement_user_con_seize_total_resources_once(E_ACHIEVEMENT_USER_CON_SEIZE):
	def __init__(self):
		self.value=2

class e_achievement_user_con_seize_total_resources(E_ACHIEVEMENT_USER_CON_SEIZE):
	def __init__(self):
		self.value=3

class E_ACHIEVEMENT_USER_CON_HANGUP(enum):
	pass

class e_achievement_user_con_hangup_total_resources(E_ACHIEVEMENT_USER_CON_HANGUP):
	def __init__(self):
		self.value=1

class E_ACHIEVEMENT_USER_CON_ARENA(enum):
	pass

class e_achievement_user_con_arena_win(E_ACHIEVEMENT_USER_CON_ARENA):
	def __init__(self):
		self.value=1

class e_achievement_user_con_arena_honor(E_ACHIEVEMENT_USER_CON_ARENA):
	def __init__(self):
		self.value=2

class e_achievement_user_con_arena_coin(E_ACHIEVEMENT_USER_CON_ARENA):
	def __init__(self):
		self.value=3

class E_ACHIEVEMENT_USER_CON_TOWER(enum):
	pass

class e_achievement_user_con_tower_win(E_ACHIEVEMENT_USER_CON_TOWER):
	def __init__(self):
		self.value=1

class e_achievement_user_con_tower_pass(E_ACHIEVEMENT_USER_CON_TOWER):
	def __init__(self):
		self.value=2

class E_ACHIEVEMENT_USER_CON_EQUIP_SLOT(enum):
	pass

class e_achievement_user_con_equip_slot_single(E_ACHIEVEMENT_USER_CON_EQUIP_SLOT):
	def __init__(self):
		self.value=0

class e_achievement_user_con_equip_slot_total(E_ACHIEVEMENT_USER_CON_EQUIP_SLOT):
	def __init__(self):
		self.value=1

class E_ACHIEVEMENT_USER_CON_TEC_RESEARCH(enum):
	pass

class e_achievement_user_con_tec_research_count(E_ACHIEVEMENT_USER_CON_TEC_RESEARCH):
	def __init__(self):
		self.value=0

class e_achievement_user_con_tec_research_full_level(E_ACHIEVEMENT_USER_CON_TEC_RESEARCH):
	def __init__(self):
		self.value=1

class E_ACHIEVEMENT_USER_CON_COMBAT(enum):
	pass

class e_achievement_user_con_combat_pve_kill(E_ACHIEVEMENT_USER_CON_COMBAT):
	def __init__(self):
		self.value=0

class e_achievement_user_con_combat_pvp_kill(E_ACHIEVEMENT_USER_CON_COMBAT):
	def __init__(self):
		self.value=1

class e_achievement_user_con_combat_win_count(E_ACHIEVEMENT_USER_CON_COMBAT):
	def __init__(self):
		self.value=2

class E_ACHIEVEMENT_USER_CON_TERRITORY(enum):
	pass

class e_achievement_user_con_territory_count(E_ACHIEVEMENT_USER_CON_TERRITORY):
	def __init__(self):
		self.value=0

class e_achievement_user_con_territory_fort_count(E_ACHIEVEMENT_USER_CON_TERRITORY):
	def __init__(self):
		self.value=1

class e_achievement_user_con_territory_castle_count(E_ACHIEVEMENT_USER_CON_TERRITORY):
	def __init__(self):
		self.value=2

class e_achievement_user_con_territory_resource_building(E_ACHIEVEMENT_USER_CON_TERRITORY):
	def __init__(self):
		self.value=3

class E_ACHIEVEMENT_USER_CON_RES_PRO(enum):
	pass

class e_achievement_user_con_res_pro_pro(E_ACHIEVEMENT_USER_CON_RES_PRO):
	def __init__(self):
		self.value=0

class e_achievement_user_con_res_pro_accumulate(E_ACHIEVEMENT_USER_CON_RES_PRO):
	def __init__(self):
		self.value=1

class E_ACHIEVEMENT_USER_CON_MILITARY_STRENGTH(enum):
	pass

class e_achievement_user_con_military_strength_one(E_ACHIEVEMENT_USER_CON_MILITARY_STRENGTH):
	def __init__(self):
		self.value=0

class e_achievement_user_con_military_strength_total(E_ACHIEVEMENT_USER_CON_MILITARY_STRENGTH):
	def __init__(self):
		self.value=1

class e_achievement_user_con_military_strength_total_conscript(E_ACHIEVEMENT_USER_CON_MILITARY_STRENGTH):
	def __init__(self):
		self.value=2

class E_ACHIEVEMENT_USER_CON_HERO(enum):
	pass

class e_achievement_user_con_hero_count(E_ACHIEVEMENT_USER_CON_HERO):
	def __init__(self):
		self.value=0

class e_achievement_user_con_hero_single_total_equip(E_ACHIEVEMENT_USER_CON_HERO):
	def __init__(self):
		self.value=1

class e_achievement_user_con_hero_total_equip(E_ACHIEVEMENT_USER_CON_HERO):
	def __init__(self):
		self.value=2

class e_achievement_user_con_hero_star_lv(E_ACHIEVEMENT_USER_CON_HERO):
	def __init__(self):
		self.value=3

class e_achievement_user_con_hero_quality_lv(E_ACHIEVEMENT_USER_CON_HERO):
	def __init__(self):
		self.value=4

class E_ACHIEVEMENT_GUILD_CON(enum):
	pass

class e_achievement_guild_con_combat(E_ACHIEVEMENT_GUILD_CON):
	def __init__(self):
		self.value=0

class e_achievement_guild_con_territory(E_ACHIEVEMENT_GUILD_CON):
	def __init__(self):
		self.value=1

class e_achievement_guild_con_guild_count(E_ACHIEVEMENT_GUILD_CON):
	def __init__(self):
		self.value=2

class e_achievement_guild_con_military_strength(E_ACHIEVEMENT_GUILD_CON):
	def __init__(self):
		self.value=3

class e_achievement_guild_con_power(E_ACHIEVEMENT_GUILD_CON):
	def __init__(self):
		self.value=4

class e_achievement_guild_con_level(E_ACHIEVEMENT_GUILD_CON):
	def __init__(self):
		self.value=5

class E_ACHIEVEMENT_GUILD_CON_COMBAT(enum):
	pass

class e_achievement_guild_con_combat_pve_kill(E_ACHIEVEMENT_GUILD_CON_COMBAT):
	def __init__(self):
		self.value=0

class e_achievement_guild_con_combat_pvp_kill(E_ACHIEVEMENT_GUILD_CON_COMBAT):
	def __init__(self):
		self.value=1

class e_achievement_guild_con_combat_win_count(E_ACHIEVEMENT_GUILD_CON_COMBAT):
	def __init__(self):
		self.value=2

class e_achievement_guild_con_combat_pvc_kill(E_ACHIEVEMENT_GUILD_CON_COMBAT):
	def __init__(self):
		self.value=3

class e_achievement_guild_con_combat_max(E_ACHIEVEMENT_GUILD_CON_COMBAT):
	def __init__(self):
		self.value=4

class E_ACHIEVEMENT_GUILD_CON_TERRITORY(enum):
	pass

class e_achievement_guild_con_territory_count(E_ACHIEVEMENT_GUILD_CON_TERRITORY):
	def __init__(self):
		self.value=0

class e_achievement_guild_con_territory_sys_castle_count(E_ACHIEVEMENT_GUILD_CON_TERRITORY):
	def __init__(self):
		self.value=1

class e_achievement_guild_con_territory_resource_building(E_ACHIEVEMENT_GUILD_CON_TERRITORY):
	def __init__(self):
		self.value=2

class e_achievement_guild_con_territory_sys_pass(E_ACHIEVEMENT_GUILD_CON_TERRITORY):
	def __init__(self):
		self.value=3

class e_achievement_guild_con_territory_max(E_ACHIEVEMENT_GUILD_CON_TERRITORY):
	def __init__(self):
		self.value=4

class E_COMPARE_TYPE(enum):
	pass

class e_compare_type_eql(E_COMPARE_TYPE):
	def __init__(self):
		self.value=1

class e_compare_type_lte(E_COMPARE_TYPE):
	def __init__(self):
		self.value=2

class e_compare_type_gte(E_COMPARE_TYPE):
	def __init__(self):
		self.value=3

class E_USER_FLAG_TYPE(enum):
	pass

class e_user_flag_achievement_finished(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=1

class e_user_flag_mission_finished(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=2

class e_user_flag_join_guild(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=3

class e_user_flag_join_guild_inner_channel(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=4

class e_user_flag_quit_guild(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=5

class e_user_flag_quit_guild_inner_channel(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=6

class e_user_flag_change_guild_position(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=7

class e_user_flag_join_guild_group(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=8

class e_user_flag_quit_guild_group(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=9

class e_user_flag_beinvited_join_guild(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=10

class e_user_flag_block_catch(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=11

class e_user_flag_block_lost(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=12

class e_user_flag_battle_record_new(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=13

class e_user_flag_update_user(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=14

class e_user_flag_update_guild_relationship(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=15

class e_user_flag_update_item(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=16

class e_user_flag_update_activity(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=17

class e_user_flag_update_liveness(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=18

class e_user_flag_update_match(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=19

class e_user_flag_update_guild_command(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=20

class e_user_flag_update_plot_quest(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=21

class e_user_flag_update_growth_fund(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=22

class e_user_flag_update_month_card(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=23

class e_user_flag_update_fame(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=24

class e_user_flag_update_assist(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=25

class e_user_flag_update_event(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=26

class e_user_flag_update_adventure(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=27

class e_user_flag_update_raffle(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=28

class e_user_flag_update_user_attr(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=29

class e_user_flag_mission_change(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=30

class e_user_flag_world_trend_finish(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=31

class e_user_flag_world_day_target(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=32

class e_user_flag_world_trend_new(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=33

class e_user_flag_world_trend_quest_finish(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=34

class e_user_flag_update_user_gold(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=35

class e_user_flag_time_limit(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=36

class e_user_flag_time_limit_chapter(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=37

class e_user_flag_time_limit_open(E_USER_FLAG_TYPE):
	def __init__(self):
		self.value=38

class E_MISSION_TYPE(enum):
	pass

class e_mission_type_branch(E_MISSION_TYPE):
	def __init__(self):
		self.value=0

class e_mission_type_main(E_MISSION_TYPE):
	def __init__(self):
		self.value=1

class E_MISSION_CON(enum):
	pass

class e_mission_con_op(E_MISSION_CON):
	def __init__(self):
		self.value=0

class e_mission_con_building_tec(E_MISSION_CON):
	def __init__(self):
		self.value=1

class e_mission_con_trap(E_MISSION_CON):
	def __init__(self):
		self.value=2

class e_mission_con_res_pro(E_MISSION_CON):
	def __init__(self):
		self.value=3

class e_mission_con_tax(E_MISSION_CON):
	def __init__(self):
		self.value=4

class e_mission_con_corpsmgr(E_MISSION_CON):
	def __init__(self):
		self.value=5

class e_mission_con_hero(E_MISSION_CON):
	def __init__(self):
		self.value=6

class e_mission_con_compose(E_MISSION_CON):
	def __init__(self):
		self.value=7

class e_mission_con_strengthen_slot(E_MISSION_CON):
	def __init__(self):
		self.value=8

class e_mission_con_combat(E_MISSION_CON):
	def __init__(self):
		self.value=9

class e_mission_con_guild(E_MISSION_CON):
	def __init__(self):
		self.value=10

class e_mission_con_territory(E_MISSION_CON):
	def __init__(self):
		self.value=11

class e_mission_con_force(E_MISSION_CON):
	def __init__(self):
		self.value=12

class e_mission_con_tower(E_MISSION_CON):
	def __init__(self):
		self.value=13

class e_mission_con_arena(E_MISSION_CON):
	def __init__(self):
		self.value=14

class e_mission_con_equip(E_MISSION_CON):
	def __init__(self):
		self.value=15

class e_mission_con_miracle(E_MISSION_CON):
	def __init__(self):
		self.value=16

class e_mission_con_seize(E_MISSION_CON):
	def __init__(self):
		self.value=17

class e_mission_con_chat(E_MISSION_CON):
	def __init__(self):
		self.value=18

class e_mission_con_record(E_MISSION_CON):
	def __init__(self):
		self.value=19

class e_mission_con_hangup(E_MISSION_CON):
	def __init__(self):
		self.value=20

class e_mission_con_lottery(E_MISSION_CON):
	def __init__(self):
		self.value=21

class e_mission_con_shop(E_MISSION_CON):
	def __init__(self):
		self.value=22

class e_mission_con_mission(E_MISSION_CON):
	def __init__(self):
		self.value=23

class e_mission_con_user(E_MISSION_CON):
	def __init__(self):
		self.value=24

class e_mission_con_guild_quest(E_MISSION_CON):
	def __init__(self):
		self.value=25

class e_mission_con_discovery(E_MISSION_CON):
	def __init__(self):
		self.value=26

class e_mission_con_adventure(E_MISSION_CON):
	def __init__(self):
		self.value=27

class e_mission_con_reserve_soldier(E_MISSION_CON):
	def __init__(self):
		self.value=28

class e_mission_con_skill_wash(E_MISSION_CON):
	def __init__(self):
		self.value=29

class e_mission_con_chapter(E_MISSION_CON):
	def __init__(self):
		self.value=30

class e_mission_con_item(E_MISSION_CON):
	def __init__(self):
		self.value=31

class e_mission_con_museum(E_MISSION_CON):
	def __init__(self):
		self.value=32

class e_mission_con_rebel(E_MISSION_CON):
	def __init__(self):
		self.value=33

class e_mission_con_soldier(E_MISSION_CON):
	def __init__(self):
		self.value=34

class e_mission_con_max(E_MISSION_CON):
	def __init__(self):
		self.value=35

class E_MISSION_CON_SKILL_WASH(enum):
	pass

class e_mission_con_skill_wash_op(E_MISSION_CON_SKILL_WASH):
	def __init__(self):
		self.value=2

class E_MISSION_CON_MISSION(enum):
	pass

class e_mission_con_mission_reward(E_MISSION_CON_MISSION):
	def __init__(self):
		self.value=0

class E_MISSION_CON_EQUIP(enum):
	pass

class e_mission_con_equip_make(E_MISSION_CON_EQUIP):
	def __init__(self):
		self.value=0

class e_mission_con_equip_decompose(E_MISSION_CON_EQUIP):
	def __init__(self):
		self.value=1

class e_mission_con_equip_has(E_MISSION_CON_EQUIP):
	def __init__(self):
		self.value=2

class E_MISSION_CON_TAX(enum):
	pass

class e_mission_con_tax_total_count(E_MISSION_CON_TAX):
	def __init__(self):
		self.value=0

class e_mission_con_tax_single_count(E_MISSION_CON_TAX):
	def __init__(self):
		self.value=1

class e_mission_con_tax_res(E_MISSION_CON_TAX):
	def __init__(self):
		self.value=2

class E_MISSION_CON_SEIZE(enum):
	pass

class e_mission_con_seize_res(E_MISSION_CON_SEIZE):
	def __init__(self):
		self.value=0

class e_mission_con_seize_count(E_MISSION_CON_SEIZE):
	def __init__(self):
		self.value=1

class e_mission_con_seize_res_once(E_MISSION_CON_SEIZE):
	def __init__(self):
		self.value=2

class E_MISSION_CON_MIRACLE(enum):
	pass

class e_mission_con_miracle_occupy(E_MISSION_CON_MIRACLE):
	def __init__(self):
		self.value=0

class e_mission_con_miracle_type(E_MISSION_CON_MIRACLE):
	def __init__(self):
		self.value=1

class E_MISSION_CON_RECORD(enum):
	pass

class e_mission_con_record_watch(E_MISSION_CON_RECORD):
	def __init__(self):
		self.value=0

class e_mission_con_record_share_world(E_MISSION_CON_RECORD):
	def __init__(self):
		self.value=1

class e_mission_con_record_share_state(E_MISSION_CON_RECORD):
	def __init__(self):
		self.value=2

class e_mission_con_record_share_guild(E_MISSION_CON_RECORD):
	def __init__(self):
		self.value=3

class E_MISSION_CON_HANGUP(enum):
	pass

class e_mission_con_hangup_time(E_MISSION_CON_HANGUP):
	def __init__(self):
		self.value=1

class e_mission_con_hangup_res(E_MISSION_CON_HANGUP):
	def __init__(self):
		self.value=2

class e_mission_con_hangup_item(E_MISSION_CON_HANGUP):
	def __init__(self):
		self.value=3

class e_mission_con_hangup_gold(E_MISSION_CON_HANGUP):
	def __init__(self):
		self.value=4

class e_mission_con_hangup_times(E_MISSION_CON_HANGUP):
	def __init__(self):
		self.value=5

class E_MISSION_CON_LOTTERY(enum):
	pass

class e_mission_con_lottery_gold(E_MISSION_CON_LOTTERY):
	def __init__(self):
		self.value=1

class e_mission_con_lottery_silver(E_MISSION_CON_LOTTERY):
	def __init__(self):
		self.value=2

class E_MISSION_CON_SHOP(enum):
	pass

class e_mission_con_shop_normal_buy(E_MISSION_CON_SHOP):
	def __init__(self):
		self.value=0

class e_mission_con_shop_guild_buy(E_MISSION_CON_SHOP):
	def __init__(self):
		self.value=1

class e_mission_con_shop_arena_buy(E_MISSION_CON_SHOP):
	def __init__(self):
		self.value=2

class e_mission_con_shop_activity_buy(E_MISSION_CON_SHOP):
	def __init__(self):
		self.value=3

class E_MISSION_CON_ARENA(enum):
	pass

class e_mission_con_arena_win(E_MISSION_CON_ARENA):
	def __init__(self):
		self.value=1

class e_mission_con_arena_honor(E_MISSION_CON_ARENA):
	def __init__(self):
		self.value=2

class e_mission_con_arena_rank_lift(E_MISSION_CON_ARENA):
	def __init__(self):
		self.value=3

class e_mission_con_arena_rank_max(E_MISSION_CON_ARENA):
	def __init__(self):
		self.value=4

class E_MISSION_CON_TOWER(enum):
	pass

class e_mission_con_tower_win(E_MISSION_CON_TOWER):
	def __init__(self):
		self.value=1

class e_mission_con_tower_pass(E_MISSION_CON_TOWER):
	def __init__(self):
		self.value=2

class e_mission_con_tower_join(E_MISSION_CON_TOWER):
	def __init__(self):
		self.value=3

class E_MISSION_CON_HERO(enum):
	pass

class e_mission_con_hero_change_equip(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=0

class e_mission_con_hero_military_rank(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=1

class e_mission_con_hero_star_lv(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=2

class e_mission_con_hero_quality_lv(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=3

class e_mission_con_hero_lv(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=4

class e_mission_con_hero_skill_level(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=5

class e_mission_con_hero_power(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=6

class e_mission_con_hero_exp_book(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=7

class e_mission_con_hero_equip_num(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=8

class e_mission_con_hero_soldiers(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=9

class e_mission_con_hero_ss_star(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=10

class e_mission_con_hero_s_star_quality(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=11

class e_mission_con_hero_ss_star_quality(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=12

class e_mission_con_hero_chip_replace(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=13

class e_mission_con_hero_lv2(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=14

class e_mission_con_hero_skill_level_op(E_MISSION_CON_HERO):
	def __init__(self):
		self.value=15

class E_HERO_SS_STAR(enum):
	pass

class e_ss_star_none(E_HERO_SS_STAR):
	def __init__(self):
		self.value=0

class e_ss_star_n(E_HERO_SS_STAR):
	def __init__(self):
		self.value=1

class e_ss_star_r(E_HERO_SS_STAR):
	def __init__(self):
		self.value=2

class e_ss_star_sr(E_HERO_SS_STAR):
	def __init__(self):
		self.value=3

class e_ss_star_ssr(E_HERO_SS_STAR):
	def __init__(self):
		self.value=4

class e_ss_star_max(E_HERO_SS_STAR):
	def __init__(self):
		self.value=5

class E_MISSION_CON_COMPOSE(enum):
	pass

class e_mission_con_compose_equip(E_MISSION_CON_COMPOSE):
	def __init__(self):
		self.value=0

class E_MISSION_CON_STRENGTHEN_SLOT(enum):
	pass

class e_mission_con_strengthen_slot_equip(E_MISSION_CON_STRENGTHEN_SLOT):
	def __init__(self):
		self.value=0

class E_MISSION_CON_GUILD(enum):
	pass

class e_mission_con_guild_join(E_MISSION_CON_GUILD):
	def __init__(self):
		self.value=0

class e_mission_con_guild_donate(E_MISSION_CON_GUILD):
	def __init__(self):
		self.value=1

class e_mission_con_guild_contribution(E_MISSION_CON_GUILD):
	def __init__(self):
		self.value=2

class e_mission_con_guild_task(E_MISSION_CON_GUILD):
	def __init__(self):
		self.value=3

class e_mission_con_guild_position(E_MISSION_CON_GUILD):
	def __init__(self):
		self.value=4

class e_mission_con_guild_group(E_MISSION_CON_GUILD):
	def __init__(self):
		self.value=5

class e_mission_con_guild_fall(E_MISSION_CON_GUILD):
	def __init__(self):
		self.value=6

class e_mission_con_guild_city(E_MISSION_CON_GUILD):
	def __init__(self):
		self.value=7

class e_mission_con_guild_assist(E_MISSION_CON_GUILD):
	def __init__(self):
		self.value=8

class E_MISSION_CON_TERRITORY(enum):
	pass

class e_mission_con_territory_occupy_empty(E_MISSION_CON_TERRITORY):
	def __init__(self):
		self.value=0

class e_mission_con_territory_occupy_others(E_MISSION_CON_TERRITORY):
	def __init__(self):
		self.value=1

class e_mission_con_territory_occupy_fort(E_MISSION_CON_TERRITORY):
	def __init__(self):
		self.value=2

class e_mission_con_territory_occupy_city(E_MISSION_CON_TERRITORY):
	def __init__(self):
		self.value=3

class e_mission_con_territory_build_resource_building(E_MISSION_CON_TERRITORY):
	def __init__(self):
		self.value=4

class e_mission_con_territory_build_fort(E_MISSION_CON_TERRITORY):
	def __init__(self):
		self.value=5

class e_mission_con_territory_build_city(E_MISSION_CON_TERRITORY):
	def __init__(self):
		self.value=6

class e_mission_con_territory_build_mill(E_MISSION_CON_TERRITORY):
	def __init__(self):
		self.value=7

class e_mission_con_territory_build_quarry(E_MISSION_CON_TERRITORY):
	def __init__(self):
		self.value=8

class e_mission_con_territory_build_mine(E_MISSION_CON_TERRITORY):
	def __init__(self):
		self.value=9

class e_mission_con_territory_build_farm(E_MISSION_CON_TERRITORY):
	def __init__(self):
		self.value=10

class e_mission_con_territory_block_discard(E_MISSION_CON_TERRITORY):
	def __init__(self):
		self.value=11

class e_mission_con_territory_occupy(E_MISSION_CON_TERRITORY):
	def __init__(self):
		self.value=12

class e_mission_con_territory_build_storage(E_MISSION_CON_TERRITORY):
	def __init__(self):
		self.value=13

class E_MISSION_CON_OP(enum):
	pass

class e_mission_con_op_change_nick_name(E_MISSION_CON_OP):
	def __init__(self):
		self.value=0

class e_mission_con_op_change_signature(E_MISSION_CON_OP):
	def __init__(self):
		self.value=1

class e_mission_con_op_change_head_entry(E_MISSION_CON_OP):
	def __init__(self):
		self.value=2

class e_mission_con_op_change_medal(E_MISSION_CON_OP):
	def __init__(self):
		self.value=3

class e_mission_con_op_one_key_harvest_resource(E_MISSION_CON_OP):
	def __init__(self):
		self.value=4

class e_mission_con_op_train_hero(E_MISSION_CON_OP):
	def __init__(self):
		self.value=5

class e_mission_con_op_exchange(E_MISSION_CON_OP):
	def __init__(self):
		self.value=6

class e_mission_con_op_decompose_equip(E_MISSION_CON_OP):
	def __init__(self):
		self.value=7

class e_mission_con_op_gold_lottery(E_MISSION_CON_OP):
	def __init__(self):
		self.value=8

class e_mission_con_op_recruit_hero(E_MISSION_CON_OP):
	def __init__(self):
		self.value=9

class e_mission_con_op_block_smash(E_MISSION_CON_OP):
	def __init__(self):
		self.value=10

class e_mission_con_op_star_lvup(E_MISSION_CON_OP):
	def __init__(self):
		self.value=11

class e_mission_con_op_quality_lvup(E_MISSION_CON_OP):
	def __init__(self):
		self.value=12

class e_mission_con_op_silver_lottery(E_MISSION_CON_OP):
	def __init__(self):
		self.value=13

class e_mission_con_op_hangup_reward(E_MISSION_CON_OP):
	def __init__(self):
		self.value=14

class e_mission_con_op_block_seize(E_MISSION_CON_OP):
	def __init__(self):
		self.value=15

class e_mission_con_op_accelerate(E_MISSION_CON_OP):
	def __init__(self):
		self.value=16

class e_mission_con_op_block_spy(E_MISSION_CON_OP):
	def __init__(self):
		self.value=18

class E_MISSION_CON_BUILDING_TEC(enum):
	pass

class e_mission_con_building_tec_lvup(E_MISSION_CON_BUILDING_TEC):
	def __init__(self):
		self.value=0

class e_mission_con_building_max_lv(E_MISSION_CON_BUILDING_TEC):
	def __init__(self):
		self.value=1

class e_mission_con_building_type_times(E_MISSION_CON_BUILDING_TEC):
	def __init__(self):
		self.value=2

class e_mission_con_tech_type_times(E_MISSION_CON_BUILDING_TEC):
	def __init__(self):
		self.value=3

class e_mission_con_building_type_count(E_MISSION_CON_BUILDING_TEC):
	def __init__(self):
		self.value=4

class e_mission_con_tech_type_count(E_MISSION_CON_BUILDING_TEC):
	def __init__(self):
		self.value=5

class e_mission_con_building_level(E_MISSION_CON_BUILDING_TEC):
	def __init__(self):
		self.value=6

class E_MISSION_CON_TRAP(enum):
	pass

class e_mission_con_trap_build(E_MISSION_CON_TRAP):
	def __init__(self):
		self.value=0

class E_MISSION_CON_CORPSMGR(enum):
	pass

class e_mission_con_corpsmgr_change_hero(E_MISSION_CON_CORPSMGR):
	def __init__(self):
		self.value=0

class e_mission_con_corpsmgr_conscript(E_MISSION_CON_CORPSMGR):
	def __init__(self):
		self.value=1

class e_mission_con_corpsmgr_corpcount(E_MISSION_CON_CORPSMGR):
	def __init__(self):
		self.value=2

class e_mission_con_corpsmgr_strength_one(E_MISSION_CON_CORPSMGR):
	def __init__(self):
		self.value=3

class e_mission_con_corpsmgr_level(E_MISSION_CON_CORPSMGR):
	def __init__(self):
		self.value=4

class e_mission_con_corpsmgr_soldier_up(E_MISSION_CON_CORPSMGR):
	def __init__(self):
		self.value=5

class e_mission_con_corpsmgr_soldier_cur(E_MISSION_CON_CORPSMGR):
	def __init__(self):
		self.value=6

class e_mission_con_corpsmgr_power(E_MISSION_CON_CORPSMGR):
	def __init__(self):
		self.value=7

class e_mission_con_corpsmgr_troop_type(E_MISSION_CON_CORPSMGR):
	def __init__(self):
		self.value=8

class e_mission_con_corpsmgr_exp_book(E_MISSION_CON_CORPSMGR):
	def __init__(self):
		self.value=9

class E_MISSION_CON_RES_PRO_TYPE(enum):
	pass

class e_mission_con_res_pro_pro(E_MISSION_CON_RES_PRO_TYPE):
	def __init__(self):
		self.value=0

class e_mission_con_res_pro_accumulate(E_MISSION_CON_RES_PRO_TYPE):
	def __init__(self):
		self.value=1

class E_MISSION_CON_COMBAT_TYPE(enum):
	pass

class e_mission_con_combat_win_count(E_MISSION_CON_COMBAT_TYPE):
	def __init__(self):
		self.value=0

class e_mission_con_combat_kill_enemy(E_MISSION_CON_COMBAT_TYPE):
	def __init__(self):
		self.value=1

class e_mission_con_combat_crusade_kill_enemy(E_MISSION_CON_COMBAT_TYPE):
	def __init__(self):
		self.value=2

class e_mission_con_combat_sys_kill_enemy(E_MISSION_CON_COMBAT_TYPE):
	def __init__(self):
		self.value=3

class E_MISSION_CON_USER(enum):
	pass

class e_mission_con_user_kp(E_MISSION_CON_USER):
	def __init__(self):
		self.value=0

class e_mission_con_user_fame_limit(E_MISSION_CON_USER):
	def __init__(self):
		self.value=1

class e_mission_con_user_fame_cur(E_MISSION_CON_USER):
	def __init__(self):
		self.value=2

class e_mission_con_user_kp_cur(E_MISSION_CON_USER):
	def __init__(self):
		self.value=3

class e_mission_con_user_kp_chapter(E_MISSION_CON_USER):
	def __init__(self):
		self.value=4

class E_LIVENESS_TYPE(enum):
	pass

class e_liveness_type_res_collect(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=0

class e_liveness_type_out_city_build(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=1

class e_liveness_type_hit_land(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=2

class e_liveness_type_occupy_land(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=3

class e_liveness_type_in_city_build_lvup(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=4

class e_liveness_type_conscript(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=5

class e_liveness_type_recruit(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=6

class e_liveness_type_lottery(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=7

class e_liveness_type_research(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=8

class e_liveness_type_tax(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=9

class e_liveness_type_res_exchange(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=10

class e_liveness_type_trap_build(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=11

class e_liveness_type_equip_resolve(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=12

class e_liveness_type_slot_strengthen(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=13

class e_liveness_type_train_hero(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=14

class e_liveness_type_guild_contribute(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=15

class e_liveness_type_user_login(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=17

class e_liveness_type_hero_quality(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=18

class e_liveness_type_hero_star(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=19

class e_liveness_type_occupy_special_land(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=20

class e_liveness_type_out_fort(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=21

class e_liveness_type_hangup(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=22

class e_liveness_type_tower(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=23

class e_liveness_type_arean(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=24

class e_liveness_type_sweep(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=25

class e_liveness_type_occupy_miracle(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=26

class e_liveness_type_send_msg(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=27

class e_liveness_type_mission_finish(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=28

class e_liveness_type_accelerate(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=29

class e_liveness_type_change_equip(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=30

class e_liveness_type_share_report(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=31

class e_liveness_type_resource_rob(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=32

class e_liveness_type_assign_junxian_(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=33

class e_liveness_type_castle_build(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=34

class e_liveness_type_fort_build(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=35

class e_liveness_type_discovery(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=36

class e_liveness_type_rebel(E_LIVENESS_TYPE):
	def __init__(self):
		self.value=37

class E_MAIL_TYPE(enum):
	pass

class e_mail_type_system(E_MAIL_TYPE):
	def __init__(self):
		self.value=0

class e_mail_type_personal(E_MAIL_TYPE):
	def __init__(self):
		self.value=1

class e_mail_type_group(E_MAIL_TYPE):
	def __init__(self):
		self.value=2

class E_HERO_RECURIT_UNLOCK_TYPE(enum):
	pass

class e_hero_recurit_unlock_type_achievement_entry(E_HERO_RECURIT_UNLOCK_TYPE):
	def __init__(self):
		self.value=0

class e_hero_recurit_unlock_type_town_hall_level(E_HERO_RECURIT_UNLOCK_TYPE):
	def __init__(self):
		self.value=1

class E_HERO_RECURIT_CONSUME_TYPE(enum):
	pass

class e_hero_recurit_consume_gold_coin(E_HERO_RECURIT_CONSUME_TYPE):
	def __init__(self):
		self.value=0

class e_hero_recurit_consume_silver_coin(E_HERO_RECURIT_CONSUME_TYPE):
	def __init__(self):
		self.value=1

class e_hero_recurit_consume_item(E_HERO_RECURIT_CONSUME_TYPE):
	def __init__(self):
		self.value=2

class E_EQUIP_BROADCAST_TYPE(enum):
	pass

class e_equip_broadcast_type_lottery(E_EQUIP_BROADCAST_TYPE):
	def __init__(self):
		self.value=0

class e_equip_broadcast_type_lottery2(E_EQUIP_BROADCAST_TYPE):
	def __init__(self):
		self.value=1

class e_equip_broadcast_type_make(E_EQUIP_BROADCAST_TYPE):
	def __init__(self):
		self.value=2

class E_BROADCAST_TYPE(enum):
	pass

class e_broadcast_type_equip(E_BROADCAST_TYPE):
	def __init__(self):
		self.value=0

class e_broadcast_type_hero(E_BROADCAST_TYPE):
	def __init__(self):
		self.value=1

class e_broadcast_type_city_occupy(E_BROADCAST_TYPE):
	def __init__(self):
		self.value=2

class e_broadcast_type_svr_maintain(E_BROADCAST_TYPE):
	def __init__(self):
		self.value=3

class e_broadcast_type_svr_clear(E_BROADCAST_TYPE):
	def __init__(self):
		self.value=4

class e_broadcast_type_self(E_BROADCAST_TYPE):
	def __init__(self):
		self.value=5

class e_broadcast_type_json(E_BROADCAST_TYPE):
	def __init__(self):
		self.value=6

class E_HERO_QUALITY(enum):
	pass

class e_hero_quality_white(E_HERO_QUALITY):
	def __init__(self):
		self.value=0

class e_hero_quality_green(E_HERO_QUALITY):
	def __init__(self):
		self.value=1

class e_hero_quality_blue(E_HERO_QUALITY):
	def __init__(self):
		self.value=2

class e_hero_quality_purple(E_HERO_QUALITY):
	def __init__(self):
		self.value=3

class e_hero_quality_orange(E_HERO_QUALITY):
	def __init__(self):
		self.value=4

class e_hero_quality_red(E_HERO_QUALITY):
	def __init__(self):
		self.value=5

class e_hero_quality_glod(E_HERO_QUALITY):
	def __init__(self):
		self.value=6

class E_ACTIVITY_COND(enum):
	pass

class e_activity_cond_town_hall_level(E_ACTIVITY_COND):
	def __init__(self):
		self.value=0

class e_activity_cond_force(E_ACTIVITY_COND):
	def __init__(self):
		self.value=1

class e_activity_cond_fame(E_ACTIVITY_COND):
	def __init__(self):
		self.value=2

class E_ACTIVITY_STATE(enum):
	pass

class e_activity_state_undone(E_ACTIVITY_STATE):
	def __init__(self):
		self.value=1

class e_activity_state_unreward(E_ACTIVITY_STATE):
	def __init__(self):
		self.value=2

class e_activity_state_finish(E_ACTIVITY_STATE):
	def __init__(self):
		self.value=4

class ORDER_SHOW(enum):
	pass

class e_order_show_market(ORDER_SHOW):
	def __init__(self):
		self.value=1

class e_order_show_limit_buy(ORDER_SHOW):
	def __init__(self):
		self.value=2

class E_MUSEUM_COLLECTION_STATUS(enum):
	pass

class e_collection_undraw(E_MUSEUM_COLLECTION_STATUS):
	def __init__(self):
		self.value=0

class e_collection_draw(E_MUSEUM_COLLECTION_STATUS):
	def __init__(self):
		self.value=1

class E_MUSEUM_GROUP_STATUS(enum):
	pass

class e_group_unactive(E_MUSEUM_GROUP_STATUS):
	def __init__(self):
		self.value=0

class e_group_active(E_MUSEUM_GROUP_STATUS):
	def __init__(self):
		self.value=1

class E_HERO_STATE(enum):
	pass

class e_hero_state_err(E_HERO_STATE):
	def __init__(self):
		self.value=-1

class e_hero_state_corps(E_HERO_STATE):
	def __init__(self):
		self.value=0

class e_hero_state_corps_out(E_HERO_STATE):
	def __init__(self):
		self.value=1

class e_hero_state_guard(E_HERO_STATE):
	def __init__(self):
		self.value=2

class e_hero_state_training(E_HERO_STATE):
	def __init__(self):
		self.value=3

class e_hero_state_hangup(E_HERO_STATE):
	def __init__(self):
		self.value=4

class e_hero_state_event(E_HERO_STATE):
	def __init__(self):
		self.value=5

class e_hero_state_idle(E_HERO_STATE):
	def __init__(self):
		self.value=6

class E_CITY_PERIOD(enum):
	pass

class e_city_period_close(E_CITY_PERIOD):
	def __init__(self):
		self.value=-1

class e_city_period_rebel(E_CITY_PERIOD):
	def __init__(self):
		self.value=0

class e_city_period_open(E_CITY_PERIOD):
	def __init__(self):
		self.value=1

class E_STABLE_DROP(enum):
	pass

class e_stable_drop_wash_skill(E_STABLE_DROP):
	def __init__(self):
		self.value=0

class state_status_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.status = E_STATE_STATUS()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.status.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.status.deserialize(buff)
		return buff

class guid(proto):
	def __init__(self):
		self.id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.id.deserialize(buff)
		return buff

class hangup_meterial(proto):
	def __init__(self):
		self.meterial_entry = cint32()
		self.meterial_num = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.meterial_entry.serialize(buff, buff_len)
		buff, buff_len = self.meterial_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.meterial_entry.deserialize(buff)
		buff = self.meterial_num.deserialize(buff)
		return buff

class hangup_drops(proto):
	def __init__(self):
		self.len_of_normal_drops = cuint16()
		self.normal_drops = []
		self.len_of_quality_drops = cuint16()
		self.quality_drops = []
		self.len_of_meterials = cuint16()
		self.meterials = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.len_of_normal_drops.serialize(buff, buff_len)
		for i in range(self.len_of_normal_drops.value):
			buff, buff_len = self.normal_drops[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_quality_drops.serialize(buff, buff_len)
		for i in range(self.len_of_quality_drops.value):
			buff, buff_len = self.quality_drops[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_meterials.serialize(buff, buff_len)
		for i in range(self.len_of_meterials.value):
			buff, buff_len = self.meterials[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.len_of_normal_drops.deserialize(buff)
		self.normal_drops = []
		for i in range(self.len_of_normal_drops.value):
			self.normal_drops.append(cint32())
			buff = self.normal_drops[i].deserialize(buff)
		buff = self.len_of_quality_drops.deserialize(buff)
		self.quality_drops = []
		for i in range(self.len_of_quality_drops.value):
			self.quality_drops.append(cint32())
			buff = self.quality_drops[i].deserialize(buff)
		buff = self.len_of_meterials.deserialize(buff)
		self.meterials = []
		for i in range(self.len_of_meterials.value):
			self.meterials.append(hangup_meterial())
			buff = self.meterials[i].deserialize(buff)
		return buff

	def add_normal_drops():
		if len(normal_drops) >= MAX_HANG_UP_DROP_NUM.value:
			return None
		normal_drops.append(ccint32())
		return normal_drops[len(normal_drops) - 1]

	def add_quality_drops():
		if len(quality_drops) >= MAX_HANG_UP_DROP_NUM.value:
			return None
		quality_drops.append(ccint32())
		return quality_drops[len(quality_drops) - 1]

	def add_meterials():
		if len(meterials) >= MAX_HANGUP_SLOT.value:
			return None
		meterials.append(hangup_meterial())
		return meterials[len(meterials) - 1]

class session_t(proto):
	def __init__(self):
		self.protocol_key = cint32()
		self.user_id = cint64()
		self.key = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.protocol_key.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.key.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.protocol_key.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.key.deserialize(buff)
		return buff

class common_result_t(proto):
	def __init__(self):
		self.result = e_op_result()
		self.tip_msg = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.result.serialize(buff, buff_len)
		buff, buff_len = self.tip_msg.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.result.deserialize(buff)
		buff = self.tip_msg.deserialize(buff)
		return buff

class platform_account_t(proto):
	def __init__(self):
		self.server_id = cint32()
		self.platform_id = cstring()
		self.self_channel = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.server_id.serialize(buff, buff_len)
		buff, buff_len = self.platform_id.serialize(buff, buff_len)
		buff, buff_len = self.self_channel.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.server_id.deserialize(buff)
		buff = self.platform_id.deserialize(buff)
		buff = self.self_channel.deserialize(buff)
		return buff

class device_info_t(proto):
	def __init__(self):
		self.mac = cstring()
		self.real_mac_addr = cstring()
		self.idfa = cstring()
		self.imei = cstring()
		self.device_type = cstring()
		self.device_id = cstring()
		self.os = cstring()
		self.app_version = cstring()
		self.real_package_name = cstring()
		self.login_way = cstring()
		self.os_version = cstring()
		self.iid = cstring()
		self.ip = cstring()
		self.device_platform = cstring()
		self.channel = cstring()
		self.channel_op = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.mac.serialize(buff, buff_len)
		buff, buff_len = self.real_mac_addr.serialize(buff, buff_len)
		buff, buff_len = self.idfa.serialize(buff, buff_len)
		buff, buff_len = self.imei.serialize(buff, buff_len)
		buff, buff_len = self.device_type.serialize(buff, buff_len)
		buff, buff_len = self.device_id.serialize(buff, buff_len)
		buff, buff_len = self.os.serialize(buff, buff_len)
		buff, buff_len = self.app_version.serialize(buff, buff_len)
		buff, buff_len = self.real_package_name.serialize(buff, buff_len)
		buff, buff_len = self.login_way.serialize(buff, buff_len)
		buff, buff_len = self.os_version.serialize(buff, buff_len)
		buff, buff_len = self.iid.serialize(buff, buff_len)
		buff, buff_len = self.ip.serialize(buff, buff_len)
		buff, buff_len = self.device_platform.serialize(buff, buff_len)
		buff, buff_len = self.channel.serialize(buff, buff_len)
		buff, buff_len = self.channel_op.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.mac.deserialize(buff)
		buff = self.real_mac_addr.deserialize(buff)
		buff = self.idfa.deserialize(buff)
		buff = self.imei.deserialize(buff)
		buff = self.device_type.deserialize(buff)
		buff = self.device_id.deserialize(buff)
		buff = self.os.deserialize(buff)
		buff = self.app_version.deserialize(buff)
		buff = self.real_package_name.deserialize(buff)
		buff = self.login_way.deserialize(buff)
		buff = self.os_version.deserialize(buff)
		buff = self.iid.deserialize(buff)
		buff = self.ip.deserialize(buff)
		buff = self.device_platform.deserialize(buff)
		buff = self.channel.deserialize(buff)
		buff = self.channel_op.deserialize(buff)
		return buff

class login_register_res_t(proto):
	def __init__(self):
		self.session = session_t()
		self.time = cuint32()
		self.time_zone = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.session.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		buff, buff_len = self.time_zone.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.session.deserialize(buff)
		buff = self.time.deserialize(buff)
		buff = self.time_zone.deserialize(buff)
		return buff

class user_resource_t(proto):
	def __init__(self):
		self.wood = cuint32()
		self.stone = cuint32()
		self.grain = cuint32()
		self.iron = cuint32()
		self.copper = cuint32()
		self.oil = cuint32()
		self.gold_coin = cuint32()
		self.silver_coin = cuint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.wood.serialize(buff, buff_len)
		buff, buff_len = self.stone.serialize(buff, buff_len)
		buff, buff_len = self.grain.serialize(buff, buff_len)
		buff, buff_len = self.iron.serialize(buff, buff_len)
		buff, buff_len = self.copper.serialize(buff, buff_len)
		buff, buff_len = self.oil.serialize(buff, buff_len)
		buff, buff_len = self.gold_coin.serialize(buff, buff_len)
		buff, buff_len = self.silver_coin.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.wood.deserialize(buff)
		buff = self.stone.deserialize(buff)
		buff = self.grain.deserialize(buff)
		buff = self.iron.deserialize(buff)
		buff = self.copper.deserialize(buff)
		buff = self.oil.deserialize(buff)
		buff = self.gold_coin.deserialize(buff)
		buff = self.silver_coin.deserialize(buff)
		return buff

class effect_data(proto):
	def __init__(self):
		self.type = E_EFFECT_TYPE()
		self.val = cint32()
		self.effect_type = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.type.serialize(buff, buff_len)
		buff, buff_len = self.val.serialize(buff, buff_len)
		buff, buff_len = self.effect_type.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.type.deserialize(buff)
		buff = self.val.deserialize(buff)
		buff = self.effect_type.deserialize(buff)
		return buff

class effect_data_array(proto):
	def __init__(self):
		self.len_of_miracle_effect = cuint16()
		self.miracle_effect = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.len_of_miracle_effect.serialize(buff, buff_len)
		for i in range(self.len_of_miracle_effect.value):
			buff, buff_len = self.miracle_effect[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.len_of_miracle_effect.deserialize(buff)
		self.miracle_effect = []
		for i in range(self.len_of_miracle_effect.value):
			self.miracle_effect.append(effect_data())
			buff = self.miracle_effect[i].deserialize(buff)
		return buff

	def add_miracle_effect():
		if len(miracle_effect) >= e_effect_type_global_max.value:
			return None
		miracle_effect.append(effect_data())
		return miracle_effect[len(miracle_effect) - 1]

class user_resource_limit_t(proto):
	def __init__(self):
		self.wood_limit = cint32()
		self.stone_limit = cint32()
		self.grain_limit = cint32()
		self.iron_limit = cint32()
		self.copper_limit = cint32()
		self.oil_limit = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.wood_limit.serialize(buff, buff_len)
		buff, buff_len = self.stone_limit.serialize(buff, buff_len)
		buff, buff_len = self.grain_limit.serialize(buff, buff_len)
		buff, buff_len = self.iron_limit.serialize(buff, buff_len)
		buff, buff_len = self.copper_limit.serialize(buff, buff_len)
		buff, buff_len = self.oil_limit.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.wood_limit.deserialize(buff)
		buff = self.stone_limit.deserialize(buff)
		buff = self.grain_limit.deserialize(buff)
		buff = self.iron_limit.deserialize(buff)
		buff = self.copper_limit.deserialize(buff)
		buff = self.oil_limit.deserialize(buff)
		return buff

class building_count_t(proto):
	def __init__(self):
		self.castle = cuint32()
		self.vice_castle = cuint32()
		self.farm = cuint32()
		self.mine = cuint32()
		self.mill = cuint32()
		self.quarry = cuint32()
		self.fort = cuint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.castle.serialize(buff, buff_len)
		buff, buff_len = self.vice_castle.serialize(buff, buff_len)
		buff, buff_len = self.farm.serialize(buff, buff_len)
		buff, buff_len = self.mine.serialize(buff, buff_len)
		buff, buff_len = self.mill.serialize(buff, buff_len)
		buff, buff_len = self.quarry.serialize(buff, buff_len)
		buff, buff_len = self.fort.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.castle.deserialize(buff)
		buff = self.vice_castle.deserialize(buff)
		buff = self.farm.deserialize(buff)
		buff = self.mine.deserialize(buff)
		buff = self.mill.deserialize(buff)
		buff = self.quarry.deserialize(buff)
		buff = self.fort.deserialize(buff)
		return buff

class land_count_t(proto):
	def __init__(self):
		self.len_of_land = cuint16()
		self.land = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.len_of_land.serialize(buff, buff_len)
		for i in range(self.len_of_land.value):
			buff, buff_len = self.land[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.len_of_land.deserialize(buff)
		self.land = []
		for i in range(self.len_of_land.value):
			self.land.append(cuint32())
			buff = self.land[i].deserialize(buff)
		return buff

	def add_land():
		if len(land) >= MAX_LAND_LEVEL.value:
			return None
		land.append(ccuint32())
		return land[len(land) - 1]

class trap_data_t(proto):
	def __init__(self):
		self.trap_entry = cint32()
		self.count = cint32()
		self.building_count = cint32()
		self.building_finish_time = cint32()
		self.building_start_time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.trap_entry.serialize(buff, buff_len)
		buff, buff_len = self.count.serialize(buff, buff_len)
		buff, buff_len = self.building_count.serialize(buff, buff_len)
		buff, buff_len = self.building_finish_time.serialize(buff, buff_len)
		buff, buff_len = self.building_start_time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.trap_entry.deserialize(buff)
		buff = self.count.deserialize(buff)
		buff = self.building_count.deserialize(buff)
		buff = self.building_finish_time.deserialize(buff)
		buff = self.building_start_time.deserialize(buff)
		return buff

class user_kill_point_t(proto):
	def __init__(self):
		self.reward = cint32()
		self.section = cint32()
		self.killpoint = cint32()
		self.progress = cint32()
		self.kp_title = cint32()
		self.period = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.reward.serialize(buff, buff_len)
		buff, buff_len = self.section.serialize(buff, buff_len)
		buff, buff_len = self.killpoint.serialize(buff, buff_len)
		buff, buff_len = self.progress.serialize(buff, buff_len)
		buff, buff_len = self.kp_title.serialize(buff, buff_len)
		buff, buff_len = self.period.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.reward.deserialize(buff)
		buff = self.section.deserialize(buff)
		buff = self.killpoint.deserialize(buff)
		buff = self.progress.deserialize(buff)
		buff = self.kp_title.deserialize(buff)
		buff = self.period.deserialize(buff)
		return buff

class castle_info_t(proto):
	def __init__(self):
		self.castle_id = cint64()
		self.centre_coord = cint32()
		self.len_of_area_list = cuint16()
		self.area_list = []
		self.building_name = cstring()
		self.defend_hero_entry_0 = cint32()
		self.defend_hero_entry_1 = cint32()
		self.defend_hero_entry_2 = cint32()
		self.cur_hp = cint32()
		self.max_hp = cint32()
		self.state = cint32()
		self.build_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.centre_coord.serialize(buff, buff_len)
		buff, buff_len = self.len_of_area_list.serialize(buff, buff_len)
		for i in range(self.len_of_area_list.value):
			buff, buff_len = self.area_list[i].serialize(buff, buff_len)
		buff, buff_len = self.building_name.serialize(buff, buff_len)
		buff, buff_len = self.defend_hero_entry_0.serialize(buff, buff_len)
		buff, buff_len = self.defend_hero_entry_1.serialize(buff, buff_len)
		buff, buff_len = self.defend_hero_entry_2.serialize(buff, buff_len)
		buff, buff_len = self.cur_hp.serialize(buff, buff_len)
		buff, buff_len = self.max_hp.serialize(buff, buff_len)
		buff, buff_len = self.state.serialize(buff, buff_len)
		buff, buff_len = self.build_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.castle_id.deserialize(buff)
		buff = self.centre_coord.deserialize(buff)
		buff = self.len_of_area_list.deserialize(buff)
		self.area_list = []
		for i in range(self.len_of_area_list.value):
			self.area_list.append(cint32())
			buff = self.area_list[i].deserialize(buff)
		buff = self.building_name.deserialize(buff)
		buff = self.defend_hero_entry_0.deserialize(buff)
		buff = self.defend_hero_entry_1.deserialize(buff)
		buff = self.defend_hero_entry_2.deserialize(buff)
		buff = self.cur_hp.deserialize(buff)
		buff = self.max_hp.deserialize(buff)
		buff = self.state.deserialize(buff)
		buff = self.build_id.deserialize(buff)
		return buff

	def add_area_list():
		if len(area_list) >= MAX_CASTLE_AREA_COORD.value:
			return None
		area_list.append(ccint32())
		return area_list[len(area_list) - 1]

class user_resource_increase_t(proto):
	def __init__(self):
		self.wood_inc = cuint32()
		self.stone_inc = cuint32()
		self.grain_inc = cuint32()
		self.iron_inc = cuint32()
		self.copper_inc = cuint32()
		self.oil_inc = cuint32()
		self.res_tick_time = cuint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.wood_inc.serialize(buff, buff_len)
		buff, buff_len = self.stone_inc.serialize(buff, buff_len)
		buff, buff_len = self.grain_inc.serialize(buff, buff_len)
		buff, buff_len = self.iron_inc.serialize(buff, buff_len)
		buff, buff_len = self.copper_inc.serialize(buff, buff_len)
		buff, buff_len = self.oil_inc.serialize(buff, buff_len)
		buff, buff_len = self.res_tick_time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.wood_inc.deserialize(buff)
		buff = self.stone_inc.deserialize(buff)
		buff = self.grain_inc.deserialize(buff)
		buff = self.iron_inc.deserialize(buff)
		buff = self.copper_inc.deserialize(buff)
		buff = self.oil_inc.deserialize(buff)
		buff = self.res_tick_time.deserialize(buff)
		return buff

class user_power_t(proto):
	def __init__(self):
		self.fame = cint32()
		self.fame_limit = cint32()
		self.fame_tick_time = cint32()
		self.land_count = cint32()
		self.land_limit = cint32()
		self.res_building_limit = cint32()
		self.res_building_num = cint32()
		self.kp_data = user_kill_point_t()
		self.len_of_medal_list = cuint16()
		self.medal_list = []
		self.force = cint32()
		self.stamina = cint32()
		self.stamina_limit = cint32()
		self.stamina_tick_time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.fame.serialize(buff, buff_len)
		buff, buff_len = self.fame_limit.serialize(buff, buff_len)
		buff, buff_len = self.fame_tick_time.serialize(buff, buff_len)
		buff, buff_len = self.land_count.serialize(buff, buff_len)
		buff, buff_len = self.land_limit.serialize(buff, buff_len)
		buff, buff_len = self.res_building_limit.serialize(buff, buff_len)
		buff, buff_len = self.res_building_num.serialize(buff, buff_len)
		buff, buff_len = self.kp_data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_medal_list.serialize(buff, buff_len)
		for i in range(self.len_of_medal_list.value):
			buff, buff_len = self.medal_list[i].serialize(buff, buff_len)
		buff, buff_len = self.force.serialize(buff, buff_len)
		buff, buff_len = self.stamina.serialize(buff, buff_len)
		buff, buff_len = self.stamina_limit.serialize(buff, buff_len)
		buff, buff_len = self.stamina_tick_time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.fame.deserialize(buff)
		buff = self.fame_limit.deserialize(buff)
		buff = self.fame_tick_time.deserialize(buff)
		buff = self.land_count.deserialize(buff)
		buff = self.land_limit.deserialize(buff)
		buff = self.res_building_limit.deserialize(buff)
		buff = self.res_building_num.deserialize(buff)
		buff = self.kp_data.deserialize(buff)
		buff = self.len_of_medal_list.deserialize(buff)
		self.medal_list = []
		for i in range(self.len_of_medal_list.value):
			self.medal_list.append(cint32())
			buff = self.medal_list[i].deserialize(buff)
		buff = self.force.deserialize(buff)
		buff = self.stamina.deserialize(buff)
		buff = self.stamina_limit.deserialize(buff)
		buff = self.stamina_tick_time.deserialize(buff)
		return buff

	def add_medal_list():
		if len(medal_list) >= MAX_EQUIP_MEDAL_NUM.value:
			return None
		medal_list.append(ccint32())
		return medal_list[len(medal_list) - 1]

class user_common_data(proto):
	def __init__(self):
		self.resource_info = user_resource_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.resource_info.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.resource_info.deserialize(buff)
		return buff

class user_summary_data_t(proto):
	def __init__(self):
		self.user_id = cint64()
		self.nick_name = cstring()
		self.signature = cstring()
		self.head_entry = cint32()
		self.block_id = cint32()
		self.guild_name = cstring()
		self.force = cint32()
		self.position = cint32()
		self.region = cint32()
		self.vip_lv = cint32()
		self.len_of_medal_list = cuint16()
		self.medal_list = []
		self.nobility_entry = cint32()
		self.invadeid = cint64()
		self.guild_id = cint64()
		self.register_time = cint32()
		self.seize_protect_time = cint32()
		self.head_type = cint32()
		self.head_url = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		buff, buff_len = self.signature.serialize(buff, buff_len)
		buff, buff_len = self.head_entry.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.guild_name.serialize(buff, buff_len)
		buff, buff_len = self.force.serialize(buff, buff_len)
		buff, buff_len = self.position.serialize(buff, buff_len)
		buff, buff_len = self.region.serialize(buff, buff_len)
		buff, buff_len = self.vip_lv.serialize(buff, buff_len)
		buff, buff_len = self.len_of_medal_list.serialize(buff, buff_len)
		for i in range(self.len_of_medal_list.value):
			buff, buff_len = self.medal_list[i].serialize(buff, buff_len)
		buff, buff_len = self.nobility_entry.serialize(buff, buff_len)
		buff, buff_len = self.invadeid.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.register_time.serialize(buff, buff_len)
		buff, buff_len = self.seize_protect_time.serialize(buff, buff_len)
		buff, buff_len = self.head_type.serialize(buff, buff_len)
		buff, buff_len = self.head_url.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_id.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		buff = self.signature.deserialize(buff)
		buff = self.head_entry.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.guild_name.deserialize(buff)
		buff = self.force.deserialize(buff)
		buff = self.position.deserialize(buff)
		buff = self.region.deserialize(buff)
		buff = self.vip_lv.deserialize(buff)
		buff = self.len_of_medal_list.deserialize(buff)
		self.medal_list = []
		for i in range(self.len_of_medal_list.value):
			self.medal_list.append(cint32())
			buff = self.medal_list[i].deserialize(buff)
		buff = self.nobility_entry.deserialize(buff)
		buff = self.invadeid.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		buff = self.register_time.deserialize(buff)
		buff = self.seize_protect_time.deserialize(buff)
		buff = self.head_type.deserialize(buff)
		buff = self.head_url.deserialize(buff)
		return buff

	def add_medal_list():
		if len(medal_list) >= MAX_EQUIP_MEDAL_NUM.value:
			return None
		medal_list.append(ccint32())
		return medal_list[len(medal_list) - 1]

class user_land_t(proto):
	def __init__(self):
		self.vcastle_num = cuint32()
		self.fort_num = cuint32()
		self.land_num = cuint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.vcastle_num.serialize(buff, buff_len)
		buff, buff_len = self.fort_num.serialize(buff, buff_len)
		buff, buff_len = self.land_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.vcastle_num.deserialize(buff)
		buff = self.fort_num.deserialize(buff)
		buff = self.land_num.deserialize(buff)
		return buff

class user_war_t(proto):
	def __init__(self):
		self.kill_point = cint32()
		self.title = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.kill_point.serialize(buff, buff_len)
		buff, buff_len = self.title.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.kill_point.deserialize(buff)
		buff = self.title.deserialize(buff)
		return buff

class user_mark_t(proto):
	def __init__(self):
		self.user_id = cint64()
		self.block_id = cint32()
		self.time = cint32()
		self.name = cstring()
		self.notice = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		buff, buff_len = self.notice.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_id.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.time.deserialize(buff)
		buff = self.name.deserialize(buff)
		buff = self.notice.deserialize(buff)
		return buff

class block_mark_t(proto):
	def __init__(self):
		self.user_id = cint64()
		self.block_id = cint32()
		self.time = cint32()
		self.name = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_id.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.time.deserialize(buff)
		buff = self.name.deserialize(buff)
		return buff

class guild_member_brief_t(proto):
	def __init__(self):
		self.guild_id = cint64()
		self.name = cstring()
		self.position = cint32()
		self.icon = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		buff, buff_len = self.position.serialize(buff, buff_len)
		buff, buff_len = self.icon.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.guild_id.deserialize(buff)
		buff = self.name.deserialize(buff)
		buff = self.position.deserialize(buff)
		buff = self.icon.deserialize(buff)
		return buff

class guild_member_t(proto):
	def __init__(self):
		self.guild_id = cint64()
		self.position = cint32()
		self.time = cint32()
		self.group_id = cint64()
		self.contribution = cint32()
		self.contribution_of_week = cint32()
		self.contribution_of_day = cint32()
		self.battle_con_of_day = cint32()
		self.contribution_of_gold = cint32()
		self.kp_data = user_kill_point_t()
		self.chat_channel_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.position.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		buff, buff_len = self.contribution.serialize(buff, buff_len)
		buff, buff_len = self.contribution_of_week.serialize(buff, buff_len)
		buff, buff_len = self.contribution_of_day.serialize(buff, buff_len)
		buff, buff_len = self.battle_con_of_day.serialize(buff, buff_len)
		buff, buff_len = self.contribution_of_gold.serialize(buff, buff_len)
		buff, buff_len = self.kp_data.serialize(buff, buff_len)
		buff, buff_len = self.chat_channel_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.guild_id.deserialize(buff)
		buff = self.position.deserialize(buff)
		buff = self.time.deserialize(buff)
		buff = self.group_id.deserialize(buff)
		buff = self.contribution.deserialize(buff)
		buff = self.contribution_of_week.deserialize(buff)
		buff = self.contribution_of_day.deserialize(buff)
		buff = self.battle_con_of_day.deserialize(buff)
		buff = self.contribution_of_gold.deserialize(buff)
		buff = self.kp_data.deserialize(buff)
		buff = self.chat_channel_id.deserialize(buff)
		return buff

class guild_brief_t(proto):
	def __init__(self):
		self.guild_id = cint64()
		self.name = cstring()
		self.icon = cint32()
		self.state = cint32()
		self.level = cint32()
		self.num = cint32()
		self.chairman_name = cstring()
		self.chairman_id = cint64()
		self.city_num = cint32()
		self.force = cint32()
		self.position = cint32()
		self.force_limit = cint32()
		self.is_limit = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		buff, buff_len = self.icon.serialize(buff, buff_len)
		buff, buff_len = self.state.serialize(buff, buff_len)
		buff, buff_len = self.level.serialize(buff, buff_len)
		buff, buff_len = self.num.serialize(buff, buff_len)
		buff, buff_len = self.chairman_name.serialize(buff, buff_len)
		buff, buff_len = self.chairman_id.serialize(buff, buff_len)
		buff, buff_len = self.city_num.serialize(buff, buff_len)
		buff, buff_len = self.force.serialize(buff, buff_len)
		buff, buff_len = self.position.serialize(buff, buff_len)
		buff, buff_len = self.force_limit.serialize(buff, buff_len)
		buff, buff_len = self.is_limit.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.guild_id.deserialize(buff)
		buff = self.name.deserialize(buff)
		buff = self.icon.deserialize(buff)
		buff = self.state.deserialize(buff)
		buff = self.level.deserialize(buff)
		buff = self.num.deserialize(buff)
		buff = self.chairman_name.deserialize(buff)
		buff = self.chairman_id.deserialize(buff)
		buff = self.city_num.deserialize(buff)
		buff = self.force.deserialize(buff)
		buff = self.position.deserialize(buff)
		buff = self.force_limit.deserialize(buff)
		buff = self.is_limit.deserialize(buff)
		return buff

class invest_info_t(proto):
	def __init__(self):
		self.invest_entry = cint32()
		self.invest_time = cint32()
		self.len_of_invest_refund_day = cuint16()
		self.invest_refund_day = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.invest_entry.serialize(buff, buff_len)
		buff, buff_len = self.invest_time.serialize(buff, buff_len)
		buff, buff_len = self.len_of_invest_refund_day.serialize(buff, buff_len)
		for i in range(self.len_of_invest_refund_day.value):
			buff, buff_len = self.invest_refund_day[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.invest_entry.deserialize(buff)
		buff = self.invest_time.deserialize(buff)
		buff = self.len_of_invest_refund_day.deserialize(buff)
		self.invest_refund_day = []
		for i in range(self.len_of_invest_refund_day.value):
			self.invest_refund_day.append(cint32())
			buff = self.invest_refund_day[i].deserialize(buff)
		return buff

	def add_invest_refund_day():
		if len(invest_refund_day) >= MAX_INVEST_REFUND_DAY.value:
			return None
		invest_refund_day.append(ccint32())
		return invest_refund_day[len(invest_refund_day) - 1]

class user_t(proto):
	def __init__(self):
		self.user_id = cint64()
		self.nick_name = cstring()
		self.signature = cstring()
		self.head_entry = cint32()
		self.vip_lv = cint32()
		self.vip_point = cint32()
		self.vip_expire_time = cint32()
		self.resource_info = user_resource_t()
		self.len_of_land_coord_list = cuint16()
		self.land_coord_list = []
		self.resource_icr = user_resource_increase_t()
		self.resource_dec = user_resource_increase_t()
		self.resource_limit = user_resource_limit_t()
		self.power_info = user_power_t()
		self.main_castle_id = cint64()
		self.invader = guild_brief_t()
		self.guild_member_data = guild_member_brief_t()
		self.building_data = building_count_t()
		self.land_data = land_count_t()
		self.sign_day = cint32()
		self.sign_time = cint32()
		self.invest_info = invest_info_t()
		self.move_time = cint32()
		self.guard_time = cint32()
		self.nobility_entry = cint32()
		self.register_time = cint32()
		self.newbie_step = cint32()
		self.region = cint32()
		self.charge_product_id_list = cstring()
		self.free_gold_lottery_surplus_time = cint32()
		self.surplus_lottery_hit_count = cint32()
		self.seize_times = cint32()
		self.seize_protect_time = cint32()
		self.wandering_cd_time = cint32()
		self.newbie_for_zhaoyu = cstring()
		self.token = cint32()
		self.token_buy_times = cint32()
		self.nick_name_change = cint32()
		self.gold_5_draw = cint32()
		self.head_type = cint32()
		self.head_url = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		buff, buff_len = self.signature.serialize(buff, buff_len)
		buff, buff_len = self.head_entry.serialize(buff, buff_len)
		buff, buff_len = self.vip_lv.serialize(buff, buff_len)
		buff, buff_len = self.vip_point.serialize(buff, buff_len)
		buff, buff_len = self.vip_expire_time.serialize(buff, buff_len)
		buff, buff_len = self.resource_info.serialize(buff, buff_len)
		buff, buff_len = self.len_of_land_coord_list.serialize(buff, buff_len)
		for i in range(self.len_of_land_coord_list.value):
			buff, buff_len = self.land_coord_list[i].serialize(buff, buff_len)
		buff, buff_len = self.resource_icr.serialize(buff, buff_len)
		buff, buff_len = self.resource_dec.serialize(buff, buff_len)
		buff, buff_len = self.resource_limit.serialize(buff, buff_len)
		buff, buff_len = self.power_info.serialize(buff, buff_len)
		buff, buff_len = self.main_castle_id.serialize(buff, buff_len)
		buff, buff_len = self.invader.serialize(buff, buff_len)
		buff, buff_len = self.guild_member_data.serialize(buff, buff_len)
		buff, buff_len = self.building_data.serialize(buff, buff_len)
		buff, buff_len = self.land_data.serialize(buff, buff_len)
		buff, buff_len = self.sign_day.serialize(buff, buff_len)
		buff, buff_len = self.sign_time.serialize(buff, buff_len)
		buff, buff_len = self.invest_info.serialize(buff, buff_len)
		buff, buff_len = self.move_time.serialize(buff, buff_len)
		buff, buff_len = self.guard_time.serialize(buff, buff_len)
		buff, buff_len = self.nobility_entry.serialize(buff, buff_len)
		buff, buff_len = self.register_time.serialize(buff, buff_len)
		buff, buff_len = self.newbie_step.serialize(buff, buff_len)
		buff, buff_len = self.region.serialize(buff, buff_len)
		buff, buff_len = self.charge_product_id_list.serialize(buff, buff_len)
		buff, buff_len = self.free_gold_lottery_surplus_time.serialize(buff, buff_len)
		buff, buff_len = self.surplus_lottery_hit_count.serialize(buff, buff_len)
		buff, buff_len = self.seize_times.serialize(buff, buff_len)
		buff, buff_len = self.seize_protect_time.serialize(buff, buff_len)
		buff, buff_len = self.wandering_cd_time.serialize(buff, buff_len)
		buff, buff_len = self.newbie_for_zhaoyu.serialize(buff, buff_len)
		buff, buff_len = self.token.serialize(buff, buff_len)
		buff, buff_len = self.token_buy_times.serialize(buff, buff_len)
		buff, buff_len = self.nick_name_change.serialize(buff, buff_len)
		buff, buff_len = self.gold_5_draw.serialize(buff, buff_len)
		buff, buff_len = self.head_type.serialize(buff, buff_len)
		buff, buff_len = self.head_url.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_id.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		buff = self.signature.deserialize(buff)
		buff = self.head_entry.deserialize(buff)
		buff = self.vip_lv.deserialize(buff)
		buff = self.vip_point.deserialize(buff)
		buff = self.vip_expire_time.deserialize(buff)
		buff = self.resource_info.deserialize(buff)
		buff = self.len_of_land_coord_list.deserialize(buff)
		self.land_coord_list = []
		for i in range(self.len_of_land_coord_list.value):
			self.land_coord_list.append(cint32())
			buff = self.land_coord_list[i].deserialize(buff)
		buff = self.resource_icr.deserialize(buff)
		buff = self.resource_dec.deserialize(buff)
		buff = self.resource_limit.deserialize(buff)
		buff = self.power_info.deserialize(buff)
		buff = self.main_castle_id.deserialize(buff)
		buff = self.invader.deserialize(buff)
		buff = self.guild_member_data.deserialize(buff)
		buff = self.building_data.deserialize(buff)
		buff = self.land_data.deserialize(buff)
		buff = self.sign_day.deserialize(buff)
		buff = self.sign_time.deserialize(buff)
		buff = self.invest_info.deserialize(buff)
		buff = self.move_time.deserialize(buff)
		buff = self.guard_time.deserialize(buff)
		buff = self.nobility_entry.deserialize(buff)
		buff = self.register_time.deserialize(buff)
		buff = self.newbie_step.deserialize(buff)
		buff = self.region.deserialize(buff)
		buff = self.charge_product_id_list.deserialize(buff)
		buff = self.free_gold_lottery_surplus_time.deserialize(buff)
		buff = self.surplus_lottery_hit_count.deserialize(buff)
		buff = self.seize_times.deserialize(buff)
		buff = self.seize_protect_time.deserialize(buff)
		buff = self.wandering_cd_time.deserialize(buff)
		buff = self.newbie_for_zhaoyu.deserialize(buff)
		buff = self.token.deserialize(buff)
		buff = self.token_buy_times.deserialize(buff)
		buff = self.nick_name_change.deserialize(buff)
		buff = self.gold_5_draw.deserialize(buff)
		buff = self.head_type.deserialize(buff)
		buff = self.head_url.deserialize(buff)
		return buff

	def add_land_coord_list():
		if len(land_coord_list) >= MAX_OWN_LAND_NUM.value:
			return None
		land_coord_list.append(ccint32())
		return land_coord_list[len(land_coord_list) - 1]

class block_data_t(proto):
	def __init__(self):
		self.coord = cint32()
		self.building_entry = cint32()
		self.e_block_type = E_BLOCK_TYPE()
		self.occupy_time = cint32()
		self.user_id = cint64()
		self.guild_id = cint64()
		self.protect_finish_time = cint32()
		self.build_finish_time = cint32()
		self.building_name = cstring()
		self.cur_hp = cint32()
		self.max_hp = cint32()
		self.guard_num = cint32()
		self.fort_corps_num = cint32()
		self.guild_name = cstring()
		self.invadeid = cint64()
		self.building_lvup = cbool()
		self.max_block_guard = cint32()
		self.cur_block_guard = cint32()
		self.guard_recover_time = cint32()
		self.state = cint32()
		self.icon = cint32()
		self.block_entry = cint32()
		self.miracle_period_entry = cint32()
		self.miracle_effect_data = effect_data()
		self.user_mark = user_mark_t()
		self.dis_event_id = cint64()
		self.rebel_event_id = cint64()
		self.city_period = E_CITY_PERIOD()
		self.rebel_cur_soldier_num = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.coord.serialize(buff, buff_len)
		buff, buff_len = self.building_entry.serialize(buff, buff_len)
		buff, buff_len = self.e_block_type.serialize(buff, buff_len)
		buff, buff_len = self.occupy_time.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.protect_finish_time.serialize(buff, buff_len)
		buff, buff_len = self.build_finish_time.serialize(buff, buff_len)
		buff, buff_len = self.building_name.serialize(buff, buff_len)
		buff, buff_len = self.cur_hp.serialize(buff, buff_len)
		buff, buff_len = self.max_hp.serialize(buff, buff_len)
		buff, buff_len = self.guard_num.serialize(buff, buff_len)
		buff, buff_len = self.fort_corps_num.serialize(buff, buff_len)
		buff, buff_len = self.guild_name.serialize(buff, buff_len)
		buff, buff_len = self.invadeid.serialize(buff, buff_len)
		buff, buff_len = self.building_lvup.serialize(buff, buff_len)
		buff, buff_len = self.max_block_guard.serialize(buff, buff_len)
		buff, buff_len = self.cur_block_guard.serialize(buff, buff_len)
		buff, buff_len = self.guard_recover_time.serialize(buff, buff_len)
		buff, buff_len = self.state.serialize(buff, buff_len)
		buff, buff_len = self.icon.serialize(buff, buff_len)
		buff, buff_len = self.block_entry.serialize(buff, buff_len)
		buff, buff_len = self.miracle_period_entry.serialize(buff, buff_len)
		buff, buff_len = self.miracle_effect_data.serialize(buff, buff_len)
		buff, buff_len = self.user_mark.serialize(buff, buff_len)
		buff, buff_len = self.dis_event_id.serialize(buff, buff_len)
		buff, buff_len = self.rebel_event_id.serialize(buff, buff_len)
		buff, buff_len = self.city_period.serialize(buff, buff_len)
		buff, buff_len = self.rebel_cur_soldier_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.coord.deserialize(buff)
		buff = self.building_entry.deserialize(buff)
		buff = self.e_block_type.deserialize(buff)
		buff = self.occupy_time.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		buff = self.protect_finish_time.deserialize(buff)
		buff = self.build_finish_time.deserialize(buff)
		buff = self.building_name.deserialize(buff)
		buff = self.cur_hp.deserialize(buff)
		buff = self.max_hp.deserialize(buff)
		buff = self.guard_num.deserialize(buff)
		buff = self.fort_corps_num.deserialize(buff)
		buff = self.guild_name.deserialize(buff)
		buff = self.invadeid.deserialize(buff)
		buff = self.building_lvup.deserialize(buff)
		buff = self.max_block_guard.deserialize(buff)
		buff = self.cur_block_guard.deserialize(buff)
		buff = self.guard_recover_time.deserialize(buff)
		buff = self.state.deserialize(buff)
		buff = self.icon.deserialize(buff)
		buff = self.block_entry.deserialize(buff)
		buff = self.miracle_period_entry.deserialize(buff)
		buff = self.miracle_effect_data.deserialize(buff)
		buff = self.user_mark.deserialize(buff)
		buff = self.dis_event_id.deserialize(buff)
		buff = self.rebel_event_id.deserialize(buff)
		buff = self.city_period.deserialize(buff)
		buff = self.rebel_cur_soldier_num.deserialize(buff)
		return buff

class block_brief_data_t(proto):
	def __init__(self):
		self.coord = cint32()
		self.block_entry = cint32()
		self.building_entry = cint32()
		self.e_block_type = E_BLOCK_TYPE()
		self.occupy_time = cint32()
		self.user_id = cint64()
		self.protect_finish_time = cint32()
		self.build_finish_time = cint32()
		self.cur_hp = cint32()
		self.building_name = cstring()
		self.max_hp = cint32()
		self.guild_id = cint64()
		self.max_block_guard = cint32()
		self.cur_block_guard = cint32()
		self.guild_name = cstring()
		self.state = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.coord.serialize(buff, buff_len)
		buff, buff_len = self.block_entry.serialize(buff, buff_len)
		buff, buff_len = self.building_entry.serialize(buff, buff_len)
		buff, buff_len = self.e_block_type.serialize(buff, buff_len)
		buff, buff_len = self.occupy_time.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.protect_finish_time.serialize(buff, buff_len)
		buff, buff_len = self.build_finish_time.serialize(buff, buff_len)
		buff, buff_len = self.cur_hp.serialize(buff, buff_len)
		buff, buff_len = self.building_name.serialize(buff, buff_len)
		buff, buff_len = self.max_hp.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.max_block_guard.serialize(buff, buff_len)
		buff, buff_len = self.cur_block_guard.serialize(buff, buff_len)
		buff, buff_len = self.guild_name.serialize(buff, buff_len)
		buff, buff_len = self.state.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.coord.deserialize(buff)
		buff = self.block_entry.deserialize(buff)
		buff = self.building_entry.deserialize(buff)
		buff = self.e_block_type.deserialize(buff)
		buff = self.occupy_time.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.protect_finish_time.deserialize(buff)
		buff = self.build_finish_time.deserialize(buff)
		buff = self.cur_hp.deserialize(buff)
		buff = self.building_name.deserialize(buff)
		buff = self.max_hp.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		buff = self.max_block_guard.deserialize(buff)
		buff = self.cur_block_guard.deserialize(buff)
		buff = self.guild_name.deserialize(buff)
		buff = self.state.deserialize(buff)
		return buff

class building_date_t(proto):
	def __init__(self):
		self.castle_id = cint64()
		self.build_id = cint32()
		self.level = cuint32()
		self.cfg_type = E_BUILDING_CONFIG_TYPE()
		self.event_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.build_id.serialize(buff, buff_len)
		buff, buff_len = self.level.serialize(buff, buff_len)
		buff, buff_len = self.cfg_type.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.castle_id.deserialize(buff)
		buff = self.build_id.deserialize(buff)
		buff = self.level.deserialize(buff)
		buff = self.cfg_type.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		return buff

class land_building_date_t(proto):
	def __init__(self):
		self.block_id = cint32()
		self.level = cuint32()
		self.start_time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.level.serialize(buff, buff_len)
		buff, buff_len = self.start_time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.block_id.deserialize(buff)
		buff = self.level.deserialize(buff)
		buff = self.start_time.deserialize(buff)
		return buff

class equip_slot_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.strengthen_lv = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.strengthen_lv.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.strengthen_lv.deserialize(buff)
		return buff

class hero_data_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.level = cint32()
		self.exp = cint32()
		self.liliang = cint32()
		self.naili = cint32()
		self.moulue = cint32()
		self.minjie = cint32()
		self.destroy = cint32()
		self.free_point = cint32()
		self.junxian = cint32()
		self.len_of_equip_slot_list = cuint16()
		self.equip_slot_list = []
		self.phy_force = cint32()
		self.phy_force_time = cint32()
		self.phy_force_max = cint32()
		self.obtain_time = cint32()
		self.train_scheme_idx = cint32()
		self.train_finish_time = cint32()
		self.train_start_time = cint32()
		self.train_slot_idx = cint32()
		self.train_castle_id = cint64()
		self.star_lv = cint32()
		self.quality = E_HERO_QUALITY()
		self.quality_lv = cint32()
		self.power = cint32()
		self.len_of_skill_lv = cuint16()
		self.skill_lv = []
		self.len_of_skill_entry = cuint16()
		self.skill_entry = []
		self.len_of_wash_skill_entry = cuint16()
		self.wash_skill_entry = []
		self.len_of_wash_quality = cuint16()
		self.wash_quality = []
		self.hangup_count = cint32()
		self.hangup_value = cint32()
		self.event_id = cint64()
		self.soldier_entry = cint32()
		self.last_spirit_buy_fresh = cint32()
		self.spirit_buy_times = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.level.serialize(buff, buff_len)
		buff, buff_len = self.exp.serialize(buff, buff_len)
		buff, buff_len = self.liliang.serialize(buff, buff_len)
		buff, buff_len = self.naili.serialize(buff, buff_len)
		buff, buff_len = self.moulue.serialize(buff, buff_len)
		buff, buff_len = self.minjie.serialize(buff, buff_len)
		buff, buff_len = self.destroy.serialize(buff, buff_len)
		buff, buff_len = self.free_point.serialize(buff, buff_len)
		buff, buff_len = self.junxian.serialize(buff, buff_len)
		buff, buff_len = self.len_of_equip_slot_list.serialize(buff, buff_len)
		for i in range(self.len_of_equip_slot_list.value):
			buff, buff_len = self.equip_slot_list[i].serialize(buff, buff_len)
		buff, buff_len = self.phy_force.serialize(buff, buff_len)
		buff, buff_len = self.phy_force_time.serialize(buff, buff_len)
		buff, buff_len = self.phy_force_max.serialize(buff, buff_len)
		buff, buff_len = self.obtain_time.serialize(buff, buff_len)
		buff, buff_len = self.train_scheme_idx.serialize(buff, buff_len)
		buff, buff_len = self.train_finish_time.serialize(buff, buff_len)
		buff, buff_len = self.train_start_time.serialize(buff, buff_len)
		buff, buff_len = self.train_slot_idx.serialize(buff, buff_len)
		buff, buff_len = self.train_castle_id.serialize(buff, buff_len)
		buff, buff_len = self.star_lv.serialize(buff, buff_len)
		buff, buff_len = self.quality.serialize(buff, buff_len)
		buff, buff_len = self.quality_lv.serialize(buff, buff_len)
		buff, buff_len = self.power.serialize(buff, buff_len)
		buff, buff_len = self.len_of_skill_lv.serialize(buff, buff_len)
		for i in range(self.len_of_skill_lv.value):
			buff, buff_len = self.skill_lv[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_skill_entry.serialize(buff, buff_len)
		for i in range(self.len_of_skill_entry.value):
			buff, buff_len = self.skill_entry[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_wash_skill_entry.serialize(buff, buff_len)
		for i in range(self.len_of_wash_skill_entry.value):
			buff, buff_len = self.wash_skill_entry[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_wash_quality.serialize(buff, buff_len)
		for i in range(self.len_of_wash_quality.value):
			buff, buff_len = self.wash_quality[i].serialize(buff, buff_len)
		buff, buff_len = self.hangup_count.serialize(buff, buff_len)
		buff, buff_len = self.hangup_value.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.soldier_entry.serialize(buff, buff_len)
		buff, buff_len = self.last_spirit_buy_fresh.serialize(buff, buff_len)
		buff, buff_len = self.spirit_buy_times.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.level.deserialize(buff)
		buff = self.exp.deserialize(buff)
		buff = self.liliang.deserialize(buff)
		buff = self.naili.deserialize(buff)
		buff = self.moulue.deserialize(buff)
		buff = self.minjie.deserialize(buff)
		buff = self.destroy.deserialize(buff)
		buff = self.free_point.deserialize(buff)
		buff = self.junxian.deserialize(buff)
		buff = self.len_of_equip_slot_list.deserialize(buff)
		self.equip_slot_list = []
		for i in range(self.len_of_equip_slot_list.value):
			self.equip_slot_list.append(equip_slot_t())
			buff = self.equip_slot_list[i].deserialize(buff)
		buff = self.phy_force.deserialize(buff)
		buff = self.phy_force_time.deserialize(buff)
		buff = self.phy_force_max.deserialize(buff)
		buff = self.obtain_time.deserialize(buff)
		buff = self.train_scheme_idx.deserialize(buff)
		buff = self.train_finish_time.deserialize(buff)
		buff = self.train_start_time.deserialize(buff)
		buff = self.train_slot_idx.deserialize(buff)
		buff = self.train_castle_id.deserialize(buff)
		buff = self.star_lv.deserialize(buff)
		buff = self.quality.deserialize(buff)
		buff = self.quality_lv.deserialize(buff)
		buff = self.power.deserialize(buff)
		buff = self.len_of_skill_lv.deserialize(buff)
		self.skill_lv = []
		for i in range(self.len_of_skill_lv.value):
			self.skill_lv.append(cint32())
			buff = self.skill_lv[i].deserialize(buff)
		buff = self.len_of_skill_entry.deserialize(buff)
		self.skill_entry = []
		for i in range(self.len_of_skill_entry.value):
			self.skill_entry.append(cint32())
			buff = self.skill_entry[i].deserialize(buff)
		buff = self.len_of_wash_skill_entry.deserialize(buff)
		self.wash_skill_entry = []
		for i in range(self.len_of_wash_skill_entry.value):
			self.wash_skill_entry.append(cint32())
			buff = self.wash_skill_entry[i].deserialize(buff)
		buff = self.len_of_wash_quality.deserialize(buff)
		self.wash_quality = []
		for i in range(self.len_of_wash_quality.value):
			self.wash_quality.append(cint32())
			buff = self.wash_quality[i].deserialize(buff)
		buff = self.hangup_count.deserialize(buff)
		buff = self.hangup_value.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.soldier_entry.deserialize(buff)
		buff = self.last_spirit_buy_fresh.deserialize(buff)
		buff = self.spirit_buy_times.deserialize(buff)
		return buff

	def add_equip_slot_list():
		if len(equip_slot_list) >= e_equip_slot_max.value:
			return None
		equip_slot_list.append(equip_slot_t())
		return equip_slot_list[len(equip_slot_list) - 1]

	def add_skill_lv():
		if len(skill_lv) >= MAX_HERO_SKILL_NUM.value:
			return None
		skill_lv.append(ccint32())
		return skill_lv[len(skill_lv) - 1]

	def add_skill_entry():
		if len(skill_entry) >= MAX_HERO_SKILL_NUM.value:
			return None
		skill_entry.append(ccint32())
		return skill_entry[len(skill_entry) - 1]

	def add_wash_skill_entry():
		if len(wash_skill_entry) >= MAX_HERO_SKILL_NUM.value:
			return None
		wash_skill_entry.append(ccint32())
		return wash_skill_entry[len(wash_skill_entry) - 1]

	def add_wash_quality():
		if len(wash_quality) >= MAX_HERO_SKILL_NUM.value:
			return None
		wash_quality.append(ccint32())
		return wash_quality[len(wash_quality) - 1]

class hero_reset_reback_item_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.num = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.num.deserialize(buff)
		return buff

class hero_reset_reback_t(proto):
	def __init__(self):
		self.silver_coin = cint32()
		self.len_of_reback_item_data_list = cuint16()
		self.reback_item_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.silver_coin.serialize(buff, buff_len)
		buff, buff_len = self.len_of_reback_item_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_reback_item_data_list.value):
			buff, buff_len = self.reback_item_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.silver_coin.deserialize(buff)
		buff = self.len_of_reback_item_data_list.deserialize(buff)
		self.reback_item_data_list = []
		for i in range(self.len_of_reback_item_data_list.value):
			self.reback_item_data_list.append(hero_reset_reback_item_t())
			buff = self.reback_item_data_list[i].deserialize(buff)
		return buff

	def add_reback_item_data_list():
		if len(reback_item_data_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		reback_item_data_list.append(hero_reset_reback_item_t())
		return reback_item_data_list[len(reback_item_data_list) - 1]

class troops_data_t(proto):
	def __init__(self):
		self.soldier_entry = cint32()
		self.soldier_num = cint32()
		self.battle_pos = cint32()
		self.conscript_soldier = cint32()
		self.finish_time = cint32()
		self.start_time = cint32()
		self.event_id = cint64()
		self.is_transform = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.soldier_entry.serialize(buff, buff_len)
		buff, buff_len = self.soldier_num.serialize(buff, buff_len)
		buff, buff_len = self.battle_pos.serialize(buff, buff_len)
		buff, buff_len = self.conscript_soldier.serialize(buff, buff_len)
		buff, buff_len = self.finish_time.serialize(buff, buff_len)
		buff, buff_len = self.start_time.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.is_transform.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.soldier_entry.deserialize(buff)
		buff = self.soldier_num.deserialize(buff)
		buff = self.battle_pos.deserialize(buff)
		buff = self.conscript_soldier.deserialize(buff)
		buff = self.finish_time.deserialize(buff)
		buff = self.start_time.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.is_transform.deserialize(buff)
		return buff

class corps_key_t(proto):
	def __init__(self):
		self.castle_id = cint64()
		self.pos_index = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.pos_index.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.castle_id.deserialize(buff)
		buff = self.pos_index.deserialize(buff)
		return buff

class corps_data_t(proto):
	def __init__(self):
		self.corps_key = corps_key_t()
		self.corps_lv = cint32()
		self.corps_exp = cint32()
		self.hero_entry = cint32()
		self.hero_entry_1 = cint32()
		self.hero_entry_2 = cint32()
		self.phy = cint32()
		self.phy_time = cint32()
		self.phy_max = cint32()
		self.len_of_troops_data_list = cuint16()
		self.troops_data_list = []
		self.cur_block_id = cint32()
		self.fort_id = cint32()
		self.event_id = cint64()
		self.corps_state = E_CORPS_STATE()
		self.heal_time = cint32()
		self.move_speed = cint32()
		self.corps_power = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.corps_lv.serialize(buff, buff_len)
		buff, buff_len = self.corps_exp.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry_1.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry_2.serialize(buff, buff_len)
		buff, buff_len = self.phy.serialize(buff, buff_len)
		buff, buff_len = self.phy_time.serialize(buff, buff_len)
		buff, buff_len = self.phy_max.serialize(buff, buff_len)
		buff, buff_len = self.len_of_troops_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_troops_data_list.value):
			buff, buff_len = self.troops_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.cur_block_id.serialize(buff, buff_len)
		buff, buff_len = self.fort_id.serialize(buff, buff_len)
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.corps_state.serialize(buff, buff_len)
		buff, buff_len = self.heal_time.serialize(buff, buff_len)
		buff, buff_len = self.move_speed.serialize(buff, buff_len)
		buff, buff_len = self.corps_power.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.corps_key.deserialize(buff)
		buff = self.corps_lv.deserialize(buff)
		buff = self.corps_exp.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.hero_entry_1.deserialize(buff)
		buff = self.hero_entry_2.deserialize(buff)
		buff = self.phy.deserialize(buff)
		buff = self.phy_time.deserialize(buff)
		buff = self.phy_max.deserialize(buff)
		buff = self.len_of_troops_data_list.deserialize(buff)
		self.troops_data_list = []
		for i in range(self.len_of_troops_data_list.value):
			self.troops_data_list.append(troops_data_t())
			buff = self.troops_data_list[i].deserialize(buff)
		buff = self.cur_block_id.deserialize(buff)
		buff = self.fort_id.deserialize(buff)
		buff = self.event_id.deserialize(buff)
		buff = self.corps_state.deserialize(buff)
		buff = self.heal_time.deserialize(buff)
		buff = self.move_speed.deserialize(buff)
		buff = self.corps_power.deserialize(buff)
		return buff

	def add_troops_data_list():
		if len(troops_data_list) >= MAX_CORPS_TROOPS_NUM.value:
			return None
		troops_data_list.append(troops_data_t())
		return troops_data_list[len(troops_data_list) - 1]

class game_event_data_t(proto):
	def __init__(self):
		self.event_id = cint64()
		self.user_summary_data = user_summary_data_t()
		self.e_event_type = E_EVENT_TYPE()
		self.src_block_id = cint32()
		self.dest_block_id = cint32()
		self.corps_key = corps_key_t()
		self.build_id = cint32()
		self.start_time = cint32()
		self.finish_time = cint32()
		self.building_name = cstring()
		self.assist = cbool()
		self.cur_times = cint32()
		self.total_times = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.user_summary_data.serialize(buff, buff_len)
		buff, buff_len = self.e_event_type.serialize(buff, buff_len)
		buff, buff_len = self.src_block_id.serialize(buff, buff_len)
		buff, buff_len = self.dest_block_id.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.build_id.serialize(buff, buff_len)
		buff, buff_len = self.start_time.serialize(buff, buff_len)
		buff, buff_len = self.finish_time.serialize(buff, buff_len)
		buff, buff_len = self.building_name.serialize(buff, buff_len)
		buff, buff_len = self.assist.serialize(buff, buff_len)
		buff, buff_len = self.cur_times.serialize(buff, buff_len)
		buff, buff_len = self.total_times.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.event_id.deserialize(buff)
		buff = self.user_summary_data.deserialize(buff)
		buff = self.e_event_type.deserialize(buff)
		buff = self.src_block_id.deserialize(buff)
		buff = self.dest_block_id.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.build_id.deserialize(buff)
		buff = self.start_time.deserialize(buff)
		buff = self.finish_time.deserialize(buff)
		buff = self.building_name.deserialize(buff)
		buff = self.assist.deserialize(buff)
		buff = self.cur_times.deserialize(buff)
		buff = self.total_times.deserialize(buff)
		return buff

class game_event_result_data_t(proto):
	def __init__(self):
		self.e_result_type = E_EVENT_RESULT_TYPE()
		self.battle_id = cint64()
		self.game_event_data = game_event_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.e_result_type.serialize(buff, buff_len)
		buff, buff_len = self.battle_id.serialize(buff, buff_len)
		buff, buff_len = self.game_event_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.e_result_type.deserialize(buff)
		buff = self.battle_id.deserialize(buff)
		buff = self.game_event_data.deserialize(buff)
		return buff

class battle_result_t(proto):
	def __init__(self):
		self.event_id = cint64()
		self.e_battle_result_type = E_BATTLE_RESULT_TYPE()
		self.block_id = cint32()
		self.battle_time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.e_battle_result_type.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.battle_time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.event_id.deserialize(buff)
		buff = self.e_battle_result_type.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.battle_time.deserialize(buff)
		return buff

class item_data_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.num = cint32()
		self.diff = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.num.serialize(buff, buff_len)
		buff, buff_len = self.diff.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.num.deserialize(buff)
		buff = self.diff.deserialize(buff)
		return buff

class corps_guard_t(proto):
	def __init__(self):
		self.block_id = cint32()
		self.user_id = cint64()
		self.castle_id = cint64()
		self.pos_index = cint32()
		self.guard_time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.pos_index.serialize(buff, buff_len)
		buff, buff_len = self.guard_time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.block_id.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.castle_id.deserialize(buff)
		buff = self.pos_index.deserialize(buff)
		buff = self.guard_time.deserialize(buff)
		return buff

class block_guard_brief_data_t(proto):
	def __init__(self):
		self.user_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_id.deserialize(buff)
		return buff

class block_fort_corps_brief_data_t(proto):
	def __init__(self):
		self.user_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_id.deserialize(buff)
		return buff

class fort_data_t(proto):
	def __init__(self):
		self.block_id = cint32()
		self.user_id = cint64()
		self.build_id = cint32()
		self.len_of_corps_key_list = cuint16()
		self.corps_key_list = []
		self.building_name = cstring()
		self.state = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.build_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_corps_key_list.serialize(buff, buff_len)
		for i in range(self.len_of_corps_key_list.value):
			buff, buff_len = self.corps_key_list[i].serialize(buff, buff_len)
		buff, buff_len = self.building_name.serialize(buff, buff_len)
		buff, buff_len = self.state.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.block_id.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.build_id.deserialize(buff)
		buff = self.len_of_corps_key_list.deserialize(buff)
		self.corps_key_list = []
		for i in range(self.len_of_corps_key_list.value):
			self.corps_key_list.append(corps_key_t())
			buff = self.corps_key_list[i].deserialize(buff)
		buff = self.building_name.deserialize(buff)
		buff = self.state.deserialize(buff)
		return buff

	def add_corps_key_list():
		if len(corps_key_list) >= MAX_FORT_CORPS_NUM.value:
			return None
		corps_key_list.append(corps_key_t())
		return corps_key_list[len(corps_key_list) - 1]

class storage_data_t(proto):
	def __init__(self):
		self.block_id = cint32()
		self.user_id = cint64()
		self.build_id = cint32()
		self.building_name = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.build_id.serialize(buff, buff_len)
		buff, buff_len = self.building_name.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.block_id.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.build_id.deserialize(buff)
		buff = self.building_name.deserialize(buff)
		return buff

class tax_data_t(proto):
	def __init__(self):
		self.levy_times = cint32()
		self.next_levy_time = cint32()
		self.add_free_times = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.levy_times.serialize(buff, buff_len)
		buff, buff_len = self.next_levy_time.serialize(buff, buff_len)
		buff, buff_len = self.add_free_times.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.levy_times.deserialize(buff)
		buff = self.next_levy_time.deserialize(buff)
		buff = self.add_free_times.deserialize(buff)
		return buff

class invader_data_t(proto):
	def __init__(self):
		self.invader_id = cint64()
		self.user = user_summary_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.invader_id.serialize(buff, buff_len)
		buff, buff_len = self.user.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.invader_id.deserialize(buff)
		buff = self.user.deserialize(buff)
		return buff

class tower_rank(proto):
	def __init__(self):
		self.user_summary_data = user_summary_data_t()
		self.rank = cint32()
		self.floors = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_summary_data.serialize(buff, buff_len)
		buff, buff_len = self.rank.serialize(buff, buff_len)
		buff, buff_len = self.floors.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_summary_data.deserialize(buff)
		buff = self.rank.deserialize(buff)
		buff = self.floors.deserialize(buff)
		return buff

class E_BATTLE_RESULT(enum):
	pass

class e_battle_result_in_battle(E_BATTLE_RESULT):
	def __init__(self):
		self.value=-1

class e_battle_result_left_win(E_BATTLE_RESULT):
	def __init__(self):
		self.value=0

class e_battle_result_right_win(E_BATTLE_RESULT):
	def __init__(self):
		self.value=1

class e_battle_result_draw(E_BATTLE_RESULT):
	def __init__(self):
		self.value=2

class e_battle_result_no_battle(E_BATTLE_RESULT):
	def __init__(self):
		self.value=3

class E_ACTOR_TYPE(enum):
	pass

class e_actor_type_null(E_ACTOR_TYPE):
	def __init__(self):
		self.value=0

class e_actor_type_hero(E_ACTOR_TYPE):
	def __init__(self):
		self.value=1

class e_actor_type_troops(E_ACTOR_TYPE):
	def __init__(self):
		self.value=2

class e_actor_type_techs(E_ACTOR_TYPE):
	def __init__(self):
		self.value=3

class e_actor_type_owner_techs(E_ACTOR_TYPE):
	def __init__(self):
		self.value=4

class e_actor_type_corps(E_ACTOR_TYPE):
	def __init__(self):
		self.value=5

class E_BATTLE_SIDE(enum):
	pass

class e_battle_side_invalid(E_BATTLE_SIDE):
	def __init__(self):
		self.value=-1

class e_battle_side_left(E_BATTLE_SIDE):
	def __init__(self):
		self.value=0

class e_battle_side_right(E_BATTLE_SIDE):
	def __init__(self):
		self.value=1

class e_battle_side_max(E_BATTLE_SIDE):
	def __init__(self):
		self.value=2

class E_ACTION_TYPE(enum):
	pass

class e_action_type_hero_skill(E_ACTION_TYPE):
	def __init__(self):
		self.value=0

class e_action_type_troops_skill(E_ACTION_TYPE):
	def __init__(self):
		self.value=1

class e_action_type_move(E_ACTION_TYPE):
	def __init__(self):
		self.value=2

class e_action_type_buf(E_ACTION_TYPE):
	def __init__(self):
		self.value=3

class e_action_type_tech_skill(E_ACTION_TYPE):
	def __init__(self):
		self.value=4

class e_action_type_combo(E_ACTION_TYPE):
	def __init__(self):
		self.value=5

class e_action_type_coprs_skill(E_ACTION_TYPE):
	def __init__(self):
		self.value=6

class E_SUB_ACTION_TYPE(enum):
	pass

class e_sub_action_type_skill_hurt(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=0

class e_sub_action_type_skill_heal(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=1

class e_sub_action_type_add_buf(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=2

class e_sub_action_type_add_buf_repeat(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=3

class e_sub_action_type_remove_buf(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=4

class e_sub_action_type_buf_hurt(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=5

class e_sub_action_type_buf_heal(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=6

class e_sub_action_type_buf_suck(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=7

class e_sub_action_type_buf_revolt_nor(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=8

class e_sub_action_type_buf_avoid(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=9

class e_sub_action_type_autotomy(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=10

class e_sub_action_type_pursue(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=11

class e_sub_action_type_effect(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=12

class e_sub_action_type_effect2(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=13

class e_sub_action_type_immune(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=14

class e_sub_action_type_do_sub_skill(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=15

class e_sub_action_type_add_buf_replace(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=16

class e_sub_action_type_add_buf_repeat_max(E_SUB_ACTION_TYPE):
	def __init__(self):
		self.value=17

class sub_action_packet_data(proto):
	def __init__(self):
		self.tar_index = cint32()
		self.param_0 = cint32()
		self.param_1 = cint32()
		self.param_2 = cint32()
		self.param_3 = cint32()
		self.param_4 = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.tar_index.serialize(buff, buff_len)
		buff, buff_len = self.param_0.serialize(buff, buff_len)
		buff, buff_len = self.param_1.serialize(buff, buff_len)
		buff, buff_len = self.param_2.serialize(buff, buff_len)
		buff, buff_len = self.param_3.serialize(buff, buff_len)
		buff, buff_len = self.param_4.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.tar_index.deserialize(buff)
		buff = self.param_0.deserialize(buff)
		buff = self.param_1.deserialize(buff)
		buff = self.param_2.deserialize(buff)
		buff = self.param_3.deserialize(buff)
		buff = self.param_4.deserialize(buff)
		return buff

class sub_action_packet(proto):
	def __init__(self):
		self.sub_action_type = E_SUB_ACTION_TYPE()
		self.data = sub_action_packet_data()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.sub_action_type.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.sub_action_type.deserialize(buff)
		buff = self.data.deserialize(buff)
		return buff

class action_packet_data(proto):
	def __init__(self):
		self.actioner_index = cint32()
		self.param_0 = cint32()
		self.param_1 = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.actioner_index.serialize(buff, buff_len)
		buff, buff_len = self.param_0.serialize(buff, buff_len)
		buff, buff_len = self.param_1.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.actioner_index.deserialize(buff)
		buff = self.param_0.deserialize(buff)
		buff = self.param_1.deserialize(buff)
		return buff

class action_packet(proto):
	def __init__(self):
		self.action_type = E_ACTION_TYPE()
		self.data = action_packet_data()
		self.len_of_subPackList = cuint16()
		self.subPackList = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.action_type.serialize(buff, buff_len)
		buff, buff_len = self.data.serialize(buff, buff_len)
		buff, buff_len = self.len_of_subPackList.serialize(buff, buff_len)
		for i in range(self.len_of_subPackList.value):
			buff, buff_len = self.subPackList[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.action_type.deserialize(buff)
		buff = self.data.deserialize(buff)
		buff = self.len_of_subPackList.deserialize(buff)
		self.subPackList = []
		for i in range(self.len_of_subPackList.value):
			self.subPackList.append(sub_action_packet())
			buff = self.subPackList[i].deserialize(buff)
		return buff

	def add_subPackList():
		if len(subPackList) >= MAX_SUB_PACKET_NUM.value:
			return None
		subPackList.append(sub_action_packet())
		return subPackList[len(subPackList) - 1]

class round_packet(proto):
	def __init__(self):
		self.round = cint32()
		self.len_of_packList = cuint16()
		self.packList = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.round.serialize(buff, buff_len)
		buff, buff_len = self.len_of_packList.serialize(buff, buff_len)
		for i in range(self.len_of_packList.value):
			buff, buff_len = self.packList[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.round.deserialize(buff)
		buff = self.len_of_packList.deserialize(buff)
		self.packList = []
		for i in range(self.len_of_packList.value):
			self.packList.append(action_packet())
			buff = self.packList[i].deserialize(buff)
		return buff

	def add_packList():
		if len(packList) >= MAX_ROUND_PACKET_NUM.value:
			return None
		packList.append(action_packet())
		return packList[len(packList) - 1]

class record_troops(proto):
	def __init__(self):
		self.battle_index = cint32()
		self.troops_index = cint32()
		self.soldier_entry = cint32()
		self.soldier_num = cint32()
		self.wounded_num = cint32()
		self.battle_pos = cint32()
		self.row_col = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.battle_index.serialize(buff, buff_len)
		buff, buff_len = self.troops_index.serialize(buff, buff_len)
		buff, buff_len = self.soldier_entry.serialize(buff, buff_len)
		buff, buff_len = self.soldier_num.serialize(buff, buff_len)
		buff, buff_len = self.wounded_num.serialize(buff, buff_len)
		buff, buff_len = self.battle_pos.serialize(buff, buff_len)
		buff, buff_len = self.row_col.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.battle_index.deserialize(buff)
		buff = self.troops_index.deserialize(buff)
		buff = self.soldier_entry.deserialize(buff)
		buff = self.soldier_num.deserialize(buff)
		buff = self.wounded_num.deserialize(buff)
		buff = self.battle_pos.deserialize(buff)
		buff = self.row_col.deserialize(buff)
		return buff

class hero_attr(proto):
	def __init__(self):
		self.liliang = cint32()
		self.naili = cint32()
		self.moulue = cint32()
		self.minjie = cint32()
		self.destroy = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.liliang.serialize(buff, buff_len)
		buff, buff_len = self.naili.serialize(buff, buff_len)
		buff, buff_len = self.moulue.serialize(buff, buff_len)
		buff, buff_len = self.minjie.serialize(buff, buff_len)
		buff, buff_len = self.destroy.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.liliang.deserialize(buff)
		buff = self.naili.deserialize(buff)
		buff = self.moulue.deserialize(buff)
		buff = self.minjie.deserialize(buff)
		buff = self.destroy.deserialize(buff)
		return buff

class record_hero(proto):
	def __init__(self):
		self.battle_index = cint32()
		self.hero_entry = cint32()
		self.level = cint32()
		self.junxian = cint32()
		self.star_lv = cint32()
		self.quality = E_HERO_QUALITY()
		self.quality_lv = cint32()
		self.len_of_equip_slot_list = cuint16()
		self.equip_slot_list = []
		self.junxian_skill = cint32()
		self.len_of_talent_skill_list = cuint16()
		self.talent_skill_list = []
		self.len_of_suit_skill_list = cuint16()
		self.suit_skill_list = []
		self.len_of_equip_skill_list = cuint16()
		self.equip_skill_list = []
		self.len_of_skill_lv = cuint16()
		self.skill_lv = []
		self.len_of_skill_entry = cuint16()
		self.skill_entry = []
		self.attr = hero_attr()
		self.power = cint32()
		self.troops_battle_index = cint32()
		self.soldier_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.battle_index.serialize(buff, buff_len)
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.level.serialize(buff, buff_len)
		buff, buff_len = self.junxian.serialize(buff, buff_len)
		buff, buff_len = self.star_lv.serialize(buff, buff_len)
		buff, buff_len = self.quality.serialize(buff, buff_len)
		buff, buff_len = self.quality_lv.serialize(buff, buff_len)
		buff, buff_len = self.len_of_equip_slot_list.serialize(buff, buff_len)
		for i in range(self.len_of_equip_slot_list.value):
			buff, buff_len = self.equip_slot_list[i].serialize(buff, buff_len)
		buff, buff_len = self.junxian_skill.serialize(buff, buff_len)
		buff, buff_len = self.len_of_talent_skill_list.serialize(buff, buff_len)
		for i in range(self.len_of_talent_skill_list.value):
			buff, buff_len = self.talent_skill_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_suit_skill_list.serialize(buff, buff_len)
		for i in range(self.len_of_suit_skill_list.value):
			buff, buff_len = self.suit_skill_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_equip_skill_list.serialize(buff, buff_len)
		for i in range(self.len_of_equip_skill_list.value):
			buff, buff_len = self.equip_skill_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_skill_lv.serialize(buff, buff_len)
		for i in range(self.len_of_skill_lv.value):
			buff, buff_len = self.skill_lv[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_skill_entry.serialize(buff, buff_len)
		for i in range(self.len_of_skill_entry.value):
			buff, buff_len = self.skill_entry[i].serialize(buff, buff_len)
		buff, buff_len = self.attr.serialize(buff, buff_len)
		buff, buff_len = self.power.serialize(buff, buff_len)
		buff, buff_len = self.troops_battle_index.serialize(buff, buff_len)
		buff, buff_len = self.soldier_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.battle_index.deserialize(buff)
		buff = self.hero_entry.deserialize(buff)
		buff = self.level.deserialize(buff)
		buff = self.junxian.deserialize(buff)
		buff = self.star_lv.deserialize(buff)
		buff = self.quality.deserialize(buff)
		buff = self.quality_lv.deserialize(buff)
		buff = self.len_of_equip_slot_list.deserialize(buff)
		self.equip_slot_list = []
		for i in range(self.len_of_equip_slot_list.value):
			self.equip_slot_list.append(equip_slot_t())
			buff = self.equip_slot_list[i].deserialize(buff)
		buff = self.junxian_skill.deserialize(buff)
		buff = self.len_of_talent_skill_list.deserialize(buff)
		self.talent_skill_list = []
		for i in range(self.len_of_talent_skill_list.value):
			self.talent_skill_list.append(cint32())
			buff = self.talent_skill_list[i].deserialize(buff)
		buff = self.len_of_suit_skill_list.deserialize(buff)
		self.suit_skill_list = []
		for i in range(self.len_of_suit_skill_list.value):
			self.suit_skill_list.append(cint32())
			buff = self.suit_skill_list[i].deserialize(buff)
		buff = self.len_of_equip_skill_list.deserialize(buff)
		self.equip_skill_list = []
		for i in range(self.len_of_equip_skill_list.value):
			self.equip_skill_list.append(cint32())
			buff = self.equip_skill_list[i].deserialize(buff)
		buff = self.len_of_skill_lv.deserialize(buff)
		self.skill_lv = []
		for i in range(self.len_of_skill_lv.value):
			self.skill_lv.append(cint32())
			buff = self.skill_lv[i].deserialize(buff)
		buff = self.len_of_skill_entry.deserialize(buff)
		self.skill_entry = []
		for i in range(self.len_of_skill_entry.value):
			self.skill_entry.append(cint32())
			buff = self.skill_entry[i].deserialize(buff)
		buff = self.attr.deserialize(buff)
		buff = self.power.deserialize(buff)
		buff = self.troops_battle_index.deserialize(buff)
		buff = self.soldier_entry.deserialize(buff)
		return buff

	def add_equip_slot_list():
		if len(equip_slot_list) >= e_equip_slot_max.value:
			return None
		equip_slot_list.append(equip_slot_t())
		return equip_slot_list[len(equip_slot_list) - 1]

	def add_talent_skill_list():
		if len(talent_skill_list) >= MAX_SKILL_LIST.value:
			return None
		talent_skill_list.append(ccint32())
		return talent_skill_list[len(talent_skill_list) - 1]

	def add_suit_skill_list():
		if len(suit_skill_list) >= MAX_SKILL_LIST.value:
			return None
		suit_skill_list.append(ccint32())
		return suit_skill_list[len(suit_skill_list) - 1]

	def add_equip_skill_list():
		if len(equip_skill_list) >= MAX_SKILL_LIST.value:
			return None
		equip_skill_list.append(ccint32())
		return equip_skill_list[len(equip_skill_list) - 1]

	def add_skill_lv():
		if len(skill_lv) >= MAX_HERO_SKILL_NUM.value:
			return None
		skill_lv.append(ccint32())
		return skill_lv[len(skill_lv) - 1]

	def add_skill_entry():
		if len(skill_entry) >= MAX_HERO_SKILL_NUM.value:
			return None
		skill_entry.append(ccint32())
		return skill_entry[len(skill_entry) - 1]

class E_ADD_ATTR_TYPE(enum):
	pass

class e_add_attr_invalid(E_ADD_ATTR_TYPE):
	def __init__(self):
		self.value=-1

class e_add_attr_tech(E_ADD_ATTR_TYPE):
	def __init__(self):
		self.value=0

class e_add_attr_vip(E_ADD_ATTR_TYPE):
	def __init__(self):
		self.value=1

class e_add_attr_medal(E_ADD_ATTR_TYPE):
	def __init__(self):
		self.value=2

class e_add_attr_medalset(E_ADD_ATTR_TYPE):
	def __init__(self):
		self.value=3

class e_add_attr_miracle(E_ADD_ATTR_TYPE):
	def __init__(self):
		self.value=4

class e_add_attr_addition(E_ADD_ATTR_TYPE):
	def __init__(self):
		self.value=5

class e_add_attr_fame(E_ADD_ATTR_TYPE):
	def __init__(self):
		self.value=6

class e_add_attr_museum(E_ADD_ATTR_TYPE):
	def __init__(self):
		self.value=7

class e_add_attr_nobility(E_ADD_ATTR_TYPE):
	def __init__(self):
		self.value=8

class record_tech(proto):
	def __init__(self):
		self.battle_index = cint32()
		self.type = E_ADD_ATTR_TYPE()
		self.entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.battle_index.serialize(buff, buff_len)
		buff, buff_len = self.type.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.battle_index.deserialize(buff)
		buff = self.type.deserialize(buff)
		buff = self.entry.deserialize(buff)
		return buff

class guild_tiny_info(proto):
	def __init__(self):
		self.guild_id = cint64()
		self.guild_name = cstring()
		self.icon = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.guild_name.serialize(buff, buff_len)
		buff, buff_len = self.icon.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.guild_id.deserialize(buff)
		buff = self.guild_name.deserialize(buff)
		buff = self.icon.deserialize(buff)
		return buff

class record_actor(proto):
	def __init__(self):
		self.user_id = cint64()
		self.head_entry = cint32()
		self.nick_name_entry = cint32()
		self.nick_name = cstring()
		self.len_of_hero = cuint16()
		self.hero = []
		self.len_of_troopsList = cuint16()
		self.troopsList = []
		self.len_of_tech_List = cuint16()
		self.tech_List = []
		self.side = E_BATTLE_SIDE()
		self.guild_info = guild_tiny_info()
		self.param = cint32()
		self.troops_max_power = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.head_entry.serialize(buff, buff_len)
		buff, buff_len = self.nick_name_entry.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		buff, buff_len = self.len_of_hero.serialize(buff, buff_len)
		for i in range(self.len_of_hero.value):
			buff, buff_len = self.hero[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_troopsList.serialize(buff, buff_len)
		for i in range(self.len_of_troopsList.value):
			buff, buff_len = self.troopsList[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_tech_List.serialize(buff, buff_len)
		for i in range(self.len_of_tech_List.value):
			buff, buff_len = self.tech_List[i].serialize(buff, buff_len)
		buff, buff_len = self.side.serialize(buff, buff_len)
		buff, buff_len = self.guild_info.serialize(buff, buff_len)
		buff, buff_len = self.param.serialize(buff, buff_len)
		buff, buff_len = self.troops_max_power.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_id.deserialize(buff)
		buff = self.head_entry.deserialize(buff)
		buff = self.nick_name_entry.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		buff = self.len_of_hero.deserialize(buff)
		self.hero = []
		for i in range(self.len_of_hero.value):
			self.hero.append(record_hero())
			buff = self.hero[i].deserialize(buff)
		buff = self.len_of_troopsList.deserialize(buff)
		self.troopsList = []
		for i in range(self.len_of_troopsList.value):
			self.troopsList.append(record_troops())
			buff = self.troopsList[i].deserialize(buff)
		buff = self.len_of_tech_List.deserialize(buff)
		self.tech_List = []
		for i in range(self.len_of_tech_List.value):
			self.tech_List.append(record_tech())
			buff = self.tech_List[i].deserialize(buff)
		buff = self.side.deserialize(buff)
		buff = self.guild_info.deserialize(buff)
		buff = self.param.deserialize(buff)
		buff = self.troops_max_power.deserialize(buff)
		return buff

	def add_hero():
		if len(hero) >= MAX_CORPS_HERO_NUM.value:
			return None
		hero.append(record_hero())
		return hero[len(hero) - 1]

	def add_troopsList():
		if len(troopsList) >= MAX_CORPS_TROOPS_NUM.value:
			return None
		troopsList.append(record_troops())
		return troopsList[len(troopsList) - 1]

	def add_tech_List():
		if len(tech_List) >= MAX_ADDITION_COUNT.value:
			return None
		tech_List.append(record_tech())
		return tech_List[len(tech_List) - 1]

class brief_record_actor(proto):
	def __init__(self):
		self.user_id = cint64()
		self.head_entry = cint32()
		self.nick_name_entry = cint32()
		self.nick_name = cstring()
		self.len_of_hero = cuint16()
		self.hero = []
		self.begin_troops_num = cint32()
		self.side = E_BATTLE_SIDE()
		self.guild_info = guild_tiny_info()
		self.param = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.head_entry.serialize(buff, buff_len)
		buff, buff_len = self.nick_name_entry.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		buff, buff_len = self.len_of_hero.serialize(buff, buff_len)
		for i in range(self.len_of_hero.value):
			buff, buff_len = self.hero[i].serialize(buff, buff_len)
		buff, buff_len = self.begin_troops_num.serialize(buff, buff_len)
		buff, buff_len = self.side.serialize(buff, buff_len)
		buff, buff_len = self.guild_info.serialize(buff, buff_len)
		buff, buff_len = self.param.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_id.deserialize(buff)
		buff = self.head_entry.deserialize(buff)
		buff = self.nick_name_entry.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		buff = self.len_of_hero.deserialize(buff)
		self.hero = []
		for i in range(self.len_of_hero.value):
			self.hero.append(record_hero())
			buff = self.hero[i].deserialize(buff)
		buff = self.begin_troops_num.deserialize(buff)
		buff = self.side.deserialize(buff)
		buff = self.guild_info.deserialize(buff)
		buff = self.param.deserialize(buff)
		return buff

	def add_hero():
		if len(hero) >= MAX_CORPS_HERO_NUM.value:
			return None
		hero.append(record_hero())
		return hero[len(hero) - 1]

class result_corps(proto):
	def __init__(self):
		self.side = E_BATTLE_SIDE()
		self.len_of_troops = cuint16()
		self.troops = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.side.serialize(buff, buff_len)
		buff, buff_len = self.len_of_troops.serialize(buff, buff_len)
		for i in range(self.len_of_troops.value):
			buff, buff_len = self.troops[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.side.deserialize(buff)
		buff = self.len_of_troops.deserialize(buff)
		self.troops = []
		for i in range(self.len_of_troops.value):
			self.troops.append(record_troops())
			buff = self.troops[i].deserialize(buff)
		return buff

	def add_troops():
		if len(troops) >= MAX_CORPS_TROOPS_NUM.value:
			return None
		troops.append(record_troops())
		return troops[len(troops) - 1]

class battle_exp_t(proto):
	def __init__(self):
		self.corps_exp = cint32()
		self.hero_exp = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.corps_exp.serialize(buff, buff_len)
		buff, buff_len = self.hero_exp.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.corps_exp.deserialize(buff)
		buff = self.hero_exp.deserialize(buff)
		return buff

class record_result(proto):
	def __init__(self):
		self.result = E_BATTLE_RESULT()
		self.destroy = cint32()
		self.battle_exp = battle_exp_t()
		self.def_battle_exp = battle_exp_t()
		self.len_of_corps_list = cuint16()
		self.corps_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.result.serialize(buff, buff_len)
		buff, buff_len = self.destroy.serialize(buff, buff_len)
		buff, buff_len = self.battle_exp.serialize(buff, buff_len)
		buff, buff_len = self.def_battle_exp.serialize(buff, buff_len)
		buff, buff_len = self.len_of_corps_list.serialize(buff, buff_len)
		for i in range(self.len_of_corps_list.value):
			buff, buff_len = self.corps_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.result.deserialize(buff)
		buff = self.destroy.deserialize(buff)
		buff = self.battle_exp.deserialize(buff)
		buff = self.def_battle_exp.deserialize(buff)
		buff = self.len_of_corps_list.deserialize(buff)
		self.corps_list = []
		for i in range(self.len_of_corps_list.value):
			self.corps_list.append(result_corps())
			buff = self.corps_list[i].deserialize(buff)
		return buff

	def add_corps_list():
		if len(corps_list) >= e_battle_side_max.value:
			return None
		corps_list.append(result_corps())
		return corps_list[len(corps_list) - 1]

class rewards_hero_t(proto):
	def __init__(self):
		self.hero_entry = cint32()
		self.len_of_add_item = cuint16()
		self.add_item = []
		self.len_of_add_hero = cuint16()
		self.add_hero = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.len_of_add_item.serialize(buff, buff_len)
		for i in range(self.len_of_add_item.value):
			buff, buff_len = self.add_item[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_add_hero.serialize(buff, buff_len)
		for i in range(self.len_of_add_hero.value):
			buff, buff_len = self.add_hero[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.hero_entry.deserialize(buff)
		buff = self.len_of_add_item.deserialize(buff)
		self.add_item = []
		for i in range(self.len_of_add_item.value):
			self.add_item.append(item_data_t())
			buff = self.add_item[i].deserialize(buff)
		buff = self.len_of_add_hero.deserialize(buff)
		self.add_hero = []
		for i in range(self.len_of_add_hero.value):
			self.add_hero.append(hero_data_t())
			buff = self.add_hero[i].deserialize(buff)
		return buff

	def add_add_item():
		if len(add_item) >= MAX_REWARD_HERO_DATA.value:
			return None
		add_item.append(item_data_t())
		return add_item[len(add_item) - 1]

	def add_add_hero():
		if len(add_hero) >= MAX_REWARD_HERO_DATA.value:
			return None
		add_hero.append(hero_data_t())
		return add_hero[len(add_hero) - 1]

class museum_collection_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.e_collection_status = E_MUSEUM_COLLECTION_STATUS()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.e_collection_status.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.e_collection_status.deserialize(buff)
		return buff

class rewards_t(proto):
	def __init__(self):
		self.resources = user_resource_t()
		self.add_resources = user_resource_t()
		self.len_of_item_change_list = cuint16()
		self.item_change_list = []
		self.len_of_add_reward_hero_list = cuint16()
		self.add_reward_hero_list = []
		self.fame = cint32()
		self.add_fame = cint32()
		self.fame_tick_time = cint32()
		self.match_coin = cint32()
		self.add_coin = cint32()
		self.killpoint = cint32()
		self.add_killpoint = cint32()
		self.contribution = cint32()
		self.add_contribution = cint32()
		self.museum_collection = museum_collection_t()
		self.reserver_soldier_num = cint32()
		self.lucky_point = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.add_resources.serialize(buff, buff_len)
		buff, buff_len = self.len_of_item_change_list.serialize(buff, buff_len)
		for i in range(self.len_of_item_change_list.value):
			buff, buff_len = self.item_change_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_add_reward_hero_list.serialize(buff, buff_len)
		for i in range(self.len_of_add_reward_hero_list.value):
			buff, buff_len = self.add_reward_hero_list[i].serialize(buff, buff_len)
		buff, buff_len = self.fame.serialize(buff, buff_len)
		buff, buff_len = self.add_fame.serialize(buff, buff_len)
		buff, buff_len = self.fame_tick_time.serialize(buff, buff_len)
		buff, buff_len = self.match_coin.serialize(buff, buff_len)
		buff, buff_len = self.add_coin.serialize(buff, buff_len)
		buff, buff_len = self.killpoint.serialize(buff, buff_len)
		buff, buff_len = self.add_killpoint.serialize(buff, buff_len)
		buff, buff_len = self.contribution.serialize(buff, buff_len)
		buff, buff_len = self.add_contribution.serialize(buff, buff_len)
		buff, buff_len = self.museum_collection.serialize(buff, buff_len)
		buff, buff_len = self.reserver_soldier_num.serialize(buff, buff_len)
		buff, buff_len = self.lucky_point.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.resources.deserialize(buff)
		buff = self.add_resources.deserialize(buff)
		buff = self.len_of_item_change_list.deserialize(buff)
		self.item_change_list = []
		for i in range(self.len_of_item_change_list.value):
			self.item_change_list.append(item_data_t())
			buff = self.item_change_list[i].deserialize(buff)
		buff = self.len_of_add_reward_hero_list.deserialize(buff)
		self.add_reward_hero_list = []
		for i in range(self.len_of_add_reward_hero_list.value):
			self.add_reward_hero_list.append(rewards_hero_t())
			buff = self.add_reward_hero_list[i].deserialize(buff)
		buff = self.fame.deserialize(buff)
		buff = self.add_fame.deserialize(buff)
		buff = self.fame_tick_time.deserialize(buff)
		buff = self.match_coin.deserialize(buff)
		buff = self.add_coin.deserialize(buff)
		buff = self.killpoint.deserialize(buff)
		buff = self.add_killpoint.deserialize(buff)
		buff = self.contribution.deserialize(buff)
		buff = self.add_contribution.deserialize(buff)
		buff = self.museum_collection.deserialize(buff)
		buff = self.reserver_soldier_num.deserialize(buff)
		buff = self.lucky_point.deserialize(buff)
		return buff

	def add_item_change_list():
		if len(item_change_list) >= MAX_CHANGE_ITEM_NUM.value:
			return None
		item_change_list.append(item_data_t())
		return item_change_list[len(item_change_list) - 1]

	def add_add_reward_hero_list():
		if len(add_reward_hero_list) >= MAX_HERO_COUNT.value:
			return None
		add_reward_hero_list.append(rewards_hero_t())
		return add_reward_hero_list[len(add_reward_hero_list) - 1]

class user_battle_result_hero_t(proto):
	def __init__(self):
		self.hero_entry = cint32()
		self.hero_exp = cuint32()
		self.hero_lv = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.hero_entry.serialize(buff, buff_len)
		buff, buff_len = self.hero_exp.serialize(buff, buff_len)
		buff, buff_len = self.hero_lv.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.hero_entry.deserialize(buff)
		buff = self.hero_exp.deserialize(buff)
		buff = self.hero_lv.deserialize(buff)
		return buff

class user_battle_result_t(proto):
	def __init__(self):
		self.corps_exp = cuint32()
		self.corps_lv = cint32()
		self.len_of_result_hero = cuint16()
		self.result_hero = []
		self.guild_exp = cuint32()
		self.dam = cuint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.corps_exp.serialize(buff, buff_len)
		buff, buff_len = self.corps_lv.serialize(buff, buff_len)
		buff, buff_len = self.len_of_result_hero.serialize(buff, buff_len)
		for i in range(self.len_of_result_hero.value):
			buff, buff_len = self.result_hero[i].serialize(buff, buff_len)
		buff, buff_len = self.guild_exp.serialize(buff, buff_len)
		buff, buff_len = self.dam.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.corps_exp.deserialize(buff)
		buff = self.corps_lv.deserialize(buff)
		buff = self.len_of_result_hero.deserialize(buff)
		self.result_hero = []
		for i in range(self.len_of_result_hero.value):
			self.result_hero.append(user_battle_result_hero_t())
			buff = self.result_hero[i].deserialize(buff)
		buff = self.guild_exp.deserialize(buff)
		buff = self.dam.deserialize(buff)
		return buff

	def add_result_hero():
		if len(result_hero) >= MAX_CORPS_TROOPS_NUM.value:
			return None
		result_hero.append(user_battle_result_hero_t())
		return result_hero[len(result_hero) - 1]

class E_MOVE_RESULT(enum):
	pass

class e_move_result_go_on(E_MOVE_RESULT):
	def __init__(self):
		self.value=0

class e_move_result_event_failed(E_MOVE_RESULT):
	def __init__(self):
		self.value=1

class e_move_result_just_win(E_MOVE_RESULT):
	def __init__(self):
		self.value=2

class e_move_result_catch_block(E_MOVE_RESULT):
	def __init__(self):
		self.value=3

class e_move_result_loose_block(E_MOVE_RESULT):
	def __init__(self):
		self.value=4

class e_move_result_fight_air(E_MOVE_RESULT):
	def __init__(self):
		self.value=5

class e_move_result_land_full(E_MOVE_RESULT):
	def __init__(self):
		self.value=6

class e_move_result_invader_user(E_MOVE_RESULT):
	def __init__(self):
		self.value=7

class e_move_result_tri_combat(E_MOVE_RESULT):
	def __init__(self):
		self.value=8

class e_move_result_fight_fail(E_MOVE_RESULT):
	def __init__(self):
		self.value=9

class e_move_result_fight_finish(E_MOVE_RESULT):
	def __init__(self):
		self.value=10

class e_move_result_seize_success(E_MOVE_RESULT):
	def __init__(self):
		self.value=11

class e_move_result_spy(E_MOVE_RESULT):
	def __init__(self):
		self.value=12

class e_move_result_smash_once(E_MOVE_RESULT):
	def __init__(self):
		self.value=13

class e_move_result_smash_twice(E_MOVE_RESULT):
	def __init__(self):
		self.value=14

class e_move_result_smash_three_times(E_MOVE_RESULT):
	def __init__(self):
		self.value=15

class e_move_result_smash_four_times(E_MOVE_RESULT):
	def __init__(self):
		self.value=16

class e_move_result_smash_five_times(E_MOVE_RESULT):
	def __init__(self):
		self.value=17

class e_move_result_smash_six_times(E_MOVE_RESULT):
	def __init__(self):
		self.value=18

class e_move_result_smash_sevent_times(E_MOVE_RESULT):
	def __init__(self):
		self.value=19

class battle_record(proto):
	def __init__(self):
		self.block_id = cint32()
		self.block_entry = cint32()
		self.combat_type = E_COMBAT_TYPE()
		self.battle_reason = cint32()
		self.len_of_record_acotr_list = cuint16()
		self.record_acotr_list = []
		self.len_of_round_packet_list = cuint16()
		self.round_packet_list = []
		self.record_acotr_result = record_result()
		self.battle_time = cint32()
		self.reward = rewards_t()
		self.nofight_type = E_NOFIGHT_TYPE()
		self.battle_result = user_battle_result_t()
		self.enemy_battle_result = user_battle_result_t()
		self.move_result = E_MOVE_RESULT()
		self.is_pvp = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.block_entry.serialize(buff, buff_len)
		buff, buff_len = self.combat_type.serialize(buff, buff_len)
		buff, buff_len = self.battle_reason.serialize(buff, buff_len)
		buff, buff_len = self.len_of_record_acotr_list.serialize(buff, buff_len)
		for i in range(self.len_of_record_acotr_list.value):
			buff, buff_len = self.record_acotr_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_round_packet_list.serialize(buff, buff_len)
		for i in range(self.len_of_round_packet_list.value):
			buff, buff_len = self.round_packet_list[i].serialize(buff, buff_len)
		buff, buff_len = self.record_acotr_result.serialize(buff, buff_len)
		buff, buff_len = self.battle_time.serialize(buff, buff_len)
		buff, buff_len = self.reward.serialize(buff, buff_len)
		buff, buff_len = self.nofight_type.serialize(buff, buff_len)
		buff, buff_len = self.battle_result.serialize(buff, buff_len)
		buff, buff_len = self.enemy_battle_result.serialize(buff, buff_len)
		buff, buff_len = self.move_result.serialize(buff, buff_len)
		buff, buff_len = self.is_pvp.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.block_id.deserialize(buff)
		buff = self.block_entry.deserialize(buff)
		buff = self.combat_type.deserialize(buff)
		buff = self.battle_reason.deserialize(buff)
		buff = self.len_of_record_acotr_list.deserialize(buff)
		self.record_acotr_list = []
		for i in range(self.len_of_record_acotr_list.value):
			self.record_acotr_list.append(record_actor())
			buff = self.record_acotr_list[i].deserialize(buff)
		buff = self.len_of_round_packet_list.deserialize(buff)
		self.round_packet_list = []
		for i in range(self.len_of_round_packet_list.value):
			self.round_packet_list.append(round_packet())
			buff = self.round_packet_list[i].deserialize(buff)
		buff = self.record_acotr_result.deserialize(buff)
		buff = self.battle_time.deserialize(buff)
		buff = self.reward.deserialize(buff)
		buff = self.nofight_type.deserialize(buff)
		buff = self.battle_result.deserialize(buff)
		buff = self.enemy_battle_result.deserialize(buff)
		buff = self.move_result.deserialize(buff)
		buff = self.is_pvp.deserialize(buff)
		return buff

	def add_record_acotr_list():
		if len(record_acotr_list) >= MAX_BATTLE_RECORD_ACTOR_LEN.value:
			return None
		record_acotr_list.append(record_actor())
		return record_acotr_list[len(record_acotr_list) - 1]

	def add_round_packet_list():
		if len(round_packet_list) >= MAX_RECORE_ROUND.value:
			return None
		round_packet_list.append(round_packet())
		return round_packet_list[len(round_packet_list) - 1]

class brief_battle_record(proto):
	def __init__(self):
		self.event_id = cint64()
		self.index = cint32()
		self.battle_id = cint64()
		self.block_id = cint32()
		self.len_of_record_acotr_list = cuint16()
		self.record_acotr_list = []
		self.result = E_BATTLE_RESULT()
		self.move_result = E_MOVE_RESULT()
		self.battle_time = cint32()
		self.is_read = cbool()
		self.block_entry = cint32()
		self.is_pvp = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.index.serialize(buff, buff_len)
		buff, buff_len = self.battle_id.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_record_acotr_list.serialize(buff, buff_len)
		for i in range(self.len_of_record_acotr_list.value):
			buff, buff_len = self.record_acotr_list[i].serialize(buff, buff_len)
		buff, buff_len = self.result.serialize(buff, buff_len)
		buff, buff_len = self.move_result.serialize(buff, buff_len)
		buff, buff_len = self.battle_time.serialize(buff, buff_len)
		buff, buff_len = self.is_read.serialize(buff, buff_len)
		buff, buff_len = self.block_entry.serialize(buff, buff_len)
		buff, buff_len = self.is_pvp.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.event_id.deserialize(buff)
		buff = self.index.deserialize(buff)
		buff = self.battle_id.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.len_of_record_acotr_list.deserialize(buff)
		self.record_acotr_list = []
		for i in range(self.len_of_record_acotr_list.value):
			self.record_acotr_list.append(brief_record_actor())
			buff = self.record_acotr_list[i].deserialize(buff)
		buff = self.result.deserialize(buff)
		buff = self.move_result.deserialize(buff)
		buff = self.battle_time.deserialize(buff)
		buff = self.is_read.deserialize(buff)
		buff = self.block_entry.deserialize(buff)
		buff = self.is_pvp.deserialize(buff)
		return buff

	def add_record_acotr_list():
		if len(record_acotr_list) >= MAX_BATTLE_RECORD_ACTOR_LEN.value:
			return None
		record_acotr_list.append(brief_record_actor())
		return record_acotr_list[len(record_acotr_list) - 1]

class guild_t(proto):
	def __init__(self):
		self.guild_id = cint64()
		self.name = cstring()
		self.chairman_id = cint64()
		self.chairman_name = cstring()
		self.icon = cint32()
		self.state = cint32()
		self.level = cint32()
		self.exp = cint32()
		self.notice = cstring()
		self.trans_time = cint32()
		self.member_num = cint32()
		self.force = cint32()
		self.force_limit = cint32()
		self.is_limit = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		buff, buff_len = self.chairman_id.serialize(buff, buff_len)
		buff, buff_len = self.chairman_name.serialize(buff, buff_len)
		buff, buff_len = self.icon.serialize(buff, buff_len)
		buff, buff_len = self.state.serialize(buff, buff_len)
		buff, buff_len = self.level.serialize(buff, buff_len)
		buff, buff_len = self.exp.serialize(buff, buff_len)
		buff, buff_len = self.notice.serialize(buff, buff_len)
		buff, buff_len = self.trans_time.serialize(buff, buff_len)
		buff, buff_len = self.member_num.serialize(buff, buff_len)
		buff, buff_len = self.force.serialize(buff, buff_len)
		buff, buff_len = self.force_limit.serialize(buff, buff_len)
		buff, buff_len = self.is_limit.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.guild_id.deserialize(buff)
		buff = self.name.deserialize(buff)
		buff = self.chairman_id.deserialize(buff)
		buff = self.chairman_name.deserialize(buff)
		buff = self.icon.deserialize(buff)
		buff = self.state.deserialize(buff)
		buff = self.level.deserialize(buff)
		buff = self.exp.deserialize(buff)
		buff = self.notice.deserialize(buff)
		buff = self.trans_time.deserialize(buff)
		buff = self.member_num.deserialize(buff)
		buff = self.force.deserialize(buff)
		buff = self.force_limit.deserialize(buff)
		buff = self.is_limit.deserialize(buff)
		return buff

class guild_application_t(proto):
	def __init__(self):
		self.guild_id = cint64()
		self.userid = cint64()
		self.time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.userid.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.guild_id.deserialize(buff)
		buff = self.userid.deserialize(buff)
		buff = self.time.deserialize(buff)
		return buff

class guild_user_application_t(proto):
	def __init__(self):
		self.guild_id = cint64()
		self.user_data = user_summary_data_t()
		self.time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.guild_id.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		buff = self.time.deserialize(buff)
		return buff

class guild_mark_t(proto):
	def __init__(self):
		self.guild_id = cint64()
		self.block_id = cint32()
		self.time = cint32()
		self.name = cstring()
		self.notice = cstring()
		self.block_entry = cint32()
		self.state = cint32()
		self.user_data = user_summary_data_t()
		self.geography = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		buff, buff_len = self.notice.serialize(buff, buff_len)
		buff, buff_len = self.block_entry.serialize(buff, buff_len)
		buff, buff_len = self.state.serialize(buff, buff_len)
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		buff, buff_len = self.geography.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.guild_id.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.time.deserialize(buff)
		buff = self.name.deserialize(buff)
		buff = self.notice.deserialize(buff)
		buff = self.block_entry.deserialize(buff)
		buff = self.state.deserialize(buff)
		buff = self.user_data.deserialize(buff)
		buff = self.geography.deserialize(buff)
		return buff

class guild_invitation_t(proto):
	def __init__(self):
		self.time = cint32()
		self.guild_data = guild_brief_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.time.serialize(buff, buff_len)
		buff, buff_len = self.guild_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.time.deserialize(buff)
		buff = self.guild_data.deserialize(buff)
		return buff

class brief_guild_member(proto):
	def __init__(self):
		self.user_data = user_summary_data_t()
		self.position = cint32()
		self.kill_point_of_week = cint32()
		self.contribution = cint32()
		self.contribution_of_week = cint32()
		self.chat_channel_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_data.serialize(buff, buff_len)
		buff, buff_len = self.position.serialize(buff, buff_len)
		buff, buff_len = self.kill_point_of_week.serialize(buff, buff_len)
		buff, buff_len = self.contribution.serialize(buff, buff_len)
		buff, buff_len = self.contribution_of_week.serialize(buff, buff_len)
		buff, buff_len = self.chat_channel_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_data.deserialize(buff)
		buff = self.position.deserialize(buff)
		buff = self.kill_point_of_week.deserialize(buff)
		buff = self.contribution.deserialize(buff)
		buff = self.contribution_of_week.deserialize(buff)
		buff = self.chat_channel_id.deserialize(buff)
		return buff

class resource_t(proto):
	def __init__(self):
		self.wood = cuint32()
		self.stone = cuint32()
		self.grain = cuint32()
		self.iron = cuint32()
		self.copper = cuint32()
		self.oil = cuint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.wood.serialize(buff, buff_len)
		buff, buff_len = self.stone.serialize(buff, buff_len)
		buff, buff_len = self.grain.serialize(buff, buff_len)
		buff, buff_len = self.iron.serialize(buff, buff_len)
		buff, buff_len = self.copper.serialize(buff, buff_len)
		buff, buff_len = self.oil.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.wood.deserialize(buff)
		buff = self.stone.deserialize(buff)
		buff = self.grain.deserialize(buff)
		buff = self.iron.deserialize(buff)
		buff = self.copper.deserialize(buff)
		buff = self.oil.deserialize(buff)
		return buff

class E_APPLICATION_PROCESS_TYPE(enum):
	pass

class e_application_process_type_pass(E_APPLICATION_PROCESS_TYPE):
	def __init__(self):
		self.value=0

class e_application_process_type_refuse(E_APPLICATION_PROCESS_TYPE):
	def __init__(self):
		self.value=1

class E_GUILD_POSITION(enum):
	pass

class e_guild_position_invalid(E_GUILD_POSITION):
	def __init__(self):
		self.value=-1

class e_guild_position_chairman(E_GUILD_POSITION):
	def __init__(self):
		self.value=0

class e_guild_position_vice_chairman(E_GUILD_POSITION):
	def __init__(self):
		self.value=1

class e_guild_position_vice_elder(E_GUILD_POSITION):
	def __init__(self):
		self.value=2

class e_guild_position_member(E_GUILD_POSITION):
	def __init__(self):
		self.value=3

class mission_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.status = cint32()
		self.parameter = cint64()
		self.level = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.status.serialize(buff, buff_len)
		buff, buff_len = self.parameter.serialize(buff, buff_len)
		buff, buff_len = self.level.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.status.deserialize(buff)
		buff = self.parameter.deserialize(buff)
		buff = self.level.deserialize(buff)
		return buff

class achievement_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.status = cint32()
		self.parameter = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.status.serialize(buff, buff_len)
		buff, buff_len = self.parameter.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.status.deserialize(buff)
		buff = self.parameter.deserialize(buff)
		return buff

class world_trend_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.status = cint32()
		self.start_time = cint32()
		self.finish_time = cint32()
		self.parameter = cint64()
		self.privdata = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.status.serialize(buff, buff_len)
		buff, buff_len = self.start_time.serialize(buff, buff_len)
		buff, buff_len = self.finish_time.serialize(buff, buff_len)
		buff, buff_len = self.parameter.serialize(buff, buff_len)
		buff, buff_len = self.privdata.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.status.deserialize(buff)
		buff = self.start_time.deserialize(buff)
		buff = self.finish_time.deserialize(buff)
		buff = self.parameter.deserialize(buff)
		buff = self.privdata.deserialize(buff)
		return buff

class state_achi_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.status = cint32()
		self.finish_time = cint32()
		self.parameter = cint64()
		self.privdata = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.status.serialize(buff, buff_len)
		buff, buff_len = self.finish_time.serialize(buff, buff_len)
		buff, buff_len = self.parameter.serialize(buff, buff_len)
		buff, buff_len = self.privdata.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.status.deserialize(buff)
		buff = self.finish_time.deserialize(buff)
		buff = self.parameter.deserialize(buff)
		buff = self.privdata.deserialize(buff)
		return buff

class E_GUILD_RELATIONSHIP(enum):
	pass

class e_guild_relationship_invalid(E_GUILD_RELATIONSHIP):
	def __init__(self):
		self.value=-1

class e_guild_relationship_friend(E_GUILD_RELATIONSHIP):
	def __init__(self):
		self.value=0

class e_guild_relationship_enemy(E_GUILD_RELATIONSHIP):
	def __init__(self):
		self.value=1

class guild_relationship_t(proto):
	def __init__(self):
		self.guild_id = cint64()
		self.tar_guild_id = cint64()
		self.relationship = cint32()
		self.time = cint32()
		self.guild_data = guild_brief_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.tar_guild_id.serialize(buff, buff_len)
		buff, buff_len = self.relationship.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		buff, buff_len = self.guild_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.guild_id.deserialize(buff)
		buff = self.tar_guild_id.deserialize(buff)
		buff = self.relationship.deserialize(buff)
		buff = self.time.deserialize(buff)
		buff = self.guild_data.deserialize(buff)
		return buff

class E_GUILDLOG_TYPE(enum):
	pass

class e_guildlog_type_event(E_GUILDLOG_TYPE):
	def __init__(self):
		self.value=0

class e_guildlog_type_member(E_GUILDLOG_TYPE):
	def __init__(self):
		self.value=1

class e_guildlog_type_battle(E_GUILDLOG_TYPE):
	def __init__(self):
		self.value=2

class e_guildlog_type_relationship(E_GUILDLOG_TYPE):
	def __init__(self):
		self.value=3

class E_GUILDLOG_EVENT(enum):
	pass

class e_guildlog_event_commission(E_GUILDLOG_EVENT):
	def __init__(self):
		self.value=0

class e_guildlog_event_lvup(E_GUILDLOG_EVENT):
	def __init__(self):
		self.value=1

class E_GUILDLOG_MEMBER(enum):
	pass

class e_guildlog_member_enter(E_GUILDLOG_MEMBER):
	def __init__(self):
		self.value=0

class e_guildlog_member_quit(E_GUILDLOG_MEMBER):
	def __init__(self):
		self.value=1

class e_guildlog_member_be_attack(E_GUILDLOG_MEMBER):
	def __init__(self):
		self.value=2

class e_guildlog_member_be_invader(E_GUILDLOG_MEMBER):
	def __init__(self):
		self.value=3

class e_guildlog_member_be_seize(E_GUILDLOG_MEMBER):
	def __init__(self):
		self.value=4

class e_guildlog_member_transform(E_GUILDLOG_MEMBER):
	def __init__(self):
		self.value=5

class E_GUILDLOG_BATTLE(enum):
	pass

class e_guildlog_battle_begin(E_GUILDLOG_BATTLE):
	def __init__(self):
		self.value=0

class e_guildlog_battle_finish_guard(E_GUILDLOG_BATTLE):
	def __init__(self):
		self.value=1

class e_guildlog_battle_seize_castle(E_GUILDLOG_BATTLE):
	def __init__(self):
		self.value=2

class e_guildlog_battle_winner_three(E_GUILDLOG_BATTLE):
	def __init__(self):
		self.value=3

class e_guildlog_battle_castle_lose(E_GUILDLOG_BATTLE):
	def __init__(self):
		self.value=4

class guildlog_t(proto):
	def __init__(self):
		self.type1 = E_GUILDLOG_TYPE()
		self.type2 = cint32()
		self.time = cint32()
		self.len_of_param_t = cuint16()
		self.param_t = []
		self.len_of_param_str = cuint16()
		self.param_str = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.type1.serialize(buff, buff_len)
		buff, buff_len = self.type2.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		buff, buff_len = self.len_of_param_t.serialize(buff, buff_len)
		for i in range(self.len_of_param_t.value):
			buff, buff_len = self.param_t[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_param_str.serialize(buff, buff_len)
		for i in range(self.len_of_param_str.value):
			buff, buff_len = self.param_str[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.type1.deserialize(buff)
		buff = self.type2.deserialize(buff)
		buff = self.time.deserialize(buff)
		buff = self.len_of_param_t.deserialize(buff)
		self.param_t = []
		for i in range(self.len_of_param_t.value):
			self.param_t.append(cint32())
			buff = self.param_t[i].deserialize(buff)
		buff = self.len_of_param_str.deserialize(buff)
		self.param_str = []
		for i in range(self.len_of_param_str.value):
			self.param_str.append(cstring())
			buff = self.param_str[i].deserialize(buff)
		return buff

	def add_param_t():
		if len(param_t) >= MAX_GUILDLOG_PARAM_NUM.value:
			return None
		param_t.append(ccint32())
		return param_t[len(param_t) - 1]

	def add_param_str():
		if len(param_str) >= MAX_GUILDLOG_PARAM_NUM.value:
			return None
		param_str.append(ccstring())
		return param_str[len(param_str) - 1]

class name_t(proto):
	def __init__(self):
		self.id = cint64()
		self.name = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.id.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.id.deserialize(buff)
		buff = self.name.deserialize(buff)
		return buff

class guild_city_rank_t(proto):
	def __init__(self):
		self.block_id = cint32()
		self.damage1 = cint32()
		self.damage_1_name = cstring()
		self.damage2 = cint32()
		self.damage_2_name = cstring()
		self.damage3 = cint32()
		self.damage_3_name = cstring()
		self.hp1 = cint32()
		self.hp_1_name = cstring()
		self.hp2 = cint32()
		self.hp_2_name = cstring()
		self.hp3 = cint32()
		self.hp_3_name = cstring()
		self.time = cint32()
		self.guild_name = cstring()
		self.chairman_name = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.damage1.serialize(buff, buff_len)
		buff, buff_len = self.damage_1_name.serialize(buff, buff_len)
		buff, buff_len = self.damage2.serialize(buff, buff_len)
		buff, buff_len = self.damage_2_name.serialize(buff, buff_len)
		buff, buff_len = self.damage3.serialize(buff, buff_len)
		buff, buff_len = self.damage_3_name.serialize(buff, buff_len)
		buff, buff_len = self.hp1.serialize(buff, buff_len)
		buff, buff_len = self.hp_1_name.serialize(buff, buff_len)
		buff, buff_len = self.hp2.serialize(buff, buff_len)
		buff, buff_len = self.hp_2_name.serialize(buff, buff_len)
		buff, buff_len = self.hp3.serialize(buff, buff_len)
		buff, buff_len = self.hp_3_name.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		buff, buff_len = self.guild_name.serialize(buff, buff_len)
		buff, buff_len = self.chairman_name.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.block_id.deserialize(buff)
		buff = self.damage1.deserialize(buff)
		buff = self.damage_1_name.deserialize(buff)
		buff = self.damage2.deserialize(buff)
		buff = self.damage_2_name.deserialize(buff)
		buff = self.damage3.deserialize(buff)
		buff = self.damage_3_name.deserialize(buff)
		buff = self.hp1.deserialize(buff)
		buff = self.hp_1_name.deserialize(buff)
		buff = self.hp2.deserialize(buff)
		buff = self.hp_2_name.deserialize(buff)
		buff = self.hp3.deserialize(buff)
		buff = self.hp_3_name.deserialize(buff)
		buff = self.time.deserialize(buff)
		buff = self.guild_name.deserialize(buff)
		buff = self.chairman_name.deserialize(buff)
		return buff

class guild_city_t(proto):
	def __init__(self):
		self.block_id = cint32()
		self.entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.block_id.deserialize(buff)
		buff = self.entry.deserialize(buff)
		return buff

class lottery_data_t(proto):
	def __init__(self):
		self.lottery_index = cint32()
		self.item_entry = cint32()
		self.item_num = cint32()
		self.price = cint32()
		self.draw_flag = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.lottery_index.serialize(buff, buff_len)
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.item_num.serialize(buff, buff_len)
		buff, buff_len = self.price.serialize(buff, buff_len)
		buff, buff_len = self.draw_flag.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.lottery_index.deserialize(buff)
		buff = self.item_entry.deserialize(buff)
		buff = self.item_num.deserialize(buff)
		buff = self.price.deserialize(buff)
		buff = self.draw_flag.deserialize(buff)
		return buff

class lottery_info_t(proto):
	def __init__(self):
		self.lottery_id = cint32()
		self.len_of_lottery_data_list = cuint16()
		self.lottery_data_list = []
		self.cur_draw_count = cint32()
		self.surplus_free_draw_count = cint32()
		self.reset_count = cint32()
		self.surplus_refresh_time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.lottery_id.serialize(buff, buff_len)
		buff, buff_len = self.len_of_lottery_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_lottery_data_list.value):
			buff, buff_len = self.lottery_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.cur_draw_count.serialize(buff, buff_len)
		buff, buff_len = self.surplus_free_draw_count.serialize(buff, buff_len)
		buff, buff_len = self.reset_count.serialize(buff, buff_len)
		buff, buff_len = self.surplus_refresh_time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.lottery_id.deserialize(buff)
		buff = self.len_of_lottery_data_list.deserialize(buff)
		self.lottery_data_list = []
		for i in range(self.len_of_lottery_data_list.value):
			self.lottery_data_list.append(lottery_data_t())
			buff = self.lottery_data_list[i].deserialize(buff)
		buff = self.cur_draw_count.deserialize(buff)
		buff = self.surplus_free_draw_count.deserialize(buff)
		buff = self.reset_count.deserialize(buff)
		buff = self.surplus_refresh_time.deserialize(buff)
		return buff

	def add_lottery_data_list():
		if len(lottery_data_list) >= MAX_LOTTERY_ITEM_LIST_NUM.value:
			return None
		lottery_data_list.append(lottery_data_t())
		return lottery_data_list[len(lottery_data_list) - 1]

class shop_item_t(proto):
	def __init__(self):
		self.item_entry = cint32()
		self.buy_count = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.buy_count.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.item_entry.deserialize(buff)
		buff = self.buy_count.deserialize(buff)
		return buff

class E_MISSION_CONDITION(enum):
	pass

class e_operate(E_MISSION_CONDITION):
	def __init__(self):
		self.value=0

class e_building(E_MISSION_CONDITION):
	def __init__(self):
		self.value=1

class e_trap(E_MISSION_CONDITION):
	def __init__(self):
		self.value=2

class e_resources(E_MISSION_CONDITION):
	def __init__(self):
		self.value=3

class e_revenue(E_MISSION_CONDITION):
	def __init__(self):
		self.value=4

class e_army(E_MISSION_CONDITION):
	def __init__(self):
		self.value=5

class e_hero(E_MISSION_CONDITION):
	def __init__(self):
		self.value=6

class e_combi_equip(E_MISSION_CONDITION):
	def __init__(self):
		self.value=7

class e_strengthen(E_MISSION_CONDITION):
	def __init__(self):
		self.value=8

class e_battle(E_MISSION_CONDITION):
	def __init__(self):
		self.value=9

class e_guild(E_MISSION_CONDITION):
	def __init__(self):
		self.value=10

class e_block(E_MISSION_CONDITION):
	def __init__(self):
		self.value=11

class effect_t(proto):
	def __init__(self):
		self.change_value = cint32()
		self.change_pct = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.change_value.serialize(buff, buff_len)
		buff, buff_len = self.change_pct.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.change_value.deserialize(buff)
		buff = self.change_pct.deserialize(buff)
		return buff

class E_CHAT_CHANNEL_TYPE(enum):
	pass

class e_chat_channel_type_invalid(E_CHAT_CHANNEL_TYPE):
	def __init__(self):
		self.value=-1

class e_chat_channel_type_world(E_CHAT_CHANNEL_TYPE):
	def __init__(self):
		self.value=0

class e_chat_channel_type_guild(E_CHAT_CHANNEL_TYPE):
	def __init__(self):
		self.value=1

class e_chat_channel_type_state(E_CHAT_CHANNEL_TYPE):
	def __init__(self):
		self.value=2

class e_chat_channel_type_self(E_CHAT_CHANNEL_TYPE):
	def __init__(self):
		self.value=3

class e_chat_channel_type_system(E_CHAT_CHANNEL_TYPE):
	def __init__(self):
		self.value=4

class e_chat_channel_type_inner_guild(E_CHAT_CHANNEL_TYPE):
	def __init__(self):
		self.value=5

class e_chat_channel_type_season(E_CHAT_CHANNEL_TYPE):
	def __init__(self):
		self.value=6

class e_chat_channel_type_battle(E_CHAT_CHANNEL_TYPE):
	def __init__(self):
		self.value=7

class e_chat_channel_type_max(E_CHAT_CHANNEL_TYPE):
	def __init__(self):
		self.value=8

class chat_channel_t(proto):
	def __init__(self):
		self.channel_id = cint64()
		self.create_user_id = cint64()
		self.channel_name = cstring()
		self.channel_type = E_CHAT_CHANNEL_TYPE()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		buff, buff_len = self.create_user_id.serialize(buff, buff_len)
		buff, buff_len = self.channel_name.serialize(buff, buff_len)
		buff, buff_len = self.channel_type.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.channel_id.deserialize(buff)
		buff = self.create_user_id.deserialize(buff)
		buff = self.channel_name.deserialize(buff)
		buff = self.channel_type.deserialize(buff)
		return buff

class E_SERVER_CHAT_CMD_TYPE(enum):
	pass

class e_server_chat_cmd_invalid(E_SERVER_CHAT_CMD_TYPE):
	def __init__(self):
		self.value=-1

class e_server_chat_cmd_login(E_SERVER_CHAT_CMD_TYPE):
	def __init__(self):
		self.value=0

class e_server_chat_cmd_add_channel(E_SERVER_CHAT_CMD_TYPE):
	def __init__(self):
		self.value=1

class e_server_chat_cmd_max(E_SERVER_CHAT_CMD_TYPE):
	def __init__(self):
		self.value=2

class sign_data_t(proto):
	def __init__(self):
		self.sign_day = cint32()
		self.rewards_str = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.sign_day.serialize(buff, buff_len)
		buff, buff_len = self.rewards_str.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.sign_day.deserialize(buff)
		buff = self.rewards_str.deserialize(buff)
		return buff

class E_ACTIVE_TYPE(enum):
	pass

class e_active_seven(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=101

class e_active_first_recharge(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=102

class e_active_limittime_recharge(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=103

class e_active_rebate_recharge(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=104

class e_active_power_achievement(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=105

class e_active_holiday(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=106

class e_active_group_member(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=107

class e_active_group_city(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=108

class e_active_persion_power(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=109

class e_active_fund_force(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=110

class e_active_month_card(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=111

class e_active_fund_num(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=112

class e_active_raffle(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=113

class e_active_day_target(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=114

class e_active_fund2(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=115

class e_active_day_gift(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=116

class e_active_timed_super(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=117

class e_active_limit2(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=118

class e_active_limit3(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=119

class e_active_fund3(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=120

class e_active_time_limit(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=121

class e_active_lucky_lottery(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=122

class e_active_japan_integral(E_ACTIVE_TYPE):
	def __init__(self):
		self.value=201

class E_ACTIVE_OPEN_MODE(enum):
	pass

class e_item_timeline(E_ACTIVE_OPEN_MODE):
	def __init__(self):
		self.value=1

class e_item_relative_sever(E_ACTIVE_OPEN_MODE):
	def __init__(self):
		self.value=2

class e_item_relative_user(E_ACTIVE_OPEN_MODE):
	def __init__(self):
		self.value=3

class e_item_relative_sever_zero(E_ACTIVE_OPEN_MODE):
	def __init__(self):
		self.value=4

class activity_data_t(proto):
	def __init__(self):
		self.activity_item_id = cint32()
		self.times = cint32()
		self.item_state = cint32()
		self.last_time = cint32()
		self.param2 = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.activity_item_id.serialize(buff, buff_len)
		buff, buff_len = self.times.serialize(buff, buff_len)
		buff, buff_len = self.item_state.serialize(buff, buff_len)
		buff, buff_len = self.last_time.serialize(buff, buff_len)
		buff, buff_len = self.param2.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.activity_item_id.deserialize(buff)
		buff = self.times.deserialize(buff)
		buff = self.item_state.deserialize(buff)
		buff = self.last_time.deserialize(buff)
		buff = self.param2.deserialize(buff)
		return buff

class guild_group_t(proto):
	def __init__(self):
		self.group_id = cint64()
		self.leader_userid = cint64()
		self.time = cint32()
		self.name = cstring()
		self.leader_name = cstring()
		self.user_num = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		buff, buff_len = self.leader_userid.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		buff, buff_len = self.leader_name.serialize(buff, buff_len)
		buff, buff_len = self.user_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.group_id.deserialize(buff)
		buff = self.leader_userid.deserialize(buff)
		buff = self.time.deserialize(buff)
		buff = self.name.deserialize(buff)
		buff = self.leader_name.deserialize(buff)
		buff = self.user_num.deserialize(buff)
		return buff

class guild_group_info(proto):
	def __init__(self):
		self.userid = cint64()
		self.group_id = cint64()
		self.time = cint32()
		self.name = cstring()
		self.len_of_guild_member_list = cuint16()
		self.guild_member_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.userid.serialize(buff, buff_len)
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		buff, buff_len = self.len_of_guild_member_list.serialize(buff, buff_len)
		for i in range(self.len_of_guild_member_list.value):
			buff, buff_len = self.guild_member_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.userid.deserialize(buff)
		buff = self.group_id.deserialize(buff)
		buff = self.time.deserialize(buff)
		buff = self.name.deserialize(buff)
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

class my_group_t(proto):
	def __init__(self):
		self.group_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.group_id.deserialize(buff)
		return buff

class war_rank_t(proto):
	def __init__(self):
		self.brief = user_summary_data_t()
		self.war_data = user_war_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.brief.serialize(buff, buff_len)
		buff, buff_len = self.war_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.brief.deserialize(buff)
		buff = self.war_data.deserialize(buff)
		return buff

class force_rank_t(proto):
	def __init__(self):
		self.brief = user_summary_data_t()
		self.land = user_land_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.brief.serialize(buff, buff_len)
		buff, buff_len = self.land.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.brief.deserialize(buff)
		buff = self.land.deserialize(buff)
		return buff

class user_detail(proto):
	def __init__(self):
		self.brief = user_summary_data_t()
		self.war_data = user_war_t()
		self.power = user_power_t()
		self.land = user_land_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.brief.serialize(buff, buff_len)
		buff, buff_len = self.war_data.serialize(buff, buff_len)
		buff, buff_len = self.power.serialize(buff, buff_len)
		buff, buff_len = self.land.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.brief.deserialize(buff)
		buff = self.war_data.deserialize(buff)
		buff = self.power.deserialize(buff)
		buff = self.land.deserialize(buff)
		return buff

class E_LIVENESS_REWARD_STATUS(enum):
	pass

class e_liveness_reward_undone(E_LIVENESS_REWARD_STATUS):
	def __init__(self):
		self.value=1

class e_liveness_reward_done(E_LIVENESS_REWARD_STATUS):
	def __init__(self):
		self.value=0

class e_liveness_reward_reward(E_LIVENESS_REWARD_STATUS):
	def __init__(self):
		self.value=2

class liveness_item(proto):
	def __init__(self):
		self.item_id = cint32()
		self.num = cint32()
		self.num_need = cint32()
		self.reward = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.item_id.serialize(buff, buff_len)
		buff, buff_len = self.num.serialize(buff, buff_len)
		buff, buff_len = self.num_need.serialize(buff, buff_len)
		buff, buff_len = self.reward.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.item_id.deserialize(buff)
		buff = self.num.deserialize(buff)
		buff = self.num_need.deserialize(buff)
		buff = self.reward.deserialize(buff)
		return buff

class liveness_info_t(proto):
	def __init__(self):
		self.liveness_point = cint32()
		self.activity_coin = cint32()
		self.surplus_refresh_time = cint32()
		self.len_of_liveness_items = cuint16()
		self.liveness_items = []
		self.len_of_draw_reward_point = cuint16()
		self.draw_reward_point = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.liveness_point.serialize(buff, buff_len)
		buff, buff_len = self.activity_coin.serialize(buff, buff_len)
		buff, buff_len = self.surplus_refresh_time.serialize(buff, buff_len)
		buff, buff_len = self.len_of_liveness_items.serialize(buff, buff_len)
		for i in range(self.len_of_liveness_items.value):
			buff, buff_len = self.liveness_items[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_draw_reward_point.serialize(buff, buff_len)
		for i in range(self.len_of_draw_reward_point.value):
			buff, buff_len = self.draw_reward_point[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.liveness_point.deserialize(buff)
		buff = self.activity_coin.deserialize(buff)
		buff = self.surplus_refresh_time.deserialize(buff)
		buff = self.len_of_liveness_items.deserialize(buff)
		self.liveness_items = []
		for i in range(self.len_of_liveness_items.value):
			self.liveness_items.append(liveness_item())
			buff = self.liveness_items[i].deserialize(buff)
		buff = self.len_of_draw_reward_point.deserialize(buff)
		self.draw_reward_point = []
		for i in range(self.len_of_draw_reward_point.value):
			self.draw_reward_point.append(cint32())
			buff = self.draw_reward_point[i].deserialize(buff)
		return buff

	def add_liveness_items():
		if len(liveness_items) >= MAX_LIVENESS_NUM.value:
			return None
		liveness_items.append(liveness_item())
		return liveness_items[len(liveness_items) - 1]

	def add_draw_reward_point():
		if len(draw_reward_point) >= MAX_LIVENESS_REWARD_NUM.value:
			return None
		draw_reward_point.append(ccint32())
		return draw_reward_point[len(draw_reward_point) - 1]

class reward_info_t(proto):
	def __init__(self):
		self.e_reward_type = E_REWARD_TYPE()
		self.param0 = cint32()
		self.param1 = cint32()
		self.param2 = cint32()
		self.param3 = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.e_reward_type.serialize(buff, buff_len)
		buff, buff_len = self.param0.serialize(buff, buff_len)
		buff, buff_len = self.param1.serialize(buff, buff_len)
		buff, buff_len = self.param2.serialize(buff, buff_len)
		buff, buff_len = self.param3.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.e_reward_type.deserialize(buff)
		buff = self.param0.deserialize(buff)
		buff = self.param1.deserialize(buff)
		buff = self.param2.deserialize(buff)
		buff = self.param3.deserialize(buff)
		return buff

class mail_head_t(proto):
	def __init__(self):
		self.mail_id = cint64()
		self.recver_id = cint64()
		self.recver_nick_name = cstring()
		self.sender_id = cint64()
		self.sender_nick_name = cstring()
		self.sendto_group_name = cstring()
		self.e_mail_type = E_MAIL_TYPE()
		self.is_readed = cbool()
		self.send_time = cint32()
		self.has_affix = cbool()
		self.title = cstring()
		self.already_pick = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.mail_id.serialize(buff, buff_len)
		buff, buff_len = self.recver_id.serialize(buff, buff_len)
		buff, buff_len = self.recver_nick_name.serialize(buff, buff_len)
		buff, buff_len = self.sender_id.serialize(buff, buff_len)
		buff, buff_len = self.sender_nick_name.serialize(buff, buff_len)
		buff, buff_len = self.sendto_group_name.serialize(buff, buff_len)
		buff, buff_len = self.e_mail_type.serialize(buff, buff_len)
		buff, buff_len = self.is_readed.serialize(buff, buff_len)
		buff, buff_len = self.send_time.serialize(buff, buff_len)
		buff, buff_len = self.has_affix.serialize(buff, buff_len)
		buff, buff_len = self.title.serialize(buff, buff_len)
		buff, buff_len = self.already_pick.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.mail_id.deserialize(buff)
		buff = self.recver_id.deserialize(buff)
		buff = self.recver_nick_name.deserialize(buff)
		buff = self.sender_id.deserialize(buff)
		buff = self.sender_nick_name.deserialize(buff)
		buff = self.sendto_group_name.deserialize(buff)
		buff = self.e_mail_type.deserialize(buff)
		buff = self.is_readed.deserialize(buff)
		buff = self.send_time.deserialize(buff)
		buff = self.has_affix.deserialize(buff)
		buff = self.title.deserialize(buff)
		buff = self.already_pick.deserialize(buff)
		return buff

class mail_body_t(proto):
	def __init__(self):
		self.mail_id = cint64()
		self.sender_position = cint32()
		self.send_time = cint32()
		self.title = cstring()
		self.content = cmail_string()
		self.already_pick = cbool()
		self.len_of_affix_list = cuint16()
		self.affix_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.mail_id.serialize(buff, buff_len)
		buff, buff_len = self.sender_position.serialize(buff, buff_len)
		buff, buff_len = self.send_time.serialize(buff, buff_len)
		buff, buff_len = self.title.serialize(buff, buff_len)
		buff, buff_len = self.content.serialize(buff, buff_len)
		buff, buff_len = self.already_pick.serialize(buff, buff_len)
		buff, buff_len = self.len_of_affix_list.serialize(buff, buff_len)
		for i in range(self.len_of_affix_list.value):
			buff, buff_len = self.affix_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.mail_id.deserialize(buff)
		buff = self.sender_position.deserialize(buff)
		buff = self.send_time.deserialize(buff)
		buff = self.title.deserialize(buff)
		buff = self.content.deserialize(buff)
		buff = self.already_pick.deserialize(buff)
		buff = self.len_of_affix_list.deserialize(buff)
		self.affix_list = []
		for i in range(self.len_of_affix_list.value):
			self.affix_list.append(reward_info_t())
			buff = self.affix_list[i].deserialize(buff)
		return buff

	def add_affix_list():
		if len(affix_list) >= MAX_MAIL_AFFIX_COUNT.value:
			return None
		affix_list.append(reward_info_t())
		return affix_list[len(affix_list) - 1]

class E_CHAT_CONTENT_TYPE(enum):
	pass

class e_chat_content_type_invalid(E_CHAT_CONTENT_TYPE):
	def __init__(self):
		self.value=-1

class e_chat_content_type_chat(E_CHAT_CONTENT_TYPE):
	def __init__(self):
		self.value=0

class e_chat_content_type_event(E_CHAT_CONTENT_TYPE):
	def __init__(self):
		self.value=1

class e_chat_content_type_war_situation(E_CHAT_CONTENT_TYPE):
	def __init__(self):
		self.value=2

class e_chat_content_type_battle_report(E_CHAT_CONTENT_TYPE):
	def __init__(self):
		self.value=3

class chat_data_t(proto):
	def __init__(self):
		self.channel_id = cint64()
		self.msg_id = cint64()
		self.user_id = cint64()
		self.guild_id = cint64()
		self.send_time = cint32()
		self.state = cint32()
		self.position = cint32()
		self.content_type = E_CHAT_CONTENT_TYPE()
		self.nick_name = cstring()
		self.guild_name = cstring()
		self.group_name = cstring()
		self.content = cstring()
		self.kp_title = cint32()
		self.server_id = cint32()
		self.head_entry = cint32()
		self.head_type = cint32()
		self.head_url = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.channel_id.serialize(buff, buff_len)
		buff, buff_len = self.msg_id.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.send_time.serialize(buff, buff_len)
		buff, buff_len = self.state.serialize(buff, buff_len)
		buff, buff_len = self.position.serialize(buff, buff_len)
		buff, buff_len = self.content_type.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		buff, buff_len = self.guild_name.serialize(buff, buff_len)
		buff, buff_len = self.group_name.serialize(buff, buff_len)
		buff, buff_len = self.content.serialize(buff, buff_len)
		buff, buff_len = self.kp_title.serialize(buff, buff_len)
		buff, buff_len = self.server_id.serialize(buff, buff_len)
		buff, buff_len = self.head_entry.serialize(buff, buff_len)
		buff, buff_len = self.head_type.serialize(buff, buff_len)
		buff, buff_len = self.head_url.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.channel_id.deserialize(buff)
		buff = self.msg_id.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		buff = self.send_time.deserialize(buff)
		buff = self.state.deserialize(buff)
		buff = self.position.deserialize(buff)
		buff = self.content_type.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		buff = self.guild_name.deserialize(buff)
		buff = self.group_name.deserialize(buff)
		buff = self.content.deserialize(buff)
		buff = self.kp_title.deserialize(buff)
		buff = self.server_id.deserialize(buff)
		buff = self.head_entry.deserialize(buff)
		buff = self.head_type.deserialize(buff)
		buff = self.head_url.deserialize(buff)
		return buff

class building_lv_t(proto):
	def __init__(self):
		self.castle_id = cint64()
		self.lv = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.lv.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.castle_id.deserialize(buff)
		buff = self.lv.deserialize(buff)
		return buff

class SEASON_STAGE(enum):
	pass

class e_season_stage_begin(SEASON_STAGE):
	def __init__(self):
		self.value=0

class e_season_stage_shopping(SEASON_STAGE):
	def __init__(self):
		self.value=1

class e_season_stage_running(SEASON_STAGE):
	def __init__(self):
		self.value=2

class e_season_stage_checking(SEASON_STAGE):
	def __init__(self):
		self.value=3

class e_season_stage_free(SEASON_STAGE):
	def __init__(self):
		self.value=4

class e_season_stage_end(SEASON_STAGE):
	def __init__(self):
		self.value=5

class season_t(proto):
	def __init__(self):
		self.season = cint32()
		self.score = cint32()
		self.rank = cint32()
		self.server_id = cint32()
		self.stage = cint32()
		self.end_time = cint32()
		self.season_reward_entry = cint32()
		self.guild_reward = cstring()
		self.score_reward = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.season.serialize(buff, buff_len)
		buff, buff_len = self.score.serialize(buff, buff_len)
		buff, buff_len = self.rank.serialize(buff, buff_len)
		buff, buff_len = self.server_id.serialize(buff, buff_len)
		buff, buff_len = self.stage.serialize(buff, buff_len)
		buff, buff_len = self.end_time.serialize(buff, buff_len)
		buff, buff_len = self.season_reward_entry.serialize(buff, buff_len)
		buff, buff_len = self.guild_reward.serialize(buff, buff_len)
		buff, buff_len = self.score_reward.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.season.deserialize(buff)
		buff = self.score.deserialize(buff)
		buff = self.rank.deserialize(buff)
		buff = self.server_id.deserialize(buff)
		buff = self.stage.deserialize(buff)
		buff = self.end_time.deserialize(buff)
		buff = self.season_reward_entry.deserialize(buff)
		buff = self.guild_reward.deserialize(buff)
		buff = self.score_reward.deserialize(buff)
		return buff

class ally_castle(proto):
	def __init__(self):
		self.user_id = cint64()
		self.block_id = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user_id.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		return buff

class E_SERVER_MSG_PARA_TYPE(enum):
	pass

class e_msg_para_type_word_entry(E_SERVER_MSG_PARA_TYPE):
	def __init__(self):
		self.value=1

class e_msg_para_type_int32(E_SERVER_MSG_PARA_TYPE):
	def __init__(self):
		self.value=2

class e_msg_para_type_int64(E_SERVER_MSG_PARA_TYPE):
	def __init__(self):
		self.value=3

class e_msg_para_type_string(E_SERVER_MSG_PARA_TYPE):
	def __init__(self):
		self.value=4

class E_SERVER_WORD(enum):
	pass

class e_server_word_mail_chat_rem(E_SERVER_WORD):
	def __init__(self):
		self.value=16326

class e_server_word_mail_guild_chairman(E_SERVER_WORD):
	def __init__(self):
		self.value=16327

class e_server_word_mail_guild_position_up(E_SERVER_WORD):
	def __init__(self):
		self.value=16328

class e_server_word_mail_guild_position_down(E_SERVER_WORD):
	def __init__(self):
		self.value=16329

class e_server_word_mail_guild_rem(E_SERVER_WORD):
	def __init__(self):
		self.value=16330

class e_server_word_mail_guild_group_up(E_SERVER_WORD):
	def __init__(self):
		self.value=16331

class e_server_word_mail_guild_group_down(E_SERVER_WORD):
	def __init__(self):
		self.value=16332

class e_server_word_mail_guild_group_rem(E_SERVER_WORD):
	def __init__(self):
		self.value=16333

class e_server_word_guild_chairman(E_SERVER_WORD):
	def __init__(self):
		self.value=16334

class e_server_word_guild_vicechairman(E_SERVER_WORD):
	def __init__(self):
		self.value=16335

class e_server_word_guild_elder(E_SERVER_WORD):
	def __init__(self):
		self.value=16336

class e_server_word_guild_member(E_SERVER_WORD):
	def __init__(self):
		self.value=16337

class e_server_word_chat_mail(E_SERVER_WORD):
	def __init__(self):
		self.value=16338

class e_server_word_guild_mail(E_SERVER_WORD):
	def __init__(self):
		self.value=16339

class e_server_word_guild_improve_mail(E_SERVER_WORD):
	def __init__(self):
		self.value=16340

class e_server_word_guild_demotion_mail(E_SERVER_WORD):
	def __init__(self):
		self.value=16341

class e_server_word_guild_group_mail(E_SERVER_WORD):
	def __init__(self):
		self.value=16342

class e_server_word_mail_chat_del(E_SERVER_WORD):
	def __init__(self):
		self.value=16343

class e_server_word_building_lvup_finish_event(E_SERVER_WORD):
	def __init__(self):
		self.value=16344

class e_server_word_block_building_build_finish_event(E_SERVER_WORD):
	def __init__(self):
		self.value=16345

class e_server_word_conscript_soldier_finish_event(E_SERVER_WORD):
	def __init__(self):
		self.value=16346

class e_server_word_tech_lvup_finish_event(E_SERVER_WORD):
	def __init__(self):
		self.value=16347

class e_server_word_combat_win_event(E_SERVER_WORD):
	def __init__(self):
		self.value=16348

class e_server_word_combat_win_land_event(E_SERVER_WORD):
	def __init__(self):
		self.value=16349

class e_server_word_combat_lose_event(E_SERVER_WORD):
	def __init__(self):
		self.value=16350

class e_server_word_combat_lose_land_event(E_SERVER_WORD):
	def __init__(self):
		self.value=16351

class e_server_word_guild_invader(E_SERVER_WORD):
	def __init__(self):
		self.value=16352

class e_server_word_city_occupy(E_SERVER_WORD):
	def __init__(self):
		self.value=16353

class e_server_word_world_city_occupy(E_SERVER_WORD):
	def __init__(self):
		self.value=16354

class e_server_word_guild_attack(E_SERVER_WORD):
	def __init__(self):
		self.value=16355

class e_server_word_pass_occupy(E_SERVER_WORD):
	def __init__(self):
		self.value=16356

class e_server_word_first_login_mail(E_SERVER_WORD):
	def __init__(self):
		self.value=17000

class e_server_word_first_pay_mail(E_SERVER_WORD):
	def __init__(self):
		self.value=17001

class e_server_word_system_mail(E_SERVER_WORD):
	def __init__(self):
		self.value=1976

class e_server_word_guild_transfer_failed_mail(E_SERVER_WORD):
	def __init__(self):
		self.value=19223

class e_server_word_invade_mail(E_SERVER_WORD):
	def __init__(self):
		self.value=40005

class e_server_word_guild_invade_mail(E_SERVER_WORD):
	def __init__(self):
		self.value=40006

class e_server_word_seize_city_mail(E_SERVER_WORD):
	def __init__(self):
		self.value=102024

class e_server_word_seize_mail_seize_city(E_SERVER_WORD):
	def __init__(self):
		self.value=102025

class e_server_word_seize_mail_city_dam(E_SERVER_WORD):
	def __init__(self):
		self.value=102027

class e_server_word_seize_mail_city_score(E_SERVER_WORD):
	def __init__(self):
		self.value=102026

class e_server_word_seize_mail_join(E_SERVER_WORD):
	def __init__(self):
		self.value=102028

class e_server_word_month_card_reward(E_SERVER_WORD):
	def __init__(self):
		self.value=111010

class e_server_word_guild_accuse_mail(E_SERVER_WORD):
	def __init__(self):
		self.value=111011

class e_server_word_mail_guild_accuse(E_SERVER_WORD):
	def __init__(self):
		self.value=111012

class e_server_word_mail_season_reward(E_SERVER_WORD):
	def __init__(self):
		self.value=17100

class e_server_word_mail_season_guild_reward(E_SERVER_WORD):
	def __init__(self):
		self.value=17101

class e_server_word_mail_season_score_reward(E_SERVER_WORD):
	def __init__(self):
		self.value=17102

class e_server_word_mail_rob_title(E_SERVER_WORD):
	def __init__(self):
		self.value=17103

class e_server_word_mail_rob_win(E_SERVER_WORD):
	def __init__(self):
		self.value=17104

class e_server_word_mail_rob_lose(E_SERVER_WORD):
	def __init__(self):
		self.value=17105

class e_server_word_mail_be_rob_title(E_SERVER_WORD):
	def __init__(self):
		self.value=17106

class e_server_word_mail_be_rob_lost(E_SERVER_WORD):
	def __init__(self):
		self.value=17107

class e_server_word_mail_be_rob_guard(E_SERVER_WORD):
	def __init__(self):
		self.value=17108

class e_server_word_mail_rob_miss(E_SERVER_WORD):
	def __init__(self):
		self.value=17115

class e_server_word_mail_delay_donate_gold_title(E_SERVER_WORD):
	def __init__(self):
		self.value=110000382

class e_server_word_mail_delay_donate_gold_content(E_SERVER_WORD):
	def __init__(self):
		self.value=110000383

class E_WORLD_NOTICE_TYPE(enum):
	pass

class e_world_notice_conquer_field(E_WORLD_NOTICE_TYPE):
	def __init__(self):
		self.value=1

class e_world_notice_guild_level(E_WORLD_NOTICE_TYPE):
	def __init__(self):
		self.value=2

class e_world_notice_guild_shili(E_WORLD_NOTICE_TYPE):
	def __init__(self):
		self.value=3

class e_world_notice_conquer_rebelcity(E_WORLD_NOTICE_TYPE):
	def __init__(self):
		self.value=4

class e_world_notice_conquer_midcity(E_WORLD_NOTICE_TYPE):
	def __init__(self):
		self.value=5

class e_world_notice_kill_emenies(E_WORLD_NOTICE_TYPE):
	def __init__(self):
		self.value=6

class E_VIP_REWARD_STATUS(enum):
	pass

class e_vip_reward_status_received(E_VIP_REWARD_STATUS):
	def __init__(self):
		self.value=0

class e_vip_reward_status_can_not_receive(E_VIP_REWARD_STATUS):
	def __init__(self):
		self.value=1

class e_vip_reward_status_can_receive(E_VIP_REWARD_STATUS):
	def __init__(self):
		self.value=2

class vip_reward_status_t(proto):
	def __init__(self):
		self.vip_lv = cint32()
		self.status = E_VIP_REWARD_STATUS()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.vip_lv.serialize(buff, buff_len)
		buff, buff_len = self.status.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.vip_lv.deserialize(buff)
		buff = self.status.deserialize(buff)
		return buff

class E_LANGUAGE_TYPE(enum):
	pass

class e_language_type_invalid(E_LANGUAGE_TYPE):
	def __init__(self):
		self.value=-1

class e_language_type_en(E_LANGUAGE_TYPE):
	def __init__(self):
		self.value=1

class e_language_type_cn(E_LANGUAGE_TYPE):
	def __init__(self):
		self.value=2

class e_language_type_cht(E_LANGUAGE_TYPE):
	def __init__(self):
		self.value=3

class e_language_type_jp(E_LANGUAGE_TYPE):
	def __init__(self):
		self.value=4

class e_language_type_tr(E_LANGUAGE_TYPE):
	def __init__(self):
		self.value=5

class e_language_type_max(E_LANGUAGE_TYPE):
	def __init__(self):
		self.value=6

class latest_chat_data_t(proto):
	def __init__(self):
		self.msg_id = cint64()
		self.user_id = cint64()
		self.guild_id = cint64()
		self.send_time = cint32()
		self.nick_name = cstring()
		self.guild_name = cstring()
		self.group_name = cstring()
		self.state = cint32()
		self.position = cint32()
		self.title = cint32()
		self.content_type = E_CHAT_CONTENT_TYPE()
		self.len_of_content = cuint16()
		self.content = []
		self.server_id = cint32()
		self.head_entry = cint32()
		self.head_type = cint32()
		self.head_url = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.msg_id.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.send_time.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		buff, buff_len = self.guild_name.serialize(buff, buff_len)
		buff, buff_len = self.group_name.serialize(buff, buff_len)
		buff, buff_len = self.state.serialize(buff, buff_len)
		buff, buff_len = self.position.serialize(buff, buff_len)
		buff, buff_len = self.title.serialize(buff, buff_len)
		buff, buff_len = self.content_type.serialize(buff, buff_len)
		buff, buff_len = self.len_of_content.serialize(buff, buff_len)
		for i in range(self.len_of_content.value):
			buff, buff_len = self.content[i].serialize(buff, buff_len)
		buff, buff_len = self.server_id.serialize(buff, buff_len)
		buff, buff_len = self.head_entry.serialize(buff, buff_len)
		buff, buff_len = self.head_type.serialize(buff, buff_len)
		buff, buff_len = self.head_url.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.msg_id.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		buff = self.send_time.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		buff = self.guild_name.deserialize(buff)
		buff = self.group_name.deserialize(buff)
		buff = self.state.deserialize(buff)
		buff = self.position.deserialize(buff)
		buff = self.title.deserialize(buff)
		buff = self.content_type.deserialize(buff)
		buff = self.len_of_content.deserialize(buff)
		self.content = []
		for i in range(self.len_of_content.value):
			self.content.append(cstring())
			buff = self.content[i].deserialize(buff)
		buff = self.server_id.deserialize(buff)
		buff = self.head_entry.deserialize(buff)
		buff = self.head_type.deserialize(buff)
		buff = self.head_url.deserialize(buff)
		return buff

	def add_content():
		if len(content) >= e_language_type_max.value:
			return None
		content.append(ccstring())
		return content[len(content) - 1]

class activity_status(proto):
	def __init__(self):
		self.activity_id = cint32()
		self.activity_type = cint32()
		self.has_reward = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.activity_id.serialize(buff, buff_len)
		buff, buff_len = self.activity_type.serialize(buff, buff_len)
		buff, buff_len = self.has_reward.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.activity_id.deserialize(buff)
		buff = self.activity_type.deserialize(buff)
		buff = self.has_reward.deserialize(buff)
		return buff

class hero_brief_data(proto):
	def __init__(self):
		self.entry = cint32()
		self.level = cint32()
		self.exp = cint32()
		self.liliang = cint32()
		self.naili = cint32()
		self.moulue = cint32()
		self.minjie = cint32()
		self.destroy = cint32()
		self.free_point = cint32()
		self.junxian = cint32()
		self.phy_force = cint32()
		self.phy_force_time = cint32()
		self.star_lv = cint32()
		self.quality = E_HERO_QUALITY()
		self.quality_lv = cint32()
		self.hangup_count = cint32()
		self.hangup_value = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.level.serialize(buff, buff_len)
		buff, buff_len = self.exp.serialize(buff, buff_len)
		buff, buff_len = self.liliang.serialize(buff, buff_len)
		buff, buff_len = self.naili.serialize(buff, buff_len)
		buff, buff_len = self.moulue.serialize(buff, buff_len)
		buff, buff_len = self.minjie.serialize(buff, buff_len)
		buff, buff_len = self.destroy.serialize(buff, buff_len)
		buff, buff_len = self.free_point.serialize(buff, buff_len)
		buff, buff_len = self.junxian.serialize(buff, buff_len)
		buff, buff_len = self.phy_force.serialize(buff, buff_len)
		buff, buff_len = self.phy_force_time.serialize(buff, buff_len)
		buff, buff_len = self.star_lv.serialize(buff, buff_len)
		buff, buff_len = self.quality.serialize(buff, buff_len)
		buff, buff_len = self.quality_lv.serialize(buff, buff_len)
		buff, buff_len = self.hangup_count.serialize(buff, buff_len)
		buff, buff_len = self.hangup_value.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.level.deserialize(buff)
		buff = self.exp.deserialize(buff)
		buff = self.liliang.deserialize(buff)
		buff = self.naili.deserialize(buff)
		buff = self.moulue.deserialize(buff)
		buff = self.minjie.deserialize(buff)
		buff = self.destroy.deserialize(buff)
		buff = self.free_point.deserialize(buff)
		buff = self.junxian.deserialize(buff)
		buff = self.phy_force.deserialize(buff)
		buff = self.phy_force_time.deserialize(buff)
		buff = self.star_lv.deserialize(buff)
		buff = self.quality.deserialize(buff)
		buff = self.quality_lv.deserialize(buff)
		buff = self.hangup_count.deserialize(buff)
		buff = self.hangup_value.deserialize(buff)
		return buff

class hangup_user_data_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.start_time = cint32()
		self.slot_0 = cint64()
		self.slot_1 = cint64()
		self.slot_2 = cint64()
		self.slot_3 = cint64()
		self.slot_4 = cint64()
		self.len_of_hero = cuint16()
		self.hero = []
		self.res = user_resource_increase_t()
		self.drops = hangup_drops()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.start_time.serialize(buff, buff_len)
		buff, buff_len = self.slot_0.serialize(buff, buff_len)
		buff, buff_len = self.slot_1.serialize(buff, buff_len)
		buff, buff_len = self.slot_2.serialize(buff, buff_len)
		buff, buff_len = self.slot_3.serialize(buff, buff_len)
		buff, buff_len = self.slot_4.serialize(buff, buff_len)
		buff, buff_len = self.len_of_hero.serialize(buff, buff_len)
		for i in range(self.len_of_hero.value):
			buff, buff_len = self.hero[i].serialize(buff, buff_len)
		buff, buff_len = self.res.serialize(buff, buff_len)
		buff, buff_len = self.drops.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.start_time.deserialize(buff)
		buff = self.slot_0.deserialize(buff)
		buff = self.slot_1.deserialize(buff)
		buff = self.slot_2.deserialize(buff)
		buff = self.slot_3.deserialize(buff)
		buff = self.slot_4.deserialize(buff)
		buff = self.len_of_hero.deserialize(buff)
		self.hero = []
		for i in range(self.len_of_hero.value):
			self.hero.append(hero_brief_data())
			buff = self.hero[i].deserialize(buff)
		buff = self.res.deserialize(buff)
		buff = self.drops.deserialize(buff)
		return buff

	def add_hero():
		if len(hero) >= MAX_HANGUP_SLOT.value:
			return None
		hero.append(hero_brief_data())
		return hero[len(hero) - 1]

class currency_info_t(proto):
	def __init__(self):
		self.resources = user_resource_t()
		self.contribution = cint32()
		self.arena_coin = cint32()
		self.activity_coin = cint32()
		self.season_coin = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.resources.serialize(buff, buff_len)
		buff, buff_len = self.contribution.serialize(buff, buff_len)
		buff, buff_len = self.arena_coin.serialize(buff, buff_len)
		buff, buff_len = self.activity_coin.serialize(buff, buff_len)
		buff, buff_len = self.season_coin.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.resources.deserialize(buff)
		buff = self.contribution.deserialize(buff)
		buff = self.arena_coin.deserialize(buff)
		buff = self.activity_coin.deserialize(buff)
		buff = self.season_coin.deserialize(buff)
		return buff

class E_SHOP_UNLOCK_TYPE(enum):
	pass

class e_shop_unlock_type_guild(E_SHOP_UNLOCK_TYPE):
	def __init__(self):
		self.value=1

class e_shop_unlock_type_private(E_SHOP_UNLOCK_TYPE):
	def __init__(self):
		self.value=2

class e_shop_unlock_type_kp(E_SHOP_UNLOCK_TYPE):
	def __init__(self):
		self.value=3

class e_shop_unlock_type_rebel(E_SHOP_UNLOCK_TYPE):
	def __init__(self):
		self.value=4

class shop_item_data_t(proto):
	def __init__(self):
		self.slot = cint32()
		self.entry = cint32()
		self.stack_count = cint32()
		self.buy_count = cint32()
		self.cost = cint32()
		self.buy_limit = cint32()
		self.unlock_type = E_SHOP_UNLOCK_TYPE()
		self.unlock_value = cint32()
		self.is_discount = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.slot.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.stack_count.serialize(buff, buff_len)
		buff, buff_len = self.buy_count.serialize(buff, buff_len)
		buff, buff_len = self.cost.serialize(buff, buff_len)
		buff, buff_len = self.buy_limit.serialize(buff, buff_len)
		buff, buff_len = self.unlock_type.serialize(buff, buff_len)
		buff, buff_len = self.unlock_value.serialize(buff, buff_len)
		buff, buff_len = self.is_discount.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.slot.deserialize(buff)
		buff = self.entry.deserialize(buff)
		buff = self.stack_count.deserialize(buff)
		buff = self.buy_count.deserialize(buff)
		buff = self.cost.deserialize(buff)
		buff = self.buy_limit.deserialize(buff)
		buff = self.unlock_type.deserialize(buff)
		buff = self.unlock_value.deserialize(buff)
		buff = self.is_discount.deserialize(buff)
		return buff

class buy_shop_item_info_t(proto):
	def __init__(self):
		self.slot = cint32()
		self.shop_entry = cint32()
		self.cost = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.slot.serialize(buff, buff_len)
		buff, buff_len = self.shop_entry.serialize(buff, buff_len)
		buff, buff_len = self.cost.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.slot.deserialize(buff)
		buff = self.shop_entry.deserialize(buff)
		buff = self.cost.deserialize(buff)
		return buff

class shop_buy_result_t(proto):
	def __init__(self):
		self.slot = cint32()
		self.shop_entry = cint32()
		self.buy_count = cint32()
		self.hero = hero_data_t()
		self.item = item_data_t()
		self.currency_info = currency_info_t()
		self.shop_item = shop_item_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.slot.serialize(buff, buff_len)
		buff, buff_len = self.shop_entry.serialize(buff, buff_len)
		buff, buff_len = self.buy_count.serialize(buff, buff_len)
		buff, buff_len = self.hero.serialize(buff, buff_len)
		buff, buff_len = self.item.serialize(buff, buff_len)
		buff, buff_len = self.currency_info.serialize(buff, buff_len)
		buff, buff_len = self.shop_item.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.slot.deserialize(buff)
		buff = self.shop_entry.deserialize(buff)
		buff = self.buy_count.deserialize(buff)
		buff = self.hero.deserialize(buff)
		buff = self.item.deserialize(buff)
		buff = self.currency_info.deserialize(buff)
		buff = self.shop_item.deserialize(buff)
		return buff

class E_SHOP_TYPE(enum):
	pass

class e_shop_type_invalid(E_SHOP_TYPE):
	def __init__(self):
		self.value=-1

class e_shop_type_normal(E_SHOP_TYPE):
	def __init__(self):
		self.value=0

class e_shop_type_guild(E_SHOP_TYPE):
	def __init__(self):
		self.value=1

class e_shop_type_arena(E_SHOP_TYPE):
	def __init__(self):
		self.value=2

class e_shop_type_activity(E_SHOP_TYPE):
	def __init__(self):
		self.value=3

class e_shop_type_resource(E_SHOP_TYPE):
	def __init__(self):
		self.value=4

class e_shop_type_npc(E_SHOP_TYPE):
	def __init__(self):
		self.value=5

class e_shop_type_silver(E_SHOP_TYPE):
	def __init__(self):
		self.value=6

class e_shop_type_season(E_SHOP_TYPE):
	def __init__(self):
		self.value=7

class e_shop_type_max(E_SHOP_TYPE):
	def __init__(self):
		self.value=8

class arena_user_brief_t(proto):
	def __init__(self):
		self.user = user_summary_data_t()
		self.honor = cint32()
		self.nick_name_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user.serialize(buff, buff_len)
		buff, buff_len = self.honor.serialize(buff, buff_len)
		buff, buff_len = self.nick_name_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user.deserialize(buff)
		buff = self.honor.deserialize(buff)
		buff = self.nick_name_entry.deserialize(buff)
		return buff

class arena_formation(proto):
	def __init__(self):
		self.index = cint32()
		self.hero_0 = cint32()
		self.hero_1 = cint32()
		self.hero_2 = cint32()
		self.troops_entry_0 = cint32()
		self.troops_num_0 = cint32()
		self.troops_entry_1 = cint32()
		self.troops_num_1 = cint32()
		self.troops_entry_2 = cint32()
		self.troops_num_2 = cint32()
		self.troops_entry_3 = cint32()
		self.troops_num_3 = cint32()
		self.troops_entry_4 = cint32()
		self.troops_num_4 = cint32()
		self.power = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.index.serialize(buff, buff_len)
		buff, buff_len = self.hero_0.serialize(buff, buff_len)
		buff, buff_len = self.hero_1.serialize(buff, buff_len)
		buff, buff_len = self.hero_2.serialize(buff, buff_len)
		buff, buff_len = self.troops_entry_0.serialize(buff, buff_len)
		buff, buff_len = self.troops_num_0.serialize(buff, buff_len)
		buff, buff_len = self.troops_entry_1.serialize(buff, buff_len)
		buff, buff_len = self.troops_num_1.serialize(buff, buff_len)
		buff, buff_len = self.troops_entry_2.serialize(buff, buff_len)
		buff, buff_len = self.troops_num_2.serialize(buff, buff_len)
		buff, buff_len = self.troops_entry_3.serialize(buff, buff_len)
		buff, buff_len = self.troops_num_3.serialize(buff, buff_len)
		buff, buff_len = self.troops_entry_4.serialize(buff, buff_len)
		buff, buff_len = self.troops_num_4.serialize(buff, buff_len)
		buff, buff_len = self.power.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.index.deserialize(buff)
		buff = self.hero_0.deserialize(buff)
		buff = self.hero_1.deserialize(buff)
		buff = self.hero_2.deserialize(buff)
		buff = self.troops_entry_0.deserialize(buff)
		buff = self.troops_num_0.deserialize(buff)
		buff = self.troops_entry_1.deserialize(buff)
		buff = self.troops_num_1.deserialize(buff)
		buff = self.troops_entry_2.deserialize(buff)
		buff = self.troops_num_2.deserialize(buff)
		buff = self.troops_entry_3.deserialize(buff)
		buff = self.troops_num_3.deserialize(buff)
		buff = self.troops_entry_4.deserialize(buff)
		buff = self.troops_num_4.deserialize(buff)
		buff = self.power.deserialize(buff)
		return buff

class arena_user_data_t(proto):
	def __init__(self):
		self.honor = cint32()
		self.free_times = cint32()
		self.buy_times = cint64()
		self.score = cint32()
		self.reward_entry = cint32()
		self.season_entry = cint32()
		self.season_rank = cint32()
		self.fresh_time = cint32()
		self.len_of_formation = cuint16()
		self.formation = []
		self.len_of_hero = cuint16()
		self.hero = []
		self.enemy = arena_user_brief_t()
		self.len_of_enemy_formation = cuint16()
		self.enemy_formation = []
		self.len_of_enemy_hero = cuint16()
		self.enemy_hero = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.honor.serialize(buff, buff_len)
		buff, buff_len = self.free_times.serialize(buff, buff_len)
		buff, buff_len = self.buy_times.serialize(buff, buff_len)
		buff, buff_len = self.score.serialize(buff, buff_len)
		buff, buff_len = self.reward_entry.serialize(buff, buff_len)
		buff, buff_len = self.season_entry.serialize(buff, buff_len)
		buff, buff_len = self.season_rank.serialize(buff, buff_len)
		buff, buff_len = self.fresh_time.serialize(buff, buff_len)
		buff, buff_len = self.len_of_formation.serialize(buff, buff_len)
		for i in range(self.len_of_formation.value):
			buff, buff_len = self.formation[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_hero.serialize(buff, buff_len)
		for i in range(self.len_of_hero.value):
			buff, buff_len = self.hero[i].serialize(buff, buff_len)
		buff, buff_len = self.enemy.serialize(buff, buff_len)
		buff, buff_len = self.len_of_enemy_formation.serialize(buff, buff_len)
		for i in range(self.len_of_enemy_formation.value):
			buff, buff_len = self.enemy_formation[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_enemy_hero.serialize(buff, buff_len)
		for i in range(self.len_of_enemy_hero.value):
			buff, buff_len = self.enemy_hero[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.honor.deserialize(buff)
		buff = self.free_times.deserialize(buff)
		buff = self.buy_times.deserialize(buff)
		buff = self.score.deserialize(buff)
		buff = self.reward_entry.deserialize(buff)
		buff = self.season_entry.deserialize(buff)
		buff = self.season_rank.deserialize(buff)
		buff = self.fresh_time.deserialize(buff)
		buff = self.len_of_formation.deserialize(buff)
		self.formation = []
		for i in range(self.len_of_formation.value):
			self.formation.append(arena_formation())
			buff = self.formation[i].deserialize(buff)
		buff = self.len_of_hero.deserialize(buff)
		self.hero = []
		for i in range(self.len_of_hero.value):
			self.hero.append(hero_brief_data())
			buff = self.hero[i].deserialize(buff)
		buff = self.enemy.deserialize(buff)
		buff = self.len_of_enemy_formation.deserialize(buff)
		self.enemy_formation = []
		for i in range(self.len_of_enemy_formation.value):
			self.enemy_formation.append(arena_formation())
			buff = self.enemy_formation[i].deserialize(buff)
		buff = self.len_of_enemy_hero.deserialize(buff)
		self.enemy_hero = []
		for i in range(self.len_of_enemy_hero.value):
			self.enemy_hero.append(hero_brief_data())
			buff = self.enemy_hero[i].deserialize(buff)
		return buff

	def add_formation():
		if len(formation) >= MAX_ARENA_CORPS_NUM.value:
			return None
		formation.append(arena_formation())
		return formation[len(formation) - 1]

	def add_hero():
		if len(hero) >= MAX_ARENA_BATTLE_HERO_NUM.value:
			return None
		hero.append(hero_brief_data())
		return hero[len(hero) - 1]

	def add_enemy_formation():
		if len(enemy_formation) >= MAX_ARENA_CORPS_NUM.value:
			return None
		enemy_formation.append(arena_formation())
		return enemy_formation[len(enemy_formation) - 1]

	def add_enemy_hero():
		if len(enemy_hero) >= MAX_ARENA_BATTLE_HERO_NUM.value:
			return None
		enemy_hero.append(hero_brief_data())
		return enemy_hero[len(enemy_hero) - 1]

class E_TOWER_STATUS(enum):
	pass

class e_tower_status_locked(E_TOWER_STATUS):
	def __init__(self):
		self.value=0

class e_tower_status_unpass(E_TOWER_STATUS):
	def __init__(self):
		self.value=1

class e_tower_status_pass(E_TOWER_STATUS):
	def __init__(self):
		self.value=2

class E_MATCH_FORMATION(enum):
	pass

class e_match_formation_att(E_MATCH_FORMATION):
	def __init__(self):
		self.value=0

class e_match_formation_def(E_MATCH_FORMATION):
	def __init__(self):
		self.value=1

class E_REWARD_STATUS(enum):
	pass

class e_tower_status_none(E_REWARD_STATUS):
	def __init__(self):
		self.value=0

class e_tower_status_cant_draw(E_REWARD_STATUS):
	def __init__(self):
		self.value=1

class e_tower_status_undraw(E_REWARD_STATUS):
	def __init__(self):
		self.value=2

class e_tower_status_draw(E_REWARD_STATUS):
	def __init__(self):
		self.value=3

class tower_reward(proto):
	def __init__(self):
		self.floor = cint32()
		self.status = E_REWARD_STATUS()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.floor.serialize(buff, buff_len)
		buff, buff_len = self.status.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.floor.deserialize(buff)
		buff = self.status.deserialize(buff)
		return buff

class tower_floor_info(proto):
	def __init__(self):
		self.mode = cint32()
		self.floor = cint32()
		self.status = E_TOWER_STATUS()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.mode.serialize(buff, buff_len)
		buff, buff_len = self.floor.serialize(buff, buff_len)
		buff, buff_len = self.status.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.mode.deserialize(buff)
		buff = self.floor.deserialize(buff)
		buff = self.status.deserialize(buff)
		return buff

class hangup_user_info(proto):
	def __init__(self):
		self.mode = cint32()
		self.floor = cint32()
		self.start_time = cint32()
		self.slot_0 = cint64()
		self.slot_1 = cint64()
		self.slot_2 = cint64()
		self.slot_3 = cint64()
		self.slot_4 = cint64()
		self.len_of_hero = cuint16()
		self.hero = []
		self.res = user_resource_increase_t()
		self.drops = hangup_drops()
		self.reward_time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.mode.serialize(buff, buff_len)
		buff, buff_len = self.floor.serialize(buff, buff_len)
		buff, buff_len = self.start_time.serialize(buff, buff_len)
		buff, buff_len = self.slot_0.serialize(buff, buff_len)
		buff, buff_len = self.slot_1.serialize(buff, buff_len)
		buff, buff_len = self.slot_2.serialize(buff, buff_len)
		buff, buff_len = self.slot_3.serialize(buff, buff_len)
		buff, buff_len = self.slot_4.serialize(buff, buff_len)
		buff, buff_len = self.len_of_hero.serialize(buff, buff_len)
		for i in range(self.len_of_hero.value):
			buff, buff_len = self.hero[i].serialize(buff, buff_len)
		buff, buff_len = self.res.serialize(buff, buff_len)
		buff, buff_len = self.drops.serialize(buff, buff_len)
		buff, buff_len = self.reward_time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.mode.deserialize(buff)
		buff = self.floor.deserialize(buff)
		buff = self.start_time.deserialize(buff)
		buff = self.slot_0.deserialize(buff)
		buff = self.slot_1.deserialize(buff)
		buff = self.slot_2.deserialize(buff)
		buff = self.slot_3.deserialize(buff)
		buff = self.slot_4.deserialize(buff)
		buff = self.len_of_hero.deserialize(buff)
		self.hero = []
		for i in range(self.len_of_hero.value):
			self.hero.append(hero_brief_data())
			buff = self.hero[i].deserialize(buff)
		buff = self.res.deserialize(buff)
		buff = self.drops.deserialize(buff)
		buff = self.reward_time.deserialize(buff)
		return buff

	def add_hero():
		if len(hero) >= MAX_HANGUP_SLOT.value:
			return None
		hero.append(hero_brief_data())
		return hero[len(hero) - 1]

class tower_info(proto):
	def __init__(self):
		self.trial_times = cint32()
		self.skip = cint32()
		self.len_of_modes = cuint16()
		self.modes = []
		self.len_of_draw_floors = cuint16()
		self.draw_floors = []
		self.len_of_hangup_infos = cuint16()
		self.hangup_infos = []
		self.corps_lv = cint32()
		self.corps_soldier = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.trial_times.serialize(buff, buff_len)
		buff, buff_len = self.skip.serialize(buff, buff_len)
		buff, buff_len = self.len_of_modes.serialize(buff, buff_len)
		for i in range(self.len_of_modes.value):
			buff, buff_len = self.modes[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_draw_floors.serialize(buff, buff_len)
		for i in range(self.len_of_draw_floors.value):
			buff, buff_len = self.draw_floors[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_hangup_infos.serialize(buff, buff_len)
		for i in range(self.len_of_hangup_infos.value):
			buff, buff_len = self.hangup_infos[i].serialize(buff, buff_len)
		buff, buff_len = self.corps_lv.serialize(buff, buff_len)
		buff, buff_len = self.corps_soldier.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.trial_times.deserialize(buff)
		buff = self.skip.deserialize(buff)
		buff = self.len_of_modes.deserialize(buff)
		self.modes = []
		for i in range(self.len_of_modes.value):
			self.modes.append(tower_floor_info())
			buff = self.modes[i].deserialize(buff)
		buff = self.len_of_draw_floors.deserialize(buff)
		self.draw_floors = []
		for i in range(self.len_of_draw_floors.value):
			self.draw_floors.append(cint32())
			buff = self.draw_floors[i].deserialize(buff)
		buff = self.len_of_hangup_infos.deserialize(buff)
		self.hangup_infos = []
		for i in range(self.len_of_hangup_infos.value):
			self.hangup_infos.append(hangup_user_info())
			buff = self.hangup_infos[i].deserialize(buff)
		buff = self.corps_lv.deserialize(buff)
		buff = self.corps_soldier.deserialize(buff)
		return buff

	def add_modes():
		if len(modes) >= TOWER_DEGREE_MAX.value:
			return None
		modes.append(tower_floor_info())
		return modes[len(modes) - 1]

	def add_draw_floors():
		if len(draw_floors) >= MAX_TOWER_LEVEL.value:
			return None
		draw_floors.append(ccint32())
		return draw_floors[len(draw_floors) - 1]

	def add_hangup_infos():
		if len(hangup_infos) >= MAX_TOWER_LEVEL.value:
			return None
		hangup_infos.append(hangup_user_info())
		return hangup_infos[len(hangup_infos) - 1]

class exp_item_t(proto):
	def __init__(self):
		self.item_entry = cint32()
		self.item_num = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.item_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.item_entry.deserialize(buff)
		buff = self.item_num.deserialize(buff)
		return buff

class E_CHALLENGE_RESULT(enum):
	pass

class e_fight_win(E_CHALLENGE_RESULT):
	def __init__(self):
		self.value=0

class e_fight_lose(E_CHALLENGE_RESULT):
	def __init__(self):
		self.value=1

class TOWER_REPORT_DEGREE(enum):
	pass

class e_degree_first(TOWER_REPORT_DEGREE):
	def __init__(self):
		self.value=0

class e_degree_perferct(TOWER_REPORT_DEGREE):
	def __init__(self):
		self.value=1

class e_degree_revent(TOWER_REPORT_DEGREE):
	def __init__(self):
		self.value=2

class e_degree_self(TOWER_REPORT_DEGREE):
	def __init__(self):
		self.value=3

class tower_report(proto):
	def __init__(self):
		self.degree = TOWER_REPORT_DEGREE()
		self.report = brief_battle_record()
		self.lost = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.degree.serialize(buff, buff_len)
		buff, buff_len = self.report.serialize(buff, buff_len)
		buff, buff_len = self.lost.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.degree.deserialize(buff)
		buff = self.report.deserialize(buff)
		buff = self.lost.deserialize(buff)
		return buff

class match_formation(proto):
	def __init__(self):
		self.index = cint32()
		self.corps_key = corps_key_t()
		self.corps_level = cint32()
		self.hero_0 = cint32()
		self.hero_1 = cint32()
		self.hero_2 = cint32()
		self.troops_entry_0 = cint32()
		self.troops_num_0 = cint32()
		self.troops_entry_1 = cint32()
		self.troops_num_1 = cint32()
		self.troops_entry_2 = cint32()
		self.troops_num_2 = cint32()
		self.troops_entry_3 = cint32()
		self.troops_num_3 = cint32()
		self.troops_entry_4 = cint32()
		self.troops_num_4 = cint32()
		self.power = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.index.serialize(buff, buff_len)
		buff, buff_len = self.corps_key.serialize(buff, buff_len)
		buff, buff_len = self.corps_level.serialize(buff, buff_len)
		buff, buff_len = self.hero_0.serialize(buff, buff_len)
		buff, buff_len = self.hero_1.serialize(buff, buff_len)
		buff, buff_len = self.hero_2.serialize(buff, buff_len)
		buff, buff_len = self.troops_entry_0.serialize(buff, buff_len)
		buff, buff_len = self.troops_num_0.serialize(buff, buff_len)
		buff, buff_len = self.troops_entry_1.serialize(buff, buff_len)
		buff, buff_len = self.troops_num_1.serialize(buff, buff_len)
		buff, buff_len = self.troops_entry_2.serialize(buff, buff_len)
		buff, buff_len = self.troops_num_2.serialize(buff, buff_len)
		buff, buff_len = self.troops_entry_3.serialize(buff, buff_len)
		buff, buff_len = self.troops_num_3.serialize(buff, buff_len)
		buff, buff_len = self.troops_entry_4.serialize(buff, buff_len)
		buff, buff_len = self.troops_num_4.serialize(buff, buff_len)
		buff, buff_len = self.power.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.index.deserialize(buff)
		buff = self.corps_key.deserialize(buff)
		buff = self.corps_level.deserialize(buff)
		buff = self.hero_0.deserialize(buff)
		buff = self.hero_1.deserialize(buff)
		buff = self.hero_2.deserialize(buff)
		buff = self.troops_entry_0.deserialize(buff)
		buff = self.troops_num_0.deserialize(buff)
		buff = self.troops_entry_1.deserialize(buff)
		buff = self.troops_num_1.deserialize(buff)
		buff = self.troops_entry_2.deserialize(buff)
		buff = self.troops_num_2.deserialize(buff)
		buff = self.troops_entry_3.deserialize(buff)
		buff = self.troops_num_3.deserialize(buff)
		buff = self.troops_entry_4.deserialize(buff)
		buff = self.troops_num_4.deserialize(buff)
		buff = self.power.deserialize(buff)
		return buff

class match_user_brief_t(proto):
	def __init__(self):
		self.user = user_summary_data_t()
		self.rank = cint32()
		self.len_of_formation = cuint16()
		self.formation = []
		self.len_of_hero = cuint16()
		self.hero = []
		self.nick_name_entry = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.user.serialize(buff, buff_len)
		buff, buff_len = self.rank.serialize(buff, buff_len)
		buff, buff_len = self.len_of_formation.serialize(buff, buff_len)
		for i in range(self.len_of_formation.value):
			buff, buff_len = self.formation[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_hero.serialize(buff, buff_len)
		for i in range(self.len_of_hero.value):
			buff, buff_len = self.hero[i].serialize(buff, buff_len)
		buff, buff_len = self.nick_name_entry.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.user.deserialize(buff)
		buff = self.rank.deserialize(buff)
		buff = self.len_of_formation.deserialize(buff)
		self.formation = []
		for i in range(self.len_of_formation.value):
			self.formation.append(match_formation())
			buff = self.formation[i].deserialize(buff)
		buff = self.len_of_hero.deserialize(buff)
		self.hero = []
		for i in range(self.len_of_hero.value):
			self.hero.append(hero_brief_data())
			buff = self.hero[i].deserialize(buff)
		buff = self.nick_name_entry.deserialize(buff)
		return buff

	def add_formation():
		if len(formation) >= MAX_MATCH_DEF_CORPS_NUM.value:
			return None
		formation.append(match_formation())
		return formation[len(formation) - 1]

	def add_hero():
		if len(hero) >= MAX_MATCH_BATTLE_HERO_NUM.value:
			return None
		hero.append(hero_brief_data())
		return hero[len(hero) - 1]

class match_user_data_t(proto):
	def __init__(self):
		self.rank = cint32()
		self.free_times = cint32()
		self.buy_times = cint32()
		self.limit_time = cint32()
		self.time_line = cint32()
		self.deftime_line = cint32()
		self.atttime_line = cint32()
		self.enemytime_line = cint32()
		self.fighttime_line = cint32()
		self.len_of_formation_def = cuint16()
		self.formation_def = []
		self.len_of_hero_def = cuint16()
		self.hero_def = []
		self.len_of_formation_att = cuint16()
		self.formation_att = []
		self.len_of_hero_att = cuint16()
		self.hero_att = []
		self.len_of_enemy = cuint16()
		self.enemy = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.rank.serialize(buff, buff_len)
		buff, buff_len = self.free_times.serialize(buff, buff_len)
		buff, buff_len = self.buy_times.serialize(buff, buff_len)
		buff, buff_len = self.limit_time.serialize(buff, buff_len)
		buff, buff_len = self.time_line.serialize(buff, buff_len)
		buff, buff_len = self.deftime_line.serialize(buff, buff_len)
		buff, buff_len = self.atttime_line.serialize(buff, buff_len)
		buff, buff_len = self.enemytime_line.serialize(buff, buff_len)
		buff, buff_len = self.fighttime_line.serialize(buff, buff_len)
		buff, buff_len = self.len_of_formation_def.serialize(buff, buff_len)
		for i in range(self.len_of_formation_def.value):
			buff, buff_len = self.formation_def[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_hero_def.serialize(buff, buff_len)
		for i in range(self.len_of_hero_def.value):
			buff, buff_len = self.hero_def[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_formation_att.serialize(buff, buff_len)
		for i in range(self.len_of_formation_att.value):
			buff, buff_len = self.formation_att[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_hero_att.serialize(buff, buff_len)
		for i in range(self.len_of_hero_att.value):
			buff, buff_len = self.hero_att[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_enemy.serialize(buff, buff_len)
		for i in range(self.len_of_enemy.value):
			buff, buff_len = self.enemy[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.rank.deserialize(buff)
		buff = self.free_times.deserialize(buff)
		buff = self.buy_times.deserialize(buff)
		buff = self.limit_time.deserialize(buff)
		buff = self.time_line.deserialize(buff)
		buff = self.deftime_line.deserialize(buff)
		buff = self.atttime_line.deserialize(buff)
		buff = self.enemytime_line.deserialize(buff)
		buff = self.fighttime_line.deserialize(buff)
		buff = self.len_of_formation_def.deserialize(buff)
		self.formation_def = []
		for i in range(self.len_of_formation_def.value):
			self.formation_def.append(match_formation())
			buff = self.formation_def[i].deserialize(buff)
		buff = self.len_of_hero_def.deserialize(buff)
		self.hero_def = []
		for i in range(self.len_of_hero_def.value):
			self.hero_def.append(hero_brief_data())
			buff = self.hero_def[i].deserialize(buff)
		buff = self.len_of_formation_att.deserialize(buff)
		self.formation_att = []
		for i in range(self.len_of_formation_att.value):
			self.formation_att.append(match_formation())
			buff = self.formation_att[i].deserialize(buff)
		buff = self.len_of_hero_att.deserialize(buff)
		self.hero_att = []
		for i in range(self.len_of_hero_att.value):
			self.hero_att.append(hero_brief_data())
			buff = self.hero_att[i].deserialize(buff)
		buff = self.len_of_enemy.deserialize(buff)
		self.enemy = []
		for i in range(self.len_of_enemy.value):
			self.enemy.append(match_user_brief_t())
			buff = self.enemy[i].deserialize(buff)
		return buff

	def add_formation_def():
		if len(formation_def) >= MAX_MATCH_DEF_CORPS_NUM.value:
			return None
		formation_def.append(match_formation())
		return formation_def[len(formation_def) - 1]

	def add_hero_def():
		if len(hero_def) >= MAX_MATCH_BATTLE_HERO_NUM.value:
			return None
		hero_def.append(hero_brief_data())
		return hero_def[len(hero_def) - 1]

	def add_formation_att():
		if len(formation_att) >= MAX_MATCH_DEF_CORPS_NUM.value:
			return None
		formation_att.append(match_formation())
		return formation_att[len(formation_att) - 1]

	def add_hero_att():
		if len(hero_att) >= MAX_MATCH_BATTLE_HERO_NUM.value:
			return None
		hero_att.append(hero_brief_data())
		return hero_att[len(hero_att) - 1]

	def add_enemy():
		if len(enemy) >= MAX_MATCH_ENEMY_NUM.value:
			return None
		enemy.append(match_user_brief_t())
		return enemy[len(enemy) - 1]

class battle_side_data_t(proto):
	def __init__(self):
		self.len_of_hero_data_list = cuint16()
		self.hero_data_list = []
		self.len_of_troops_data_list = cuint16()
		self.troops_data_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.len_of_hero_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_hero_data_list.value):
			buff, buff_len = self.hero_data_list[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_troops_data_list.serialize(buff, buff_len)
		for i in range(self.len_of_troops_data_list.value):
			buff, buff_len = self.troops_data_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.len_of_hero_data_list.deserialize(buff)
		self.hero_data_list = []
		for i in range(self.len_of_hero_data_list.value):
			self.hero_data_list.append(hero_data_t())
			buff = self.hero_data_list[i].deserialize(buff)
		buff = self.len_of_troops_data_list.deserialize(buff)
		self.troops_data_list = []
		for i in range(self.len_of_troops_data_list.value):
			self.troops_data_list.append(troops_data_t())
			buff = self.troops_data_list[i].deserialize(buff)
		return buff

	def add_hero_data_list():
		if len(hero_data_list) >= MAX_CORPS_HERO_NUM.value:
			return None
		hero_data_list.append(hero_data_t())
		return hero_data_list[len(hero_data_list) - 1]

	def add_troops_data_list():
		if len(troops_data_list) >= MAX_CORPS_TROOPS_NUM.value:
			return None
		troops_data_list.append(troops_data_t())
		return troops_data_list[len(troops_data_list) - 1]

class laofan_hero_data_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.level = cint32()
		self.exp = cint32()
		self.star_lv = cint32()
		self.quality = E_HERO_QUALITY()
		self.quality_lv = cint32()
		self.equip_entry_0 = cint32()
		self.equip_strengthen_lv_0 = cint32()
		self.equip_entry_1 = cint32()
		self.equip_strengthen_lv_1 = cint32()
		self.equip_entry_2 = cint32()
		self.equip_strengthen_lv_2 = cint32()
		self.equip_entry_3 = cint32()
		self.equip_strengthen_lv_3 = cint32()
		self.equip_entry_4 = cint32()
		self.equip_strengthen_lv_4 = cint32()
		self.equip_entry_5 = cint32()
		self.equip_strengthen_lv_5 = cint32()
		self.skill_entry_0 = cint32()
		self.skill_entry_1 = cint32()
		self.skill_entry_2 = cint32()
		self.skill_lv_0 = cint32()
		self.skill_lv_1 = cint32()
		self.skill_lv_2 = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.level.serialize(buff, buff_len)
		buff, buff_len = self.exp.serialize(buff, buff_len)
		buff, buff_len = self.star_lv.serialize(buff, buff_len)
		buff, buff_len = self.quality.serialize(buff, buff_len)
		buff, buff_len = self.quality_lv.serialize(buff, buff_len)
		buff, buff_len = self.equip_entry_0.serialize(buff, buff_len)
		buff, buff_len = self.equip_strengthen_lv_0.serialize(buff, buff_len)
		buff, buff_len = self.equip_entry_1.serialize(buff, buff_len)
		buff, buff_len = self.equip_strengthen_lv_1.serialize(buff, buff_len)
		buff, buff_len = self.equip_entry_2.serialize(buff, buff_len)
		buff, buff_len = self.equip_strengthen_lv_2.serialize(buff, buff_len)
		buff, buff_len = self.equip_entry_3.serialize(buff, buff_len)
		buff, buff_len = self.equip_strengthen_lv_3.serialize(buff, buff_len)
		buff, buff_len = self.equip_entry_4.serialize(buff, buff_len)
		buff, buff_len = self.equip_strengthen_lv_4.serialize(buff, buff_len)
		buff, buff_len = self.equip_entry_5.serialize(buff, buff_len)
		buff, buff_len = self.equip_strengthen_lv_5.serialize(buff, buff_len)
		buff, buff_len = self.skill_entry_0.serialize(buff, buff_len)
		buff, buff_len = self.skill_entry_1.serialize(buff, buff_len)
		buff, buff_len = self.skill_entry_2.serialize(buff, buff_len)
		buff, buff_len = self.skill_lv_0.serialize(buff, buff_len)
		buff, buff_len = self.skill_lv_1.serialize(buff, buff_len)
		buff, buff_len = self.skill_lv_2.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.level.deserialize(buff)
		buff = self.exp.deserialize(buff)
		buff = self.star_lv.deserialize(buff)
		buff = self.quality.deserialize(buff)
		buff = self.quality_lv.deserialize(buff)
		buff = self.equip_entry_0.deserialize(buff)
		buff = self.equip_strengthen_lv_0.deserialize(buff)
		buff = self.equip_entry_1.deserialize(buff)
		buff = self.equip_strengthen_lv_1.deserialize(buff)
		buff = self.equip_entry_2.deserialize(buff)
		buff = self.equip_strengthen_lv_2.deserialize(buff)
		buff = self.equip_entry_3.deserialize(buff)
		buff = self.equip_strengthen_lv_3.deserialize(buff)
		buff = self.equip_entry_4.deserialize(buff)
		buff = self.equip_strengthen_lv_4.deserialize(buff)
		buff = self.equip_entry_5.deserialize(buff)
		buff = self.equip_strengthen_lv_5.deserialize(buff)
		buff = self.skill_entry_0.deserialize(buff)
		buff = self.skill_entry_1.deserialize(buff)
		buff = self.skill_entry_2.deserialize(buff)
		buff = self.skill_lv_0.deserialize(buff)
		buff = self.skill_lv_1.deserialize(buff)
		buff = self.skill_lv_2.deserialize(buff)
		return buff

class laofan_troops_data_t(proto):
	def __init__(self):
		self.soldier_entry = cint32()
		self.soldier_num = cint32()
		self.battle_pos = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.soldier_entry.serialize(buff, buff_len)
		buff, buff_len = self.soldier_num.serialize(buff, buff_len)
		buff, buff_len = self.battle_pos.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.soldier_entry.deserialize(buff)
		buff = self.soldier_num.deserialize(buff)
		buff = self.battle_pos.deserialize(buff)
		return buff

class equip_make_consume_item_t(proto):
	def __init__(self):
		self.item_entry = cint32()
		self.item_num = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.item_entry.serialize(buff, buff_len)
		buff, buff_len = self.item_num.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.item_entry.deserialize(buff)
		buff = self.item_num.deserialize(buff)
		return buff

class guild_command_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.idx = cint32()
		self.block_id = cint32()
		self.is_effect = cint32()
		self.time = cint32()
		self.create_time = cint32()
		self.mark = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.idx.serialize(buff, buff_len)
		buff, buff_len = self.block_id.serialize(buff, buff_len)
		buff, buff_len = self.is_effect.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		buff, buff_len = self.create_time.serialize(buff, buff_len)
		buff, buff_len = self.mark.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.idx.deserialize(buff)
		buff = self.block_id.deserialize(buff)
		buff = self.is_effect.deserialize(buff)
		buff = self.time.deserialize(buff)
		buff = self.create_time.deserialize(buff)
		buff = self.mark.deserialize(buff)
		return buff

class guild_command_data(proto):
	def __init__(self):
		self.len_of_command_list = cuint16()
		self.command_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.len_of_command_list.serialize(buff, buff_len)
		for i in range(self.len_of_command_list.value):
			buff, buff_len = self.command_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.len_of_command_list.deserialize(buff)
		self.command_list = []
		for i in range(self.len_of_command_list.value):
			self.command_list.append(guild_command_t())
			buff = self.command_list[i].deserialize(buff)
		return buff

	def add_command_list():
		if len(command_list) >= MAX_GUILD_COMMAND_NUM.value:
			return None
		command_list.append(guild_command_t())
		return command_list[len(command_list) - 1]

class SHARE_RECORD_TYPE(enum):
	pass

class e_share_record_type_world(SHARE_RECORD_TYPE):
	def __init__(self):
		self.value=1

class e_share_record_type_state(SHARE_RECORD_TYPE):
	def __init__(self):
		self.value=2

class e_share_record_type_guild(SHARE_RECORD_TYPE):
	def __init__(self):
		self.value=3

class e_share_record_type_group(SHARE_RECORD_TYPE):
	def __init__(self):
		self.value=4

class user_month_card_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.time = cint32()
		self.reward_times = cint32()
		self.total_times = cint32()
		self.b_pick = cbool()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		buff, buff_len = self.reward_times.serialize(buff, buff_len)
		buff, buff_len = self.total_times.serialize(buff, buff_len)
		buff, buff_len = self.b_pick.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.time.deserialize(buff)
		buff = self.reward_times.deserialize(buff)
		buff = self.total_times.deserialize(buff)
		buff = self.b_pick.deserialize(buff)
		return buff

class fame_task_t(proto):
	def __init__(self):
		self.chapter = cint32()
		self.has_reward = cbool()
		self.len_of_mission_list = cuint16()
		self.mission_list = []
		self.fame = cint32()
		self.len_of_fame_rewards = cuint16()
		self.fame_rewards = []
		self.len_of_finished_list = cuint16()
		self.finished_list = []

	def serialize(self, buff, buff_len):
		buff, buff_len = self.chapter.serialize(buff, buff_len)
		buff, buff_len = self.has_reward.serialize(buff, buff_len)
		buff, buff_len = self.len_of_mission_list.serialize(buff, buff_len)
		for i in range(self.len_of_mission_list.value):
			buff, buff_len = self.mission_list[i].serialize(buff, buff_len)
		buff, buff_len = self.fame.serialize(buff, buff_len)
		buff, buff_len = self.len_of_fame_rewards.serialize(buff, buff_len)
		for i in range(self.len_of_fame_rewards.value):
			buff, buff_len = self.fame_rewards[i].serialize(buff, buff_len)
		buff, buff_len = self.len_of_finished_list.serialize(buff, buff_len)
		for i in range(self.len_of_finished_list.value):
			buff, buff_len = self.finished_list[i].serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.chapter.deserialize(buff)
		buff = self.has_reward.deserialize(buff)
		buff = self.len_of_mission_list.deserialize(buff)
		self.mission_list = []
		for i in range(self.len_of_mission_list.value):
			self.mission_list.append(mission_t())
			buff = self.mission_list[i].deserialize(buff)
		buff = self.fame.deserialize(buff)
		buff = self.len_of_fame_rewards.deserialize(buff)
		self.fame_rewards = []
		for i in range(self.len_of_fame_rewards.value):
			self.fame_rewards.append(E_MISSION_STATUS())
			buff = self.fame_rewards[i].deserialize(buff)
		buff = self.len_of_finished_list.deserialize(buff)
		self.finished_list = []
		for i in range(self.len_of_finished_list.value):
			self.finished_list.append(cint32())
			buff = self.finished_list[i].deserialize(buff)
		return buff

	def add_mission_list():
		if len(mission_list) >= MAX_MISSION_NUM.value:
			return None
		mission_list.append(mission_t())
		return mission_list[len(mission_list) - 1]

	def add_fame_rewards():
		if len(fame_rewards) >= MAX_FAME_REAWRD_NUM.value:
			return None
		fame_rewards.append(E_MISSION_STATUS())
		return fame_rewards[len(fame_rewards) - 1]

	def add_finished_list():
		if len(finished_list) >= MAX_TOTAL_MISSION_NUM.value:
			return None
		finished_list.append(ccint32())
		return finished_list[len(finished_list) - 1]

class NPC_INFO_TYPE(enum):
	pass

class e_npc_info_invalid(NPC_INFO_TYPE):
	def __init__(self):
		self.value=-1

class e_npc_info_dialogue(NPC_INFO_TYPE):
	def __init__(self):
		self.value=1

class e_npc_info_liveness(NPC_INFO_TYPE):
	def __init__(self):
		self.value=2

class e_npc_info_exchange(NPC_INFO_TYPE):
	def __init__(self):
		self.value=3

class e_npc_info_shop(NPC_INFO_TYPE):
	def __init__(self):
		self.value=4

class E_NPC_LIVE_STATUS(enum):
	pass

class e_npc_live_invalid(E_NPC_LIVE_STATUS):
	def __init__(self):
		self.value=-1

class e_npc_live_open(E_NPC_LIVE_STATUS):
	def __init__(self):
		self.value=0

class e_npc_live_finish(E_NPC_LIVE_STATUS):
	def __init__(self):
		self.value=1

class e_npc_live_close(E_NPC_LIVE_STATUS):
	def __init__(self):
		self.value=2

class E_NPC_DIALOGUE_TYPE(enum):
	pass

class DIALOGUE_TYPE_NONE(E_NPC_DIALOGUE_TYPE):
	def __init__(self):
		self.value=-1

class DIALOGUE_TYPE_ONE(E_NPC_DIALOGUE_TYPE):
	def __init__(self):
		self.value=1

class DIALOGUE_TYPE_TWO(E_NPC_DIALOGUE_TYPE):
	def __init__(self):
		self.value=2

class DIALOGUE_TYPE_THREE(E_NPC_DIALOGUE_TYPE):
	def __init__(self):
		self.value=3

class DIALOGUE_TYPE_FOUR(E_NPC_DIALOGUE_TYPE):
	def __init__(self):
		self.value=4

class npc_info_t(proto):
	def __init__(self):
		self.group_id = cint32()
		self.type = NPC_INFO_TYPE()
		self.status = E_NPC_LIVE_STATUS()
		self.entry = cint32()
		self.end_time = cint32()
		self.next_time = cint32()
		self.parameter = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.group_id.serialize(buff, buff_len)
		buff, buff_len = self.type.serialize(buff, buff_len)
		buff, buff_len = self.status.serialize(buff, buff_len)
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.end_time.serialize(buff, buff_len)
		buff, buff_len = self.next_time.serialize(buff, buff_len)
		buff, buff_len = self.parameter.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.group_id.deserialize(buff)
		buff = self.type.deserialize(buff)
		buff = self.status.deserialize(buff)
		buff = self.entry.deserialize(buff)
		buff = self.end_time.deserialize(buff)
		buff = self.next_time.deserialize(buff)
		buff = self.parameter.deserialize(buff)
		return buff

class museum_group_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.e_group_status = E_MUSEUM_GROUP_STATUS()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.e_group_status.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.e_group_status.deserialize(buff)
		return buff

class user_event_flag_with_param(proto):
	def __init__(self):
		self.flag = cint32()
		self.param1 = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.flag.serialize(buff, buff_len)
		buff, buff_len = self.param1.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.flag.deserialize(buff)
		buff = self.param1.deserialize(buff)
		return buff

class discovery_event_type(enum):
	pass

class e_discovery_event_type_treasure(discovery_event_type):
	def __init__(self):
		self.value=0

class e_discovery_event_type_mine(discovery_event_type):
	def __init__(self):
		self.value=1

class e_discovery_event_type_trade(discovery_event_type):
	def __init__(self):
		self.value=2

class discovery_event_rate(enum):
	pass

class e_discovery_event_rate_white(discovery_event_rate):
	def __init__(self):
		self.value=0

class e_discovery_event_rate_green(discovery_event_rate):
	def __init__(self):
		self.value=1

class e_discovery_event_rate_blue(discovery_event_rate):
	def __init__(self):
		self.value=2

class e_discovery_event_rate_purple(discovery_event_rate):
	def __init__(self):
		self.value=3

class e_discovery_event_rate_orange(discovery_event_rate):
	def __init__(self):
		self.value=4

class user_discovery_t(proto):
	def __init__(self):
		self.level = cint32()
		self.map = cint32()
		self.discovery_times = cint32()
		self.rob_times = cint32()
		self.assist_times = cint32()
		self.dis_recover_time = cint32()
		self.discovery_buy_times = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.level.serialize(buff, buff_len)
		buff, buff_len = self.map.serialize(buff, buff_len)
		buff, buff_len = self.discovery_times.serialize(buff, buff_len)
		buff, buff_len = self.rob_times.serialize(buff, buff_len)
		buff, buff_len = self.assist_times.serialize(buff, buff_len)
		buff, buff_len = self.dis_recover_time.serialize(buff, buff_len)
		buff, buff_len = self.discovery_buy_times.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.level.deserialize(buff)
		buff = self.map.deserialize(buff)
		buff = self.discovery_times.deserialize(buff)
		buff = self.rob_times.deserialize(buff)
		buff = self.assist_times.deserialize(buff)
		buff = self.dis_recover_time.deserialize(buff)
		buff = self.discovery_buy_times.deserialize(buff)
		return buff

class user_seized_resource(proto):
	def __init__(self):
		self.event_id = cint64()
		self.resource_info = user_resource_t()
		self.resource_need = user_resource_t()
		self.user = user_summary_data_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.resource_info.serialize(buff, buff_len)
		buff, buff_len = self.resource_need.serialize(buff, buff_len)
		buff, buff_len = self.user.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.event_id.deserialize(buff)
		buff = self.resource_info.deserialize(buff)
		buff = self.resource_need.deserialize(buff)
		buff = self.user.deserialize(buff)
		return buff

class user_res_reap_data_t(proto):
	def __init__(self):
		self.reap_wood_tick_time = cint32()
		self.reap_stone_tick_time = cint32()
		self.reap_grain_tick_time = cint32()
		self.reap_iron_tick_time = cint32()
		self.res_add_data = user_resource_increase_t()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.reap_wood_tick_time.serialize(buff, buff_len)
		buff, buff_len = self.reap_stone_tick_time.serialize(buff, buff_len)
		buff, buff_len = self.reap_grain_tick_time.serialize(buff, buff_len)
		buff, buff_len = self.reap_iron_tick_time.serialize(buff, buff_len)
		buff, buff_len = self.res_add_data.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.reap_wood_tick_time.deserialize(buff)
		buff = self.reap_stone_tick_time.deserialize(buff)
		buff = self.reap_grain_tick_time.deserialize(buff)
		buff = self.reap_iron_tick_time.deserialize(buff)
		buff = self.res_add_data.deserialize(buff)
		return buff

class E_ADVENTURE_EVENT_TYPE(enum):
	pass

class e_adventure_event_type_sweep(E_ADVENTURE_EVENT_TYPE):
	def __init__(self):
		self.value=0

class e_adventure_event_type_reward(E_ADVENTURE_EVENT_TYPE):
	def __init__(self):
		self.value=1

class adventure_event(proto):
	def __init__(self):
		self.event_id = cint64()
		self.type = E_ADVENTURE_EVENT_TYPE()
		self.create_time = cint32()
		self.first = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.type.serialize(buff, buff_len)
		buff, buff_len = self.create_time.serialize(buff, buff_len)
		buff, buff_len = self.first.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.event_id.deserialize(buff)
		buff = self.type.deserialize(buff)
		buff = self.create_time.deserialize(buff)
		buff = self.first.deserialize(buff)
		return buff

class adventure_addtion_time_type(enum):
	pass

class addtion_type_quality(adventure_addtion_time_type):
	def __init__(self):
		self.value=0

class addtion_type_star(adventure_addtion_time_type):
	def __init__(self):
		self.value=1

class addtion_type_level(adventure_addtion_time_type):
	def __init__(self):
		self.value=2

class addtion_type_job(adventure_addtion_time_type):
	def __init__(self):
		self.value=3

class addtion_type_max(adventure_addtion_time_type):
	def __init__(self):
		self.value=4

class reserver_soldier_t(proto):
	def __init__(self):
		self.castle_id = cint64()
		self.num = cint32()
		self.time = cint32()
		self.day_buy_time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.castle_id.serialize(buff, buff_len)
		buff, buff_len = self.num.serialize(buff, buff_len)
		buff, buff_len = self.time.serialize(buff, buff_len)
		buff, buff_len = self.day_buy_time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.castle_id.deserialize(buff)
		buff = self.num.deserialize(buff)
		buff = self.time.deserialize(buff)
		buff = self.day_buy_time.deserialize(buff)
		return buff

class E_SOLDIER_TYPE(enum):
	pass

class e_soldier_infantry(E_SOLDIER_TYPE):
	def __init__(self):
		self.value=0

class e_soldier_cavalry(E_SOLDIER_TYPE):
	def __init__(self):
		self.value=1

class e_soldier_archer(E_SOLDIER_TYPE):
	def __init__(self):
		self.value=2

class raffle_data(proto):
	def __init__(self):
		self.raffle_id = cint64()
		self.start_time = cint32()
		self.next_free_time = cint32()
		self.free_times = cint32()
		self.halve_times = cint32()
		self.draw_total = cint32()
		self.surplus_lottery_hit_count = cint32()
		self.draw_today = cint32()
		self.draw_limit = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.raffle_id.serialize(buff, buff_len)
		buff, buff_len = self.start_time.serialize(buff, buff_len)
		buff, buff_len = self.next_free_time.serialize(buff, buff_len)
		buff, buff_len = self.free_times.serialize(buff, buff_len)
		buff, buff_len = self.halve_times.serialize(buff, buff_len)
		buff, buff_len = self.draw_total.serialize(buff, buff_len)
		buff, buff_len = self.surplus_lottery_hit_count.serialize(buff, buff_len)
		buff, buff_len = self.draw_today.serialize(buff, buff_len)
		buff, buff_len = self.draw_limit.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.raffle_id.deserialize(buff)
		buff = self.start_time.deserialize(buff)
		buff = self.next_free_time.deserialize(buff)
		buff = self.free_times.deserialize(buff)
		buff = self.halve_times.deserialize(buff)
		buff = self.draw_total.deserialize(buff)
		buff = self.surplus_lottery_hit_count.deserialize(buff)
		buff = self.draw_today.deserialize(buff)
		buff = self.draw_limit.deserialize(buff)
		return buff

class E_FUNC_UNLOCK_TYPE(enum):
	pass

class e_func_unlock_type_draw(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=0

class e_func_unlock_type_break(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=1

class e_func_unlock_type_upgrade(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=2

class e_func_unlock_type_spy(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=3

class e_func_unlock_type_smash(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=4

class e_func_unlock_type_guard(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=5

class e_func_unlock_type_seize(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=6

class e_func_unlock_type_discovery(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=7

class e_func_unlock_type_hall2(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=8

class e_func_unlock_type_hall3(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=9

class e_func_unlock_type_hall4(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=10

class e_func_unlock_type_storage(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=11

class e_func_unlock_type_fort(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=12

class e_func_unlock_type_vice_castle(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=13

class e_func_unlock_type_match(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=14

class e_func_unlock_type_tower(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=15

class e_func_unlock_type_blk_rebel(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=16

class e_func_unlock_type_blk_world_trend(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=17

class e_func_unlock_type_munitions_place(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=18

class e_func_unlock_type_hero_use_exp(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=19

class e_func_unlock_type_main_tips_list(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=20

class e_func_unlock_type_block_help(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=21

class e_func_unlock_type_military_camp(E_FUNC_UNLOCK_TYPE):
	def __init__(self):
		self.value=22

class E_FUNC_UNLOCK_CONDITION_TYPE(enum):
	pass

class e_func_unlock_type_condition_fiction(E_FUNC_UNLOCK_CONDITION_TYPE):
	def __init__(self):
		self.value=0

class e_func_unlock_type_condition_tech(E_FUNC_UNLOCK_CONDITION_TYPE):
	def __init__(self):
		self.value=1

class e_func_unlock_type_condition_building(E_FUNC_UNLOCK_CONDITION_TYPE):
	def __init__(self):
		self.value=2

class e_func_unlock_type_condition_fame(E_FUNC_UNLOCK_CONDITION_TYPE):
	def __init__(self):
		self.value=3

class e_func_unlock_type_condition_mission(E_FUNC_UNLOCK_CONDITION_TYPE):
	def __init__(self):
		self.value=4

class E_SUB_TYPE_LOTTERY(enum):
	pass

class e_sub_type_lottery_silver(E_SUB_TYPE_LOTTERY):
	def __init__(self):
		self.value=0

class e_sub_type_lottery_gold(E_SUB_TYPE_LOTTERY):
	def __init__(self):
		self.value=1

class e_sub_type_lottery_season(E_SUB_TYPE_LOTTERY):
	def __init__(self):
		self.value=2

class wt_quest_t(proto):
	def __init__(self):
		self.entry = cint32()
		self.status = cint32()
		self.parameter = cint64()
		self.level = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.entry.serialize(buff, buff_len)
		buff, buff_len = self.status.serialize(buff, buff_len)
		buff, buff_len = self.parameter.serialize(buff, buff_len)
		buff, buff_len = self.level.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.entry.deserialize(buff)
		buff = self.status.deserialize(buff)
		buff = self.parameter.deserialize(buff)
		buff = self.level.deserialize(buff)
		return buff

class wt_guild_rank_t(proto):
	def __init__(self):
		self.rank = cint32()
		self.name = cstring()
		self.parameter = cint32()
		self.region = cint32()
		self.guild_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.rank.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		buff, buff_len = self.parameter.serialize(buff, buff_len)
		buff, buff_len = self.region.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.rank.deserialize(buff)
		buff = self.name.deserialize(buff)
		buff = self.parameter.deserialize(buff)
		buff = self.region.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		return buff

class wt_user_rank_t(proto):
	def __init__(self):
		self.rank = cint32()
		self.name = cstring()
		self.parameter = cint32()
		self.guild_name = cstring()
		self.user_id = cint64()
		self.guild_id = cint64()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.rank.serialize(buff, buff_len)
		buff, buff_len = self.name.serialize(buff, buff_len)
		buff, buff_len = self.parameter.serialize(buff, buff_len)
		buff, buff_len = self.guild_name.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.rank.deserialize(buff)
		buff = self.name.deserialize(buff)
		buff = self.parameter.deserialize(buff)
		buff = self.guild_name.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		return buff

class user_rebel_data_t(proto):
	def __init__(self):
		self.search_times = cint32()
		self.max_id = cint32()
		self.recover_time = cint32()
		self.buy_times = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.search_times.serialize(buff, buff_len)
		buff, buff_len = self.max_id.serialize(buff, buff_len)
		buff, buff_len = self.recover_time.serialize(buff, buff_len)
		buff, buff_len = self.buy_times.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.search_times.deserialize(buff)
		buff = self.max_id.deserialize(buff)
		buff = self.recover_time.deserialize(buff)
		buff = self.buy_times.deserialize(buff)
		return buff

class E_SOLDIER_LEVEL(enum):
	pass

class e_soldier_level_1(E_SOLDIER_LEVEL):
	def __init__(self):
		self.value=1

class e_soldier_level_2(E_SOLDIER_LEVEL):
	def __init__(self):
		self.value=2

class e_soldier_level_3(E_SOLDIER_LEVEL):
	def __init__(self):
		self.value=3

class e_soldier_level_max(E_SOLDIER_LEVEL):
	def __init__(self):
		self.value=4

class guild_crusade_t(proto):
	def __init__(self):
		self.guild_data = guild_brief_t()
		self.dam = cuint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.guild_data.serialize(buff, buff_len)
		buff, buff_len = self.dam.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.guild_data.deserialize(buff)
		buff = self.dam.deserialize(buff)
		return buff

class guild_assist_event_t(proto):
	def __init__(self):
		self.event_id = cint64()
		self.user_id = cint64()
		self.nick_name = cstring()
		self.head_entry = cint32()
		self.build_id = cint32()
		self.build_lv = cint32()
		self.total_times = cint32()
		self.cur_times = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.event_id.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		buff, buff_len = self.head_entry.serialize(buff, buff_len)
		buff, buff_len = self.build_id.serialize(buff, buff_len)
		buff, buff_len = self.build_lv.serialize(buff, buff_len)
		buff, buff_len = self.total_times.serialize(buff, buff_len)
		buff, buff_len = self.cur_times.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.event_id.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		buff = self.head_entry.deserialize(buff)
		buff = self.build_id.deserialize(buff)
		buff = self.build_lv.deserialize(buff)
		buff = self.total_times.deserialize(buff)
		buff = self.cur_times.deserialize(buff)
		return buff

class guild_gift_item(proto):
	def __init__(self):
		self.ID = cint64()
		self.user_id = cint64()
		self.nick_name = cstring()
		self.box_id = cint32()
		self.start_time = cint32()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.ID.serialize(buff, buff_len)
		buff, buff_len = self.user_id.serialize(buff, buff_len)
		buff, buff_len = self.nick_name.serialize(buff, buff_len)
		buff, buff_len = self.box_id.serialize(buff, buff_len)
		buff, buff_len = self.start_time.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.ID.deserialize(buff)
		buff = self.user_id.deserialize(buff)
		buff = self.nick_name.deserialize(buff)
		buff = self.box_id.deserialize(buff)
		buff = self.start_time.deserialize(buff)
		return buff

class map_color(proto):
	def __init__(self):
		self.county_id = cint32()
		self.guild_id = cint64()
		self.flag_id = cint32()
		self.guild_name = cstring()
		self.color = cstring()

	def serialize(self, buff, buff_len):
		buff, buff_len = self.county_id.serialize(buff, buff_len)
		buff, buff_len = self.guild_id.serialize(buff, buff_len)
		buff, buff_len = self.flag_id.serialize(buff, buff_len)
		buff, buff_len = self.guild_name.serialize(buff, buff_len)
		buff, buff_len = self.color.serialize(buff, buff_len)
		return buff, buff_len

	def deserialize(self, buff):
		buff = self.county_id.deserialize(buff)
		buff = self.guild_id.deserialize(buff)
		buff = self.flag_id.deserialize(buff)
		buff = self.guild_name.deserialize(buff)
		buff = self.color.deserialize(buff)
		return buff

class E_HEAD_TYPE(enum):
	pass

class e_head_invalid(E_HEAD_TYPE):
	def __init__(self):
		self.value=-1

class e_head_game(E_HEAD_TYPE):
	def __init__(self):
		self.value=0

class e_head_museum(E_HEAD_TYPE):
	def __init__(self):
		self.value=1

class e_head_sns(E_HEAD_TYPE):
	def __init__(self):
		self.value=2

