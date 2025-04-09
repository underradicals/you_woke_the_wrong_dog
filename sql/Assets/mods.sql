select distinct
    d.json -> 'displayProperties' ->> 'icon' as IconUrl
    from DestinyInventoryItemDefinition d, json_each(d.json, '$.itemCategoryHashes') where d.json ->> 'itemType' = 19 and
    (
        json_each.value = 4104513227 or
        json_each.value = 610365472 or
        json_each.value = 141186804 or
        json_each.value = 1043342778
    ) and d.json ->> 'itemTypeDisplayName' != 'Weapon Ornament';