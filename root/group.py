import uiScriptLocale
import app
import localeInfo

LOCALE_PATH = uiScriptLocale.LOGIN_PATH

import uiScriptLocale

window = {
	"name" : "evo2board",
	"style" : ("movable", "float",),

	"x" : 100,
	"y" : 100,

	"width" : 180,
	"height" : 200,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 180,
			"height" : 200,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : 165,
					"color" : "gray",

					"children" :
					(
						{ 
						"name":"titlename", 
						"type":"text", 
						
						"x":0, 
						"y":3, 
						
						"horizontal_align":"center", 
						"text_horizontal_align":"center",
						
						"text": "Grup kurma ayarlarý", 
						 },
					),
				},
			## Überschrift
				{
					"name" : "Überschrift",
					"type" : "text",

					"x" : 30,
					"y" : 34,

					"text" : "Grup adý:",
				},
				{
					"name" : "Gamemasta1",
					"type" : "button",

					"x" : 45,
					"y" : 155,

					"text" : localeInfo.GRUPOLUSTUR,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "NameSlot",
					"type" : "slotbar",

					"x" : 30,
					"y" : 54,
					"width" : 120,
					"height" : 18,
				},
				{
					"name" : "ID_EditLine",
					"type" : "editline",

					"x" : 35,
					"y" : 56,

					"width" : 120,
					"height" : 18,

					"input_limit" : 16,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				
				{
					"name" : "Überschrift2",
					"type" : "text",

					"x" : 30,
					"y" : 104,

					"text" : localeInfo.GRUPUYELERITEXT,
				},
				{
					"name" : "NameSlot2",
					"type" : "slotbar",

					"x" : 30,
					"y" : 124,
					"width" : 120,
					"height" : 18,
				},
				{
					"name" : "PW_EditLine",
					"type" : "editline",

					"x" : 35,
					"y" : 126,

					"width" : 120,
					"height" : 18,

					"input_limit" : 900,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				
				
			),
		},
	),
}
