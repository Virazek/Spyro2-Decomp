.psx
.create "dynamic_cost.bin", 0x800651E0

; Unlock ID is assumed to be stored in the a0 register

DYNAMIC_COST:
  lui t0,0x8006
  lw t1,0x5184
  addu t0,t0,t1
  sll t1,a0,0x02



.close