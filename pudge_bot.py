import discord
from discord.ext import commands
from discord.utils import get
import random

bot = commands.Bot(command_prefix='-')

heroes_2 = [
25,
89,
100,
64,
103,
101,
68,
62,
74,
16,
118,
109,
111,
84,
46,
113,
40,
53,
66,
1,
94,
41,
43,
44,
112,
14,
45,
55,
56,
92,
50,
19,
52,
54,
97,
59,
60,
24,
25,
102,
104,
75,
107,
108,
66,
115
]

heroes_1 = [
0,
1,
39,
56,
30,
69,
45,
18,
14,
60,
38,
50,
19,
65,
51,
52,
61,
7,
67,
70,
71,
49,
48,
46,
40,
44,
47,
94,
41,
75,
66
]

heroes_image = [
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/2/26/Abaddon_icon.png/225px-Abaddon_icon.png?version=9c37a80286c2aaeec0a15fd34bf12c40",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/f/fe/Alchemist_icon.png/225px-Alchemist_icon.png?version=362ad1d92c189517ec2b15833387bf86",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/2/23/Axe_icon.png/225px-Axe_icon.png?version=d413ab8cb99ff0f733309172115e20bb",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/d/d9/Beastmaster_icon.png/225px-Beastmaster_icon.png?version=d9c4363fc97f4527a58498dac7266d79",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/1/1e/Brewmaster_icon.png/225px-Brewmaster_icon.png?version=9946f66bcc10983465756f155d52e717",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/4/4d/Bristleback_icon.png/225px-Bristleback_icon.png?version=8647a57e688d012e0d3f7984ca7efafa",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/e/ed/Centaur_Warrunner_icon.png/225px-Centaur_Warrunner_icon.png?version=f141f94d695ca2aa413707c02b7f82f1",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/f/fe/Chaos_Knight_icon.png/225px-Chaos_Knight_icon.png?version=46147a7cb2e2e0209ff8be7acd1dfed8",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/d/d8/Clockwerk_icon.png/225px-Clockwerk_icon.png?version=681d642d01b65fabc8f75f5ecd9cb2da",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/4/40/Doom_icon.png/225px-Doom_icon.png?version=e3e57710ad79e62679c2ed5e69656e78",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/5/59/Dragon_Knight_icon.png/225px-Dragon_Knight_icon.png?version=1813485ab886b8b9117fc06f552ad676",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/b/be/Earth_Spirit_icon.png/225px-Earth_Spirit_icon.png?version=ea26b9bbd940a36532744ca04f76bf2f",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/a/a5/Earthshaker_icon.png/225px-Earthshaker_icon.png?version=cc91a6b6a57add38bec9405a25653ab5",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/1/1a/Elder_Titan_icon.png/225px-Elder_Titan_icon.png?version=cc636b882f7fe5c0d6e2f43fd804c60b",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/d/d3/Huskar_icon.png/225px-Huskar_icon.png?version=feabd6d91177ed86fe47e71b3c690b09",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/8/8d/Io_icon.png/225px-Io_icon.png?version=b6bdcea3eba28b3060d5fbb6951bd6d7",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/c/c0/Kunkka_icon.png/225px-Kunkka_icon.png?version=781456205eb2133ebfa33f5e31b4532b",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/a/a2/Legion_Commander_icon.png/225px-Legion_Commander_icon.png?version=e945534c3c586f6d111c1b824608150b",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/2/2b/Lifestealer_icon.png/225px-Lifestealer_icon.png?version=481f63f64277c216ff4e80a14e2297de",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/d/d6/Lycan_icon.png/225px-Lycan_icon.png?version=1bafecfeefa0c7c14ac0a58d074769c9",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/b/ba/Magnus_icon.png/225px-Magnus_icon.png?version=b9a2fc6da3218e73849ba155fc4fd50d",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/9/9d/Mars_icon.png/225px-Mars_icon.png?version=0c94c4799b8752ddbf95b32ceff69d86",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/1/15/Night_Stalker_icon.png/225px-Night_Stalker_icon.png?version=62f9997f3ec8bcc500bbfa5bc4018648",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/e/e2/Omniknight_icon.png/225px-Omniknight_icon.png?version=51b024dcec1ced8815525da22faec5ed",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/1/14/Phoenix_icon.png/225px-Phoenix_icon.png?version=2f300056a16b7cb4488546d9de019df4",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/c/c0/Pudge_icon.png/225px-Pudge_icon.png?version=5bd993407aa0a89d83e4dbbfa237f137",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/7/79/Sand_King_icon.png/225px-Sand_King_icon.png?version=e8812ff9cceef4e663ae25ac33e3ebaf",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/7/7e/Slardar_icon.png/225px-Slardar_icon.png?version=c6ef771ed33e3fec68c1b58f283cc4c5",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/7/7a/Snapfire_icon.png/225px-Snapfire_icon.png?version=66973925785132f3f23f53f3fb3f28b7",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/d/df/Spirit_Breaker_icon.png/225px-Spirit_Breaker_icon.png?version=2c129f6c0a27e9e8f08d89ccd554ce8a",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/1/1b/Sven_icon.png/225px-Sven_icon.png?version=930f13c9ea06b45d8732d31ccdd6ead1",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/d/d5/Tidehunter_icon.png/225px-Tidehunter_icon.png?version=9a334360a73caf448978d191f5bc8930",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/9/9a/Timbersaw_icon.png/225px-Timbersaw_icon.png?version=bc7763171f7ff04bc6cdd79084811a52",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/5/55/Tiny_icon.png/225px-Tiny_icon.png?version=cf36f48314e84c8a3ce3aeb50a4c39d9",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/3/3f/Treant_Protector_icon.png/225px-Treant_Protector_icon.png?version=bd70c80ef5eb94d7d840081e52b68832",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/c/ce/Tusk_icon.png/225px-Tusk_icon.png?version=7d1b174e105d84859c469bed57041b70",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/1/18/Underlord_icon.png/225px-Underlord_icon.png?version=60f5880558b078929cfab3314bf84f18",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/6/61/Undying_icon.png/225px-Undying_icon.png?version=24a8790129f3376ce9d3882a2208f09a",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/1/1e/Wraith_King_icon.png/225px-Wraith_King_icon.png?version=2de15c85f19caf616c9dbdd91e7cf3db",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/8/8e/Anti-Mage_icon.png/225px-Anti-Mage_icon.png?version=cd8b9f36144755d29cd7be214f9f7c00",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/0/07/Arc_Warden_icon.png/225px-Arc_Warden_icon.png?version=5ca43d03baa9d482e35621b07512c796",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/5/56/Bloodseeker_icon.png/225px-Bloodseeker_icon.png?version=2cf0fb12a046a1a0d76023d2af15744b",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/a/a6/Bounty_Hunter_icon.png/225px-Bounty_Hunter_icon.png?version=3eda163ff139059a1dee690a062afa8d",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/d/df/Broodmother_icon.png/225px-Broodmother_icon.png?version=4280d36157f3adeebf1c29b303c65164",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/c/cb/Clinkz_icon.png/225px-Clinkz_icon.png?version=c82ebba024a2707a20bcf8dc4a1a351c",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/8/80/Drow_Ranger_icon.png/225px-Drow_Ranger_icon.png?version=4f6c9037800142ae55b5fb8e6eeee8ec",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/9/91/Ember_Spirit_icon.png/225px-Ember_Spirit_icon.png?version=c770921c5435a6031b279c46b3565426",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/7/73/Faceless_Void_icon.png/225px-Faceless_Void_icon.png?version=3a6745d8dca441692d0fb5bef2101c9d",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/4/4f/Gyrocopter_icon.png/225px-Gyrocopter_icon.png?version=e004c5289de30ba1d173f0c0b0fce329",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/0/03/Juggernaut_icon.png/225px-Juggernaut_icon.png?version=b3e09e8897d04ac3525e8d485480b7d7",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/5/5d/Lone_Druid_icon.png/225px-Lone_Druid_icon.png?version=27f3c94470b0dcd8ef77ea9b95bb5d4d",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/7/7d/Luna_icon.png/225px-Luna_icon.png?version=f4521e8369f595ef08e40146aceb3c9b",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/c/cc/Medusa_icon.png/225px-Medusa_icon.png?version=e026e2303396f4fd1bf227aec95c705d",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/8/85/Meepo_icon.png/225px-Meepo_icon.png?version=683b6011445f9ba7c149a40041926881",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/1/12/Mirana_icon.png/225px-Mirana_icon.png?version=7ec8ce3f1af56f922535a4dfa7d85a1d",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/7/7b/Monkey_King_icon.png/225px-Monkey_King_icon.png?version=039e4d8ac3b78133810191f1bd84befa",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/7/7b/Morphling_icon.png/225px-Morphling_icon.png?version=ebf34abefd2f486fe3fb9dc998bd47e4",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/6/60/Naga_Siren_icon.png/225px-Naga_Siren_icon.png?version=e1b1559ceee7c100e35ab3d1d6c9579f",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/f/fa/Nyx_Assassin_icon.png/225px-Nyx_Assassin_icon.png?version=bada0040d2cada7eef3630f922a26f52",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/4/4e/Pangolier_icon.png/225px-Pangolier_icon.png?version=485a98d811d9bec12c1f6503e98fc987",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/8/8e/Phantom_Assassin_icon.png/225px-Phantom_Assassin_icon.png?version=9865db1a421ffaf2f458c9c908401480",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/8/81/Phantom_Lancer_icon.png/225px-Phantom_Lancer_icon.png?version=e54b99456774b6af7894bc2a99f32861",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/6/66/Razor_icon.png/225px-Razor_icon.png?version=3fe274ddc7943bceae65a3899d5324e1",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/7/7d/Riki_icon.png/225px-Riki_icon.png?version=6e517897ef28b59d8eda6cbecb20e44c",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/3/36/Shadow_Fiend_icon.png/225px-Shadow_Fiend_icon.png?version=5db40d1edee0fad1ee515b3b52c5e6d8",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/a/aa/Slark_icon.png/225px-Slark_icon.png?version=bd913c0397e076afa1bd873757f0a467",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/5/51/Sniper_icon.png/225px-Sniper_icon.png?version=110a1b640f54fb83632e2426ea66cb00",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/f/ff/Spectre_icon.png/225px-Spectre_icon.png?version=64a8bec63685d52606ab470e5cdfeb8d",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/9/9c/Templar_Assassin_icon.png/225px-Templar_Assassin_icon.png?version=2eeb36ca44cb910ed13b8c1dbfd7b929",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/5/52/Terrorblade_icon.png/225px-Terrorblade_icon.png?version=279254dd0c491f6136047e9be887cbf3",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/f/f0/Troll_Warlord_icon.png/225px-Troll_Warlord_icon.png?version=a6c96f006715c488a3cb7db9208a07b9",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/4/40/Ursa_icon.png/225px-Ursa_icon.png?version=fcaa4dbe9c77521489e003b5d5f804b0",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/2/20/Vengeful_Spirit_icon.png/225px-Vengeful_Spirit_icon.png?version=c7768fa99d424a08022a813e1abe6554",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/2/25/Venomancer_icon.png/225px-Venomancer_icon.png?version=ab41ba39b78d5aa2593df42a7a0cb066",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/5/5f/Viper_icon.png/225px-Viper_icon.png?version=68d2c93af0c80cf8e369e483d4c572dd",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/0/09/Weaver_icon.png/225px-Weaver_icon.png?version=e8a4e691cbdd2fb5d6d623a429800a3f",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/6/67/Ancient_Apparition_icon.png/225px-Ancient_Apparition_icon.png?version=65bf392e63dd39991806e1d8218445d8",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/c/c3/Bane_icon.png/225px-Bane_icon.png?version=f134db92edf224873178e366f8ec56f0",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/f/f2/Batrider_icon.png/225px-Batrider_icon.png?version=b302cf8397d32fc8d19e47398051b5df",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/6/61/Chen_icon.png/225px-Chen_icon.png?version=38e6dd9b6bb0a1749821f960ee5c11cb",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/2/27/Crystal_Maiden_icon.png/225px-Crystal_Maiden_icon.png?version=5238784a67ccdeebb8f1c4b86fd8a656",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/c/c5/Dark_Seer_icon.png/225px-Dark_Seer_icon.png?version=e08dc4a736b5c552a4ce0c5d29428a5d",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/3/3c/Dark_Willow_icon.png/225px-Dark_Willow_icon.png?version=8a31f898483c504e12cee024bf152df4",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/e/e6/Dazzle_icon.png/225px-Dazzle_icon.png?version=d24c637de3a67c6ccb66ad9d2f29506e",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/d/d7/Death_Prophet_icon.png/225px-Death_Prophet_icon.png?version=08099390c67fdd96f47a3bdfae9d0f2c",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/9/97/Disruptor_icon.png/225px-Disruptor_icon.png?version=af0f003529f51aa46043ef1705f0bc04",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/4/41/Enchantress_icon.png/225px-Enchantress_icon.png?version=384d2f3beffd910fe94004a73f774370",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/f/f7/Enigma_icon.png/225px-Enigma_icon.png?version=a5c8520fd41de3f1f58468b3649d3dad",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/d/d7/Grimstroke_icon.png/225px-Grimstroke_icon.png?version=f0bf75bc4a24bb0e1187f24bffe75998",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/0/00/Invoker_icon.png/225px-Invoker_icon.png?version=dc6b8c9aa57a47d41ac9583cdee0602e",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/2/2f/Jakiro_icon.png/225px-Jakiro_icon.png?version=234c437015014caa1ae41aed9ee9ee41",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/b/b9/Keeper_of_the_Light_icon.png/225px-Keeper_of_the_Light_icon.png?version=d88127b9a0afadcd92850acda819d13a",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/2/26/Leshrac_icon.png/225px-Leshrac_icon.png?version=03cbd8bb593cc40de86330cd272d9a37",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/b/bb/Lich_icon.png/225px-Lich_icon.png?version=d76a08450e2ae2b687133a394f62930e",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/3/35/Lina_icon.png/225px-Lina_icon.png?version=739d5bbb616d9570341783e1b15bc1b8",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/b/b8/Lion_icon.png/225px-Lion_icon.png?version=0f37e3228c6a9da1cede8dd092e148d7",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/c/c4/Nature%27s_Prophet_icon.png/225px-Nature%27s_Prophet_icon.png?version=57524f09bcfd989c3d141583b935518c",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/a/a6/Necrophos_icon.png/225px-Necrophos_icon.png?version=cc40dbca1480191edf04c04a67892848",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/e/e0/Ogre_Magi_icon.png/225px-Ogre_Magi_icon.png?version=08c9a4879f0d621ee73d08a14e4bf616",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/7/72/Oracle_icon.png/225px-Oracle_icon.png?version=674679804d1041a322b6653af10a07fd",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/9/99/Outworld_Devourer_icon.png/225px-Outworld_Devourer_icon.png?version=1d1275d9399f12e84295dfff791edc9d",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/1/13/Puck_icon.png/225px-Puck_icon.png?version=44f1dc0f40f4d14ebbdc818d04e9c419",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/c/cd/Pugna_icon.png/225px-Pugna_icon.png?version=ee1f91a070e71eaa68c9fcefee814b13",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/a/a1/Queen_of_Pain_icon.png/225px-Queen_of_Pain_icon.png?version=9ceb2ee733cd0ee5d619bdcab5f2ae7b",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/8/8a/Rubick_icon.png/225px-Rubick_icon.png?version=6dd7037647389849b89adf0981ad3b3e",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/f/f3/Shadow_Demon_icon.png/225px-Shadow_Demon_icon.png?version=7216705a344126aa70e27801769bf465",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/9/96/Shadow_Shaman_icon.png/225px-Shadow_Shaman_icon.png?version=6caaf33edf660e3d41b057054007d4a5",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/9/9f/Silencer_icon.png/225px-Silencer_icon.png?version=883f9e4cefbdbbf098b00759bdc06fd6",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/b/bf/Skywrath_Mage_icon.png/225px-Skywrath_Mage_icon.png?version=41b3fbaab30da6d0de1a90c9b895db54",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/1/13/Storm_Spirit_icon.png/225px-Storm_Spirit_icon.png?version=4a37e9e60f979de82e7f9edac83d89f9",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/f/fa/Techies_icon.png/225px-Techies_icon.png?version=5e75d56558964afb7548e2182a909a67",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/d/d1/Tinker_icon.png/225px-Tinker_icon.png?version=a0f61be9fa945f1994f9e535f0fbcaba",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/9/9e/Visage_icon.png/225px-Visage_icon.png?version=276430ceea4409a5eb2425bb9de4a340",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/9/99/Void_Spirit_icon.png/225px-Void_Spirit_icon.png?version=2a26b89e17f12fe281139d7dcd4f3f06",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/3/3f/Warlock_icon.png/225px-Warlock_icon.png?version=86c48efc0dfbef2f521a484b186317af",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/6/60/Windranger_icon.png/225px-Windranger_icon.png?version=8b348f1d209b3db3f78c2047d9968178",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/4/4a/Winter_Wyvern_icon.png/225px-Winter_Wyvern_icon.png?version=98ce3df75df51c7459a0458126a9243b",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/3/33/Witch_Doctor_icon.png/225px-Witch_Doctor_icon.png?version=ae7f459f3032561f6b518f9e17c08e14",
"https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/3/3f/Zeus_icon.png/225px-Zeus_icon.png?version=1aa45d1ab42e6e7d193498b0d254384c",
]

heroes = [
"Abaddon",
"Alchemist",
"Axe",
"Beastmaster",
"Brewmaster",
"Bristleback",
"Centaur Warrunner",
"Chaos Knight",
"Clockwerk",
"Doom",
"Dragon Knight",
"Earth Spirit",
"Earthshaker",
"Elder Titan",
"Huskar",
"Io",
"Kunkka",
"Legion Commander",
"Lifestealer",
"Lycan",
"Magnus",
"Mars",
"Night Stalker",
"Omniknight",
"Phoenix",
"Pudge",
"Sand King",
"Slardar",
"Snapfire",
"Spirit Breaker",
"Sven",
"Tidehunter",
"Timbersaw",
"Tiny",
"Treant Protector",
"Tusk",
"Underlord",
"Undying",
"Wraith King",
"Anti-Mage",
"Arc Warden",
"Bloodseeker",
"Bounty Hunter",
"Broodmother",
"Clinkz",
"Drow Ranger",
"Ember Spirit",
"Faceless Void",
"Gyrocopter",
"Juggernaut",
"Lone Druid",
"Luna",
"Medusa",
"Meepo",
"Mirana",
"Monkey King",
"Morphling",
"Naga Siren",
"Nyx Assassin",
"Pangolier",
"Phantom Assassin",
"Phantom Lancer",
"Razor",
"Riki",
"Shadow Fiend",
"Slark",
"Sniper",
"Spectre",
"Templar Assassin",
"Terrorblade",
"Troll Warlord",
"Ursa",
"Vengeful Spirit",
"Venomancer",
"Viper",
"Weaver",
"Ancient Apparation",
"Bane",
"Batrider",
"Chen",
"Crystal Maiden",
"Dark Seer",
"Dark Willow",
"Dazzle",
"Death Prophet",
"Disruptor",
"Enchantress",
"Enigma",
"Grimstroke",
"Invoker",
"Jakiro",
"Keeper of the Light",
"Leshrac",
"Lich",
"Lina",
"Lion",
"Nature's Prophet",
"Necrophos",
"Ogre Magi",
"Oracle",
"Outworld Devourer",
"Puck",
"Pugna",
"Queen of Pain",
"Rubick",
"Shadow Demon",
"Shadow Shaman",
"Sliencer",
"Skywrath Mage",
"Storm Spirit",
"Techies",
"Tinker",
"Visage",
"Void Spirit",
"Warlock",
"Windranger",
"Winter Wyvern",
"Witch Doctor",
"Zeus",
]

predictions = [
"если вы проявите инициативу, успех не заставит себя ждать.",
"твои надежды и планы сбудутся сверх всяких ожиданий.",
"сегодня ты будешь попадать каждым хуком!",
"тебе пора отдохнуть.",
"тебе предлагается мечта всей жизни. Скажите да!",
"сегодня ты выиграешь мид!",
"тебя ждет приятный сюрприз.",
"время – ваш союзник, лучше отложить принятие важного решения хотя бы на день.",
"сегодня ты сделаешь rampage!",
"готовься к романтическим приключениям."
]

answer_ball = [
"Давно пора!",
"Не сегодня.",
"Не-е-ет!",
"Не-а!",
"Время нарезать!",
"А вот и нет.",
"Будет сделано.",
"А то!",
]

@bot.command()
async def hero(ctx, arg = None):
	if arg == None:
		hero = random.randint(0, 116)
		emb = discord.Embed(title = heroes[hero], colour = discord.Color.from_rgb(48, 255, 165))
		emb.set_image(url = heroes_image[hero])
		if 0 <= hero <= 38:
			emb.set_thumbnail(url = "https://gamepedia.cursecdn.com/dota2_gamepedia/7/7a/Strength_attribute_symbol.png")
			await ctx.send(embed = emb)
		elif 38 <= hero <= 75:
			emb.set_thumbnail(url = "https://gamepedia.cursecdn.com/dota2_gamepedia/2/2d/Agility_attribute_symbol.png")
			await ctx.send(embed = emb)
		elif 75 < hero:
			emb.set_thumbnail(url = "https://gamepedia.cursecdn.com/dota2_gamepedia/5/56/Intelligence_attribute_symbol.png")
			await ctx.send(embed = emb)
	elif arg == "1":
		arg = int(arg)
		hero = random.randint(0, 30)
		hero_h = heroes_1[hero]
		emb = discord.Embed(title = heroes[hero_h], colour = discord.Color.from_rgb(48, 255, 165))
		emb.set_image(url = heroes_image[hero_h])
		if 0 <= hero_h <= 38:
			emb.set_thumbnail(url = "https://gamepedia.cursecdn.com/dota2_gamepedia/7/7a/Strength_attribute_symbol.png")
			await ctx.send(embed = emb)
		elif 38 <= hero_h <= 75:
			emb.set_thumbnail(url = "https://gamepedia.cursecdn.com/dota2_gamepedia/2/2d/Agility_attribute_symbol.png")
			await ctx.send(embed = emb)
		elif 75 < hero_h:
			emb.set_thumbnail(url = "https://gamepedia.cursecdn.com/dota2_gamepedia/5/56/Intelligence_attribute_symbol.png")
			await ctx.send(embed = emb)
	elif arg == "2":
		arg = int(arg)
		hero = random.randint(0, 45)
		print (hero)
		hero_h = heroes_2[hero]
		print (hero_h)
		emb = discord.Embed(title = heroes[hero_h], colour = discord.Color.from_rgb(48, 255, 165))
		emb.set_image(url = heroes_image[hero_h])
		if 0 <= hero_h <= 38:
			emb.set_thumbnail(url = "https://gamepedia.cursecdn.com/dota2_gamepedia/7/7a/Strength_attribute_symbol.png")
			await ctx.send(embed = emb)
		elif 38 <= hero_h <= 75:
			emb.set_thumbnail(url = "https://gamepedia.cursecdn.com/dota2_gamepedia/2/2d/Agility_attribute_symbol.png")
			await ctx.send(embed = emb)
		elif 75 < hero_h:
			emb.set_thumbnail(url = "https://gamepedia.cursecdn.com/dota2_gamepedia/5/56/Intelligence_attribute_symbol.png")
			await ctx.send(embed = emb)

@bot.command()
async def flip(ctx):
	f = random.randint(1, 2)
	if f == 1:
		emb = discord.Embed(title = "Решка!", colour = discord.Color.from_rgb(48, 255, 165))
		emb.set_image(url = "https://castlots.org/img/ru_reshka.png" )
		await ctx.send(embed = emb)
	elif f == 2:
		emb = discord.Embed(title = "Орёл!", colour = discord.Color.from_rgb(48, 255, 165))
		emb.set_image(url = "https://castlots.org/img/ru_orel.png" )
		await ctx.send(embed = emb)

@bot.command()
async def ball(ctx, text = None):
	if text == None:
		await ctx.send("Напишите какое либо действие")
	else:

		b = random.randint(0, 7)
		emb = discord.Embed( title = answer_ball[b], colour = discord.Color.from_rgb(48, 255, 165))
		await ctx.send(embed = emb)

@bot.command()
async def FortuneMeat(ctx):
	p = random.randint(0, 9)
	emb = discord.Embed( title = f"{ctx.author}, " +  predictions[p], colour = discord.Color.from_rgb(48, 255, 165))
	await ctx.send(embed = emb)

@bot.command()
async def pudge(ctx):
	await ctx.send(
	"Свежее мясо! Вот команды которые есть: \n"
	"1. -roll 1число 2число(выводит рандомное число из этих двух) \n"
	"2. -duel @пользователь(вызывает на дуэль пользователя) \n"
	"3. -FortuneMeat(вызывает случайное предсказание) \n"
	"4. -ball действие(показывает делать это действие или нет) \n"
	"5. -flip(выпадает орёл или решка) \n"
	"6. -hero(рандомный герой, можно написать 1 или 2(роль)) \n"
	"7. -pudge(показывает данный список) "
	)

@bot.command()
async def duel( ctx, member: discord.Member = None):
    if member is None:
        await ctx.send('Укажи кого хочешь позвать на дуель!')
    else:
        a = random.randint(1,2)
        if a == 1:
            emb = discord.Embed( title = f"Победитель - {ctx.author}", colour = discord.Color.blue())
            await ctx.send( embed = emb )

            emb = discord.Embed( title = f"Проигравший - {member}", colour = discord.Color.red())
            await ctx.send( embed = emb )
        else:
            emb = discord.Embed( title = f"Победитель - {member}", colour = discord.Color.blue())
            await ctx.send( embed = emb )

            emb = discord.Embed( title = f"Проигравший - {ctx.author}", colour = discord.Color.red())
            await ctx.send( embed = emb )

@bot.command()
async def roll(ctx, arg1 = None, arg2 = None):
	if arg1 == None and arg2 == None:
		otvet = random.randint(1, 100)
	elif arg1 != None and arg2 == None:
		arg1 = int(arg1)
		otvet = random.randint(1, arg1)
	elif arg1 == None and arg2 != None:
		arg2 = int(arg2)
		otvet = random.randint(1, arg2)
	else:
		arg1 = int(arg1)
		arg2 = int(arg2)
		otvet = random.randint(arg1, arg2)
	await ctx.send(str(otvet))


bot.run('NzI5NDYxOTM1OTk2Nzk3MDI5.XwJSrw.vdgFAcFTUjE5Guo-6VdnWtFKL48')