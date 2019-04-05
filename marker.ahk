#SingleInstance, force
#MaxHotkeysPerInterval 9000

^q::
	BlockInput, MouseMove
	MouseGetPos, oldMousePosX, oldMousePosY
	
	Send, !6
	MouseMove, 674, 335
	Send, ^{Click}
	Send, ^v
	Send, !6
	
	MouseMove, %oldMousePosX%, %oldMousePosY%
	BlockInput, MouseMoveOff