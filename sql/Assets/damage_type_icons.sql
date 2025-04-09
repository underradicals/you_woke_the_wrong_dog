select distinct
    json -> 'displayProperties' ->> 'icon' as DamageTypeIconUrl
from DestinyDamageTypeDefinition where DamageTypeIconUrl IS NOT NULL;