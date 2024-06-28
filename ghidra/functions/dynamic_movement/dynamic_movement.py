# These are memory addresses. They contain 1 if this item has been given, and 0 otherwise
ARCHIPELAGO_MOVEMENT_ITEM_SWIM: int
ARCHIPELAGO_MOVEMENT_ITEM_CLIMB: int
ARCHIPELAGO_MOVEMENT_ITEM_HEADBASH: int
ARCHIPELAGO_MOVEMENT_ITEM_CHARGE: int
ARCHIPELAGO_MOVEMENT_ITEM_GLIDE: int # These two are different. The each successive bit denotes the progressive level of this
ARCHIPELAGO_MOVEMENT_ITEM_FLUTTER: int

# Parenthesis around an address denote the value stored there
# A nonzero return indicates that Spyro has this ability.
def dynamic_movement(state_id: int) -> int:
    CHECK_ADDRESS: int
    # Check swim
    if state_id == 0x2A:
        CHECK_ADDRESS = ARCHIPELAGO_MOVEMENT_ITEM_SWIM
    # Check climb
    if state_id in [0x2F, 0x32]:
        CHECK_ADDRESS = ARCHIPELAGO_MOVEMENT_ITEM_CLIMB
    # Check headbash
    if state_id == 0x2E:
        CHECK_ADDRESS = ARCHIPELAGO_MOVEMENT_ITEM_HEADBASH
    # Check flutter
    if state_id == 0x11:
        CHECK_ADDRESS = ARCHIPELAGO_MOVEMENT_ITEM_FLUTTER



    # Check charge
    if state_id in [0x0C, 0x15, 0x19, 0x3D]:
        return ((ARCHIPELAGO_MOVEMENT_ITEM_CHARGE) >> (state_id > 0x15)) & 1
        

    # Check glide
    if state_id in [0x10, 0x21]:
        return ((ARCHIPELAGO_MOVEMENT_ITEM_GLIDE) >> (state_id > 0x15)) & 1

    return (CHECK_ADDRESS)