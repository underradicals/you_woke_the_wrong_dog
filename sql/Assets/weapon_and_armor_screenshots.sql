select distinct
    json ->> 'screenshot' as ScreenshotUrl
from DestinyInventoryItemDefinition where json ->> 'itemType' = 3 or json ->> 'itemType' = 2;