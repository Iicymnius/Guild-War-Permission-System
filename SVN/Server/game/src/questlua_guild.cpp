//find;

	ALUA(guild_get_exp_level0)
	{
		lua_pushnumber(L, guild_exp_table2[MINMAX(0, lua_tonumber(L, 1), GUILD_MAX_LEVEL)]);
		return 1;
	}

//add below;

#ifdef ENABLE_WAR_PERMISSION
	ALUA(guild_grade_war)
	{
		CQuestManager& q = CQuestManager::instance();
		LPCHARACTER ch = q.GetCurrentCharacterPtr();
		CGuild* pGuild = ch->GetGuild();

		lua_pushnumber(L, pGuild ? pGuild->HasGradeAuth(pGuild->GetMember(ch->GetPlayerID())->grade, GUILD_AUTH_WAR) : 0);

		return 1;
	}
#endif

//find again;

			{ "get_exp_level0",			guild_get_exp_level0		},

//add below;

#ifdef ENABLE_WAR_PERMISSION
			{ "grade_war",				guild_grade_war				},
#endif