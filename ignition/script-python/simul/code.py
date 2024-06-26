import time
def move_to_source_car(path):
	sourcePos=system.tag.read(path+'/Coordinate/X_Location').value
	system.tag.write('[default]PressIF_TransferCart/TC_AGTC/TransComm/ActualPosition_PLCTOSM',sourcePos)
	time.sleep(10)
	system.tag.write('[default]PressIF_TransferCart/TC_AGTC/TransComm/InSourcePos_PLCTOSM',1)
	system.tag.write('[default]PressIF_TransferCart/TC_AGTC/TransComm/SourceRollRun_PLCTOSM',1)
	system.tag.write(path+'/TransComm/SourceRollRun_PLCTOSM',1)
	time.sleep(10)
	system.tag.write('[default]PressIF_TransferCart/TC_AGTC/TransComm/InSourcePos_PLCTOSM',0)
	system.tag.write('[default]PressIF_TransferCart/TC_AGTC/TransComm/SourceRollRun_PLCTOSM',0)
	system.tag.write(path+'/TransComm/SourceRollRun_PLCTOSM',0)
	system.tag.write('[default]PressIF_TransferCart/TC_AGTC/LocOccupied_PLCTOSM',1)
	system.tag.write(path+'/LocOccupied_PLCTOSM',0)
	

	
	
	
def move_to_dest_car(path):
	sourcePos=system.tag.read(path+'/Coordinate/X_Location').value
	system.tag.write('[default]PressIF_TransferCart/TC_AGTC/TransComm/ActualPosition_PLCTOSM',sourcePos)
	system.tag.write(path+'/LocOccupied_PLCTOSM',0)
	time.sleep(10)
	system.tag.write('[default]PressIF_TransferCart/TC_AGTC/TransComm/InDestPos_PLCTOSM',1)
	system.tag.write('[default]PressIF_TransferCart/TC_AGTC/TransComm/DestRollRun_PLCTOSM',1)
	system.tag.write(path+'/TransComm/DestRollRun_PLCTOSM',1)
	time.sleep(10)
	system.tag.write('[default]PressIF_TransferCart/TC_AGTC/TransComm/InDestPos_PLCTOSM',0)
	system.tag.write('[default]PressIF_TransferCart/TC_AGTC/TransComm/DestRollRun_PLCTOSM',0)
	system.tag.write(path+'/TransComm/DestRollRun_PLCTOSM',0)
	system.tag.write('[default]PressIF_TransferCart/TC_AGTC/LocOccupied_PLCTOSM',0)
	system.tag.write(path+'/LocOccupied_PLCTOSM',1)

	

	
	
	