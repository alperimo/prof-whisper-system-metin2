#Prof Whisper System, V.1.4
#by Fatihbab34™
import uiScriptLocale
import chr
import app
import localeInfo

ROOT = "d:/ymir work/ui/public/"

window = {
	"name" : "WhisperDialog",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 450,
	"height" : 280,

	"children" :
	(
		{
			"name" : "board",
			"type" : "thinboard",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 600,
			"height" : 280,

			"children" :
			(
				## Title
				{
					"name" : "name_slot",
					"type" : "image",
					"style" : ("attach",),

					"x" : 10,
					"y" : 10,

					"image":"d:/ymir work/ui/public/Parameter_Slot_05.sub",

					"children" :
					(
						{
							"name" : "titlename",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"text" : uiScriptLocale.WHISPER_NAME,
						},
						{
							"name" : "titlename_edit",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 120,
							"height" : 17,

							"input_limit" : chr.PLAYER_NAME_MAX_LEN,

							"text" : uiScriptLocale.WHISPER_NAME,
						},
					),
				},

				{
					"name" : "gamemastermark",
					"type" : "expanded_image",
					"style" : ("attach",),

					"x" : 206,
					"y" : 6,

					"x_scale" : 0.2,
					"y_scale" : 0.2,

					"image" : app.GetLocalePath() + "/effect/m2devwh.tga",
				},

				#Message Sistem:
				{
					"name"	: "okunmayankisiler",
					"type"	: "image",
					
					"x" : 148 + 10+25+20+8+40+50+50 + 20, 
                    "y" : 30-15-5-2,
					
					"image":"d:/ymir work/ui/public/Parameter_Slot_05.sub",
					
					"text" : localeInfo.MYKONUSMA,
					
					"children" :
					(
						{
							"name" : "okunmayantext",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"text" : localeInfo.MYKONUSMA,
						},
						{
							"name" : "sec",
							"type" : "button",
							
							"x" : 20+85,
							"y" : 2,
							
							"default_image" : "locale/ui/+.tga",
							"over_image" : "locale/ui/+.tga",
							"down_image" : "locale/ui/+.tga",
						},
					),
				},
				
				#Arama
				{
					"name" : "araslotbar",
					"type" : "slotbar",
					"x" : 148 + 10+25+20+8+40+50+50 + 20 - 15 - 20 - 90 - 50, 
                    "y" : 30-15-5 + 30 - 15 + 8,
					"width" : 94+30+20+80+50+30+30-8,
					"height" : 18,
					"children" :
					(
						{
							"name" : "oyuncuara",
							"type" : "editline",
							
							"width" : 92,
							"height" : 48,
							
							"text"	: "",
							
							"input_limit" : 160,
							
							"x" : 2,
							"y" : 2,
						
						},
						
				
					),
					
				},
				
				{
					"name" : "AraButton",
					"type" : "button",
					
					"x" : 148 + 10+25+20+8+40+50+50 + 20 - 15 + 100 + 30 + 70 - 30 - 8, 
                    "y" : 30-15-5 + 30 - 6-2,
					
					"text" : "Ara",
					
					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
				},
				
				## Button
				{
					"name" : "ignorebutton",
					"type" : "button",

					"x" : 145 + 30 + 20,
					"y" : 10-2+1+1,

					"text" : localeInfo.IMZA,

					#"default_image" : "d:/ymir work/ui/public/small_thin_button_01.sub",
					#"over_image" : "d:/ymir work/ui/public/small_thin_button_02.sub",
					#"down_image" : "d:/ymir work/ui/public/small_thin_button_03.sub",
					"default_image" : "locale/ui/config/imza.tga",
					"over_image" : "locale/ui/config/imza2.tga",
					"down_image" : "locale/ui/config/imza2.tga",
				},
				{ 
					"name" : "gecmis_chat", 
					"type" : "toggle_button", 

					"x" : 148 + 10+9000, 
					"y" : 10,

					"text" : "Gecmis M.", 

					"default_image" : "d:/ymir work/ui/public/small_thin_button_01.sub", 
					"over_image" : "d:/ymir work/ui/public/small_thin_button_02.sub", 
					"down_image" : "d:/ymir work/ui/public/small_thin_button_03.sub", 
				}, 
				{ 
                    "name" : "group_chat", 
                    "type" : "toggle_button", 

                    "x" : 148 + 10+25+20+8 + 30 + 20, 
                    "y" : 10 - 2 - 2,

                    "text" : "Grup PM", 

                    "default_image" : "d:/ymir work/ui/public/small_thin_button_01.sub", 
                    "over_image" : "d:/ymir work/ui/public/small_thin_button_02.sub", 
                    "down_image" : "d:/ymir work/ui/public/small_thin_button_03.sub", 
                }, 
                { 
                    "name" : "group_add", 
                    "type" : "toggle_button", 

                    "x" : 119, 
                    "y" : 10,

                    "tooltip_text" : "Oyuncu ekle", 

                    "default_image" : "d:/ymir work/ui/game/windows/messenger_add_friend_01.sub", 
                    "over_image" : "d:/ymir work/ui/game/windows/messenger_add_friend_02.sub", 
                    "down_image" : "d:/ymir work/ui/game/windows/messenger_add_friend_03.sub", 
                },
				{ 
                    "name" : "group_delete", 
                    "type" : "button", 

                    "x" : 119+23, 
                    "y" : 10,

                    "tooltip_text" : localeInfo.GRUP_CIKAR, 

                    #"default_image" : "locale/ui/setting-icon.tga", 
                    #"over_image" : "locale/ui/setting-icon.tga", 
                    #"down_image" : "locale/ui/setting-icon.tga",
					"default_image" : "d:/ymir work/ui/game/windows/messenger_guild_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/messenger_guild_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/messenger_guild_03.sub",
                }, 
				{ 
					"name" : "delete", 
					"type" : "button", 

					"x" : 119+23, 
					"y" : 10,

					"tooltip_text" : localeInfo.SOHBETAYARLARI, 

					#"default_image" : "locale/ui/setting-icon.tga", 
					#"over_image" : "locale/ui/setting-icon.tga", 
					#"down_image" : "locale/ui/setting-icon.tga",
					"default_image" : "d:/ymir work/ui/game/windows/messenger_guild_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/messenger_guild_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/messenger_guild_03.sub",
                }, 
				{
					"name" : "reportviolentwhisperbutton",
					"type" : "button",

					"x" : 145,
					"y" : 10,

					"text" : "",

					"default_image" : "d:/ymir work/ui/public/large_b11utton_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_bu1tton_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_bu11tton_03.sub",
				},
				{
					"name" : "acceptbutton",
					"type" : "button",

					"x" : 145,
					"y" : 10,

					"text" : "Tamam",

					 "default_image" : "d:/ymir work/ui/public/small_thin_button_01.sub", 
                    "over_image" : "d:/ymir work/ui/public/small_thin_button_02.sub", 
                    "down_image" : "d:/ymir work/ui/public/small_thin_button_03.sub", 
				},
				{
					"name" : "minimizebutton",
					"type" : "button",

					"x" : 450 - 41,
					"y" : 12,

					"tooltip_text" : uiScriptLocale.MINIMIZE,

					"default_image" : "d:/ymir work/ui/public/minimize_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/minimize_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/minimize_button_03.sub",
				},
				{
					"name" : "closebutton",
					"type" : "button",

					"x" : 450 - 24,
					"y" : 12,

					"tooltip_text" : uiScriptLocale.CLOSE,

					"default_image" : "d:/ymir work/ui/public/close_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/close_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/close_button_03.sub",
				},

				## ScrollBar
				{
					"name" : "scrollbar",
					"type" : "thin_scrollbar",

					"x" : 450 - 25,
					"y" : 35,

					"size" : 450 - 160,
				},
				
				#Yazıyor...
				{
					"name" : "yaziyor",
					"type" : "text",
					
					"x" : 95-9,
					"y" : 10+3,
					
					"text" : localeInfo.YAZIYOR,
					
				},
				
				#"Smiles", gülücükler
				{
					"name" : "smiles",
					"type" : "image",
					
					"x" : 10,
					"y" : 205 - 60 + 300,
					
					"image": "locale/ui/smiles/d.tga",
				},
				
				#Renk Tablosu
				{
					"name" : "renkbutton",
					"type" : "button",

					"x" : 450 - 80,
					"y" : 40,
					
					#"vertical_align" : "bottom",

					"text" : "",
					"tooltip_text" : localeInfo.RENKSEC,

					"default_image" : "locale/ui/config/renkler/beyaz.tga",
					"over_image" : "locale/ui/config/renkler/bos.tga",
					"down_image" : "locale/ui/config/renkler/bos.tga",
				},
				

				## Edit Bar
				{
					"name" : "editbar",
					"type" : "bar",

					"x" : 10,
					"y" : 205 - 60,

					"width" : 450 - 18,
					"height" : 50,

					"color" : 0x77000000,

					"children" :
					(
						{
							"name" : "chatline",
							"type" : "editline",

							"x" : 1,
							"y" : 1,

							"width" : 450 - 70,
							"height" : 40,

							"with_codepage" : 1,
							"input_limit" : 40,
							"limit_width" : 450 - 90,
							"multi_line" : 1,
						},
						{
							"name" : "karakterkelime",
							"type" : "text",
							
							"x" : 450 - 80 - 25 - 40 + 30 + 30 + 20 + 40 + 40 + 20 + 20 - 3 - 2,
							"y" : 15,
							
							"text" : "(0)",
							
						},
						{
							"name" : "sendbutton",
							"type" : "button",

							"x" : 450 - 80,
							"y" : 10,

							"text" : uiScriptLocale.WHISPER_SEND,

							"default_image" : "d:/ymir work/ui/public/xlarge_thin_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/xlarge_thin_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/xlarge_thin_button_03.sub",
						},
					),
				},
			),
		},
	),
}
