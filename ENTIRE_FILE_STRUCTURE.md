Below is a breakdown of the files in this latin language mod

## Top Level Files (Required for mod)
1. [CHANGELOG.md](CHANGELOG.md) - the changes to your mod over time
2. [README.md](README.md) - a description of your mod
3. [icon.png](icon.png) - a 256x256 image for your mod
4. [manifest.json](manifest.json) - metadata about the mod

## AutoTranslatorConfig.ini

[AutoTranslatorConfig.ini](BepInEx/config/AutoTranslatorConfig.ini) is where you set the language code like `la` or whatever you choose. (Ex. Language=la)

## The Translation Files (config folder)

The config folder contains the translations. There are 2 kinds of translations.

### Terminal Translations
The NewTerminal translations, used to translate the terminal itself.

1. [Verbs](BepInEx/config/NewTerminal-Verbs.cfg)
2. [Special](BepInEx/config/NewTerminal-Special.cfg)
3. [Other](BepInEx/config/NewTerminal-Other.cfg)

### la Translations
The latin translations used for everything besides the terminal.

1. [Creature](BepInEx/config/la/Creature.txt) ✅
1. [Interactive](BepInEx/config/la/Interactive.txt) ✅
1. [Location](BepInEx/config/la/Location.txt) ✅
1. [MainMenu](BepInEx/config/la/MainMenu.txt) ✅
1. [Scrap&items](BepInEx/config/la/Scrap&items.txt) ✅
1. [UI](BepInEx/config/la/UI.txt)
