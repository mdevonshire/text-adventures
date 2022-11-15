@echo off

Choice /M "Do you want to start game"
If Errorlevel 2 Goto Exit
If Errorlevel 1 Goto Start
Goto End
:Exit
cls
color 07
Echo Goodbye
Pause
Goto End
:Start
cls
color 07
Echo Are You Ready?
Pause
cls
Echo This game is a word adventure.
Echo You will go and climb trees and fight monsters
Echo and lots of other cool stuff.
pause
goto 123
:123
cls
echo Do you want to enter the Jungle world or the Ocean World?
Echo 1. Jungle World
Echo 2. Ocean World (NOT MADE YET)
Choice /C 12
If errorlevel 2 goto 456
If errorlevel 1 goto jungleintro
:jungleintro
cls
color 2F 
Echo Warping to the jungle world...
pause
cls
Echo You look around the strange little hut you find yourself in. The air is heavy and you can hear the birds a chirping merrily outside. The hut has only a few things in it. A wooden table sits next to a hurridly made bed and in the other corner of the room sits a wooden chest.
pause
goto chest
:chest
cls
Choice /M "Do you want to open the chest?"
if errorlevel 2 goto outsidewc
if errorlevel 1 goto openchest
:outsidewc
cls
echo You walk away from the chest and step outside.
pause
goto nsewwc
:nsewwc
cls
echo Where do you want to go?    N
echo 1. North                    !
echo 2. South                 W--!--E
echo 3. East                     !
echo 4. West                     S
echo 5. Back into the hut
choice /C 12345
if errorlevel 5 goto hutwc
if errorlevel 4 goto westwc
if errorlevel 3 goto eastwc
if errorlevel 2 goto southwc
if errorlevel 1 goto northwc
:westwc
cls
echo You walk westwards and before long you get quite thirsty. You find a stream to drink from and kneel down at the waters edge to drink. Suddenly a large man-eating pirranah attacks you. You have no means of defending yourself and you die an excruciatingly painful death.
pause
goto death
:death
cls
color 40
echo You died
echo         _  _
echo   ___ (~ )( ~)
echo  /   \_\ \/ /
echo {   D_ ]\ \/
echo {   D _]/\ \
echo  \___/ / /\ \
echo       (_ )( _)
echo         ~  ~
Choice /m "Do you want to try again?"
if errorlevel 2 goto Exit
if errorlevel 1 goto Start
:End
exit
:eastwc
cls 
echo To the east of the hut lies a large cliff face. You cannot see what is abouve it
pause
goto cliffwc
:cliffwc
cls
choice /m "Do you want to climb the cliff?"
if errorlevel 2 goto ncliffwc
if errorlevel 1 goto climbcliffwc
:ncliffwc
cls
choice /m "Do you want to go back to the hut?"
if errorlevel 2 goto cliffwc
if errorlevel 1 goto ywbtth
:hutwc
cls
echo You see the chest in the corner.
pause
goto chest
:climbcliffwc
cls
echo After a hour or so of dragging youself up the cliff you finally reach the top. Suddenly some natives jump out in front of you and look at you closely. They spot something on your chest and start attacking you with spears. A spear inpales you and you plummet down over the cliff, your life already slipping away.
pause 
goto death 
:northwc
cls
echo You walk to the north of the hut and soon the trees and plants and vines are so thick that you cannot go any furthur.
pause
goto dycwn
:dycwn
cls
choice /m "Do you continue walking north?."
if errorlevel 2 goto nbth
if errorlevel 1 goto snakendeath
:nbth
cls
choice /m "Do you go back to the hut?"
if errorlevel 2 goto dycwn
if errorlevel 1 goto ywbtth
:ywbtth
cls
echo You walk back to the hut
pause
goto nsewwc
:snakendeath
cls
echo You edge your way furthur into the leafy undergrowth and you realise you are getting nowhere. Just when you think that all hope is lost you have a lightbulb moment. You decide that you could climb a vine to get on higher ground.
pause
goto climbvineQ
:climbvineQ
cls
choice /m "Do you climb the vine?"
if errorlevel 2 goto sgbth
if errorlevel 1 goto sdeath
:sgbth
cls
choice /m "Do you go back to the hut?"
if errorlevel 2 goto climbvineQ
if errorlevel 1 goto ywbtth
:sdeath
cls
echo You jump up and grab on to a vine just abouve you. The vine hisses at you and then you realise that the vine is acctually a snake. With sharp refexes you let go of the snake but not before it bites you and injects the leathal venon. There is nothing you can do. Your vision goes blurry as you slowly slip from consciousness. 
pause
goto death
:southwc
cls
echo You walk aound to the back of the hut and find a path leading south so you decide to follow it.  
pause
cls  
echo Eventually you reach the end of the path and it leads to a beach. You see a warning sign that warns people of the man-eating sharks. You even see fins circling in the water. You quickly run back along the path to get away from the beach, you weren't going to take any chances. 
pause
goto ywbtth
:openchest
cls
echo You open the chest.
pause
cls
echo Inside the chest is a knife and a book
pause
cls
echo What do you take out of the chest?
echo 1. The knife
echo 2. The book
echo 3. Both
echo 4. Nothing
choice /c 1234
if errorlevel 4 goto outsidewc
if errorlevel 3 goto 4
if errorlevel 2 goto 4
if errorlevel 1 goto nsewkogo
:nsewkogo
cls
echo You close the chest and walk outside
pause
goto nsewko
:nsewko
cls
echo Where do you want to go?    N
echo 1. North                    !
echo 2. South                 W--!--E
echo 3. East                     !
echo 4. West                     S
echo 5. Back into the hut
choice /C 12345
if errorlevel 5 goto hutk o
if errorlevel 4 goto 2
if errorlevel 3 goto 2
if errorlevel 2 goto 2
if errorlevel 1 goto 2
:hutko
cls
echo You walk into the hut and see the chest in the corner.
pause
goto chestko
:chestko
cls
echo This is a dead end Program incomplete
pause
goto nsewko
:456
cls
echo This is a dead end Program incomplete
pause
goto 123
:4
cls
echo This is a dead end Program incomplete
pause
goto openchest
:2
cls
echo This is a dead end Program incomplete
pause
goto nsewko






























