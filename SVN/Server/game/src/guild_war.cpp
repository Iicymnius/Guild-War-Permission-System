//find;

	if (gw.state != GUILD_WAR_ON_WAR)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("�̹� ������ �������ϴ�."));
		return;
	}

//add below;

#ifdef ENABLE_WAR_PERMISSION
	if (!HasGradeAuth(GetMember(ch->GetPlayerID())->grade, GUILD_AUTH_WAR))
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("savasizin"));
		return;
	}
#endif