select distinct
    json -> 'displayProperties' ->> 'icon' as IconUrl
from DestinyInventoryItemDefinition where json ->> 'itemType' = 3 or json ->> 'itemType' = 2;