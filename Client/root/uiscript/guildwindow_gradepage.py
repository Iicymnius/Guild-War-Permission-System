#find;

			{
				"name" : "SkillAuthority", "type" : "text", "x" : 303, "y" : 5, "text" : uiScriptLocale.GUILD_GRADE_PERMISSION_SKILL,#"x" and "y" may differ.
			},

#add below;

			#if app.ENABLE_WAR_PERMISSION:
			{
				"name" : "WarAuthority", "type" : "text", "x" : 320-57+48, "y" : 5, "text" : "Savaþ",#Edit "x" and "y" according to you.
			},