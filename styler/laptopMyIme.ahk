#Include IME.ahk

; sc07B::Shift
; sc07B::Space
sc079::Space

Space::Shift

sc03A::Tab
Tab::Esc
sc029::NumLock
Esc::ScrollLock

; sc073::sc029
;sc070::sc029
sc07B & sc079:: sc029
 
AppsKey::RWin

#Include libs/muhenkan.ahk
; #Include libs/DirectInput.ahk


