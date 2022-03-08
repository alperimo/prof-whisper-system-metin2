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

	"width" : 300,
	"height" : 140,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 300,
			"height" : 140,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : 285,
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
						
						"text": localeInfo.GRUPUYEEKLEMEBOLUMU, 
						 },
					),
				},
			## Überschrift
				{
					"name" : "Gamemasta1",
					"type" : "button",

					"x" : 110,
					"y" : 100,

					"text" : "Ekle",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},	
				{
					"name" : "Überschrift2",
					"type" : "text",

					"x" : 30,
					"y" : 44,

					"text" : "Oyuncu Adý:",
				},
				{
					"name" : "NameSlot2",
					"type" : "slotbar",

					"x" : 30,
					"y" : 64,
					"width" : 240,
					"height" : 18,
				},
				{
					"name" : "ID_EditLine",
					"type" : "editline",

					"x" : 35,
					"y" : 66,

					"width" : 240,
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
