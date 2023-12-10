# Lethal Company Latin Translation

[![Lethal Company in Latin](https://img.youtube.com/vi/fYiwEOz51OU/0.jpg)](https://www.youtube.com/watch?v=fYiwEOz51OU)

This project is a Latin translation of Lethal Company.


## Install Instructions

Install the thunderstore mod manager:
1. [Download Thunderstore Mod Manager Here](https://www.overwolf.com/app/Thunderstore-Thunderstore_Mod_Manager) (Download and follow installer)

Install the latin mod (and 2 mods it depends on):
1. [BepInExPack](https://thunderstore.io/c/lethal-company/p/BepInEx/BepInExPack/)
2. [New Terminal](https://thunderstore.io/c/lethal-company/p/Aavild/NewTerminal/)
3. [Lethal Company Latin Localization](https://thunderstore.io/c/lethal-company/p/LudusTranslationis/Lethal_Company_Latin_Localization/)

After you have the mod manager downloaded, downloading the mods is as simple as clicking "Install with Mod Manager" on all 3 of the mod links.

![image](https://github.com/benjenkinsv95/lethal-company-latin-mod/assets/6377344/95a5a736-387e-42e5-bea8-a904a8287b7d)

Once all 3 mods are installed, you can play it in latin by clicking the "Modded play" button at the top

![image](https://github.com/benjenkinsv95/lethal-company-latin-mod/assets/6377344/22ef1cc2-c2c2-4b4d-aa8d-0039b5117757)


## Future Improvements

Note: I will be working on:
1. removing the remaining English in the game (I know about and am having trouble replacing 'Random seed', 'COLLECTED', 'DECEASED', 'No survivors', 'GRADE', and some text if you fail quota)
2. ensuring items are in the correct cases where they are being used (nom vs acc. etc.)
3. reviewing the translations in the terminal (some english remains, but trying to remove it)
4. where possible/it makes sense, using roman numerals (though on numbers in the millions... eh...)
5. (Potential) eventually replacing english text assets (like the posters or potentially the text in the folder)

All of the translations can be found in the files linked below.

## Submit a Translation

Have an idea to improve a translation?

[Add your suggestion here](https://github.com/benjenkinsv95/lethal-company-latin-mod/issues/new) | [or Share it on the Discord](https://discord.gg/x9ccNeFTWV)


## Game Menus & UI Translations
The latin translations used for everything besides the terminal.

1. [Creature](BepInEx/config/la/Creature.txt) ✅
2. [Interactive](BepInEx/config/la/Interactive.txt) ✅
3. [Location](BepInEx/config/la/Location.txt) ✅
4. [MainMenu](BepInEx/config/la/MainMenu.txt) ✅
5. [Scrap&items](BepInEx/config/la/Scrap&items.txt) ✅
6. [UI](BepInEx/config/la/UI.txt) ✅


## Terminal Translations
The NewTerminal translations, used to translate the terminal itself.

1. [Other](BepInEx/config/NewTerminal-Other.cfg)
2. [Special](BepInEx/config/NewTerminal-Special.cfg)
3. [Verbs](BepInEx/config/NewTerminal-Verbs.cfg)

## Contributors

Made with the help of the following contributors:

1. Benjaminus Johannes Quintus
2. Hadriánus Mathis

## Make a build of the mod

1. Open the terminal (or git bash for windows)
2. `cd` into the folder of the mod
3. run `python build.py`
