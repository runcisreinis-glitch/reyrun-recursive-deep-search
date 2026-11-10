# How cheats work, and how to separate technology from sales claims

**Wallhack and aimbot describe the advantage obtained; DMA describes an access mechanism.** These can be combined in one system. A "DMA aimbot" label therefore says nothing by itself about quality, safety or whether the demonstration is real.

## Three different concepts

**Wallhack and the broader ESP category** use information the game normally hides from the player: an opponent's position, outline or other data. This may involve displaying information available in memory as a separate overlay or changing rendering. One essential limit is that reading memory cannot recover a hidden position that the server never sends to the client. Riot describes precisely this *Fog of War* approach; practical use must also account for visibility changes and latency. [Riot's technical explanation](https://www.riotgames.com/en/news/demolishing-wallhacks-valorants-fog-war)

**Aimbot** automates aiming. Some variants use game data; others use computer vision to analyze visible screen pixels and adjust controls from those. "AI" may refer to a real recognition model or merely a marketing label. Screen analysis does not itself see through walls, nor does it prevent analysis of the player's resulting behaviour. *GAN-Aimbots* examines these approaches and behavioural imitation; its experimental outcome is not a guarantee for every game. [2022 study](https://arxiv.org/html/2205.07060v1)

**DMA, Direct Memory Access,** is direct hardware access to memory, also used normally by legitimate devices. A cheating system attempts to use it to obtain game data. It is not an invisibility card: an IOMMU limits which memory regions a device may access. The outcome depends on hardware, firmware and functioning protections. Microsoft documentation explicitly distinguishes Windows protection after system loading from protection during boot. [Microsoft](https://learn.microsoft.com/de-de/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt)

## Who develops these systems, and what does anti-cheat do?

It helps to distinguish the author, adapter, seller and researcher. An author understands the game's data flow; another contributor may work on graphics, input automation or drivers. A seller may sell someone else's work. Researchers study similar mechanisms to test protections. These are different roles: a technical video proves neither authorship nor trustworthiness.

Anti-cheat commonly has several layers: game and system integrity checks, access monitoring, server-rule checks and behavioural analysis. A kernel driver provides different visibility from an ordinary program, but does not solve every problem. Architectures differ: Epic's described EAC Linux v2 plans to use platform protections and eBPF without its own anti-cheat kernel module. [Epic's architecture](https://onlineservices.epicgames.com/news/introducing-easy-anti-cheat-linux-v2?lang=ja)

**Server authority** means the server makes the final decision about game state. The server must still evaluate client requests; a central server alone does not prevent sending unnecessary information or automated aiming. [Unreal's networking model](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-overview-for-unreal-engine)

**Self-reported developer experience:** Inferna Studio writes that its own anti-cheat mistakenly banned a developer's account. This is one author's account, not an independently verified test or a measurement of false-ban frequency. It helps explain why a suspicious signal and proven cheating are not synonyms. [Experience report](https://infernastudio.com/articles/our-anti-cheat-banned-a-player-it-was-us)

## Where to learn, and which claims to question

[Reverse Engineering Stack Exchange](https://reverseengineering.stackexchange.com/tour), Ghidra project discussions and game-engine developers' documentation are useful for technical questions. **Ghidra** helps inspect compiled code; **debuggers** such as WinDbg let you inspect your own program's execution, memory and registers. These are general research tools. [Ghidra](https://github.com/NationalSecurityAgency/ghidra) · [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/)

When assessing a claim, I would ask three things:

- **What exactly is being demonstrated?** Version, environment, input, complete output and known limitations are more informative than a montage of selected wins.
- **Can the claim be tested?** "Never detectable," "works everywhere" and "AI, therefore safe" are not technical evidence.
- **Do the sources agree?** Repository history, the author's explanation and a repeatable demonstration help establish provenance. Review counts or a request to disable protections do not by themselves establish trustworthiness.

**A useful next step:** in your own offline Unity or Unreal scene, create two characters and a wall, enable the developer's diagnostic display, and compare "the data exists" with "the object is visible." Then use your own local client/server example to check which data is transmitted. This makes the source of the problem and the purpose of the protection easier to understand.
