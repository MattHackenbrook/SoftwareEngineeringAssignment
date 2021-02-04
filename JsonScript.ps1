﻿$outputFile = "C:\Users\3picm\Documents\softeng\CCPS406\jsonFile.txt" #change me

$knifeTraits = @{"damage" = 10; "durability" = 3}
$knife = @{"name" = "knife"; "traits" = $knifeTraits}
$cocaineTraits = @{"strength" = 5; "uses" = 1}
$cocaine = @{"name" = "cocaine"; "traits" = $cocaineTraits}
$dresserContents = @($knife, $cocaine)
$dresser = @{"name" = "dresser"; "content" = $dresserContents}
$sock = @{"name" = "sock"}
$boxContents = @($sock)
$box = @{"name" = "cardboard box"; "content" = $boxContents}
$containers = @($dresser, $box)
$cell = @{"name" = "my cell"; "containers" = $containers}







$rooms = @{}
$prison = @{"name" = "Shankshaw Penitentiary"; "rooms" = $rooms}

$prison | ConvertTo-Json -Depth 10 | Out-File -FilePath $outputFile
