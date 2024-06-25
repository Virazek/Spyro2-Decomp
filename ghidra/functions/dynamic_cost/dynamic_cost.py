UNLOCK_STATE_START = 0x80065184
UNLOCK_TYPE_TOTALS_START = 0x80065178

def verify_unlock_cost(UNLOCK_ID: int) -> bool:
    # Values within parenthesis denote evaluating the value at that address

    # We first load the 'unlock state' table address for this specific unlock ID
    UNLOCK_STATE_ADDR: int = UNLOCK_STATE_START + UNLOCK_ID << 2
    # Note that bitshifting left by 2 is the same as multiplying by 4

    # Next, we load the value to compare from the unlock type totals table
    COMPARE: int = UNLOCK_TYPE_TOTALS_START + (UNLOCK_STATE_ADDR + 0x01)
    
    # We need to compare this as a halfword if we are comparing gems, since gem counts could be 2-bytes
    # But otherwise, we can compare a single byte; the only way I see to change this is to double the size of the totals table so they are all halfwords
    return (UNLOCK_STATE_ADDR + 0x02) >= COMPARE
