attach database 'D:\D2App\d2.db' as target;

-- Drop Tables
drop table if exists target.Weapons;


-- Create Tables
create table if not exists target.Weapons(
    id integer not null ,
    name text not null ,
    flavor_text text not null ,
    display_name text not null ,
    tier_type text not null ,
    ammo_type text not null ,
    slot text not null ,
    damage_type text not null ,
    damage_type_url text not null ,
    icon_url text not null ,
    watermark_url text not null ,
    screenshot_url text not null ,
    constraint pk_weapon primary key (id)
);

create index if not exists target.idx_weapon_name on Weapons (name);
create index if not exists target.idx_weapon_display_name on Weapons (display_name);
create index if not exists target.idx_weapon_tier_type on Weapons (tier_type);
create index if not exists target.idx_weapon_ammo_type on Weapons (ammo_type);
create index if not exists target.idx_weapon_slot on Weapons (slot);
create index if not exists target.idx_weapon_damage_type on Weapons (damage_type);


insert into target.Weapons (id, name, flavor_text, display_name, tier_type, ammo_type, slot, damage_type, damage_type_url, icon_url, watermark_url, screenshot_url)
with weapon_cte as (
    select
        'hash' as ItemId ,
        'displayProperties' as DisplayProperties ,
        'name' as Name ,
        'icon' as Icon ,
        'iconWatermark' as Watermark ,
        'screenshot' as Screenshot ,
        'flavorText' as FlavorText ,
        'itemTypeDisplayName' as DisplayName ,
        'inventory' as Inventory ,
        'tierTypeName' as TierType ,
        'equippingBlock' as Equipment ,
        'ammoType' as AmmoType ,
        'equipmentSlotTypeHash' as Slot ,
        'defaultDamageTypeHash' as DamageType

)
select
    json ->> ItemId ,
    json -> DisplayProperties ->> Name as Name ,
    json ->> FlavorText as FlavorText ,
    json ->> DisplayName as DisplayName ,
    json -> Inventory ->> TierType as TierType ,
    case json -> Equipment ->> AmmoType
        when 3 then 'Heavy'
        when 2 then 'Special'
        when 1 then 'Primary'
    end as AmmoType ,
    case json -> Equipment ->> Slot
        when 953998645 then 'Power'
        when 2465295065 then 'Energy'
        when 1498876634 then 'Kinetic'
    end as Slot,
    (
    select
        json ->> DisplayProperties ->> Name
    from DestinyDamageTypeDefinition dd
    where d.json ->> DamageType = dd.json ->> ItemId
    ) as DamageType ,
    (
    select
        json ->> DisplayProperties ->> Icon
    from DestinyDamageTypeDefinition dd
    where d.json ->> DamageType = dd.json ->> ItemId
    ) as DamageIconUrl ,
    json -> DisplayProperties ->> Icon as IconUrl ,
    json ->> Watermark as WatermarkUrl ,
    json ->> Screenshot as Screenshot
from DestinyInventoryItemDefinition d, weapon_cte where json ->> 'itemType' = 3;

-- Update Tables

detach database target;