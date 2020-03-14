from pywinauto.application import Application
from pywinauto.keyboard import SendKeys
import time
import subprocess as sp
command = '"C:\Program Files (x86)\Equis\MetaStock\MsWin.exe"'
def open_app(cmd_command):
    global command
    sp.Popen(cmd_command)
    time.sleep(5)
open_app(command)
SendKeys("%c"
         "{ENTER}")
time.sleep(5)
msp = Application().connect(title_re="MetaStock Professional")
msp.MetaStockProfessional.MenuItem("Tools->The Explorer").Click()
#first scan
msp.TheExporer.edit.ClickInput()
SendKeys("{TAB}{TAB}{TAB}" #coloumn A
         "If{(}H{>} PriceChannelHigh{(}5 {)} ,H, PriceChannelHigh{(}5 {)} {)}",with_spaces=True)
SendKeys("{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{RIGHT}"#ColoumnB
         "+{DOWN}+{DOWN}+{DOWN}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}"
         "If{(}L{<} PriceChannelLow{(}5 {)} ,L, PriceChannelLow{(}5 {)} {)}",with_spaces=True)
SendKeys("{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{RIGHT}"#ColoumnC
         "+{DOWN}+{DOWN}+{DOWN}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}"
         "H",with_spaces=True)
SendKeys("{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{RIGHT}"#ColoumnD
         "+{DOWN}+{DOWN}+{DOWN}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}+{RIGHT}"
         "L",with_spaces=True)
msp.ExploratioEditor.OK.ClickInput()
msp.TheExporer.Explore.ClickInput()
msp.SelectSecuritiesFor5DAYHIGHLOWdaily.OK.ClickInput()
time.sleep(3)
msp.ExploratioCompleted.Reports.ClickInput()
