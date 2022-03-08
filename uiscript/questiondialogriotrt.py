import uiScriptLocale
import localeInfo

window = {
	"name" : "QuestionDialog",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH/2 - 125,
	"y" : SCREEN_HEIGHT/2 - 52,

	"width" : 280+100,
	"height" : 105,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 280+100,
			"height" : 105,

			"children" :
			(
				{
					"name" : "kapat",
					"type" : "button",

					"x" : +98+100 - 20 - 9,
					"y" : 8,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					"tooltip_text" : localeInfo.EGERKAPATIRSAN,

					"default_image" : "d:/ymir work/ui/public/close_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/close_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/close_button_03.sub",
				},
				
				{
					"name" : "sonraki",
					"type" : "button",

					"x" : +98+100 - 30 - 20 - 7,
					"y" : 25+14,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					
					"text" : ">>>",
					"tooltip_text" : "Sonraki Talep",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				
				{
					"name" : "onceki",
					"type" : "button",

					"x" : 20,
					"y" : 25+14,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "left",
					
					"text" : "<<<",
					"tooltip_text" : localeInfo.ONCEKITALEP,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				
				{
					"name" : "message1",
					"type" : "text",

					"x" : 0,
					"y" : 25,

					"text" : uiScriptLocale.MESSAGE,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",
				},
				{
					"name" : "message2",
					"type" : "text",

					"x" : 0,
					"y" : 50,

					"text" : "Kabul et veya Reddet?;",

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",
				},
				{
					"name" : "accept",
					"type" : "button",

					"x" : -40,
					"y" : 68,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					"text" : uiScriptLocale.YES,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "cancel",
					"type" : "button",

					"x" : +40,
					"y" : 68,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					"text" : uiScriptLocale.NO,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}