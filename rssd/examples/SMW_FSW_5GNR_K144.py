##########################################################
### Rohde & Schwarz Automation for demonstration use.
###
### Purpose: FSW/SMW 5G NR Demo
### Author:  mclim
### Date:    2018.07.05
### Descrip: FSW 3.20-18.7.1.0 Beta
###          SMW 4.30 SP2
##########################################################
### User Entry
##########################################################
import os
BaseDir = os.path.dirname(os.path.realpath(__file__))
OutFile = BaseDir + "\\data\\SMW_FSW_5GNR"

print __file__

SMW_IP   = '192.168.1.114'                    #IP Address
FSW_IP   = '192.168.1.109'                    #IP Address
Freq     = 10e9
SWM_Out  = 0

NR_Dir   = 'UL'
NR_BW    = 100
NR_SubSp = 30e3
NR_RB    = 100
NR_RBO   = 0
NR_Mod   = 'QPSK'

##########################################################
### Code Start
##########################################################
from rssd.SMW_5GNR_K144 import VSG
from rssd.FSW_5GNR_K144 import VSA
from rssd.FileIO        import FileIO
import time

f = FileIO()
DataFile = f.Init(OutFile)
SMW = VSG()
SMW.jav_Open(SMW_IP,f.sFName)
FSW = VSA()
FSW.jav_Open(FSW_IP,f.sFName)

##########################################################
### Instrument Settings
##########################################################
SMW.Set_Freq(Freq)
SMW.Set_5GNR_Direction(NR_Dir)
SMW.Set_5GNR_ChannelBW(NR_BW)
SMW.Set_5GNR_SubSpace(NR_SubSp)
SMW.Set_5GNR_ResBlock(NR_RB)
SMW.Set_5GNR_ResBlockOffset(NR_RBO)
SMW.Set_5GNR_Modulation(NR_Mod)
SMW.Set_RFPwr(SWM_Out)                    #Output Power
SMW.Set_RFState('ON')                     #Turn RF Output on

FSW.Set_Freq(Freq)
FSW.Set_SweepCont(1)
FSW.Init_5GNR()
FSW.Set_5GNR_Direction(NR_Dir)
FSW.Set_5GNR_ChannelBW(NR_BW)
FSW.Set_5GNR_SubSpace(NR_SubSp)
FSW.Set_5GNR_ResBlock(NR_RB)
FSW.Set_5GNR_ResBlockOffset(NR_RBO)
FSW.Set_5GNR_Modulation(NR_Mod)

EVM = Get_5GNR_EVMParams()
OutStr = "%d,%s"%(freq,EVM)
f.write(OutStr)

SMW.jav_ClrErr()                          #Clear Errors
FSW.jav_ClrErr()                          #Clear Errors
