#Include, IME.ahk

#IF IME_GET()==0
; todo this is not need.

1::*
2::+
3::-
4::"

7::'
8::(
9::SendInput,{{}
0::[

sc073::SendInput, {:}

+1::SendInput, {`%}
+2::$
+3::SendInput,{`^}
+4::~

+7::`
+8::)
+9::SendInput,{}}
+0::SendInput,]

[::@
]::#

+[::SendInput,{\}
+]::_

+/::|
+`;::&

@::=
+@::!
+sc028::?

; 1::\
; 2::{
; 3::}
; 4::'
; 5::@
; 6::#
; 7::"
; 8::[
; 9::]
; 0::(
; -::)
; ^::*
; \::~
; [::-
; ]::+
; sc073::SendInput, {:}

; @::=

; +1::_
; +2::SendInput, {`%}
; +3::$
; +4::~
; +8::`
; +9::^
; +^::~
; +/::|
; +`;::&
; +@::!
; +sc028::?