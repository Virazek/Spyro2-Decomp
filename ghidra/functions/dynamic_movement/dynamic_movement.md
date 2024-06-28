There is a function in ROM at 0x80035D38 (?HANDLE_SPYRO_STATE_CHANGES) that handles changing Spyro's state from one to another. Most, if not all state changes should have to go through this function. It checks controller registers to see what action to take, then calls another subroutine (?CHANGE_SPYRO_STATE, 0x800351D8) with the parameter of the state to change to.

e.g.
case 5:
/* In a jump */
...
      if ((WRAM_CONTROLLER_HELD & 0x80) == 0) {
        if (((WRAM_CONTROLLER_PRESSED & 0x10) != 0) && (SRAM_ABILITY_HEADBASH != 0)) {
          uVar2 = ?EXECUTE_MOVEMENT(&WRAM_SPYRO_X_POSITION,0x364);
          iVar3 = 0x2e; 
          /* This is headbash */
          if (uVar2 == 0) goto LAB_800366d8;
        }
      }
      else {
                    /* This handles air-charging */
        iVar3 = 0x15;
        if (0 < ?WRAM_SPYRO_ROLL_ANGLE_VELOCITY) {
          ?WRAM_SPYRO_ROLL_ANGLE_VELOCITY = 0;
        }
LAB_800366d8:
        ?CHANGE_SPYRO_STATE(iVar3);
      }


There is a pretty obvious path to take to lock certain abilities then:

Modify the ?CHANGE_SPYRO_STATE subroutine to jump to another subroutine that does additional handling to determine whether Spyro has the movement option, then have ?CHANGE_SPYRO_STATE end execution if the subroutine returns that Spyro doesn't have that ability. From preliminary testing, this looks somewhat fine?
This also doesn't handle flame or spitting objects.

It's actually probably better to handle swim, climb, and headbash here instead and let the vanilla game's memory handle buying them as a location.

Spyro State IDs:
0x00: Standing
0x01: Walking-Accelerating
0x02: Walking-At Max Speed
0x03: Walking-Decelerating
0x05: Jumping
0x06: Flopping
0x07: Flame
0x09: Ice Skating
0x0C: Charging
0x0D: Bonking
0x0E: Standing on the edge of a platform
0x0F: Hit by projectile
0x10: Gliding
0x11: Fluttering
0x13: Idle (Looking around)
0x15: Charging in air
0x19: Supercharge jump
0x1A: Crushed
0x1C: Burned by lava
0x1F: Dying
0x21: Superflight
0x26: Idle (Grooming self)
0x28: Swimming underwater (NOT diving/charging)
0x29: Stationary underwater
0x2A: Charging underwater
0x2C: Swimming on water's surface
0x2E: Headbash
0x2F: Climbing (stationary on ladder)
0x32: Climbing (moving on ladder)
0x35: Spitting object
0x3D: Supercharge


We could reserve 61 bytes to make a full table to check for this, make everything check individually, or hopefully find some weird arithmetic to compress this table. Given that we may have to adjust for progressive charge/flight, probably best to take the middle path.