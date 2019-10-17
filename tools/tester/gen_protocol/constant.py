from basetype import *
class ConstantDefine(enum):
	pass

class MT_MajorVer(ConstantDefine):
	def __init__(self):
		self.value=0

class MT_ProtoVer(ConstantDefine):
	def __init__(self):
		self.value=0

class MT_MinorVer(ConstantDefine):
	def __init__(self):
		self.value=0

class MT_ReserVer(ConstantDefine):
	def __init__(self):
		self.value=0

class TIME_OF_NEW_DAY(ConstantDefine):
	def __init__(self):
		self.value=0

class CITY_CIRCLE(ConstantDefine):
	def __init__(self):
		self.value=1

class MAX_CASTLE_AREA_COORD(ConstantDefine):
	def __init__(self):
		self.value=6

class MAX_OWN_LAND_NUM(ConstantDefine):
	def __init__(self):
		self.value=300

class MAX_GET_LAND_NUM(ConstantDefine):
	def __init__(self):
		self.value=300

class MAX_MAP_CITY_NUM(ConstantDefine):
	def __init__(self):
		self.value=500

class MAX_BUILDING_COUNT(ConstantDefine):
	def __init__(self):
		self.value=200

class MAX_CORPS_TROOPS_NUM(ConstantDefine):
	def __init__(self):
		self.value=3

class MAX_HERO_COUNT(ConstantDefine):
	def __init__(self):
		self.value=255

class MAX_CORPS_COUNT(ConstantDefine):
	def __init__(self):
		self.value=50

class MAX_GAME_EVENT_NUM(ConstantDefine):
	def __init__(self):
		self.value=20

class MAX_GAME_EVENT_RESULT_NUM(ConstantDefine):
	def __init__(self):
		self.value=20

class MAX_BATTLE_RESULT_NUM(ConstantDefine):
	def __init__(self):
		self.value=20

class GM_COMMAND_COUNT(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_CASTLE_NUM(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_CASTLE_CORPS_NUM(ConstantDefine):
	def __init__(self):
		self.value=5

class MAX_GAME_CHUNK_NUM(ConstantDefine):
	def __init__(self):
		self.value=1000

class MAX_GET_ITEM_NUM(ConstantDefine):
	def __init__(self):
		self.value=1000

class MAX_CHANGE_ITEM_NUM(ConstantDefine):
	def __init__(self):
		self.value=999

class MAX_EQUIP_MEDAL_NUM(ConstantDefine):
	def __init__(self):
		self.value=4

class MAX_FORT_CORPS_NUM(ConstantDefine):
	def __init__(self):
		self.value=5

class MAX_FORT_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_STORAGE_NUM(ConstantDefine):
	def __init__(self):
		self.value=50

class MAX_TRAP_COUNT(ConstantDefine):
	def __init__(self):
		self.value=20

class MAX_BLOCK_USER_NUM(ConstantDefine):
	def __init__(self):
		self.value=300

class MAX_BLOCK_GUARD_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_BATTLE_RECORD_NUM(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_ARENA_RECORD_NUM(ConstantDefine):
	def __init__(self):
		self.value=12

class MAX_READ_BATTLE_RECORD_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_BATTLE_RECORD_ACTOR_LEN(ConstantDefine):
	def __init__(self):
		self.value=2

class MAX_ROUND(ConstantDefine):
	def __init__(self):
		self.value=8

class MAX_RECORE_ROUND(ConstantDefine):
	def __init__(self):
		self.value=9

class MAX_ROUND_PACKET_NUM(ConstantDefine):
	def __init__(self):
		self.value=150

class MAX_SUB_PACKET_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_INVADER_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_LAND_LEVEL(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_STATE_NUM(ConstantDefine):
	def __init__(self):
		self.value=10

class BLOCK_DISTANCE(ConstantDefine):
	def __init__(self):
		self.value=17

class MAX_HERO_SKILL_NUM(ConstantDefine):
	def __init__(self):
		self.value=3

class SOLDIER_ATK_CONST(ConstantDefine):
	def __init__(self):
		self.value=5000

class SOLDIER_DEF_CONST(ConstantDefine):
	def __init__(self):
		self.value=5000

class SOLDIER_SPEED_CONST(ConstantDefine):
	def __init__(self):
		self.value=3000

class ATK_INCOME_CONST(ConstantDefine):
	def __init__(self):
		self.value=100

class DEF_INCOME_CONST(ConstantDefine):
	def __init__(self):
		self.value=70

class ATK_THRESHOLD(ConstantDefine):
	def __init__(self):
		self.value=300

class DEF_THRESHOLD(ConstantDefine):
	def __init__(self):
		self.value=-100

class HERO_LILIANG_INCOME_CONST(ConstantDefine):
	def __init__(self):
		self.value=50

class HERO_NAILI_INCOME_CONST(ConstantDefine):
	def __init__(self):
		self.value=50

class HERO_ATK_DMG_THRESHOLD(ConstantDefine):
	def __init__(self):
		self.value=3000

class HERO_SUB_SKILL_CONST(ConstantDefine):
	def __init__(self):
		self.value=1000

class HERO_SKILL_DMG_THRESHOLD(ConstantDefine):
	def __init__(self):
		self.value=3000

class SKILL_DMG_CONST(ConstantDefine):
	def __init__(self):
		self.value=45

class SKILL_HEAL_CONST(ConstantDefine):
	def __init__(self):
		self.value=40

class BATTLE_DMG_WAVE_PCT(ConstantDefine):
	def __init__(self):
		self.value=1000

class RECOVER_WOUNDER_PCT(ConstantDefine):
	def __init__(self):
		self.value=10000

class TROOPS_EFFECT_DMG_PCT(ConstantDefine):
	def __init__(self):
		self.value=5000

class CORPS_EFFECT_DMG_PCT(ConstantDefine):
	def __init__(self):
		self.value=5000

class HALL_ENTRY(ConstantDefine):
	def __init__(self):
		self.value=0

class STORAGE_ENTRY(ConstantDefine):
	def __init__(self):
		self.value=2

class MAX_GUILD_NUM(ConstantDefine):
	def __init__(self):
		self.value=1000

class MAX_GUILD_MEMBER(ConstantDefine):
	def __init__(self):
		self.value=500

class MAX_GUILD_INVITATION(ConstantDefine):
	def __init__(self):
		self.value=30

class MAX_GUILD_APPLICATION(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_USER_APPLICATION(ConstantDefine):
	def __init__(self):
		self.value=20

class MAX_GUILD_MARK(ConstantDefine):
	def __init__(self):
		self.value=20

class MAX_GUILD_LIST(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_GUILD_RELATIONSHIP(ConstantDefine):
	def __init__(self):
		self.value=50

class MAX_FREEMAN_LIST(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_GUILDLOG_PARAM_NUM(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_GUILDLOG_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_GUILD_CITY_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_GUILD_COMMAND_NUM(ConstantDefine):
	def __init__(self):
		self.value=30

class MAX_USER_MARK(ConstantDefine):
	def __init__(self):
		self.value=1

class MAX_BLOCK_MARK(ConstantDefine):
	def __init__(self):
		self.value=200

class MAX_BLOCK_USER_MARK(ConstantDefine):
	def __init__(self):
		self.value=1

class MAX_GUILD_GIFT_LIST_NUM(ConstantDefine):
	def __init__(self):
		self.value=300

class MAX_RESOURCE_NUM(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_MISSION_NUM(ConstantDefine):
	def __init__(self):
		self.value=500

class MAX_TOTAL_MISSION_NUM(ConstantDefine):
	def __init__(self):
		self.value=500

class MAX_ACHIEVEMENT_NUM(ConstantDefine):
	def __init__(self):
		self.value=200

class MAX_WORLD_TREND_NUM(ConstantDefine):
	def __init__(self):
		self.value=25

class MAX_STATE_ACHI_NUM(ConstantDefine):
	def __init__(self):
		self.value=50

class MAX_SHOP_BUY_ITEM(ConstantDefine):
	def __init__(self):
		self.value=1

class MAX_SHOP_ITEM_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_HERO_EQUIP_SLOT_STRENGTHEN_ITEM_NUM(ConstantDefine):
	def __init__(self):
		self.value=2

class MAX_EQUIP_COMBINE_ITEM_NUM(ConstantDefine):
	def __init__(self):
		self.value=2

class MAX_EQUIP_RESOLVE_ITEM_NUM(ConstantDefine):
	def __init__(self):
		self.value=2

class MAX_LOTTERY_ITEM_LIST_NUM(ConstantDefine):
	def __init__(self):
		self.value=5

class MAX_LOTTERY_POOL_ENTRY_NUM(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_LOTTERY_POOL_ITEM_NUM(ConstantDefine):
	def __init__(self):
		self.value=5

class LOTTERY_DRAW_B(ConstantDefine):
	def __init__(self):
		self.value=5

class LOTTERY_DRAW_K(ConstantDefine):
	def __init__(self):
		self.value=5

class LOTTERY_RESET_B(ConstantDefine):
	def __init__(self):
		self.value=300

class LOTTERY_RESET_K(ConstantDefine):
	def __init__(self):
		self.value=0

class SILVER_COIN_ONCE_CONSUME(ConstantDefine):
	def __init__(self):
		self.value=1000

class MAX_NOTICE_NUM(ConstantDefine):
	def __init__(self):
		self.value=180

class MAX_SIGNATURE_NUM(ConstantDefine):
	def __init__(self):
		self.value=128

class MAX_NICK_NAME_NUM(ConstantDefine):
	def __init__(self):
		self.value=12

class MAX_GUILD_NAME_NUM(ConstantDefine):
	def __init__(self):
		self.value=12

class MAX_CHAT_CHANNEL_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_GUILD_GROUP(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_GUILD_GROUP_MEMBER(ConstantDefine):
	def __init__(self):
		self.value=50

class MAX_SIGN_DAY(ConstantDefine):
	def __init__(self):
		self.value=28

class MAX_ACTIVE_OPEN(ConstantDefine):
	def __init__(self):
		self.value=20

class MAX_ACTIVE_DAY(ConstantDefine):
	def __init__(self):
		self.value=200

class MAX_ACTIVITY_CACHE_NUM(ConstantDefine):
	def __init__(self):
		self.value=500

class MAX_WAR_RANK(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_GUILD_RANK(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_FORCE_RANK(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_INVEST_REFUND_DAY(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_CHAT_MSG_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_CHAT_CHANNEL_MEMBER_NUM(ConstantDefine):
	def __init__(self):
		self.value=500

class MAX_LIVENESS_TYPE(ConstantDefine):
	def __init__(self):
		self.value=20

class MAX_LIVENESS_REWARD_NUM(ConstantDefine):
	def __init__(self):
		self.value=6

class MAX_MAIL_SEND_NUM(ConstantDefine):
	def __init__(self):
		self.value=500

class MAX_MAIL_COUNT(ConstantDefine):
	def __init__(self):
		self.value=500

class MAX_MAIL_AFFIX_COUNT(ConstantDefine):
	def __init__(self):
		self.value=5

class MAX_MAIL_TITLE_LEN(ConstantDefine):
	def __init__(self):
		self.value=128

class MAX_MAIL_CONTENT_LEN(ConstantDefine):
	def __init__(self):
		self.value=1024

class MAX_CHAT_CHANNEL_NAME_NUM(ConstantDefine):
	def __init__(self):
		self.value=13

class MAX_CITY_RANK_MEMBER(ConstantDefine):
	def __init__(self):
		self.value=3

class MAX_USER_FLAG_NUM(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_RECORD_PK_RANK(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_SYS_INFO_LEN(ConstantDefine):
	def __init__(self):
		self.value=1024

class MAX_WORLD_CITY_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_STATE_CITY_NUM(ConstantDefine):
	def __init__(self):
		self.value=5

class MAX_ALARM_RANGE(ConstantDefine):
	def __init__(self):
		self.value=3

class MAX_VIP_LV(ConstantDefine):
	def __init__(self):
		self.value=64

class MAX_REWARD_HERO_DATA(ConstantDefine):
	def __init__(self):
		self.value=1

class MAX_BLOCK_LEVEL(ConstantDefine):
	def __init__(self):
		self.value=9

class FIRST_GOLD_LOTTERY_DROP_ENTRY(ConstantDefine):
	def __init__(self):
		self.value=100

class FIRST_SILVER_LOTTERY_DROP_ENTRY(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_SKILL_LIST(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_LOTTERY_REWARD_NUM(ConstantDefine):
	def __init__(self):
		self.value=20

class MAX_PRESENT_ITEM(ConstantDefine):
	def __init__(self):
		self.value=1

class MAX_TECH_COUNT(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_ADDITION_COUNT(ConstantDefine):
	def __init__(self):
		self.value=200

class MAX_USER_FORCE_RANK(ConstantDefine):
	def __init__(self):
		self.value=1000

class MAX_HANGUP_BUILDING(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_HANGUP_SLOT(ConstantDefine):
	def __init__(self):
		self.value=5

class MAX_SHOP_KINDS(ConstantDefine):
	def __init__(self):
		self.value=60

class MAX_ARENA_CORPS_NUM(ConstantDefine):
	def __init__(self):
		self.value=3

class MAX_ARENA_HERO_NUM(ConstantDefine):
	def __init__(self):
		self.value=3

class MAX_ARENA_RANK_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_ARENA_BATTLE_HERO_NUM(ConstantDefine):
	def __init__(self):
		self.value=9

class MAX_MATCH_DEF_CORPS_NUM(ConstantDefine):
	def __init__(self):
		self.value=1

class MAX_MATCH_BATTLE_HERO_NUM(ConstantDefine):
	def __init__(self):
		self.value=3

class MAX_MATCH_ENEMY_NUM(ConstantDefine):
	def __init__(self):
		self.value=3

class MAX_MATCH_RANK_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class TOTAL_MATCH_RANK_NUM(ConstantDefine):
	def __init__(self):
		self.value=10000

class MATCH_CROPS_DEF_INDEX(ConstantDefine):
	def __init__(self):
		self.value=0

class MATCH_CROPS_ATT_INDEX(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_CORPS_HERO_NUM(ConstantDefine):
	def __init__(self):
		self.value=3

class MAX_LIVENESS_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_TOWER_LEVEL(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_TOWER_CORPS_NUM(ConstantDefine):
	def __init__(self):
		self.value=3

class MAX_TOWER_HERO_NUM(ConstantDefine):
	def __init__(self):
		self.value=3

class TOWER_FREE_TRIVAL_TIMES(ConstantDefine):
	def __init__(self):
		self.value=3

class TOWER_DEGREE_MAX(ConstantDefine):
	def __init__(self):
		self.value=3

class TOWER_REPORT_NUMS(ConstantDefine):
	def __init__(self):
		self.value=13

class TOWER_SELF_REPORT_NUMS(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_USE_EXP_ITEM_TYPE_NUM(ConstantDefine):
	def __init__(self):
		self.value=5

class MAX_NEW_FOR_ZHAOYU(ConstantDefine):
	def __init__(self):
		self.value=128

class MAX_ACTIVE_CODE_LEN(ConstantDefine):
	def __init__(self):
		self.value=16

class MAX_SINGLE_GIFT_COUNT(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_GIFT_RETRY_COUNT(ConstantDefine):
	def __init__(self):
		self.value=5

class GIFT_DISCARD_RETRY_COUNT(ConstantDefine):
	def __init__(self):
		self.value=15

class MAX_EQUIP_MAKE_ITEM_TYPE_NUM(ConstantDefine):
	def __init__(self):
		self.value=1

class MAX_TOWER_RANK_NUM(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_ADVISE_NUM(ConstantDefine):
	def __init__(self):
		self.value=20

class MAX_TOTAL_GUILD_QUEST_NUM(ConstantDefine):
	def __init__(self):
		self.value=256

class MAX_SOLDIER_TYPE(ConstantDefine):
	def __init__(self):
		self.value=3

class MAX_FUND_REWARD_ITEM(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_HERO_COMBINE_NUM(ConstantDefine):
	def __init__(self):
		self.value=1

class MAX_ADDITION_EFFECT_NUM(ConstantDefine):
	def __init__(self):
		self.value=20

class MAX_SHOP_TYPE(ConstantDefine):
	def __init__(self):
		self.value=5

class MAX_HANG_UP_DROP_NUM(ConstantDefine):
	def __init__(self):
		self.value=8

class MAX_FAME_REAWRD_NUM(ConstantDefine):
	def __init__(self):
		self.value=20

class MAX_NPC_DLG_GROUP_NUM(ConstantDefine):
	def __init__(self):
		self.value=20

class MAX_OPEN_NPC_DLG_REWARD_NUM(ConstantDefine):
	def __init__(self):
		self.value=1

class MAX_GET_MUSEUM_COLLECTION_NUM(ConstantDefine):
	def __init__(self):
		self.value=1000

class MAX_GET_MUSEUM_GROUP_NUM(ConstantDefine):
	def __init__(self):
		self.value=300

class MAX_DISCOVERY_EVENT(ConstantDefine):
	def __init__(self):
		self.value=20

class MAX_DISCOVERY_SEARCH_RANGE(ConstantDefine):
	def __init__(self):
		self.value=3

class MAX_GUILD_ASSIST_RESOURCE_PER_PAGE(ConstantDefine):
	def __init__(self):
		self.value=6

class MAX_ADVENTURE_EVENT_NUM(ConstantDefine):
	def __init__(self):
		self.value=6

class RESERVER_SOLDIER_PRODUCE_TIME(ConstantDefine):
	def __init__(self):
		self.value=5

class RESERVER_SOLDIER_PRODUCE_HOUR_TIMES(ConstantDefine):
	def __init__(self):
		self.value=12

class MAX_RAFFLE_EVENT_NUM(ConstantDefine):
	def __init__(self):
		self.value=60

class MAX_RAFFLE_REWARD_NUM(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_HERO_CHIP_OPER_ITEM(ConstantDefine):
	def __init__(self):
		self.value=3

class MAX_USER_MONTH_CARD(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_MIN_MAP_NUM(ConstantDefine):
	def __init__(self):
		self.value=800

class MAX_TIMES_SUPER_GIFT(ConstantDefine):
	def __init__(self):
		self.value=20

class SILVER_COIN_ONCE_CONSUME_DRAW_TICKET(ConstantDefine):
	def __init__(self):
		self.value=1

class MAX_TOTAL_WT_QUEST_NUM(ConstantDefine):
	def __init__(self):
		self.value=50

class MAX_WT_GROUP_QUEST_NUM(ConstantDefine):
	def __init__(self):
		self.value=10

class MAX_WT_RANK_NUM(ConstantDefine):
	def __init__(self):
		self.value=50

class WT_RANK_MAIL_REWARD_TITLE(ConstantDefine):
	def __init__(self):
		self.value=100032

class WT_GUILD_RANK_MAIL_REWARD_CONTENT(ConstantDefine):
	def __init__(self):
		self.value=100033

class WT_USER_RANK_MAIL_REWARD_CONTENT(ConstantDefine):
	def __init__(self):
		self.value=100034

class MAX_CRUSADE_GUILD_RANK(ConstantDefine):
	def __init__(self):
		self.value=100

class MAX_SERVER_ACTIVITY_NUM(ConstantDefine):
	def __init__(self):
		self.value=30

class MAX_ASSIST_NUM(ConstantDefine):
	def __init__(self):
		self.value=800

class MAX_USER_TIME_LIMIT(ConstantDefine):
	def __init__(self):
		self.value=50

class MAX_COUNTY_NUM(ConstantDefine):
	def __init__(self):
		self.value=43

class MAX_LUCKY_TREASURE(ConstantDefine):
	def __init__(self):
		self.value=10

