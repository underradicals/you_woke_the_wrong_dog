drop table if exists Weapon;

create table if not exists Weapon (
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

create index if not exists idx_weapon_name on Weapon (name);
create index if not exists idx_weapon_display_name on Weapon (display_name);
create index if not exists idx_weapon_tier_type on Weapon (tier_type);
create index if not exists idx_weapon_ammo_type on Weapon (ammo_type);
create index if not exists idx_weapon_slot on Weapon (slot);
create index if not exists idx_weapon_damage_type on Weapon (damage_type);