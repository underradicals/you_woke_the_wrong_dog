select distinct
    json ->> 'iconWatermark' as WatermarkUrl
from DestinyInventoryItemDefinition where json ->> 'itemType' = 3 or json ->> 'itemType' = 2;