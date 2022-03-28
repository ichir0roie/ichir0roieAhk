#Include IME.ahk

; Space::Shift

sc03A::Tab
Tab::Esc
sc029::NumLock
Esc::ScrollLock

sc07B & sc079:: sc029
sc079 & sc07B:: sc029
sc07B::Space
sc079::Enter

AppsKey::RWin

; #Include libs/muhenkan.ahk
#Include libs/space.ahk
; #Include libs/DirectInput.ahk



