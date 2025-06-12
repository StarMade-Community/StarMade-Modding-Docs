# Table of Contents
- [Introduction](#introduction)
    - [StarMade](#starmade)
    - [StarLoader](#starloader)
    - [StarLoader for Non-Modders](#starloader-for-non-modders)
    - [Downloading and Installing Mods](#downloading-and-installing-mods)
- [Modding Basics](modding-basics.md)(Todo)
  - [Setup](modding-basics.md#setup)(Todo)
- [Events](events.md)(Todo)
  - [Event Listeners](events.md#event-listeners)(Todo)
  - [Fast Listeners](events.md#fast-listeners)(Todo)
- [Mod Template](mod-template.md)(Todo)
- [Miscellaneous](miscellaneous.md)
  - [Building StarMade](building-starmade.md#building-starmade)
# Introduction
## StarMade
StarMade is a 3D voxel space sandbox game that allows players to build and explore in a vast universe.
It combines elements of construction, exploration, and combat, providing a unique experience for players who enjoy 
creativity and strategy.
## StarLoader
StarLoader is a modding framework and API for StarMade that allows players to create and manage mods for the game. The 
project started in 2019 and has since evolved to support a wide range of modding capabilities, including custom blocks, 
items, sounds, visual effects, and more. StarLoader is integrated into the base game, allowing users to download, 
install, and manage mods directly from the main menu.
## StarLoader for Non-Modders
StarLoader is designed to be user-friendly, even for those who are not familiar with modding. It provides a simple
interface for downloading and installing mods, as well as a built-in mod manager for managing installed mods.
## Downloading and Installing Mods
To download and install mods, players can access the mod manager from the main menu. From there, you can browse and
download mods directly from StarMade dock. Once a mod is downloaded, it will be automatically installed, and you can 
enable or disable it from the mod manager.

If you are joining a modded server and do not have the required mods installed, StarLoader will automatically download,
install, and enable them for you before joining the server. Note: Certain mods require the client to perform a
soft-restart to apply changes. If a mod is marked as "core_mod", "requires_class_resize", or "hard_load_all_classes"
in the mod.json file, a soft-restart is required to apply the changes. In this case, the game will automatically perform 
this function for you and then will directly connect you to the server.

You can also manually install mods by placing the mod jar in the "mods" folder located in the StarMade game directory.