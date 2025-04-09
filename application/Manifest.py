from typing import Any, TypedDict


class WorldContentSchema:
  DestinyArtDyeChannelDefinition: str
  DestinyArtDyeReferenceDefinition: str
  DestinyPlaceDefinition: str
  DestinyActivityDefinition: str
  DestinyActivityTypeDefinition: str
  DestinyClassDefinition: str
  DestinyGenderDefinition: str
  DestinyInventoryBucketDefinition: str
  DestinyRaceDefinition: str
  DestinyUnlockDefinition: str
  DestinyStatGroupDefinition: str
  DestinyProgressionMappingDefinition: str
  DestinyFactionDefinition: str
  DestinyVendorGroupDefinition: str
  DestinyRewardSourceDefinition: str
  DestinyUnlockValueDefinition: str
  DestinyRewardMappingDefinition: str
  DestinyRewardSheetDefinition: str
  DestinyItemCategoryDefinition: str
  DestinyDamageTypeDefinition: str
  DestinyActivityModeDefinition: str
  DestinyMedalTierDefinition: str
  DestinyAchievementDefinition: str
  DestinyActivityGraphDefinition: str
  DestinyActivityInteractableDefinition: str
  DestinyBondDefinition: str
  DestinyCharacterCustomizationCategoryDefinition: str
  DestinyCharacterCustomizationOptionDefinition: str
  DestinyCollectibleDefinition: str
  DestinyDestinationDefinition: str
  DestinyEntitlementOfferDefinition: str
  DestinyEquipmentSlotDefinition: str
  DestinyEventCardDefinition: str
  DestinyFireteamFinderActivityGraphDefinition: str
  DestinyFireteamFinderActivitySetDefinition: str
  DestinyFireteamFinderLabelDefinition: str
  DestinyFireteamFinderLabelGroupDefinition: str
  DestinyFireteamFinderOptionDefinition: str
  DestinyFireteamFinderOptionGroupDefinition: str
  DestinyStatDefinition: str
  DestinyInventoryItemDefinition: str
  DestinyInventoryItemLiteDefinition: str
  DestinyItemTierTypeDefinition: str
  DestinyLoadoutColorDefinition: str
  DestinyLoadoutIconDefinition: str
  DestinyLoadoutNameDefinition: str
  DestinyLocationDefinition: str
  DestinyLoreDefinition: str
  DestinyMaterialRequirementSetDefinition: str
  DestinyMetricDefinition: str
  DestinyObjectiveDefinition: str
  DestinySandboxPerkDefinition: str
  DestinyPlatformBucketMappingDefinition: str
  DestinyPlugSetDefinition: str
  DestinyPowerCapDefinition: str
  DestinyPresentationNodeDefinition: str
  DestinyProgressionDefinition: str
  DestinyProgressionLevelRequirementDefinition: str
  DestinyRecordDefinition: str
  DestinyRewardAdjusterPointerDefinition: str
  DestinyRewardAdjusterProgressionMapDefinition: str
  DestinyRewardItemListDefinition: str
  DestinySackRewardItemListDefinition: str
  DestinySandboxPatternDefinition: str
  DestinySeasonDefinition: str
  DestinySeasonPassDefinition: str
  DestinySocialCommendationDefinition: str
  DestinySocketCategoryDefinition: str
  DestinySocketTypeDefinition: str
  DestinyTraitDefinition: str
  DestinyUnlockCountMappingDefinition: str
  DestinyUnlockEventDefinition: str
  DestinyUnlockExpressionMappingDefinition: str
  DestinyVendorDefinition: str
  DestinyMilestoneDefinition: str
  DestinyActivityModifierDefinition: str
  DestinyReportReasonCategoryDefinition: str
  DestinyArtifactDefinition: str
  DestinyBreakerTypeDefinition: str
  DestinyChecklistDefinition: str
  DestinyEnergyTypeDefinition: str
  DestinySocialCommendationNodeDefinition: str
  DestinyGuardianRankDefinition: str
  DestinyGuardianRankConstantsDefinition: str
  DestinyLoadoutConstantsDefinition: str
  DestinyFireteamFinderConstantsDefinition: str
  DestinyGlobalConstantsDefinition: str



class MobileGearCDN(TypedDict):
  Geometry: str
  Texture: str
  PlateRegion: str
  Gear: str
  Shader: str


class JsonWorldComponentContentPaths(TypedDict):
  en: WorldContentSchema 
  fr: WorldContentSchema 
  es: WorldContentSchema 
  es_mx: WorldContentSchema
  de: WorldContentSchema 
  it: WorldContentSchema 
  ja: WorldContentSchema 
  pt_br: WorldContentSchema
  ru: WorldContentSchema 
  pl: WorldContentSchema 
  ko: WorldContentSchema 
  zh_cht: WorldContentSchema
  zh_chs: WorldContentSchema


class JsonWorldContentPaths(TypedDict):
  en: str 
  fr: str 
  es: str 
  es_mx: str
  de: str 
  it: str 
  ja: str 
  pt_br: str
  ru: str 
  pl: str 
  ko: str 
  zh_cht: str
  zh_chs: str


class MobileWorldContentPaths(TypedDict):
  en: str 
  fr: str 
  es: str 
  es_mx: str
  de: str 
  it: str 
  ja: str 
  pt_br: str
  ru: str 
  pl: str 
  ko: str 
  zh_cht: str
  zh_chs: str


class MobileGearAssetDataBasesItem(TypedDict):
  version: int
  path: str

class ManifestResponse(TypedDict):
  version: str
  mobileAssetContentPath: str
  mobileGearAssetDataBases: list[MobileGearAssetDataBasesItem]
  mobileWorldContentPaths: MobileWorldContentPaths
  jsonWorldContentPaths: JsonWorldContentPaths
  jsonWorldComponentContentPaths: JsonWorldComponentContentPaths
  mobileClanBannerDatabasePath: str
  mobileGearCDN: MobileGearCDN
  iconImagePyramidInfo: list[None]
  


class Manifest(TypedDict):
  Response: ManifestResponse
  ErrorCode: int
  ThrottleSeconds: int
  ErrorStatus: str
  Message: str
  MessageData: dict[str, Any]