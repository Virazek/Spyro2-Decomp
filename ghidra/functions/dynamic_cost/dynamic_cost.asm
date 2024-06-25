.psx
.create "dynamic_cost.bin", 0x800651E0


; Unlock ID is assumed to be stored in the a0 register

; This function will never call another one, so we should hopefully not need to store ra in the stack
DYNAMIC_COST:
  addiu sp,sp,-0x0F
  sw t0,0x0F(sp)
  sw t1,0x0C(sp)
  sw t2,0x08(sp)
  sw t3,0x04(sp)

  


  lw t0,0x80065184 ; UNLOCK_STATE_START
  sll a0,a0,0x02 ; UNLOCK_ID << 2
  addu t0,t0,a0 ; UNLOCK_STATE_ADDR


  lw t1,0x80065178 ; UNLOCK_TYPE_TOTALS_START
  lw t2,0x01(t0) ; (UNLOCK_STATE_ADDR + 0x01) = COMPARE_TYPE
  nop
  addu t1,t1,t2 ; COMPARE_ADDRESS = UNLOCK_TYPE_TOTALS_START + COMPARE_TYPE
  
  beq t2,0x00,org(GemCompare)
  NonGemCompare:
  lb t1,0x00(t1) ; COMPARE = (COMPARE_ADDRESS)
  lb t3,0x02(t0) ; (UNLOCK_STATE_ADDR + 0x02)
  nop
  slt v0,t1,t3
  j org(Return)
  nop
  GemCompare:
  lh t1,0x00(t1) ; COMPARE = (COMPARE_ADDRESS)
  lh t3,0x02(t0) ; (UNLOCK_STATE_ADDR + 0x02)
  nop
  slt v0,t1,t3
  Return:

  lw t0,0x0F(sp)
  lw t1,0x0C(sp)
  lw t2,0x08(sp)
  lw t3,0x04(sp)
  addiu sp,sp,0x0F

  jr ra
  nop

.close