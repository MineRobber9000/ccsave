import ccsave.customenum as enum

class Preferences(enum.Enum):
	def __init__(self):
		super(Preferences, self).__init__()
		self.define("particles")
		self.define("popup_numbers")
		self.define("pref_2")
		self.define("pref_3")
		self.define("pref_4")
		self.define("fancy_graphics")
		self.define("pref_6")
		self.define("pref_7")
		self.define("pref_8")
		self.define("pref_9")
		self.define("pref_10")
		self.define("pref_11")
		self.define("pref_12")
		self.define("css_filters")
		self.define("pref_14")
		self.define("pref_15")
		self.define("pref_16")
class Upgrades(enum.Enum):
	def __init__(self):
		super(Upgrades,self).__init__()
class Achievements(enum.Enum):
	def __init__(self):
		super(Achievements,self).__init__()
		self.define('wake_and_bake')
		self.define('making_some_dough')
		self.define('so_baked_right_now')
		self.define('fledgling_bakery')
		self.define('affluent_bakery')
		self.define('world_famous_bakery')
		self.define('cosmic_bakery')
		self.define('galactic_bakery')
		self.define('universal_bakery')
		self.define('timeless_bakery')
		self.define('infinite_bakery')
		self.define('immortal_bakery')
		self.define('you_can_stop_now')
		self.define('cookies_all_the_way_down')
		self.define('overdose')
		self.define('how?')
		self.define('casual_baking')
		self.define('hardcore_baking')
		self.define('steady_tasty_stream')
		self.define('cookie_monster')
		self.define('mass_producer')
		self.define('cookie_vortex')
		self.define('cookie_pulsar')
		self.define('cookie_quasar')
		self.define('a_world_filled_with_cookies')
		self.define('lets_never_bake_again')
		self.define('sacrifice')
		self.define('oblivion')
		self.define('from_scratch')
		self.define('neverclick')
		self.define('clicktastic')
		self.define('clickathlon')
		self.define('clickolympics')
		self.define('clickorama')
		self.define('click')
		self.define('double_click')
		self.define('mouse_wheel')
		self.define('of_mice_and_men')
		self.define('the_digital')
		self.define('just_wrong')
		self.define('grandmas_cookies')
		self.define('sloppy_kisses')
		self.define('retirement_home')
		self.define('my_first_farm')
		self.define('reap_what_you_sow')
		self.define('farm_ill')
		self.define('production_chain')
		self.define('industrial_revolution')
		self.define('global_warming')
		self.define('you_know_the_drill')
		self.define('excavation_site')
		self.define('hollow_the_planet')
		self.define('expedition')
		self.define('galactic_highway')
		self.define('far_far_away')
		self.define('transmutation')
		self.define('transmogrification')
		self.define('gold_member')
		self.define('a_whole_new_world')
		self.define('now_youre_thinking')
		self.define('dimensional_shift')
		self.define('time_warp')
		self.define('alternate_timeline')
		self.define('rewriting_history')
		self.define('one_with_everything')
		self.define('mathematician')
		self.define('base_10')
		self.define('golden_cookie')
		self.define('lucky_cookie')
		self.define('a_stroke_of_luck')
		self.define('cheated_cookies_taste_awful')
		self.define('uncanny_clicker')
		self.define('builder')
		self.define('architect')
		self.define('enhancer')
		self.define('augmenter')
		self.define('cookie_dunker')
		self.define('fortune')
		self.define('true_neverclick')
		self.define('elder_nap')
		self.define('elder_slumber')
		self.define('elder')
		self.define('elder_calm')
		self.define('engineer')
		self.define('leprechaun')
		self.define('black_cats_paw')
		self.define('nihilism')
		self.define('antibatter')
		self.define('quirky_quarks')
		self.define('it_does_matter!')
		self.define('upgrader')
		self.define('centennial')
		self.define('hardcore')
		self.define('speed_baking_i')
		self.define('speed_baking_ii')
		self.define('speed_baking_iii')
		self.define('getting_even_with_the_oven')
		self.define('now_this_is_pod_smashing')
		self.define('chirped_out')
		self.define('follow_the_white_rabbit')
		self.define('clickasmic')
		self.define('friend_of_the_ancients')
		self.define('ruler_of_the_ancients')
		self.define('wholesome')
		self.define('just_plain_lucky')
		self.define('itchscratcher')
		self.define('wrinklesquisher')
		self.define('moistburster')
		self.define('spooky_cookies')
		self.define('coming_to_town')
		self.define('all_hail_santa')
		self.define('let_it_snow')
		self.define('oh_deer')
		self.define('sleigh_of_hand')
		self.define('reindeer_sleigher')
		self.define('perfect_agriculture')
		self.define('ultimate_automation')
		self.define('can_you_dig_it')
		self.define('type_ii_civilization')
		self.define('gild_wars')
		self.define('brain_split')
		self.define('time_duke')
		self.define('molecular_maestro')
		self.define('lone_photon')
		self.define('dazzling_glimmer')
		self.define('blinding_flash')
		self.define('unending_glow')
		self.define('lord_of_constructs')
		self.define('lord_of_progress')
		self.define('bicentannial')
		self.define('lovely_cookies')
		self.define('centennial_and_a_half')
		self.define('tiny_cookie')
		self.define('you_win_a_cookie')
		self.define('click_delegator')
		self.define('gushing_grannies')
		self.define('i_hate_manure')
		self.define('the_incredible_machine')
		self.define('never_dig_down')
		self.define('and_beyond')
		self.define('magnus_opus')
		self.define('with_starange_eons')
		self.define('spacetime_jigamaroo')
		self.define('supermassive')
		self.define('praise_the_sun')
		self.define('clickageddon')
		self.define('clicknarok')
		self.define('extreme_polydactyly')
		self.define('dr._t')
		self.define('the_old_never_bothered_me_anyway')
		self.define('homegrown')
		self.define('technocracy')
		self.define('the_center_of_the_earth')
		self.define('we_come_in_peace')
		self.define('the_secrets_of_the_universe')
		self.define('realm_of_the_mad_god')
		self.define('forever_and_ever')
		self.define('walk_the_planck')
		self.define('rise_and_shine')
		self.define('god_complex')
		self.define('third_party')
		self.define('dematerialise')
		self.define('nil_zero_zilch')
		self.define('transcendence')
		self.define('obliterate')
		self.define('negative_void')
		self.define('the_hunt_is_on')
		self.define('egging_on')
		self.define('mass_easteria')
		self.define('hide_and_seek_champion')
		self.define('whats_in_a_name')
		self.define('pretty_penny')
		self.define('fit_the_bill')
		self.define('a_loan_in_the_dark')
		self.define('need_for_greed')
		self.define('its_the_economy_stupid')
		self.define('your_time_to_shrine')
		self.define('shady_sect')
		self.define('new_age_cult')
		self.define('organised_religion')
		self.define('fanaticism')
