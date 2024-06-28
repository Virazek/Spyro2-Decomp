Any function that touches the vanilla cost/state array indexes it with a local variable whose corresponding values are so:
0x01: Crystal Glacier bridge
0x02: Aquaria Towers submarine
0x03: Magma Cone elevator
0x04: Glimmer bridge
0x05: Swim
0x06: Climb
0x07: Headbash
0x08: Aquaria Towers
0x0B: Zephyr
0x0C: Shady Oasis
0x0D: Icy Speedway
0x13: Canyon Speedway

I THINK 0x09 should be in use but I've never seen it touched. 0x0A, 0x0E, and 0x0F all seem unused

Orb unlocks are handled differently, and are handled by level scripts:
e.g.,
For the 8-Orb Professor-locked door in Autumn Plains, the script loaded into RAM is 
800781C8 lw v0,$8006702C (Load current Orb count)
800781D0 nop
800781D4 slti v0,v0,$8 (Check if the Orb count is less than 8)
800781D8 bne v0,0,$800781F0 (If the comparison evaluates to false (the orb count is more than 8), continue execution, otherwise jump)
800781DC nop
800781E0 addiu t7,0,$2
800781E4 sb t7,$2(s0)
800781E8 addiu t6,0,$1
800781EC sb t6,$5(s0)
...
(After conversation with the Professor...)
800783C0 subiu t6,0,$1
800783C4 lui at,$8006
800783C8 sh t7,$4702(at) 

Non-Gem unlocks are:
Dragon Shores, Ocean Speedway, Crush, Gulp, Ripto, Metro Speedway, Dragon Shores main door, Dragon Shores theater, Autumn Plains 8-Orb door, and permanent superflame door

We lay out our cost/state table as such:
0x00 1b IS_UNLOCKED
0x01 1b UNLOCK_TYPE
0x02 2b UNLOCK_COST (unlock cost should max out at 0x2710 = 10000)

and fill it with the following entries:
0x04: Crystal Glacier bridge (0x01)
0x08: Aquaria Towers submarine (0x02)
0x0C: Magma Cone elevator (0x03)
0x10: Glimmer bridge (0x04)
0x14: Swim (0x05)
0x18: Climb (0x06)
0x1C: Headbash (0x07)
0x20: Aquaria Towers (0x08)
0x24: Ocean Speedway (0x09)
0x28: Metro Speedway (0x0A)
0x2C: Zephyr (0x0B)
0x30: Shady Oasis (0x0C)
0x34: Icy Speedway (0x0D)
0x38: Dragon Shores (0x0E)
0x3C: Dragon Shores main door (0x0F)
0x40: Dragon Shores theater (0x10)
0x44: Permanent superflame door (0x11)
0x48: Autumn Plains 8-Orb door (0x12)
0x4C: Canyon Speedway (0x13)
0x50: Crush (0x14)
0x54: Gulp (0x15)
0x58: Ripto (0x16)

Unlock types are as follows:
0x0: Gems
0x2: Orbs
0x3: Talismans
0x4: Dragon Shores tickets
IGNORE ALL THE FOLLOWING UNTIL I KNOW HOW TO IMPLEMENT THEM IN APWORLD, THE ROMHACKING WILL SUPPORT THEM THOUGH
0x5: 100% Gem locations
0x6: Orb locations
0x7: Talisman locations
0x8: Dragon Shores ticket locations
0x9: Boss kills
0xA: Skill points

For simplicity, we also pre-calculate the different values that can be checked

So, assume unlock type totals calculations start at 0x80065178, unlock states start at 0x80065184, and the verify unlock cost function starts at 0x800651E0




We need some additional handling elsewhere to show the cost to the player when showing the text.