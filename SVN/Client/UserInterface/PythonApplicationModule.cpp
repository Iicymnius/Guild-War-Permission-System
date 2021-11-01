//find;

#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM", 0);
#endif

//add below;

#ifdef ENABLE_WAR_PERMISSION
	PyModule_AddIntConstant(poModule, "ENABLE_WAR_PERMISSION", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_WAR_PERMISSION", 0);
#endif