#Include IME.ahk

; sc07B::Shift
; sc07B::Space
sc079::Space

Space::Shift

sc03A::Tab
Tab::sc029
sc029::Esc
Esc::NumLock

AppsKey::RWin
sc070::RAlt

#Include, muhenkan.ahk

;use input mode,this is last
#Include DirectInput.ahk
#Include, PrintDate.ahk
#Include, PrintMaru.ahk
#Include, FileCreater.ahk
;#Include, ColemakBreak.ahk

