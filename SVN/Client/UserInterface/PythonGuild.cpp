//find;

	PyModule_AddIntConstant(poModule, "AUTH_SKILL", GUILD_AUTH_SKILL);

//add below;

#ifdef ENABLE_WAR_PERMISSION
	PyModule_AddIntConstant(poModule, "AUTH_WAR", GUILD_AUTH_WAR);
#endif