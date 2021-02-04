$outputFile = "C:\Users\Matthew\Desktop\textfile.txt" #change me

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

$cell | ConvertTo-Json -Depth 10 | Out-File -FilePath $outputFile

$sandwichTraits = @{"health" = 10; "strength" = 3}
$sandwich = @{"name" = "sandwich"; "traits" = $sandwichTraits}
$keyTraits = @{"intelligence" = 2; "uses" = 5}
$key = @{"name" = "key"; "traits" = $keyTraits}
$pantryContents = @($sandwich, $key)
$pantry = @{"name" = "pantry"; "content" = $dresserContents}
$fork = @{"name" = "fork"}
$spoon = @{"name" = "spoon"}
$kitchenContents = @($fork, $spoon)
$storageRack = @{"name" = "kitchen supplies"; "content" = $kitchenContents}
$canister = @($pantry, $storageRack)
$cafeteria = @{"name" = "prison cafeteria"; "canister" = $containers}
