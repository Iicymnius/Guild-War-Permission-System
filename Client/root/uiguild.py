#find;

	GRADE_SKILL_AUTHORITY = 4

#add below;

	if app.ENABLE_WAR_PERMISSION:
		GRADE_WAR_AUTHORITY = 5

#find again;

				gradeNameSlot = EditableTextSlot(page, 58, yPos)

#change;

				if app.ENABLE_WAR_PERMISSION:
					gradeNameSlot = EditableTextSlot(page, 58 - 19, yPos)
				else:
					gradeNameSlot = EditableTextSlot(page, 58, yPos)

#find again;

				inviteAuthorityCheckBox = CheckBox(page, 124, yPos, event)

#change;

				if app.ENABLE_WAR_PERMISSION:
					inviteAuthorityCheckBox = CheckBox(page, 124 - 24, yPos, event)
				else:
					inviteAuthorityCheckBox = CheckBox(page, 124, yPos, event)

#find again;

				driveoutAuthorityCheckBox = CheckBox(page, 181, yPos, event)

#change;

				if app.ENABLE_WAR_PERMISSION:
					driveoutAuthorityCheckBox = CheckBox(page, 181 - 29, yPos, event)
				else:
					driveoutAuthorityCheckBox = CheckBox(page, 181, yPos, event)

#find again;

				noticeAuthorityCheckBox = CheckBox(page, 238, yPos, event)

#change;

				if app.ENABLE_WAR_PERMISSION:
					noticeAuthorityCheckBox = CheckBox(page, 238 - 34, yPos, event)
				else:
					noticeAuthorityCheckBox = CheckBox(page, 238, yPos, event)

#find again;

				skillAuthorityCheckBox = CheckBox(page, 295, yPos, event)

#change;

				if app.ENABLE_WAR_PERMISSION:
					skillAuthorityCheckBox = CheckBox(page, 295 - 39, yPos, event)
				else:
					skillAuthorityCheckBox = CheckBox(page, 295, yPos, event)

#find again;

			gradeSlotList = []

#add above;

			if app.ENABLE_WAR_PERMISSION:
				event = lambda argSelf=proxy(self), argIndex=index, argAuthority=1<<4: apply(argSelf.OnCheckAuthority, (argIndex,argAuthority))
				warAuthorityCheckBox = CheckBox(page, 308, yPos, event)
				page.Children.append(warAuthorityCheckBox)

#find again;

			gradeSlotList.append(skillAuthorityCheckBox)

#add below;

			if app.ENABLE_WAR_PERMISSION:
				gradeSlotList.append(warAuthorityCheckBox)

#find again;

			slotList[self.GRADE_SKILL_AUTHORITY].SetCheck(authority & guild.AUTH_SKILL)

#add below;

			if app.ENABLE_WAR_PERMISSION:
				slotList[self.GRADE_WAR_AUTHORITY].SetCheck(authority & guild.AUTH_WAR)